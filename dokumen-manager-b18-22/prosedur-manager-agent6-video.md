# Prosedur Manager untuk Agent 6: satu Reels dari ide sampai siap-unggah (B18.21)

Ditetapkan Felix 18 Nov 2026 lewat prompt prosedur lengkap, dijawab "1a 2b 3a". Berkas ini **menggantikan** aturan lama yang berbeda soal suara, audio, rakit, dan tenggat video. Yang tidak disebut di sini tetap memakai `alur/video.md` (termasuk B18.19), B18.7, B18.8, B18.11, B18.20, dan `claude/agent-manager.md`.

Keputusan Felix yang membentuk berkas ini:
- **Tenggat (1a):** MP4 versi dasar paling lambat 15.00. Versi final `siap-unggah` sudah ter-push **sebelum 18.00**, karena 18.00 adalah pemeriksaan penentu Manager cloud untuk Reels 19.30.
- **Berkas alat (2b):** nama berkas yang belum ada di folder fast4project ditandai **[PERLU DICEK FELIX]** sampai Felix menyalinnya dari laptop pembuat video.
- **Suara (3a):** standar 18-19 Nov menggantikan aturan lama sepenuhnya. Baris "minimal suara bawaan (edge-tts)" di B18.7 butir 1 tidak berlaku lagi untuk video final.
- **Musik latar sederhana (Felix 19 Nov 2026, berlaku mulai video berikutnya):** setiap Reels baru boleh dan sebaiknya memakai musik latar tipis buatan kode, di bawah narator. Aturannya di bagian A.6 butir 13 sampai 16. Ini menggantikan kalimat "tanpa musik latar" di `alur/video.md` bagian 3 dan 3c. Aturan nol lagu berhak cipta tidak berubah: musiknya disintesis dari kode, bukan lagu orang.

Pertentangan yang ditemukan dan cara menyelesaikannya ada di bagian akhir.

---

## A. Prompt prosedur Manager → Agent 6

### 1. Peran dan batas
| Pihak | Boleh | Tidak boleh |
|---|---|---|
| **Manager** (cloud) | memilih ide, menulis naskah dan brief, memberi perintah ke laptop, menilai laporan dengan daftar periksa D, bertanya ke Felix, menayangkan setelah Felix mengetik "unggah" | memproduksi video, mengubah seri atau niche tanpa Felix, menayangkan tanpa persetujuan |
| **Agent 6** (Content Media Expert) | menulis ulang naskah dalam batas brief, membuat suara, merakit, QC, mengisi status | menayangkan, mengubah seri, mengarang angka atau klien |
| **Laptop (Claude Code)** | menjalankan produksi, QC, mengunggah media ke repo, mengisi dan mendorong `status/laptop.json` | memposting ke Instagram atau TikTok |
| **Felix** | memilih opsi, menjawab "Unggah sekarang / Revisi / Tunda / Batalkan", memutuskan harga dan penghapusan | tidak diminta memeriksa hal teknis satu per satu |

Laporan ke Felix: pendek, satu langkah, langsung bisa dieksekusi (Felix pengidap ADHD).

### 2. Langkah 0: fakta keras
- fast4project: jasa desain slide, pitch deck, katalog usaha, presentasi, milik Felix.
- Kalimat posisi (sejak 16 Nov 2026): "Presentasi, pitch deck, katalog usaha, dan konten yang membangun trust: rapi dan meyakinkan, dibantu AI."
- Seri wajib, satu per video: S-A Kesalahan umum · S-B Istilah investor · S-C Bedah slide · S-D Angka dan klaim · S-E Katalog usaha · S-F Presentasi kuliah/kerja · S-G Konten yang membangun trust (field `audiens` umkm atau kreator wajib). **Di luar seri = BLOKIR.**
- Jadwal: Reels Senin sampai Sabtu 19.30 WIB. Laptop jalan 10.00 dan 15.00. Manager cloud memeriksa 09.00, 12.00, 15.00, 18.00, 21.00.
- **Nol** harga. **Nol** kata "klien". **Nol** janji hasil. **Nol** angka karangan (angka contoh berlabel "ilustratif"). Usaha contoh berlabel "usaha karangan untuk portofolio" di layar.
- **Nol** wajah buatan AI, **nol** avatar, **nol** lagu berhak cipta.
- Narator AI tanpa nama dan tidak pernah memakai "saya" untuk pengalaman.
- Tidak ada yang diunggah tanpa Felix mengetik "unggah" untuk file **persis itu**. Laptop tidak pernah memposting (B18.8).

