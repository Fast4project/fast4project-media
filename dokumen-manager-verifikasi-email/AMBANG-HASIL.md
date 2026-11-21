# Ambang hasil

Enam status yang dipakai Manager, dipetakan ke tindakan oleh `verifikasi_email.py`.

| Status | Tindakan | Artinya |
|---|---|---|
| `safe` | **KIRIM** | kotak surat terdeteksi ada dan menerima surat |
| `risky` | **TANYA FELIX** | catch-all, kotak penuh, atau tidak pasti; bisa terkirim, bisa mental |
| `unknown` | **TANYA FELIX** | server tidak menjawab pasti (sering Gmail atau Outlook, atau port 25 diblokir) |
| `mx-saja` | **TANYA FELIX** | Reacher tidak tersedia; hanya sintaks dan MX yang dicek, kotak surat belum diperiksa |
| `invalid` | **BUANG** | alamat tidak ada atau dinonaktifkan; jangan dikirim |
| `tanpa-mx` | **BUANG** | domain tidak punya server surat |

Status ketujuh, `sintaks-salah` (bentuk alamat tidak sah), juga **BUANG**.

## Cara membaca
- Hanya `safe` yang berstatus KIRIM. Selain itu Felix yang memutuskan.
- `mx-saja` bukan lolos. Artinya alamat belum terbukti ada. Kalau semua hasil `mx-saja`, penyebabnya hampir selalu port 25 tertutup, bukan alamatnya buruk.
- `invalid`, `tanpa-mx`, dan `sintaks-salah`: draf Gmail dibuang oleh Felix, alamat tidak dikirim.
- Status ini bukan jaminan. Bounce nyata hanya terlihat setelah kirim.

## Kode keluar skrip
0 selesai (ada atau tidak ada alamat buruk) · 2 mesin tidak siap · 3 tidak ada alamat untuk diperiksa.
