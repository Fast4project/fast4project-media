# Batas harian dan jeda

| Batas | Nilai | Asal |
|---|---|---|
| Alamat per jalan skrip | **30** (`MAKS_PER_JALAN`, bisa diubah dengan `--maks`) | skrip |
| Jeda antar alamat | **2 detik** (`JEDA_DETIK`), supaya server surat tidak menganggap penyerang | skrip |
| Waktu tunggu per alamat | **60 detik** (`--batas`) | skrip |
| Target draf outreach | **10 per hari kerja (Sen sampai Sab) = 60 per minggu**, ke usaha yang berbeda | aturan B11 |
| Riset per batch | paling banyak **20 pencarian** | aturan B11 |

## Catatan
- Target 10 per hari adalah batas atas, bukan paksaan. Prospek sah kurang dari 10: masukkan yang sah, jangan padding, catat jumlah dan penyebabnya.
- 10 draf per hari ada di bawah batas 30 per jalan, jadi satu jalan cukup untuk satu hari.
- Skrip tidak mengirim email apa pun. Verifikasi hanya membuka percakapan SMTP sampai tahap pemeriksaan penerima.
- Batas pengiriman Gmail dan batas layanan pihak ketiga tidak diatur oleh skrip ini dan tidak tertulis di sini.