### 3. Memilih ide
1. **Gerbang sinkron tayang.** Tarik semua posting Instagram, termasuk Reels, lewat Windsor. Cek tumpang tindih topik dengan yang sudah tayang dan dengan `claude/pantangan-topik.md`. Tumpang tindih = ganti ide.
2. **Rotasi seri.** Seri yang sama maksimal dua hari berturut-turut. Ikuti porsi seri minggu itu yang sudah disetujui Felix.
3. **Level funnel** ditulis di brief: TOFU, MOFU, atau BOFU, dengan pemicu komentar yang cocok levelnya.
4. Ide di luar seri atau kena pantangan = BLOKIR. Pakai naskah cadangan, jangan memaksa.

### 4. Menulis naskah
1. **Hook** berisi masalah nyata yang dialami penonton, tanpa jargon.
2. **Istilah** dijelaskan di baris 2 dengan konteks dan maksudnya.
3. **Semua yang tampil di layar diucapkan** oleh narator.
4. **Payoff** sebelum dan sesudah muncul di 55 sampai 80 persen durasi.
5. **Penutup** menggemakan hook.
6. **Pemicu komentar** satu kata atau satu angka.
7. **Rantai teks:** `/gaya-ngomong-gaul` → `/copy-hangat-berlogika` → `/stop-slop` → cek tulisan manusia (`python alat/cek-tulisan-manusia.py <berkas> --jenis vo`, KRITIS nol; untuk caption `--jenis caption`). Cek VO dijalankan pada **bahan suara** (angka dan singkatan sudah ditulis seperti dibaca).
8. Dilarang pengalaman, klien, atau angka karangan (B18.20).
9. **Tengah pembahasan sejelas Reels 25 Nov V4 (Felix 20 Nov, B18.22):** contoh usaha dibuka dengan satu kalimat siapa menjual apa ke siapa; jargon diganti kata sehari-hari (dek → presentasi, permintaan → apa yang kamu minta, sampel → satu bungkus, langkah pertama → cara mulai); tiap butir = perintah sehari-hari + contoh konkret dengan penanda "Di contoh ini:"; "kamu" untuk penonton, "kami/mereka" untuk usaha contoh. Kejelasan menang atas durasi. Rincian: `alur/video.md` B18.22 butir 1–5.

### 5. Tema edit A sampai D
Pilih satu tema dan tulis alasannya satu kalimat. Tema yang sama tidak dipakai tiga kali berturut-turut. Satu video memakai satu jenis transisi.

