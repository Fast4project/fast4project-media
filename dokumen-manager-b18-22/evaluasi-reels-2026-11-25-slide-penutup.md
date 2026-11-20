# Rekap proses dan evaluasi edit: Reels "Slide terakhirmu cuma terima kasih?" (Rab 25 Nov 2026)

Agent 6 lewat `/manager lanjut A6`, Felix di layar, Jum 20 Nov 2026. Seri S-A, TOFU, tema A, usaha contoh Kopi Lereng Ranu (usaha karangan untuk portofolio). Empat versi dalam satu sesi. Hasil akhir **V4 siap-unggah** (`video/2026-11-25-slide-penutup/final-v4.mp4`). Aturan yang lahir dari sini ada di `alur/video.md` bagian "Koreksi Felix 20 Nov 2026 (B18.22)" dan `claude/prosedur-manager-agent6-video.md` A.4 dan A.6 butir 22–24.

## 1 · Jalannya pekerjaan

| Versi | Yang berubah | Hasil ukur | Perintah atau keputusan Felix |
|---|---|---|---|
| V1 | Produksi dari nol: naskah ditulis di laptop (berkas Project tidak ada di laptop), VO Liam satu tarikan, tema A, musik hangat −17 dB | retensi 5/6 (G3 41% setelah 2 putaran), 33,5 dtk, −14,5 LUFS | "produksi disini dari 0 sesuai prosedur" |
| V2 | Musik hangat dinaikkan ke −12 dB | −14,4 LUFS | **"tambahkan background music nya"**: musik −17 dB tidak terdengar |
| V3 | Trek baru `semangat` 112 BPM (kick, clap, hi-hat, bas, stab) | energi >300 Hz 39%, narator +19,7 dB di pita bicara | **"background music stimulatif ada beatnya"** |
| V4 | Naskah tengah ditulis ulang tanpa jargon, VO baru, adegan disusun ulang (14 adegan), trek `beat-pelan` 88 BPM | **retensi 6/6** (G3 28%), 38,9 dtk, −14,4 LUFS | **"pembahasan tengah diperjelas, penjelasan lebih sederhana, dilarang jargon; beat lebih slow"** |

## 2 · Evaluasi: apa yang kurang dan kenapa

| Yang dikoreksi Felix | Penyebab | Perbaikan yang dipakai |
|---|---|---|
| Musik latar tidak terasa | Trek pad −17 dB di bawah narator hilang di speaker HP (masalah yang sama dengan 19 Nov) | Musik di −12 dB (`--celah-db 8 --turun-db 4`) |
| Musik kurang menggugah | Trek pad/petikan tanpa ketukan | Trek berketukan buatan kode (kick + clap + hi-hat + bas + akor pendek + efek pompa) |
| Ketukan terlalu cepat | 112 BPM dengan hi-hat seperenambelas terasa terburu-buru di bawah narasi | **88 BPM**, hi-hat dan petikan seperdelapan (`beat-pelan`) |
| Isi tengah kurang jelas | (1) Contoh tidak menyebut siapa menjual ke siapa, jadi "uji coba di kedaimu" tidak punya konteks. (2) Kata yang terdengar wajar bagi pembuat tapi asing bagi pemilik usaha: "dek", "permintaanmu", "uji coba", "sampel", "langkah pertama". (3) "kamu" (pembuat presentasi) dan "kami" (usaha contoh) tercampur dalam satu kalimat | Satu kalimat konteks sebelum membedah ("penjual biji kopi, kirim presentasi ke pemilik kafe"), jargon diganti kata sehari-hari, contoh diberi penanda "Di contoh ini:" |

Tabel ganti kata (V1 → V4): dek → presentasi · permintaanmu → tulis apa yang kamu minta · uji coba → coba · sampel → satu bungkus · langkah pertama → cara mulai yang gampang · kontak → siapa yang bisa dihubungi.

## 3 · Evaluasi teknis rakit (ditemukan sendiri, diperbaiki tanpa bertanya)

1. **Lafal dicek gratis dengan transkrip Scribe** (`creative_transcribe_audio` disambung ke node suara). Transkrip memberi waktu tiap kata, lalu dipetakan ke garis waktu yang heningnya sudah dipendekkan (`waktu_kata.py`). Titik potong adegan diturunkan dari kata, bukan ditebak.
2. **Uji strip sebelum render penuh menemukan 7 cacat:** penanda 1-2-3 menimpa kata "kasih", judul panjang terpotong di kanan (lupa kelas `fit`), halftone menyentuh judul dan label, label karangan satu baris keluar layar, teks baris kartu 38 px terlalu kecil, cincin tinta lepas dari logo saat kartu berdenyut, kata "atau" abu-abu tak terbaca di pil oranye.
3. **1,2 dtk layar kosong** sebelum pil MAKASIH dan kartu "3 hal" muncul. Perbaikannya: elemen tampil samar sejak awal adegan, lalu menyala tepat di katanya.
4. **G3 detik mati 41% di V1** walau sudah 2 putaran (tekstur 8 fps, napas kartu, kamera lebih hidup). Yang menurunkannya ke 28% di V4 adalah **adegan yang lebih pendek** (14 adegan × 1,7–4,5 dtk), dipotong di awal tiap kalimat. Geser halaman penuh tema A menaikkan rata-rata gerak, jadi adegan panjang yang tenang terhitung diam.
5. **Ukuran file 140 MB** karena tekstur 8 fps. Encode ulang `-crf 22 -maxrate 8M` dengan audio disalin menjadi 32–38 MB.
6. **Peringatan "tepi 0 px" dari cek-posisi-tengah palsu** (grid penuh layar). Yang dipakai: titik berat 40–53% dan melihat frame.
7. **Durasi bertambah** dari 33,5 ke 38,9 dtk setelah penjelasan ditambah. Felix memilih kejelasan; durasi > 28 dtk dicatat, tidak menahan tayang.

## 4 · Biaya

Empat versi. Suara ElevenLabs: 507 × 2 take (V1) + 627 × 2 take (V4) ≈ 2.270 kredit dari kuota 40.000. Transkrip Scribe 0 kredit. Render penuh ±3–4 menit per putaran.

## 5 · Yang belum terverifikasi

- Telinga Felix: musik `beat-pelan` di HP, lafal "we-a" dan "Kopi Lereng Ranu".
- Durasi 38,9 dtk terhadap skip rate: dinilai pasca-tayang (≥ 7 hari) di `claude/papan-skor-reels.md`.
