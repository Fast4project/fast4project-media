#!/usr/bin/env python3
"""Verifikasi email prospek outreach fast4project (Agent 4).

Memeriksa apakah sebuah alamat email BENAR-BENAR bisa menerima surat, tanpa
mengirim apa pun. Memakai Reacher (github.com/reacherhq/check-if-email-exists,
MIT) sebagai mesin; hanya pustaka standar Python, tanpa pip.

Tiga lapis, dipakai berurutan:
  1. Sintaks + domain punya MX (lewat nslookup/dig).      -> selalu jalan
  2. Reacher HTTP (Docker, localhost:8080) atau CLI.       -> cek kotak surat
  3. Hasil dipetakan ke tindakan: KIRIM / TANYA FELIX / BUANG.

Contoh:
  python alat/verifikasi-email/verifikasi_email.py --cek-siap
  python alat/verifikasi-email/verifikasi_email.py <alamat-1> <alamat-2>
  python alat/verifikasi-email/verifikasi_email.py --dari-file claude/outreach-antrian.md --bagian "Antrian siap dikirim" --keluar outreach/hasil-verifikasi.csv

Kode keluar: 0 selesai (ada atau tidak ada email buruk) · 2 mesin tidak siap · 3 input kosong.
Batas jujur: hasil adalah TEBAKAN berbasis protokol SMTP, bukan jaminan. Gmail, Outlook,
dan domain catch-all sering keluar `risky`/`unknown`. Bounce nyata hanya terlihat setelah kirim.
"""
import argparse
import csv
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)+")
SINTAKS_RE = re.compile(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(\.[A-Za-z0-9\-]+)+$")
MAKS_PER_JALAN = 30
JEDA_DETIK = 2.0
HOST_UJI_PORT25 = "gmail-smtp-in.l.google.com"

# status akhir -> (tindakan, penjelasan)
TINDAKAN = {
    "safe": ("KIRIM", "kotak surat terdeteksi ada dan menerima surat"),
    "risky": ("TANYA FELIX", "domain catch-all / kotak penuh / tidak pasti; bisa terkirim, bisa mental"),
    "unknown": ("TANYA FELIX", "server tidak menjawab pasti (sering Gmail/Outlook atau port 25 diblokir)"),
    "invalid": ("BUANG", "alamat tidak ada atau dinonaktifkan; jangan dikirim"),
    "mx-saja": ("TANYA FELIX", "hanya sintaks + MX dicek (Reacher tidak tersedia); kotak surat belum diperiksa"),
    "sintaks-salah": ("BUANG", "bentuk alamat tidak sah"),
    "tanpa-mx": ("BUANG", "domain tidak punya server surat"),
}


def ambil_email(sumber):
    """Ambil alamat unik dari teks (urutan kemunculan dipertahankan)."""
    lihat, hasil = set(), []
    for m in EMAIL_RE.findall(sumber):
        e = m.strip(".,;:)").lower()
        if e not in lihat:
            lihat.add(e)
            hasil.append(e)
    return hasil


def ambil_bagian(teks, judul):
    """Potong teks markdown: dari heading '## ...judul...' sampai heading '## ' berikutnya."""
    baris, ambil, hasil = teks.splitlines(), False, []
    for b in baris:
        if b.startswith("## "):
            ambil = judul.lower() in b.lower()
            continue
        if ambil:
            hasil.append(b)
    return "\n".join(hasil)


def punya_mx(domain):
    """True/False bila bisa dipastikan, None bila alat DNS tidak ada."""
    perintah = None
    if shutil.which("nslookup"):
        perintah = ["nslookup", "-type=MX", domain]
    elif shutil.which("dig"):
        perintah = ["dig", "+short", "MX", domain]
    if not perintah:
        return None
    try:
        out = subprocess.run(perintah, capture_output=True, text=True, timeout=15)
    except Exception:
        return None
    teks = (out.stdout + out.stderr).lower()
    if "mail exchanger" in teks or "mx preference" in teks:
        return True
    if perintah[0] == "dig" and out.stdout.strip():
        return True
    if "non-existent" in teks or "nxdomain" in teks or "can't find" in teks:
        return False
    # nslookup tanpa MX tetapi domain ada: A record dipakai sebagai cadangan menurut RFC 5321
    if "address" in teks and "mail exchanger" not in teks:
        return None
    return None


def tanya_reacher_http(email, server, dari, halo, proxy, batas):
    badan = {"to_email": email}
    if dari:
        badan["from_email"] = dari
    if halo:
        badan["hello_name"] = halo
    if proxy:
        h, _, p = proxy.partition(":")
        badan["proxy"] = {"host": h, "port": int(p or 1080)}
    req = urllib.request.Request(
        server, data=json.dumps(badan).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=batas) as r:
        return json.loads(r.read().decode("utf-8"))


def tanya_reacher_cli(email, biner, batas):
    out = subprocess.run([biner, email], capture_output=True, text=True, timeout=batas)
    teks = out.stdout.strip()
    # CLI mencetak satu objek JSON (kadang diawali log)
    awal = teks.find("{")
    if awal < 0:
        raise RuntimeError("CLI Reacher tidak mengeluarkan JSON: " + (out.stderr or teks)[:200])
    return json.loads(teks[awal:])


def ringkas(j):
    """Ubah balasan Reacher jadi (status, catatan)."""
    status = (j.get("is_reachable") or "unknown").lower()
    if status not in ("safe", "risky", "invalid", "unknown"):
        status = "unknown"
    smtp = j.get("smtp") or {}
    misc = j.get("misc") or {}
    mx = j.get("mx") or {}
    cat = []
    if smtp.get("is_catch_all"):
        cat.append("catch-all")
    if smtp.get("has_full_inbox"):
        cat.append("kotak penuh")
    if smtp.get("is_disabled"):
        cat.append("dinonaktifkan")
    if smtp.get("is_deliverable") is True:
        cat.append("deliverable")
    if smtp.get("can_connect_smtp") is False:
        cat.append("tak bisa konek SMTP")
    if misc.get("is_role_account"):
        cat.append("alamat peran (seperti info atau admin)")
    if misc.get("is_disposable"):
        cat.append("sekali pakai")
    if mx and mx.get("accepts_mail") is False:
        cat.append("MX tidak menerima")
    if j.get("error"):
        cat.append("error: " + str(j["error"])[:80])
    return status, "; ".join(cat)


def cek_satu(email, a):
    if not SINTAKS_RE.match(email):
        return "sintaks-salah", ""
    domain = email.rsplit("@", 1)[1]
    mx = punya_mx(domain)
    if mx is False:
        return "tanpa-mx", "domain " + domain
    try:
        if a.cli:
            return ringkas(tanya_reacher_cli(email, a.cli, a.batas))
        if a.server:
            return ringkas(tanya_reacher_http(email, a.server, a.dari, a.halo, a.proxy, a.batas))
    except (urllib.error.URLError, socket.timeout, OSError, RuntimeError, ValueError) as e:
        return "mx-saja", "Reacher gagal: %s" % str(e)[:90]
    return "mx-saja", "tanpa Reacher"


def cek_siap(a):
    ok = True
    print("== Cek kesiapan ==")
    # 1. DNS
    print("DNS (nslookup/dig): ", end="")
    t = punya_mx("gmail.com")
    print({True: "OK", False: "gmail.com tanpa MX? aneh", None: "alat DNS tidak ada atau tak menjawab"}[t])
    ok &= t is True
    # 2. Port 25 keluar
    print("Port 25 keluar ke %s: " % HOST_UJI_PORT25, end="", flush=True)
    try:
        s = socket.create_connection((HOST_UJI_PORT25, 25), timeout=8)
        s.close()
        print("TERBUKA")
        p25 = True
    except Exception as e:
        print("TERTUTUP (%s)" % type(e).__name__)
        p25 = False
    # 3. Reacher
    r_ok = False
    if a.cli and shutil.which(a.cli):
        print("Reacher CLI: ditemukan (%s)" % shutil.which(a.cli))
        r_ok = True
    else:
        base = a.server.rsplit("/v0/", 1)[0]
        try:
            urllib.request.urlopen(base + "/version", timeout=4).read()
            print("Reacher HTTP: hidup di %s" % base)
            r_ok = True
        except Exception:
            # beberapa versi tidak punya /version; cukup ada yang menjawab di port
            try:
                host, port = base.replace("http://", "").replace("https://", "").split(":")[0:2]
                socket.create_connection((host, int(port.split("/")[0])), timeout=3).close()
                print("Reacher HTTP: port terbuka di %s" % base)
                r_ok = True
            except Exception:
                print("Reacher HTTP: TIDAK hidup di %s (jalankan alat/verifikasi-email/pasang-reacher.ps1)" % base)
    print()
    if r_ok and p25:
        print("SIAP: verifikasi kotak surat penuh bisa dijalankan.")
        return 0
    if not p25:
        print("Port 25 tertutup: Reacher tidak bisa mengecek kotak surat dari jaringan ini.")
        print("Skrip tetap bisa mengecek sintaks + MX (status `mx-saja`). Coba jaringan lain (hotspot) atau minta ISP membuka port 25.")
    if not r_ok:
        print("Reacher belum jalan: pasang dulu dengan pasang-reacher.ps1 (Docker) atau unduh CLI dari halaman rilis.")
    return 2


def main():
    ap = argparse.ArgumentParser(description="Verifikasi email prospek (Reacher + MX).")
    ap.add_argument("email", nargs="*", help="alamat email (boleh banyak)")
    ap.add_argument("--dari-file", action="append", default=[], help="file teks/md/csv yang berisi email (boleh diulang)")
    ap.add_argument("--bagian", help="untuk file markdown: hanya baca bagian '## ...' yang judulnya memuat teks ini (mis. 'Antrian siap dikirim')")
    ap.add_argument("--keluar", help="simpan hasil ke CSV ini")
    ap.add_argument("--server", default=os.environ.get("REACHER_SERVER", "http://localhost:8080/v0/check_email"))
    ap.add_argument("--cli", default=os.environ.get("REACHER_CLI", ""), help="jalur biner check_if_email_exists (menggantikan server)")
    ap.add_argument("--dari", default=os.environ.get("REACHER_FROM", ""), help="alamat MAIL FROM untuk uji SMTP (domain yang kamu miliki)")
    ap.add_argument("--halo", default=os.environ.get("REACHER_HELLO", ""), help="hostname untuk HELO")
    ap.add_argument("--proxy", default=os.environ.get("REACHER_PROXY", ""), help="proxy SOCKS5 host:port bila perlu")
    ap.add_argument("--batas", type=float, default=60.0, help="detik per email")
    ap.add_argument("--maks", type=int, default=MAKS_PER_JALAN, help="maksimal email per jalan")
    ap.add_argument("--tanpa-reacher", action="store_true", help="hanya sintaks + MX")
    ap.add_argument("--cek-siap", action="store_true", help="cek DNS, port 25, dan Reacher lalu berhenti")
    a = ap.parse_args()

    if a.tanpa_reacher:
        a.server = ""
        a.cli = ""
    if a.cek_siap:
        sys.exit(cek_siap(a))

    daftar = list(a.email)
    for f in a.dari_file:
        with open(f, encoding="utf-8", errors="replace") as fh:
            isi = fh.read()
            if a.bagian:
                isi = ambil_bagian(isi, a.bagian)
            daftar += ambil_email(isi)
    daftar = [e.lower() for e in dict.fromkeys(daftar)]
    # alamat milik pengirim sendiri tidak perlu diperiksa (diisi lewat variabel lingkungan, dipisah koma)
    lewati = {x.strip().lower() for x in os.environ.get("VERIFIKASI_LEWATI", "").split(",") if x.strip()}
    daftar = [e for e in daftar if e not in lewati]
    if not daftar:
        print("Tidak ada email untuk diperiksa.")
        sys.exit(3)
    if len(daftar) > a.maks:
        print("Ada %d email; hanya %d pertama yang diperiksa jalan ini (batas --maks)." % (len(daftar), a.maks))
        daftar = daftar[: a.maks]

    baris = []
    for i, e in enumerate(daftar):
        status, cat = cek_satu(e, a)
        tindakan, arti = TINDAKAN.get(status, ("TANYA FELIX", ""))
        baris.append({"email": e, "status": status, "tindakan": tindakan, "catatan": cat or arti,
                      "dicek": time.strftime("%Y-%m-%d %H:%M")})
        print("%-34s %-14s %-12s %s" % (e, status, tindakan, cat or arti), flush=True)
        if i < len(daftar) - 1 and (a.cli or a.server):
            time.sleep(JEDA_DETIK)

    hitung = {}
    for b in baris:
        hitung[b["tindakan"]] = hitung.get(b["tindakan"], 0) + 1
    print()
    print("Ringkasan: %d dicek · KIRIM %d · TANYA FELIX %d · BUANG %d" % (
        len(baris), hitung.get("KIRIM", 0), hitung.get("TANYA FELIX", 0), hitung.get("BUANG", 0)))
    if a.keluar:
        os.makedirs(os.path.dirname(os.path.abspath(a.keluar)), exist_ok=True)
        with open(a.keluar, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=["email", "status", "tindakan", "catatan", "dicek"])
            w.writeheader()
            w.writerows(baris)
        print("Disimpan: " + a.keluar)
    sys.exit(0)


if __name__ == "__main__":
    main()