### 6. Standar suara, audio, dan rakit (koreksi Felix 18-19 Nov 2026, tidak boleh dilemahkan)
1. Narator = ElevenLabs "Liam - Energetic, Social Media Creator", resep Reels 13 Nov: model `eleven_multilingual_v2`, **tanpa tag emosi**, intonasi profesional, tenang, hangat, jelas, enak didengar, tidak antusias berlebihan.
2. Seluruh naskah dibuat dalam **satu tarikan** (satu generate), bukan per baris. Jeda diatur tanda baca.
3. Lewat API: stability 0,35, similarity 0,75, style 0,35, speaker boost, speed 1,10, `language_code` id. Lewat connector: model dan suara sama, kecepatan asli.
4. **Dilarang:** edge-tts untuk video final · `eleven_v4` bertag emosi sebagai default · meregangkan tempo di laptop (rubberband atau atempo membuat suara bindeng) · SFX berpita sempit · lowpass pada SFX · tunda Haas, pelebar stereo, atau reverb (membuat suara mantul).
5. Durasi diatur dengan **memendekkan hening saja** (`video/_bangun/susun_vo_hd.py`) atau memadatkan naskah sebelum suara dibuat. Lebih dari 28 detik = catatan, tidak menahan tayang.
6. Ejaan bahan suara boleh disesuaikan supaya dibaca benar (angka seperti dibaca, "DM" jadi "di-em", "WA" jadi "we-a"). Teks layar dan caption tidak berubah. Kata yang salah lafal dibuat ulang.
7. Volume per baris: hook dan ajakan +1,5 sampai +2 dB, baris sindiran atau pelan −3 dB, supaya LRA ≥ 3.
8. Audio: VO highpass 70 Hz saja. SFX dari `video/_sfx-hd/` (48 kHz rentang penuh, tanpa gema). Mix lewat `video/_bangun/campur_hd.py <folder> --musik <tenang|hangat>`. Target −14,3 ± 0,5 LUFS, true peak ≤ −1,5 dBFS, AAC 320k.
9. **Urutan rakit:** naskah terkunci → cek tulisan manusia (KRITIS nol) → suara satu tarikan → waktu frasa → titik potong adegan di awal frasa → adegan (tema edit A sampai D, satu jenis transisi) → peta SFX per ketukan → uji strip frame → render → mix → QC. Ganti suara = semua ketukan adegan dan SFX disusun ulang dari waktu frasa yang baru.
10. Adegan ≤ 4,5 detik. Teks hook + kata pertama VO + SFX hit serentak di detik 0. Benda yang disebut muncul ≤ 0,3 detik setelah katanya. Latar tidak pernah beku. Isi di pita tengah (titik berat 40 sampai 55 persen, margin kiri ≥ 80 px, kanan ≥ 110 px). Label karangan di y ≈ 1372. Hiasan tidak menyentuh teks.
11. QC wajib sebelum lapor (lihat bagian 7).
12. **Kuota suara habis → berhenti dan tanya Felix** dengan opsi tinggal pencet. Jangan turun ke edge-tts.
13. **Musik latar sederhana (Felix 19 Nov 2026).** Sumber hanya paket buatan kode `video/_musik-hd/` (dibuat `python -I -X utf8 video/_bangun/buat_musik_hd.py`, nol hak cipta). Dua trek: **`tenang`** (pad hangat + bas lembut, 76 BPM) untuk topik yang menjelaskan atau serius, **`hangat`** (pad + petikan tipis, 92 BPM) untuk topik ringan atau ajakan. Pilih satu dan tulis alasannya satu kalimat di brief. Trek yang sama tidak dipakai tiga Reels berturut-turut. Lagu dari pustaka Instagram, TikTok, atau internet **dilarang** tertanam, walau bebas royalti, kecuali Felix menyebut sumbernya dan lisensinya tercatat.
14. **Tingkat dan cara mix.** Musik selalu di bawah narator dan tidak pernah bersaing dengan SFX. Otomatis oleh `campur_hd.py --musik`: musik dikecilkan mengikuti tingkat narator, di celah hening ±10 dB di bawah narator, saat narator bicara turun 7 dB lagi (±17 dB di bawah narator), masuk halus 0,1 detik dan keluar 1,6 detik di akhir. Mono di tengah, **tanpa lowpass, tanpa Haas, tanpa pelebar stereo, tanpa reverb** (larangan yang sama dengan SFX). Angka tingkat tidak diubah tanpa Felix.
15. **Syarat lolos.** Musik tidak mengubah target butir 8 (−14,3 ± 0,5 LUFS, true peak ≤ −1,5 dBFS, LRA ≥ 3). Setelah mix, baca baris keluaran `campur_hd.py`: narator X dBFS, musik saat bicara ±17 dB di bawahnya. Kata narator harus tetap jelas; musik yang menenggelamkan satu kata = turunkan, bukan naikkan narator. Sesi tanpa layar tidak bisa mendengar: tulis di `qc` "musik belum didengar Felix".
16. **Tidak ada musik** bila Felix bilang tanpa musik untuk video itu, atau bila videonya sudah bergantung pada keheningan (jeda dramatis). Jalankan `campur_hd.py` tanpa `--musik`. Reels yang sudah siap-unggah atau tayang tidak dirakit ulang hanya untuk menambah musik.
17. **Musik harus terasa di HP (koreksi Felix 19 Nov malam, rombak bedah-dana).** Trek `tenang` (pad + bas) hilang di speaker HP pada −17 dB. Trek ketiga **`penasaran`** (100 BPM, petikan arpeggio register tengah + ketukan lembut + pad, `video/_bangun/buat_musik_penasaran.py`) untuk Reels bedah/temuan. Untuk trek berirama ini pakai `campur_hd.py <folder> --musik penasaran --celah-db 8 --turun-db 4` (±12 dB di bawah narator saat bicara). Narator tetap jelas; target loudness butir 8 tidak berubah.
17b. **Trek berketukan `semangat` (Felix 20 Nov, Reels slide-penutup: "background music stimulatif ada beatnya").** 112 BPM, kick + clap + hi-hat + bas sinkopasi + stab akor + efek pompa, dibuat `video/_bangun/buat_musik_semangat.py` (nol hak cipta), diseimbangkan supaya terdengar di HP (energi > 300 Hz ≥ 35%). Campur seperti trek berirama: `--musik semangat --celah-db 8 --turun-db 4` (±12 dB di bawah narator). Cek pita bicara 1–4 kHz: narator tetap ≥ 15 dB (median) di atas musik. Versi lebih pelan (Felix 20 Nov: "beat music yang lebih slow bpm nya"): `buat_musik_semangat.py 88 beat-pelan` (88 BPM, hi-hat dan petikan seperdelapan), campur sama. Pilihan trek sekarang: tenang · hangat · penasaran · semangat · beat-pelan; trek yang sama tidak dipakai tiga Reels berturut-turut.
18. **Tanpa ganti warna latar antarpotongan (koreksi Felix 19 Nov).** Mengganti warna latar atau memberi garis kilat di tiap potongan terlihat seperti pindah adegan dan mengganggu. Satu warna latar sepanjang video. Potongan = tata letak baru dengan warna sama. Gerak hidup didapat dari: tekstur kertas halus berganti 8 fps, dorong kamera vertikal pelan, dan objek yang masuk tepat di katanya.
19. **Alur yang bikin penasaran (koreksi Felix 19 Nov).** Hook tampil utuh di frame 0, lalu buka loop dalam 3 detik pertama, misalnya tiga penanda merah bernomor jatuh ke slide contoh ("ada 3 lubang"). Selama isi, tampilkan peta progres kecil (kanan atas) yang mencentang tiap lubang yang selesai dibedah. Sebelum ajakan, tampilkan hasil (ringkasan perbaikan). Naskah VO tidak diubah untuk ini: hook dikuatkan lewat visual dan ritme.
20. **Pertanyaan penutup tidak dipotong cepat (koreksi Felix 20 Nov).** Bagian "dari tiga temuan ini, … yang mana?" = **satu adegan mengalir**: ringkasan bernomor (1 … · 2 … · 3 …, isinya kata yang sudah diucapkan) masuk satu per satu, lalu judul pertanyaan, lalu baris menyala tepat saat angkanya diucapkan, lalu ajakan komentar. Penonton harus tahu arti tiap angka sebelum diminta menjawab. Adegan ini boleh > 4,5 dtk (G4 = catatan B12.2).
21. **Teknis rakit kode yang wajib (pelajaran rombak bedah-dana).** (a) `transform` tiap elemen ditulis ulang tiap frame, jangan ditambah ke nilai lama (skala punch menumpuk dan judul membesar keluar layar). (b) Zoom punch pada teks memakai titik asal kiri dan lebar teks ≤ 820 px supaya margin tetap ≥ 80/110. (c) File hasil > ±50 MB (tekstur menahan kompresi) di-encode ulang `-crf 22 -maxrate 8M` dengan audio disalin, sebelum `unggah_media.py`. (d) Frame QC diambil dari **file final** (`ffmpeg -ss`), bukan hanya dari uji HTML. (e) Penggantian string lewat PowerShell yang memakai `` `n `` atau backtick sering memotong kode: periksa baris hasilnya, atau pakai Edit.

22. **Musik bawaan = `beat-pelan` 88 BPM (Felix 20 Nov, B18.22).** `buat_musik_semangat.py 88 beat-pelan`, campur `--musik beat-pelan --celah-db 8 --turun-db 4`. Ini menggantikan bawaan `tenang`/`hangat` −17 dB di butir 13–14 (tidak terdengar di HP). Cek di `qc`: energi > 300 Hz ≥ 35% dan narator ≥ 15 dB di atas musik pada pita 1–4 kHz.
23. **Waktu dari transkrip, adegan pendek (pelajaran Reels 25 Nov).** Lafal dicek dan waktu kata diambil dari transkrip Scribe (0 kredit), dipetakan ke VO yang heningnya dipendekkan (templat `video/2026-11-25-slide-penutup/waktu_kata.py`). Titik potong di awal tiap kalimat, adegan 1,7–4,5 dtk, judul layar = kata yang diucapkan, tidak ada layar kosong > 1 dtk (elemen tampil samar dulu, menyala di katanya).
24. **Uji strip dua kali dengan daftar periksa B18.22 butir 11** sebelum render penuh: penanda tidak menimpa teks, judul panjang `fit`, hiasan ≥ 30 px dari teks dan label, label karangan dua baris di dalam layar, teks kartu ≥ 38 px, coretan tinta ikut transform kartu, teks pendamping di elemen yang menyala ikut warna.

### 7. Kartu skor dan QC
Sebelum melapor, laptop menjalankan semuanya dan menulis hasilnya satu baris di field `qc`:
- `ukur-retensi` G1 sampai G6 (`video/_referensi-gaya/ukur-retensi.py`)
- `cek-format` (`video/_referensi-gaya/cek-format.py`)
- LUFS, true peak, LRA (dengan musik tetap harus di target butir 6.8)
- tingkat musik terhadap narator (baris keluaran `campur_hd.py --musik`), dicatat di `qc`
- cek galat halaman
- lembar frame dari `final.mp4` **dilihat**, bukan hanya dibuat
- `cek-posisi-tengah` (`alat/cek-posisi-tengah.py`)
- `cek-overlap` (`alat/cek-overlap.py`)
- `cek-tulisan-manusia` untuk VO dan caption

Format satu baris: `qc: G1-G6 <lolos|catatan> · format <ok> · LUFS <n> · TP <n> · LRA <n> · musik <tenang|hangat|tanpa> −17 dB di bawah narator, belum didengar Felix · galat halaman <0> · frame dilihat <ya> · posisi tengah <ok> · tulisan manusia KRITIS <0>`

Gerbang hook dan retensi **tidak menahan tayang**: maksimal dua putaran perbaikan, sisanya dicatat di `papan-skor-reels.md`. **Yang menahan tayang hanya:** BLOKIR · klaim atau angka tanpa label · harga · janji hasil · teks rusak · kata KRITIS.

### 8. Serah terima
Per item di `status/laptop.json` (jangan menulis materi klien, nama orang, atau angka keuangan karena isinya publik):
`format, nama, seri, audiens, tema, jam_tayang, status, judul, caption (persis), caption_tiktok (≤ 150 karakter sebelum tagar), urls, qc, alasan_pilihan`
- Status: `dikerjakan`, `siap-unggah`, `terhambat`. Versi revisi menambah `ganti_dari`.
- Unggah URL publik: `python alat/unggah_media.py --folder <nama> --file video/<tanggal>-<slug>/final.mp4`, kode keluar 0 wajib.
- Versi dasar ter-push sebelum 15.00. Versi final `siap-unggah` ter-push **sebelum 18.00**.
- `STATUS.md` di tiap folder `video/<tanggal>-<slug>/` memuat status terakhir dan hasil QC.
- MP4 asli tanpa watermark disimpan di folder yang sama untuk TikTok (B17).

### 9. Gerbang Felix
1. Manager menawarkan pratinjau, lalu satu pertanyaan opsi: **Unggah sekarang / Revisi / Tunda / Batalkan**.
2. Revisi suara, audio, atau visual dikerjakan **tanpa rencana baru**. Versi lama dipindah ke `arsip/`. Versi revisi disimpan sebagai file baru (misalnya `final-v2.mp4`), tidak menimpa file yang sudah disetujui, lalu diserahkan lagi untuk konfirmasi.
3. Tidak dijawab sampai tenggat → Manager menjelaskan opsi tayang apa adanya (bila lolos syarat), tayang besok, atau naskah cadangan. Tidak pernah tayang tanpa persetujuan.

### 10. Keputusan
- **Teknis** (QC gagal, suara salah lafal, posisi teks): diperbaiki sendiri.
- **Isi dan selera** (hook mana, tema mana): dikumpulkan jadi **satu** pertanyaan opsi.
- **Posting, harga, hapus file:** gerbang Felix.

---

## B. Templat brief produksi per Reels

Simpan sebagai `produksi-<tanggal>-<slug>.md`.

```
# Produksi Reels <hari> <tanggal> <jam tayang> WIB: <judul>

