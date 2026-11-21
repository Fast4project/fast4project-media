# Cara pakai `/verifikasi-email`

Perintah ini dijalankan di laptop Felix, bukan di cloud. Argumen: satu atau beberapa alamat, atau kosong untuk seluruh bagian "Antrian siap dikirim" di berkas antrian outreach.

## Langkah perintah
1. Jalankan `python alat/verifikasi-email/verifikasi_email.py --cek-siap`. Kode keluar 2 berarti ada yang kurang (Docker atau Reacher belum jalan, atau port 25 tertutup). Lanjut dengan `--tanpa-reacher` bila Felix setuju; hasilnya hanya sintaks dan MX (`mx-saja`).
2. Ada alamat di argumen: periksa alamat itu. Argumen kosong: baca bagian "Antrian siap dikirim" dan jalankan skrip dengan `--dari-file ... --bagian "Antrian siap dikirim" --keluar <berkas CSV>`.
3. Lapor ke Felix satu baris per usaha: usaha, status, tindakan. Kelompokkan: KIRIM, TANYA FELIX, BUANG. Untuk BUANG: "hapus draf Gmail untuk usaha itu, jangan dikirim".
4. Perbarui kolom Verifikasi di berkas antrian lokal (status dan tanggal). Jangan mengubah isi draf, jangan mengirim apa pun, jangan menghapus draf Gmail sendiri.
5. Di bawah `/manager otomatis`: tulis hanya **jumlah** di status laptop, misalnya `{"dicek": n, "kirim": n, "tanya": n, "buang": n}`. Alamat dan nama usaha tetap di laptop karena berkas status bersifat publik.
6. Sebut batasnya sekali: hasil adalah tebakan protokol SMTP, bukan jaminan.

## Contoh pemanggilan skrip
```
python alat/verifikasi-email/verifikasi_email.py --cek-siap
python alat/verifikasi-email/verifikasi_email.py <alamat-1> <alamat-2>
python alat/verifikasi-email/verifikasi_email.py --dari-file <berkas-antrian>.md --bagian "Antrian siap dikirim" --keluar <berkas>.csv
python alat/verifikasi-email/verifikasi_email.py <alamat> --tanpa-reacher
```

## Opsi penting
| Opsi | Fungsi |
|---|---|
| `--cek-siap` | cek DNS, port 25, dan Reacher lalu berhenti |
| `--tanpa-reacher` | hanya sintaks + MX |
| `--keluar` | simpan hasil ke CSV (hanya di laptop) |
| `--maks` | batas alamat per jalan (bawaan 30) |
| `--batas` | detik tunggu per alamat (bawaan 60) |
| `--cli` / `--server` | jalur biner Reacher atau alamat server Reacher |

Variabel lingkungan opsional: `REACHER_SERVER`, `REACHER_CLI`, `REACHER_FROM`, `REACHER_HELLO`, `REACHER_PROXY`, `VERIFIKASI_LEWATI` (alamat pengirim yang dilewati, dipisah koma).
