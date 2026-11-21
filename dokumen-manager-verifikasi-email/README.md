# Verifikasi email prospek (salinan baca untuk Manager cloud)

Salinan dokumentasi dari laptop Felix. Dibagikan supaya Manager cloud tahu cara kerja alat, apa arti hasilnya, dan batasnya. **Cloud tidak menjalankan alat ini**: port 25 di cloud tertutup, jadi verifikasi hanya jalan di laptop.

Skrip di folder ini sudah dibersihkan: tanpa alamat email, tanpa kunci, tanpa daftar prospek. Perilaku sama dengan versi laptop, kecuali daftar alamat yang dilewati kini dibaca dari variabel lingkungan `VERIFIKASI_LEWATI`.

| Berkas | Isi |
|---|---|
| `verifikasi_email.py` | Pembungkus Python tanpa pip: baca alamat dari argumen atau file, tanya Reacher, petakan ke tindakan, simpan CSV |
| `AMBANG-HASIL.md` | Enam status hasil dan tindakannya |
| `CARA-PAKAI.md` | Cara memakai `/verifikasi-email` dan skrip |
| `BATAS-HARIAN.md` | Batas volume dan jeda |

## Mesin
**Reacher** (github.com/reacherhq/check-if-email-exists, lisensi MIT). Cek sintaks, MX, SMTP, kotak dinonaktifkan atau penuh, catch-all, alamat peran. Dijalankan lewat Docker di `127.0.0.1:8080`, atau lewat biner CLI.

## Kesiapan (`--cek-siap`)
Memeriksa tiga hal: alat DNS, **port 25 keluar terbuka**, dan Reacher hidup. Port 25 tertutup (umum di jaringan rumah dan seluler) berarti kotak surat tidak bisa diperiksa. Skrip lalu turun ke `mx-saja` (hanya sintaks + MX).

## Batas jujur
- Hasil adalah tebakan berbasis protokol SMTP, bukan jaminan. Bounce nyata hanya terlihat setelah kirim.
- Skrip diuji hanya terhadap server Reacher tiruan dan jalur `mx-saja`. Jalur Reacher asli belum pernah berjalan penuh.
- Verifikasi tidak menambah jumlah prospek; ia hanya menyaring. Pasokan alamat tetap dari situs resmi usaha.
- Alamat tetap harus tertulis di situs atau profil resmi usaha itu. Dilarang menebak pola alamat lalu "memverifikasinya".
- Hasil CSV hanya disimpan di laptop dan tidak pernah masuk repo ini.