Seri: <S-A sampai S-G> · Audiens: <umkm|kreator|pemilik usaha|mahasiswa> · Level: <TOFU|MOFU|BOFU> · Tema edit: <A|B|C|D> (alasan satu kalimat)
Suara: Liam resep 13 Nov (multilingual v2, satu tarikan, tanpa tag, tanpa peregangan tempo)   ← baris ini TIDAK boleh diganti
Musik: <beat-pelan (bawaan)|semangat|penasaran|hangat|tanpa> (alasan satu kalimat; paket video/_musik-hd/, ±12 dB di bawah narator, trek tidak sama tiga Reels berturut-turut)
Contoh usaha: <nama> = <penjual apa> → <pembaca presentasinya siapa> (satu kalimat konteks, B18.22)
Gerbang sinkron tayang: <AMAN|BENTROK> (cek Windsor <tanggal>, daftar posting yang dibandingkan)
Bahan contoh: <usaha karangan untuk portofolio, berlabel di layar; angka berlabel ilustratif>

Hook (3 varian): <A> ← dipilih · <B> · <C>

| Detik | Teks layar / ucapan (petunjuk intonasi tenang, hanya catatan baca) | Visual |
|---|---|---|
| 0-1,5 | | |
| ... | | |

Pemicu komentar: <satu kata atau satu angka>

Caption (persis):
<teks>

caption_tiktok (persis, ≤ 150 karakter sebelum tagar, tanpa ajakan DM):
<teks>

Kriteria selesai:
- final.mp4 1080x1920 30 fps, VO Liam standar 18-19 Nov + SFX HD + musik latar sederhana + label karangan
- QC butir 7 lengkap dan satu baris qc terisi
- cek-tulisan-manusia KRITIS nol (VO dan caption)
- status/laptop.json = siap-unggah, ter-push sebelum 18.00
```

---

## C. Templat perintah Claude Code untuk laptop

```
/manager lanjut A6 produksi Reels <hari> <tanggal> 19.30 "<hook>" dari file produksi-<tanggal>-<slug>.md di Project. Hasil video/<tanggal>-<slug>/final.mp4 1080x1920 dengan VO Liam standar 18-19 Nov + SFX HD + musik latar beat-pelan (campur_hd.py --musik beat-pelan --celah-db 8 --turun-db 4) + label karangan, alur acuan B18.22 (Reels 25 Nov V4), QC lengkap, catat di status/laptop.json sebagai siap-unggah dan push sebelum 18.00 (versi dasar sebelum 15.00). Jangan ubah naskah, seri, atau niche, dan jangan memposting.
```

Untuk revisi: ganti kalimat pertama dengan `/manager lanjut A6 revisi Reels <tanggal>: <catatan Felix>`, simpan hasil sebagai `final-v2.mp4`, tulis `ganti_dari` di status.

---

## D. Daftar periksa akhir (Manager sebelum menawarkan "Unggah sekarang")

- [ ] Status item `siap-unggah`, jam diperbarui sebelum 18.00, `urls` terisi dan bisa dibuka
- [ ] Seri di daftar S-A sampai S-G, audiens terisi (S-G wajib), tema edit tidak sama tiga kali berturut-turut
- [ ] Gerbang sinkron tayang AMAN dan tidak kena pantangan topik
- [ ] Hook berisi masalah nyata, tanpa jargon; istilah dijelaskan; semua teks layar diucapkan
- [ ] Nol harga, nol kata "klien", nol janji hasil, nol angka karangan tanpa label "ilustratif"
- [ ] Label "usaha karangan untuk portofolio" ada di layar bila memakai usaha contoh
- [ ] Nol wajah buatan AI, nol avatar, nol lagu berhak cipta
- [ ] Suara Liam resep 13 Nov, satu tarikan, tanpa tag emosi, tanpa peregangan tempo; bukan edge-tts
- [ ] Musik latar dari `video/_musik-hd/` (bawaan `beat-pelan` ±12 dB, B18.22) atau "tanpa" dengan alasan; trek tidak sama tiga Reels berturut-turut; `qc` mencatat tingkat musik, energi > 300 Hz, selisih pita bicara, dan "belum didengar Felix"
- [ ] Tengah pembahasan: konteks siapa menjual ke siapa, nol jargon, tiap butir punya contoh konkret (B18.22)
- [ ] Baris `qc` lengkap: G1 sampai G6, format, LUFS −14,3 ± 0,5, true peak ≤ −1,5, LRA ≥ 3, galat halaman, frame dilihat, posisi tengah
- [ ] `cek-tulisan-manusia` KRITIS nol untuk VO dan caption
- [ ] `caption` persis dan `caption_tiktok` ≤ 150 karakter sebelum tagar, tanpa ajakan DM
- [ ] Tidak ada yang menahan tayang (BLOKIR, klaim tanpa label, harga, janji hasil, teks rusak, kata KRITIS)
- [ ] Revisi: file baru, `ganti_dari` terisi, file lama di `arsip/`

Bila satu kotak kosong: Manager memperbaiki yang teknis, mengumpulkan yang isi menjadi satu pertanyaan opsi, dan tidak menawarkan "Unggah sekarang" sebelum kotak lengkap.

---

## Pertentangan yang ditemukan (maksimal 5)

1. **Tenggat push:** prompt menulis 18.00 di satu tempat dan 15.00 di tempat lain. Diputuskan 1a: dasar 15.00, final sebelum 18.00.
2. **edge-tts:** B18.7 butir 1 masih menulis "minimal suara bawaan (edge-tts)". Standar 18-19 Nov melarangnya untuk video final. Diputuskan 3a: standar baru menang. `.claude/commands/manager.md` butir 1f juga memuat kalimat lama dan perlu dibaca dengan aturan ini.
3. **Gaya suara:** B18.7 meminta VO "antusias" dan naskah berpetunjuk, dokumen produksi lama memakai suara "Pemandu Ceria". Standar baru meminta tenang, hangat, tidak antusias berlebihan, tanpa tag emosi. Standar baru menang.
4. **SFX:** B18.19 menyuruh SFX lebih menggoda "dalam batas B18.7", sedangkan standar baru melarang SFX berpita sempit, lowpass, dan reverb. Batas diperketat ke standar baru.
5. **Berkas alat:** `video/_bangun/susun_vo_hd.py`, `video/_bangun/campur_hd.py`, `video/_bangun/buat_sfx_hd.py`, `video/_sfx-hd/` sudah ada di folder fast4project (dicek 19 Nov), jadi tanda [PERLU DICEK FELIX] untuk berkas itu dicabut. Berkas baru 19 Nov: `video/_bangun/buat_musik_hd.py` dan `video/_musik-hd/`. Berkas Manager cloud perlu disalin ulang ke Project supaya sama.
6. **Musik latar:** `alur/video.md` bagian 3 butir terakhir dan 3c menulis "tanpa musik latar" (6 Nov). Diputuskan Felix 19 Nov: musik latar sederhana buatan kode boleh dan dipakai mulai video berikutnya (A.6 butir 13 sampai 16). Nol lagu berhak cipta tetap berlaku.

---

## E. Arahan singkat untuk Manager cloud: musik latar (Felix 19 Nov 2026)

Tempel ke chat Manager cloud, dan salin ulang berkas ini ke Project supaya sama dengan laptop.

```
Mulai Reels berikutnya, tambahkan musik latar sederhana. Aturannya ada di prosedur-manager-agent6-video.md A.6 butir 13 sampai 16.
1. Musik hanya dari paket buatan kode: tenang (menjelaskan, serius) atau hangat (ringan, ajakan). Tulis pilihan dan alasannya satu kalimat di brief produksi, baris "Musik:". Trek yang sama tidak dipakai tiga Reels berturut-turut.
2. Laptop mencampurnya dengan campur_hd.py --musik <nama>, sekitar 17 dB di bawah narator. Narator, SFX, dan target loudness tidak berubah.
3. Dilarang lagu dari pustaka Instagram, TikTok, atau internet.
4. Di perintah ke laptop tulis: "VO Liam standar 18-19 Nov + SFX HD + musik latar <tenang|hangat> + label karangan".
5. Sebelum menawarkan "Unggah sekarang", cek baris qc memuat tingkat musik dan catatan "belum didengar Felix". Reels yang sudah siap-unggah atau tayang tidak dirakit ulang.
```
