# Alur: Agent 6 — Content Media Expert

Strategi konten, storytelling, copywriting, dan produksi video Reels/Shorts untuk memasarkan jasa desain pitch deck. Konten organik untuk membangun kepercayaan, bukan iklan.

Baca `CLAUDE.md` lebih dulu. Aturan di sana berlaku di seluruh berkas ini.

Dijalankan dengan **`/mulai-video`**.

**Aturan global:** keputusan berbasis data · hasil siap produksi · nol jargon · nol analisis yang diulang · nol penjelasan yang tidak diperlukan.

---

> **B18.21 (18 Nov 2026) menang atas bagian suara, audio, rakit, dan tenggat di bawah bila berbeda:** `claude/prosedur-manager-agent6-video.md`.

## Koreksi Felix 20 Nov 2026 (B18.22) — alur acuan untuk setiap Reels berikutnya

Dari Reels "Slide terakhirmu cuma terima kasih?" (4 versi, rekap: `claude/evaluasi-reels-2026-11-25-slide-penutup.md`). Hasil V4 adalah **acuan bentuk** untuk video berikutnya. Menambah B18.19 di bawah dan `claude/prosedur-manager-agent6-video.md`; bila berbeda, bagian ini yang menang.

**Naskah (tengah pembahasan wajib sejelas ini):**
1. **Contoh usaha dibuka dengan satu kalimat konteks: siapa menjual apa ke siapa**, sebelum slidenya dibedah. Contoh: "Contohnya Kopi Lereng Ranu, penjual biji kopi. Mereka kirim presentasi ke pemilik kafe." Di layar, konteks itu digambar sebagai alur (penjual → presentasi → pembaca).
2. **Dilarang jargon, termasuk kata yang terdengar wajar bagi pembuat.** Ganti dengan kata sehari-hari: dek → presentasi · permintaan → apa yang kamu minta · uji coba → coba · sampel → satu bungkus / contoh barang · langkah pertama → cara mulai yang gampang · kontak → siapa yang bisa dihubungi · CTA → ajakan. Uji: pemilik warung yang belum pernah membuat presentasi paham dalam sekali dengar.
3. **Tiap butir daftar = perintah sehari-hari + contoh konkret dari usaha contoh**, dengan penanda "Di contoh ini:". "Kamu" hanya untuk penonton, "kami/mereka" hanya untuk usaha contoh. Keduanya tidak dicampur dalam satu kalimat tanpa penanda.
4. **Kejelasan menang atas durasi.** Durasi > 28 dtk karena penjelasan dicatat sebagai catatan, tidak dipotong dengan mengorbankan konteks. Sebagai pegangan: ±500 huruf ucapan ≈ 33 dtk, ±630 huruf ≈ 39 dtk (Liam tempo asli).
5. Rantai teks tetap: `/gaya-ngomong-gaul` → `/copy-hangat-berlogika` → `/stop-slop` → `cek-tulisan-manusia` (KRITIS 0). Revisi naskah di tengah pekerjaan cukup `/stop-slop` + `cek-tulisan-manusia`, lalu caption dan caption_tiktok disesuaikan dengan ucapan baru.

**Musik (bawaan baru):**
6. **Musik latar bawaan = berketukan pelan `beat-pelan` 88 BPM** (`python -I -X utf8 video/_bangun/buat_musik_semangat.py 88 beat-pelan`), dicampur `campur_hd.py <folder> --musik beat-pelan --celah-db 8 --turun-db 4` (±12 dB di bawah narator). Trek pad −17 dB **tidak dipakai lagi** karena tidak terdengar di HP. Trek lain (`semangat` 112 BPM, `penasaran`, `hangat`) hanya bila Felix memintanya atau untuk rotasi (trek sama tidak tiga Reels berturut-turut).
7. **Dua cek musik wajib di `qc`:** energi trek di atas 300 Hz ≥ 35% (terdengar di speaker HP), dan di pita bicara 1–4 kHz narator ≥ 15 dB (median) di atas musik.

**Rakit dan QC:**
8. **Lafal dicek dengan transkrip Scribe** (`creative_transcribe_audio` disambung ke node suara, 0 kredit) sebelum menyusun. Waktu tiap kata dipetakan ke garis waktu yang heningnya sudah dipendekkan (`video/2026-11-25-slide-penutup/waktu_kata.py` sebagai templat), dan **semua titik potong, SFX, dan elemen masuk diturunkan dari waktu kata**.
9. **Adegan pendek, dipotong di awal tiap kalimat**: 1,7–4,5 dtk. Adegan > 4,5 dtk dibelah di kalimat berikutnya. Judul layar = kata yang sedang diucapkan. Inilah yang membuat G3 lolos (41% → 28%).
10. **Tidak ada layar kosong > 1 dtk:** elemen yang akan menyala tampil samar sejak awal adegan, lalu menyala tepat di katanya.
11. **Uji strip wajib dua kali** (sebelum dan sesudah perbaikan) dengan daftar periksa: angka/penanda tidak menimpa teks · judul panjang memakai `fit` · hiasan (halftone) ≥ 30 px dari teks dan label · label karangan dua baris di dalam layar · teks di kartu ≥ 38 px · coretan tinta mengikuti transform kartunya · teks pendamping di pil yang menyala ikut warna (`color:inherit`).
12. **Revisi = file baru** (`final-v2`, `-v3`, `-v4`), versi lama ke `arsip/vN/`, `ganti_dari` = commit URL sebelumnya, `STATUS.md` diberi bagian per versi.

## Koreksi Felix 16 Nov 2026 (B18.19) — berlaku untuk setiap Reels

Dari Reels "Deck atau katalog". Menambah, tidak mengganti, B18.7 dan bagian 3b–3c di bawah.

1. **Hook = masalah nyata yang jelas, tanpa jargon.** Kalimat pertama menyebut kejadian yang dialami pembeli atau pemilik usaha dengan kata sehari-hari (contoh: "Pembeli cuma tanya harga, tapi kamu kirim presentasi kerja sama. Ya dia bingung!"). Hook tidak membuka dengan istilah yang belum dijelaskan.
2. **Istilah dijelaskan sederhana, dengan konteks dan maksud.** Istilah yang tak terhindarkan (deck, katalog, Ledger, dst.) dijelaskan di adegan berikutnya dalam satu kalimat: apa itu, dipakai untuk siapa, dan untuk apa. Uji: orang yang belum pernah mendengar istilahnya bisa mengulang artinya setelah menonton.
3. **Selesaikan sampai tuntas.** Agent 6 menyelesaikan seluruh rantai (naskah, VO, SFX, mix, QC) sendiri dan menyerahkan video yang sudah lolos. Dilarang menyuruh Felix memeriksa audio satu-satu. Pemeriksaan audio dilakukan sendiri: loudness (−14 ± 1 LUFS), true peak ≤ −1,5 dB, VO dan teks selaras (selisih ≤ 0,3 dtk), tidak ada kata terpotong, tiap SFX tepat sasaran. Hasilnya ditulis di `qc` sebagai satu baris.
4. **"Rapikan" = naskah dan teks layar saja.** Permintaan Felix merapikan, menyederhanakan, atau memperbaiki kata tidak menyentuh konsep visual, tema edit, atau urutan adegan. Konsep visual hanya berubah bila Felix menyebutnya.
5. **Visual dan SFX lebih menggoda, tetap dalam batas B18.7 butir 2 (maks. satu efek per 1,5 dtk, 3–5 jenis).** Palet efek: hit, whoosh, pop, ding (denting), riser, tick (ketukan ringan). Pergantian adegan utama memakai **transisi wipe kuning**. Gerak visual tiap 2–3 dtk (zoom punch, teks kinetik satu kata kunci).
6. **Dibuat di laptop yang tidak punya folder atau git:** jangan mengarang caption dan jangan membuat `status/laptop.json` baru. Caption dan `caption_tiktok` asli diambil dari `status/laptop.json` di repo `Fast4project/fast4project-media` (gh api, hanya membaca). Hasil berupa MP4 final plus baris `qc`; langkah publikasi: salin ke folder fast4project, `python alat/unggah_media.py --folder reels-<dd>-nov-<slug> --file <mp4> --keluar urls.json`, ubah item di status menjadi `siap-unggah`, lalu `--status`.
6b. **Naskah VO dan caption lolos standar tulisan manusia B18.20** (`claude/standar-tulisan-manusia.md`, `python alat/cek-tulisan-manusia.py <naskah> --jenis vo` dan `--jenis caption`, KRITIS nol): angka ditulis seperti dibaca, nol emoji dan singkatan, kalimat utuh.
7. **Skrip ulang-pakai** (`alat/reels/shoot.py`, `tl.py`, `mix.py`, `scene.html` dan `CLAUDE.md` kerja dari laptop pembuat) dipakai bila ada di perangkat; bila tidak, salin dari laptop pembuat ke folder fast4project sebelum video berikutnya supaya prosedurnya sama di semua perangkat.
8. **Unggah tetap B18.8/B19:** Windsor `create_video_post` hanya setelah Felix menyetujui file PERSIS itu (nama file, durasi, caption, jam). Tidak ada unggah otomatis.

---

## Langkah 0 · Fakta keras — dibaca sebelum apa pun

- **Nol kata "klien"** yang menunjuk klien Felix. Nol "sudah dipercaya", "biasanya saya mengerjakan".
- **Usaha karangan berlabel di layar** saat slidenya muncul (SEMBADA, SkillSwap, Noxfit, StockWaze, Nestly, ORBIT SIP). Disebut di voice-over saja tidak cukup — orang menonton tanpa suara.
- **Nol janji hasil.** Bukan "deck ini bikin investor yakin". Yang boleh: apa yang dikerjakan dan kenapa.
- **Nol angka karangan.** Angka ilustratif berlabel "ilustratif" di layar. Nol harga.
- **Suara AI boleh. Tokoh AI tidak.**

  | Boleh | Tidak boleh |
  |---|---|
  | Suara AI membacakan naskah sebagai **narator** — menjelaskan cara kerja, membedah slide, menyebut keputusan desain | Suara AI yang **berperan jadi orang**: punya nama, mengaku pernah memakai jasa Felix, bercerita pengalaman, atau berbicara seolah pemesan |
  | Narator tanpa nama, tanpa wajah, tanpa riwayat | "Saya" untuk pengalaman yang tidak ada. "Saya" hanya kalau yang bicara Felix sendiri |

  Suara yang berperan jadi orang adalah testimoni karangan, cuma tanpa wajah. Yang membuatnya karangan bukan wajahnya, tapi pengakuannya.

- **Nol wajah buatan mesin**, tetap berlaku penuh: nol avatar AI, nol lipsync ke wajah buatan, nol talking head kecuali Felix merekam dirinya sendiri. Parameter avatar di model mana pun tidak pernah dipakai.
- **Jangan menyebut video sudah dibuat, dirender, atau diedit kalau filenya belum ada dan belum dibuka.** **Menulis timeline bukan melihat video.** Project CapCut yang sudah ditulis tetap belum dinilai sampai framenya dibuka di Peran 3.

Salah satunya tidak bisa dipenuhi → berhenti, beri tahu Felix.

---

## Cek skill lebih dulu

Ketik atau periksa bahwa skill ini tersedia: `/revisi-carousel-hots`, `/copy-hangat-berlogika`, `/stop-slop`, `/otomasi-capcut`.

**`/reels-tema-blend` (12 Nov 2026) menentukan tema edit tiap video** — empat tema hasil campuran lima sumber, pustaka gerak `alat/gaya-blend/blend-kit.js`, render `alat/gaya-blend/render_tema.mjs`. Baca SKILL.md-nya sebelum Peran 2.

**`/video-making` sudah ada di `.claude/skills/video-making/`.** Cabang "dibangun dengan kode" butuh tiga alat di komputer Felix — cek sekali dengan `ffmpeg -version`, `node -v`, dan `npx playwright --version`. Ada yang belum terpasang → sebut perintah pasangnya ke Felix (`winget install Gyan.FFmpeg`, `winget install OpenJS.NodeJS`, `npx playwright install chromium`), satu kali, lalu tunggu. Jangan menawarkan CapCut sebagai jalan pintas hanya karena alatnya belum ada.

Ada yang tidak tersedia → berhenti, sebutkan yang hilang ke Felix. Jangan merakit langkahnya dari ingatan. Yang hilang `/otomasi-capcut` dan editornya CapCut → jangan menyentuh file project sama sekali; tawarkan Canva atau tunggu skillnya dipasang.

---

## Cek sistem visual lebih dulu — berlaku untuk semua video

Buka `claude/sistem-visual-video.md` dan lihat keadaannya.

- **[DIKUNCI]** → baca seluruhnya. Tujuh aturan tata bahasa gerak di bagian 2 menentukan kolom Visual di naskah Peran 2, cara merakit di Bagian B, dan uji gaya di Peran 3.

**Baca juga `claude/evaluasi-reels-project2-v4.md`** — evaluasi terukur video pertama yang gagal 5 dari 6 gerbang retensi. Isinya yang menurunkan kerangka babak di Peran 2 butir 1b dan gerbang di Peran 3 butir 2.
- **[BELUM DIKUNCI]** → minta referensinya, lalu **berhenti dan tunggu**:

  > **Kirim dulu 3–5 contoh motion graphic yang gayanya kamu mau** — tautan Pinterest atau filenya, taruh di `video/_referensi-gaya/`.

  Referensi masuk → buat lembar 12 frame tiap video, ukur temponya dengan `video/_referensi-gaya/ukur-gerak.py`, saring yang diambil dan yang tidak, tulis ke `claude/sistem-visual-video.md`, tunjukkan ke Felix, baru lanjut.

**Ini bukan bagian dari Higgsfield.** Gaya menentukan teks, latar, objek, dan transisi — semuanya dikerjakan di editor, dipakai atau tidaknya Higgsfield. Video tanpa sistem visual yang terkunci akan dirakit dengan gaya karangan sendiri, dan hasilnya slide yang di-zoom di latar polos.

Jangan memilih gaya sendiri, dan jangan memakai gaya dari video sebelumnya tanpa mengeceknya ke berkas itu. Referensi baru hanya diminta kalau Felix minta ganti arah.

---

## Peran 1 · Content strategy & concept

### 1 · Baca datanya

- **Kesimpulan Agent 1 Peran 1** — laporan minggu terbaru di `laporan/`.
- **Gerbang sinkron tayang (WAJIB PERTAMA)** — jalankan `alur/gerbang-sinkron-tayang.md`: tarik semua posting Instagram (carousel dan Reels), simpan `laporan/<tanggal>-tayang.json`, jalankan `alat/cek-overlap.py` untuk setiap konsep. Konsep yang topiknya sudah tayang di Reels atau carousel tidak boleh dipilih.
- **Bank ide** — `claude/bank-ide-carousel-fast4project.md`, dan tabel statusnya (catatan, bukan kebenaran; kebenaran ada di gerbang di atas).
- **Carousel yang sudah dibangun** — `carousel/*/STATUS.md`.
- **Pantangan topik** — `claude/pantangan-topik.md`.
- **Jadwal dan kalender** — `claude/jadwal-kalender-konten.md`: slot Kamis yang dikerjakan minggu ini (jam A atau B, bagian 5). **Sejak 12 Nov 2026 berlaku ATURAN KERAS KONTEN (`claude/agent-manager.md` B12, jadwal bagian 6d): Reels Senin–Sabtu 19.30 (6 per minggu, lantai 5), fase konsisten 13 Nov – 6 Des; tiga varian hook, pilih satu, jalan; G1/G2 dan S1–S10 tetap dijalankan tetapi hanya memicu satu putaran perbaikan ≤ 30 menit, lalu tetap tayang dengan catatan "hook lemah" (yang menahan tayang hanya isi kembar BLOKIR, klaim/angka tanpa label, harga, janji hasil, [CEK KATA] KRITIS, teks rusak); topik tidak boleh kembar; tiap Reels punya pemicu komentar di layar penutup dan caption; target komentar per Reels di `claude/papan-skor-reels.md`**, baris kalender, dan kartu konten (bagian 7). Konsep dipilih untuk slot itu, bukan sembarang hari.
- **Funnel dan hook** — `claude/funnel-konten-fast4project.md` (checklist hook, checklist isi, ritme) dan metrik Reels di laporan terbaru (skip rate, avg watch time).
- **Log pilar** — `video/_pilar-log.md`: porsi pilar sepuluh video terakhir dan status pilar testimoni.
- **Inventaris deck** — daftar isi `deck/` dibandingkan dengan tujuh deck di `deck/README.md` (Dasar Trading, Antropometri, SEMBADA, SkillSwap, Noxfit, StockWaze, Nestly). Tulis ke Felix deck mana yang **ada** dan mana yang **belum ada**.

**"Berbasis performa" hanya sejauh datanya kuat.** Total posting di bawah 8 → katakan bahwa pola performa belum bisa dipercaya, dan pilih berdasarkan kebutuhan segmen, bukan berdasarkan angka yang terlalu sedikit untuk berarti apa-apa. Nol angka performa yang dikarang atau diperkirakan.

### 2 · Tiga bentuk konten yang dipakai

| Bentuk | Isinya | Bahan wajib |
|---|---|---|
| **Penjelasan bersuara** | Narator menjelaskan satu keputusan dalam membuat slide profesional — satu keputusan per video, bukan daftar tips | Naskah yang lolos rantai teks + slide dari `deck/` sebagai contoh |
| **Bedah mockup dek** | Dek ditampilkan bagian per bagian, tiap bagian dijelaskan fungsinya: apa yang dijawab slide itu dan kenapa urutannya begitu | **PDF dek asli dari `deck/`.** Dek yang tidak ada filenya tidak dibedah |
| **Organic content** | Potongan pendek dari carousel yang sudah tayang, atau satu pengamatan dari bank ide | Teks final carousel, atau ide bank yang lewat `/revisi-carousel-hots` |

**Rekaman layar bukan bentuk konten tersendiri.** Itu bahan: kalau Felix mengirim rekaman layar, rekaman itu disinkronkan ke naskah di Peran 2. Kalau tidak ada, video tetap jalan tanpa itu.

### 2b · Tiga pilar konten — edukasi, entertaining, testimoni

Setiap video dan setiap ide **wajib berlabel satu pilar**. Pilar adalah tujuannya; bentuk di tabel 2 adalah cara membawakannya.

| Pilar | Tujuan | Bentuk yang cocok | Target porsi |
|---|---|---|---|
| **Edukasi** | Penonton paham satu keputusan slide yang benar dan kenapa | Penjelasan bersuara, bedah mockup dek | ±50% |
| **Entertaining** | Penonton berhenti menggulir karena merasa "ini gue banget", lalu mengingat akunnya | Situasi presentasi yang relatable ditampilkan lewat slide dan teks per ketukan, kuis "slide mana yang salah", bedah nada santai, POV tanpa aktor | ±30% |
| **Testimoni** | Bukti bahwa orang nyata pernah memakai jasanya | Teks asli dari orang nyata di layar, sebelum-sesudah dari pekerjaan nyata | ±20% **hanya bila aktif** |

**Entertaining: batasnya.** Lucu dari situasinya, bukan dari mengejek orang atau deck nyata milik orang lain. Nol manusia buatan AI dan nol cerita pengalaman karangan ("waktu itu ada pemesan…"). Nol stereotip kelompok. Tetap ada satu ajakan ringan di akhir, tetap memakai sistem visual video, tetap lewat rantai teks. Lucu yang menabrak pantangan topik atau berubah jadi janji hasil dibuang.

**Testimoni: pilar yang dijaga paling ketat.** Status dibaca dari `video/_pilar-log.md`. Klien asli per 28 Okt 2026: 0, jadi status awalnya **BELUM AKTIF**.
- **Belum aktif:** nol video berlabel testimoni. Nol kutipan karangan, nol "kata pemesan", nol suara atau wajah yang berperan jadi pemesan. Agent menulis **satu kali** per putaran ide: "Pilar testimoni belum aktif, bahannya belum ada", lalu mengisi slotnya dengan edukasi atau entertaining. **Bukti proses** (sebelum-sesudah dari pekerjaan Felix sendiri, berlabel "usaha karangan untuk portofolio") boleh, tetapi **tidak boleh dilabeli atau diperlakukan sebagai testimoni**.
- **Aktif hanya bila semua ini ada:** teks atau tangkapan layar asli dari orang nyata · izin tertulis untuk tampil (nama atau inisial yang disetujui) disimpan di `klien/<proyek>/izin-testimoni.md` · tidak diubah maknanya, boleh dipotong hanya dengan tanda. Ada satu yang kurang → tetap belum aktif.
- Kutipan tampil sebagai **teks di layar** dengan atribusi. Narator tidak membacakannya seolah itu pengalamannya sendiri.
- Mengaktifkan pilar ini adalah **[GERBANG FELIX]**: Felix yang menyatakan bahannya asli, bukan agent.

**Porsi dibaca dari sepuluh video terakhir** di `_pilar-log.md`. Sampel di bawah 10 → porsi hanya panduan, dikatakan terus terang.

### 3 · Tiga ide video

Tiap ide: **pilar** (edukasi / entertaining / testimoni) · **level TOFU/MOFU/BOFU, tahap funnel, dan satu CTA** · **tiga varian hook 3 detik, satu dipilih beserta alasannya** · **kalimat janji** (satu kalimat: "Setelah menonton, [segmen] bisa [satu tindakan] karena [satu alasan]"; kalau ada "dan" yang menyambung dua gagasan, pecah jadi dua ide) · **garis cerita** ("mengira … → ternyata … → jadi …": satu pergeseran keyakinan, bukan daftar tips) · **tangga** (satu konten level berikutnya yang ditunjuk lewat satu baris di caption, bukan CTA kedua) · **bentuk** (dari tabel di atas) · **angle** · **hook** (terbaca tanpa suara dalam 1,5 detik) · **segmen sasaran** · **pesan utama** · **satu ajakan** · **sumbernya**.

**Bedakan dua jenis sumber, karena pemeriksaannya beda:**

| Sumber | Status klaimnya | Yang harus terjadi |
|---|---|---|
| Carousel yang sudah dibangun | Sudah lolos `/revisi-carousel-hots`, `/perjelas-teks-carousel`, [CEK KATA] | Pakai teks finalnya. **Video tidak boleh menambah klaim** di luar itu |
| Ide bank yang belum dibangun | **Belum diperiksa sama sekali** | Naskah video wajib lewat `/revisi-carousel-hots` di Peran 2 sebelum produksi |

Tolak ide yang mengulang topik di `claude/pantangan-topik.md`.

**Sebar pilarnya.** Tiga ide mencakup **semua pilar yang aktif**, satu per pilar bila bisa; tidak ada pilar yang mengisi ketiganya. Pilar yang porsinya paling jauh di bawah targetnya didahulukan.

**Sebar levelnya (aturan 6 Nov 2026).** Porsi level dibaca dari kolom Level di `video/_pilar-log.md` dan dari kalender `claude/jadwal-kalender-konten.md` bagian 8. Target awal ±60% TOFU, ±30% MOFU, ±10% BOFU (hipotesis, `claude/funnel-konten-fast4project.md` bagian 7). Aturannya: **BOFU tidak mendahului MOFU**; tiap Reels TOFU menunjuk ke topik yang akan didalami di konten MOFU; klien asli 0 → BOFU berisi cara kerja dan contoh berlabel karangan, bukan testimoni. Sampel di bawah 10 → porsi hanya panduan, dikatakan terus terang.

**Sebar sumbernya (aturan 5 Nov 2026).** Tiga ide wajib memakai **deck atau carousel sumber yang berbeda**; satu deck maksimal dipakai di satu dari tiga ide. Hanya satu deck yang ada di `deck/` → jangan diam-diam semua ide bersumber dari situ: katakan terus terang bahwa pilihan terbatas karena deck lain belum ada, lalu minta Felix mengirim PDF deck yang belum ada (minimal tiga deck berbeda tersedia sebelum ide dibuat), atau jalankan ide dari bank/carousel sebagai pengganti. "Kamu pilih" = lanjut dengan yang ada dan catat keterbatasannya.

### 4 · Rekomendasikan satu, lalu [CEK & PERBAIKI]

Checklist: tiap ide menunjuk sumbernya · bentuknya jelas · nol angka performa karangan · hook terbaca tanpa suara · nol janji hasil · nol topik pantangan · nol jargon · bedah dek hanya untuk dek yang filenya ada · tiga ide bersumber berbeda · tiap ide berlabel pilar · nol ide testimoni selagi pilarnya belum aktif · nol bukti proses yang dilabeli testimoni · **kalimat janji satu kalimat tanpa dua gagasan** · **garis cerita terisi** · **level + satu CTA yang cocok levelnya** (TOFU kirim ke teman, MOFU simpan, BOFU DM kata kunci) · BOFU tidak mendahului MOFU · tangga menunjuk satu konten.

### 5 · Minta bahan dan tool, lalu berhenti

> **Mana yang mau dibikin, dan dirakit di mana?**
>
> 1. Pilih nomor ide.
> 2. Kirim bahannya ke `video/<nama>/bahan/`: PDF dek, carousel, slide, rekaman layar, logo. **Slide yang ditampilkan harus dari `deck/` — file aslinya.**
> 3. **Editornya:** **dibangun dengan kode (disarankan)** — Claude merender, menonton, dan memperbaiki sendiri; kamu hanya menerima file final · **CapCut** — Claude menulis project-nya, tiap putaran kamu yang mengekspor · **Canva**.
>
> Bisa dijawab sekaligus, mis. "ide 2, kode, elemen editor, kamu pilih konsepnya" — gerbang Peran 2 lalu dilewati.
> 4. **Objek utama tiap adegan dari mana?** **Elemen editor** (ikon dan bentuk Canva/CapCut) · **Higgsfield** (Claude menyusun spesifikasinya, kamu yang generate) · **foto objek bebas royalti**. Gayanya sama di ketiganya — diambil dari `claude/sistem-visual-video.md`.

Lalu **berhenti dan tunggu**. Editor menentukan bentuk seluruh keluaran Peran 2 — menulis project CapCut tidak sama dengan menulis instruksi Canva.

---

## Peran 2 · Video brainstorm & production

Peran ini punya dua bagian, dan batasnya adalah gerbang **"Produksi yang mana?"**.

**Jangan merakit apa pun sebelum gerbang itu.** Yang disusun sebelum gerbang ada tiga konsep; merakit ketiganya berarti dua rakitan dibuang. Untuk CapCut itu lebih buruk lagi: menulis project untuk konsep yang belum dipilih berarti menyentuh file project demi pekerjaan yang kemungkinan besar dibatalkan.

---

# BAGIAN A · Sebelum gerbang — disusun untuk ketiga konsep

### 1 · Tiga alternatif konsep

Satu per pendekatan: **storytelling** · **problem–solution** · **sebelum–sesudah mockup**.

**Tiap konsep membawa satu tema edit blend** (`.claude/skills/reels-tema-blend/` bagian 2–3: A Kolase Kertas Hidup · B Malam Garis Terang · C Sketsa Cat Air Bercerita · D Bedah Dek Editorial). Gerbang pilihan Felix memuat opsi tema dengan rekomendasi pertama; tema yang sama tidak dipakai tiga Reels berturut-turut. Tidak dijawab → rekomendasi.

**Sebelum–sesudah hanya sah kalau file "sebelum"-nya ada** (`deck/<nama>-draf.pdf` atau di `bahan/`). Deck portofolio semuanya versi jadi. Membuat versi berantakan sendiri — dengan tangan atau dengan AI — berarti mengarang bukti, walaupun hasilnya meyakinkan. File "sebelum" tidak ada → ganti alternatif ketiga dengan **sebelum–sesudah keputusan**: slide jadinya ditampilkan, lalu teks layar menjelaskan apa yang dipotong dan kenapa.

### 1b · Kerangka babak — wajib, sebelum menulis naskah

Ditambahkan 5 Nov 2026 dari `claude/evaluasi-reels-project2-v4.md`. Video v4 gagal karena **jawabannya jatuh di detik 12,3 dari 34,5** — 64% durasi berjalan setelah pertanyaannya terjawab, dan tidak ada satu detik pun yang menyebut taruhannya.

Tiap konsep dipetakan ke lima babak **beserta detiknya**, sebelum naskah per adegan ditulis:

| Babak | Porsi durasi | Isinya | Gagal kalau |
|---|---|---|---|
| **Hook** | 0–12% | Bukti utama sudah di layar + pertanyaan utuh | Pertanyaan baru utuh setelah detik 0,8 · layar sebagian besar kosong · jawaban sudah bocor |
| **Tension** | 12–28% | **Akibatnya**, bukan keadaannya. Apa yang hilang kalau dibiarkan | Hanya mendeskripsikan keadaan · masalah yang sama diulang dengan kalimat lain |
| **Bukti** | 28–58% | Slide asli dibedah, bagian yang dibicarakan di-zoom | Bukti berupa ikon, bukan slide · slide muncul setelah 50% durasi |
| **Payoff** | 58–80% | Jawaban + perubahan yang terlihat (sebelum–sesudah dari file yang sama) | Payoff jatuh sebelum 55% durasi · jawaban hanya diucapkan, tidak diperlihatkan |
| **Penutup** | 80–100% | Satu instruksi yang bisa dipakai ulang + satu ajakan + sambung balik ke hook | Berhenti pada kartu diam · ajakan tidak menunjuk apa pun di layar |

**Dua aturan keras:**
1. **Payoff tidak boleh jatuh sebelum 55% durasi.** Begitu pertanyaannya terjawab, alasan bertahan habis.
2. **Satu gagasan masalah, satu adegan.** Masalah yang sama dengan tiga ikon berbeda tetap satu informasi, dan memakan 24% durasi di v4.

### 2 · Untuk tiap konsep

- **Hook 1–3 detik**, tiga varian. Situasi yang segmennya kenali, bukan pertanyaan retoris generik ("Pernah nggak sih…?").
  - **Frame 0 sudah berisi gambar penuh**, bukan teks yang mengetik masuk ke layar kosong.
  - **Pertanyaan utuh sebelum detik 0,8.** Dua baris muncul bersamaan; aturan "≤ 3 kata per ketukan" berlaku untuk kalimat penjelas, bukan untuk pertanyaan hook.
  - **Satu pattern interrupt di 0–0,4 detik:** masuk dari gelap, atau lingkaran aksen yang membuka. Perubahan terang-gelap adalah kejut termurah yang kebaca di feed.
  - **Jawaban tidak boleh muncul di hook.** Kata kuncinya ditahan sampai babak Payoff.
- **Naskah per adegan:**

  | Detik | **Babak** | Teks layar (≤ 7 kata, dipecah per ketukan suara) | Kata besar + aksen | Voice-over | Objek utama | Latar + dekor | Gerak | Audio |
  |---|---|---|---|---|---|---|---|---|

- **Durasi 22–28 detik**, **9:16**. (Sebelum 5 Nov 2026: 20–35. Dipersempit karena v4 yang 34,5 detik punya 60% detik hampir diam; durasi panjang mengundang adegan pengisi.)
- **Satu zona teks per layar.** Kata besar **atau** kalimat bawah, tidak keduanya. Di v4 tiap adegan memuat kata besar di atas dan kalimat penuh di bawah yang mengatakan hal yang sama — penonton membaca dua kali dan matanya terbelah. Kalimat bawah yang memparafrase kata besar **dilarang**.
- **Subtitle** sinkron, ≤ 7 kata per layar. Subtitle **sama persis dengan voice-over**, bukan parafrase dari teks layar.
- **Satu ajakan** yang cocok dengan objektifnya (simpan / bagikan / DM satu kata kunci).

Kolom-kolom visual diisi dari tujuh aturan tata bahasa gerak di `claude/sistem-visual-video.md` bagian 2. **Adegan 2–4,5 detik.** Teks layar ditulis berikut titik pecahnya ("Slide kamu / **penuh** / tapi / nggak **dibaca**") supaya bisa muncul mengikuti suara, bukan sekaligus.

**Slide asli, subtitle, dan label selalu ditempel di editor**, tidak pernah dibuat generator AI. Rinciannya di butir 7.

**Objek utama diambil dari slide, bukan dari pustaka ikon.** Ditambahkan 5 Nov 2026: tujuh dari sepuluh adegan di v4 memakai ikon clip-art di dalam lingkaran — tumpukan kertas, kaca pembesar, pensil, pesawat kertas. Ikon kecil yang terkurung lingkaran dan diam adalah kebalikan dari aturan 3 (satu objek besar, terpotong, boleh keluar bingkai, bergerak pelan), dan itu yang membuat video terbaca seperti templat.

| Gagasan di naskah | Objek yang dipakai |
|---|---|
| "slidenya terlalu padat" | Tangkapan blok paragraf dari slide asli, diperbesar sampai keluar bingkai |
| "mana yang dibaca duluan" | Slide yang sama dengan tiga kotak sorot muncul bergantian |
| "satu pesan utama" | Satu baris yang tersisa setelah sisanya memudar |
| Butuh objek nyata (gunting, pensil) | Satu objek besar terpotong tepi bingkai, bergerak pelan — **nol lingkaran pembungkus, nol ikon rata tengah** |

### 3 · Aturan yang berlaku di semua tool

- **Area aman Reels:** Instagram menutup sekitar **14% atas** dan **20% bawah**. Teks layar, label sumber, dan label karangan tidak boleh di situ. **B18.11 (13 Nov): isi terkumpul di tengah** — titik berat vertikal 40–55% tinggi layar, hook dan visual utama di pita 25–75%, subtitle di y ≈ 1080–1260, label karangan di y ≈ 1300–1400; cek dengan `python alat/cek-posisi-tengah.py frame*.png`.
- **Slide 16:9 di layar 9:16 tidak terbaca utuh.** Zoom ke bagian yang diceritakan.
- **Bingkai slide tipis, tanpa bayangan, tanpa perangkat 3D** — sama dengan aturan mockup `alur/paket.md`.
- **Satu gerakan kamera per adegan**, mengikuti tempo voice-over. Teks dan objek bergerak di lapisannya sendiri — itu bukan gerakan kamera kedua.
- **Nol lagu berhak cipta tertanam.** Audio bawaan model AI dimatikan. **Musik latar sederhana (Felix 19 Nov 2026; bawaan diganti 20 Nov, B18.22 butir 6):** hanya paket buatan kode `video/_musik-hd/`. Bawaan sekarang `beat-pelan` 88 BPM, dicampur `video/_bangun/campur_hd.py <folder> --musik beat-pelan --celah-db 8 --turun-db 4` ±12 dB di bawah narator. Aturan lengkap: `claude/prosedur-manager-agent6-video.md` A.6 butir 13–16. Tidak ada lagu dari pustaka mana pun kecuali Felix menyebut sumbernya dan lisensinya dicatat di STATUS.md.

### 3b · Karakter suara narator — antusias, menjelaskan, tidak membosankan

Ditambahkan 6 Nov 2026. Berlaku untuk suara AI maupun rekaman Felix. Karakternya: **teman yang baru menemukan trik berguna dan ingin kamu tahu**, bukan pembaca berita dan bukan iklan yang berteriak. Menjelaskan dengan "kamu", kalimat pendek, kata kerja aktif.

| Babak | Arahan suara |
|---|---|
| **Hook** (0–3 dtk) | Suara mulai **sebelum 0,5 detik**, tanpa "halo" atau tarikan napas panjang. Energi tertinggi di seluruh video, tempo sedikit lebih cepat dari badan video, nada naik di akhir pertanyaan atau situasi. Tidak lebih pelan dari sisa video |
| **Tension** | Sedikit lebih pelan dan rendah, jeda 0,3–0,4 dtk sebelum akibatnya disebut |
| **Bukti** | Jelas dan tegas; tekanan pada nama bagian slide yang sedang di-zoom |
| **Payoff** | Jeda 0,3–0,5 dtk sebelum kata kunci, lalu naik dan **tekankan kata kuncinya**; ini puncak kedua setelah hook |
| **Penutup** | Hangat dan naik di ajakan; kalimat terakhir menyambung ke hook |

**Naskah memuat arahan suara di kolom Audio:** kata yang ditekan ditulis **tebal**, jeda ditulis `[0,3s]`, dan tiap adegan diberi satu kata emosi (penasaran / tegas / lega / ajak). Contoh: `Kamu baru bahas langkah 1, [0,2s] audiens **sudah baca** langkah 3.` — penasaran.

**Dihindari:** pembacaan datar dengan tekanan yang sama di tiap kata · akhir kalimat selalu turun · jeda di atas 1 detik · berteriak atau "banget guys" berlebihan · antusias yang berubah jadi janji hasil (semangat boleh, klaim tidak) · tokoh yang berperan jadi orang (aturan di atas tetap berlaku).

**Kalau alat suara punya pengaturan:** pilih suara hangat berenergi sedang-tinggi, gaya percakapan (bukan "berita" atau "formal"), tempo sedikit di atas normal; catat nama suara dan pengaturannya di `video/<nama>/STATUS.md` supaya video berikutnya terdengar sama.

**Yang bisa diukur dan yang tidak.** `cek-format.py` memeriksa empat proksi: suara mulai ≤ 0,5 dtk (V1), tidak ada jeda sunyi > 1,0 dtk (V2), 3 detik pertama tidak lebih pelan dari rata-rata (V3), dan rentang loudness ≥ 3 LU supaya tidak datar (V4). Ambangnya hipotesis awal dari satu video. **"Antusias" sendiri tidak bisa diukur skrip**, jadi Felix mendengar satu kali pada video pertama di Peran 3 butir 5 ("Suaranya sudah pas, atau ganti?"), dan pilihannya dicatat.

### 3c · SFX — efek suara yang tepat

Ditambahkan 6 Nov 2026. SFX adalah **penanda visual yang bisa didengar**: tiap efek menandai satu perubahan di layar, supaya orang yang menonton dengan suara merasakan ritmenya dan orang yang menonton tanpa suara tidak kehilangan apa pun. ~~Tanpa musik latar~~ **Diganti 19 Nov 2026: musik latar sederhana buatan kode dipakai (bagian 3), SFX tetap penanda visual dan musik tidak boleh bersaing dengannya.** Aturan nol lagu berhak cipta tetap.

**Sumber:** paket orisinal buatan kode, nol hak cipta — `python video/_referensi-gaya/buat-sfx.py` menghasilkan `video/_sfx/` (whoosh, swipe, pop, tick, riser, hit, ding, glitch). SFX dari luar hanya yang bebas royalti dan sumbernya dicatat di STATUS.md.

| Momen | SFX | Waktu | Gain (dB) | Aturan |
|---|---|---|---|---|
| Pattern interrupt di hook (0–0,4 dtk) | `whoosh` | detik 0,05–0,3 | −12 | Satu saja di hook; narator mulai ≤ 0,5 dtk, efek tidak menimpa kata pertama |
| Kata besar muncul | `pop` | tepat saat muncul | −14 | Hanya kata besar, bukan tiap teks |
| Ketukan teks per kata (hitungan, kuis) | `tick` | per ketukan | −18 | Maksimal tiga beruntun |
| Pergantian adegan, objek masuk atau keluar bingkai | `swipe` (kecil) / `whoosh` (besar) | di awal transisi | −14 | Tidak di tiap potongan; boleh sunyi |
| Tampilan "salah" atau "sebelum" | `glitch` | saat slide salah muncul | −14 | Hanya untuk yang salah, bukan hiasan |
| 1–2 detik sebelum payoff | `riser` | berakhir sebelum kata kunci | −16 | Satu per video, selesai sebelum narator menyebut jawabannya |
| Payoff, kata kunci jatuh | `hit` | tepat di kata kunci | −12 | Satu per video — puncaknya |
| Jawaban benar, "sesudah", ajakan simpan | `ding` | saat perubahan terlihat; saat ajakan | −14 | Maksimal dua: lega di payoff, ajak di penutup |

**Aturan umum**
1. **Maksimal satu efek per 1,5 detik** rata-rata. Lebih ramai dari itu terdengar seperti templat dan bersaing dengan narator.
2. **Satu fungsi, satu bunyi, selama satu akun** (`pop` selalu kata besar, `ding` selalu "benar" atau ajakan), supaya penonton belajar bahasanya.
3. **Sinkron dalam ±0,1 detik** dengan perubahan visual yang ditandainya (±1–3 frame di 30 fps). Efek yang telat terdengar salah, bukan estetik.
4. **Narator menang.** SFX tidak dipasang di atas kata yang ditekan narator; `pasang-sfx.py` menurunkan jalur efek otomatis saat narator berbicara dan menolak gain di atas −8 dB.
5. **Tidak ada SFX di detik hening yang disengaja** (jeda 0,3–0,5 dtk sebelum payoff dibiarkan sunyi; sunyi membuat `hit` terasa).
6. SFX tidak mengubah isi atau klaim.

**Cara kerja:** Peran 2 menulis lembar isyarat `video/<nama>/sfx-cue.csv` (`detik,nama_sfx,gain_db`, satu baris per efek) dari kolom Audio naskah. Setelah render, jalankan `python video/_referensi-gaya/pasang-sfx.py <video>.mp4 <cue>.csv <keluaran>.mp4`. Video tidak di-encode ulang. Jalur CapCut: tempatkan `.wav` dari `video/_sfx/` di trek audio pada detik yang sama (lewat `/otomasi-capcut` bila mendukung trek audio; kalau tidak, serahkan daftar isyarat).

### 4 · Teks lewat rantai pemeriksaan

1. **Ide dari bank yang belum dibangun → JALANKAN `/revisi-carousel-hots`** pada naskah. Ide dari carousel yang sudah dibangun → lewati, tapi cocokkan: nol klaim di luar teks final carousel.
2. **JALANKAN `/copy-hangat-berlogika`** — voice-over dan teks layar. Tidak boleh membongkar klaim yang sudah diputuskan.
3. **[CEK KATA]** — `/stop-slop`, kata terlarang, nol jargon.

### 5 · [CEK & PERBAIKI], rekomendasikan, berhenti

Checklist: lima babak terpetakan beserta detiknya · **payoff jatuh di atas 55% durasi** · satu gagasan masalah satu adegan · satu zona teks per layar, nol kalimat yang memparafrase kata besar · objek utama dari slide, nol ikon dalam lingkaran · sebelum–sesudah hanya dengan file "sebelum" asli · area aman dihormati · nol klaim baru · label karangan dan ilustratif ada di rencana layar · narator tidak berperan jadi orang · nol janji hasil · **uji nilai**: setelah menonton, penonton bisa menyebut satu keputusan, satu alasan, dan satu hal yang bisa dikerjakan sendiri pada slide miliknya — semuanya dari slide asli, bukan klaim baru · tiap ketukan memberi informasi baru (ketukan yang mengulang dibuang) · garis cerita "mengira → ternyata → jadi" terbaca dari babak Tension ke Payoff · **22–28 detik**, 9:16.

> **Produksi yang mana?** Sebut nomor konsep dan varian hook-nya.

Lalu **berhenti dan tunggu**. Nol file project disentuh sampai jawabannya masuk.

---

# BAGIAN B · Sesudah Felix memilih — hanya satu konsep yang dikerjakan

### 6 · Aset gerak dari Higgsfield — kalau dipakai

**Referensi gayanya sudah diminta dan dikunci di awal** ("Cek sistem visual lebih dulu"). Di sini tidak diminta ulang. Objek, pola prompt, dan daftar objek yang dilarang (uang, piala, grafik naik — terbaca sebagai janji hasil) ada di `claude/sistem-visual-video.md` bagian 6.

**Referensi dipakai untuk gaya, tempo, dan palet — bukan untuk ditiru per detik.** Membuat ulang satu karya tertentu shot demi shot berarti membuat ulang karya orang, bukan terinspirasi.

**Higgsfield — apa yang otonom, apa yang tidak (dicek 5 Nov 2026).** Felix sudah mengizinkan semua izin connector, tapi connector hanya punya tujuh alat baca/impor: daftar workspace, pilih workspace, daftar model, detail model, saldo, riwayat hasil, impor MP4. **Tidak ada alat generate**, jadi izin tambahan tidak mengubahnya.

| Otonom (Claude jalankan sendiri, tanpa bertanya) | Tetap Felix |
|---|---|
| Cek saldo, pilih workspace, baca daftar model dan parameternya, pilih id model yang cocok | Menekan generate di aplikasi Higgsfield |
| Menulis spesifikasi lengkap (model, rasio, prompt, negatif, seed) | Mengunduh hasil dan menaruhnya di `video/<nama>/bahan/` |
| Membaca riwayat hasil (`show_generations`) untuk menemukan hasil yang sudah Felix buat, lalu mencoba mengambilnya lewat tautan hasil sebelum minta Felix mengirim ulang | Menyetujui pemakaian kredit |

**Cek saldo dulu, sebelum menyusun spesifikasi.** Saldo 0 atau paket gratis (per 5 Nov 2026: 0 kredit, paket free) → katakan sekali, lalu pakai **jalur otonom**: gambar statis lewat `generate-image` Canva (objek hero, foto, tekstur), gerak dikerjakan di editor kode atau CapCut dari gambar itu. Higgsfield dipakai hanya untuk klip gerak yang memang tidak bisa dibuat di editor, dan hanya bila ada kredit.

**MCP Higgsfield tidak bisa membuat video.** Yang bisa dilakukan dari sini: membaca daftar model dan parameternya, melihat saldo, melihat hasil yang sudah ada, dan mengimpor MP4. **Generate dijalankan Felix di aplikasi Higgsfield.** Jadi yang diserahkan Claude adalah spesifikasi siap-pakai, bukan klaim bahwa asetnya sudah jadi.

Tiap spesifikasi aset memuat:

| Bagian | Isi |
|---|---|
| Model | id model yang benar-benar ada di daftar, beserta alasan singkat pemilihannya |
| Rasio | **9:16** |
| Durasi klip | sesuai adegan; model punya batas sendiri, cek dulu |
| Resolusi | secukupnya untuk Reels, bukan yang termahal |
| **Audio** | **mati.** Hampir semua model menyalakan audio secara bawaan. Audio bawaan model menabrak aturan nol lagu berhak cipta dan menimpa voice-over |
| Prompt | gerakan, suasana, cahaya, komposisi, area kosong untuk slide |
| **Negatif** | **no text, no letters, no logos, no people, no faces** |
| Konsistensi | seed/gaya/palet sama antarklip |

**Nol avatar.** Parameter avatar di model mana pun tidak dipakai — itu manusia buatan AI (Langkah 0).

### 7 · Generator AI tidak bisa menulis teks

Huruf di dalam klip yang dihasilkannya jadi coretan yang mirip huruf. Pembagiannya tegas:

| Dibuat AI | Ditempel belakangan di editor |
|---|---|
| Gerakan kamera, suasana, cahaya, transisi abstrak | **Slide asli dari `deck/`** |
| Latar, tekstur, permukaan kosong untuk ditempeli | **Subtitle dan teks layar** |
| Klip pembuka tanpa teks | **Label "usaha karangan" dan "ilustratif"** |

Prompt AI **tidak pernah** meminta slide, tulisan, angka, logo, atau wajah. Prompt yang meminta "slide pitch deck berubah jadi rapi" menghasilkan slide palsu dengan tulisan ngaco — itu mockup karangan.

### 8 · Rakit, sesuai editor dari Peran 1

- **CapCut → JALANKAN `/otomasi-capcut`.** Claude menulis project-nya langsung: memotong jeda dan bagian gagal, menyinkronkan rekaman layar, menyusun timeline dari naskah, **memasang teks per ketukan suara, latar gradasi dan dekor, objek utama**, adjustment layer, dan zoom halus. Aturan keselamatan filenya ada di dalam skill itu dan tidak boleh dilewati.
- **Canva →** instruksi per adegan: latar dan dekor apa, objek apa, teks per ketukan dengan detik munculnya, kata besar dan aksennya, animasi masuk, transisi lingkaran aksen.
- **Kode → JALANKAN `/video-making`.** Tiap adegan digambar sebagai halaman HTML 1080×1920 mengikuti `claude/sistem-visual-video.md` — teks per ketukan, objek utama, latar berdekor, transisi lingkaran aksen — lalu difilmkan dengan Playwright dan disambung dengan ffmpeg. Gambar dulu beberapa frame di momen terpadat dan **lihat**; baru render penuh. Slide asli dari `deck/` ditempel sebagai gambar, tidak digambar ulang. Hasil di `video/<nama>/render/`.

### 9 · Grading dan gerakan

- **Adjustment layer untuk footage dan latar, bukan untuk slide.** Menaikkan kontras dan saturasi aman untuk rekaman dan aset gerak. Slide dek itu barang bukti hasil kerja Felix — warnanya lewat apa adanya. Yang ditonton orang harus dek yang benar-benar dibuat, bukan versi yang sudah digeser warnanya.
- **Arah grading diambil dari `claude/sistem-visual-video.md`**, bukan dikarang per video.
- **Zoom mengikuti aturan di butir 3, tidak dibuat aturan baru.** Yang ditambahkan di sini hanya cara memasangnya: pelan, satu arah, tanpa pantulan di ujung.

### 10 · [CEK & PERBAIKI] rakitannya, lalu serahkan

Checklist: prompt AI nol teks, nol wajah, nol avatar · audio model dimatikan · grading tidak kena slide · area aman masih kosong setelah dirakit · label karangan dan ilustratif benar-benar ada di layar · isi tidak berubah dari naskah yang sudah lolos rantai teks · **tiap adegan di timeline memuat teks per ketukan, satu objek utama, dan latar berdekor** — kalau ada adegan yang isinya cuma slide di latar polos, rakitannya belum selesai.

Lalu serahkan ke Peran 3 — dan ingat Langkah 0: **menulis timeline bukan melihat video.** Peran 2 **tidak pernah** melapor "video selesai" ke Felix; laporan hanya keluar dari Peran 3 butir 5, dengan kartu skor.

---

## Peran 3 · Video audit & refinement

**Peran 3 berjalan otomatis tepat setelah rakitan selesai, tanpa menunggu Felix.** Konfirmasi "videonya sudah jadi" bukan hasil kerja: video baru boleh dilaporkan selesai setelah **butir 2, 2b, dan 2c lolos semua** (atau putarannya habis, lihat butir 3). Siklusnya: **evaluasi menyeluruh → daftar kelemahan beserta detiknya → revisi otomatis sekaligus → evaluasi ulang dari awal → ulangi sampai lolos.**

### 1 · Buka videonya — sungguhan

Ambil frame di detik 0, 1,5, tengah, dan akhir, dan **lihat**.

- **Kode →** file render ada di `video/<nama>/render/`. Langsung diaudit di sini, **tanpa Felix**.
- **CapCut →** timeline itu JSON, bukan gambar; yang dinilai hanya file ekspor. Folder ekspor CapCut disetel **sekali** ke `video/<nama>/ekspor/` (CapCut → Ekspor → Simpan ke). Claude mengambil sendiri file `.mp4` terbaru dari folder itu — Felix tidak memindahkan apa pun. Belum ada file baru di sana → minta satu kali ekspor, lalu tunggu.

### 2 · Uji gaya, lalu periksa delapan hal

**Jalankan gerbang retensi dulu — ini yang menentukan lolos atau tidak:**

```
python video/_referensi-gaya/ukur-retensi.py <file>.mp4
```

Enam gerbang, dikalibrasi dari referensi di `video/_referensi-gaya/` (ref2 dan ref4 lolos penuh) dan dari kegagalan v4 (`claude/evaluasi-reels-project2-v4.md`):

| Gerbang | Lolos kalau | v4 |
|---|---|---|
| **G1 tenaga hook** | Gerak 3 detik pertama ≥ 0,80× rata-rata video (target 1,10×) | 0,42× — pembukanya kurang dari separuh tenaga videonya sendiri |
| **G2 frame beku** | Nol frame diam > 1,0 detik | 2,7 detik, 16 kejadian |
| **G3 detik mati** | < 35% detik hampir diam | 60% |
| **G4 adegan** | Nol adegan > 4,5 detik | satu adegan 5,4 detik |
| **G5 penutup** | 2 detik terakhir tidak beku | 0,9 — berhenti mati di titik perulangan |
| **G6 ruang kosong** | Isi mengisi ≥ 45% tinggi bingkai | lolos |

Ada yang GAGAL → **perbaiki, jangan diserahkan.** Semuanya masuk kategori teknis di butir 3, jadi dikerjakan sendiri tanpa bertanya ke Felix.

`ukur-gerak.py` yang lama tetap ada untuk menyandingkan lembar frame dengan referensi, tapi **verdict-nya diambil dari `ukur-retensi.py`**.

| Hal | Lolos kalau |
|---|---|
| Hook | Terbaca tanpa suara dalam 1,5 detik |
| Pacing | Tiap adegan punya fungsi; yang bisa dibuang tanpa pesan berubah → dibuang |
| Visual | Lolos uji gaya; konsisten satu palet; nol teks ngaco dari generator AI di mana pun |
| Mockup | Slide asli, berlabel sumber; usaha karangan berlabel; warna slide tidak digeser grading |
| Subtitle | ≤ 7 kata, sinkron, di luar area tertutup UI Reels |
| Audio | Nol lagu berhak cipta tertanam; narator tidak berperan jadi orang |
| Transisi | Satu jenis, tidak mengalihkan dari pesan |
| CTA | Satu, cocok dengan objektif |

Plus fakta keras Langkah 0: nol "klien", nol harga, nol wajah buatan mesin, nol klaim baru.


### 2b · Empat hal yang hanya bisa dinilai dengan mata — buka lembar framenya

Skrip tidak bisa membaca ini. Buka `<file>-lembar.jpg` dan **lihat**, lalu jawab satu per satu. Keempatnya adalah temuan berulang dari v4.

| Hal | Gagal kalau | Perbaikannya |
|---|---|---|
| **Posisi payoff** | Jawaban/kata kuncinya muncul sebelum 55% durasi, atau sudah bocor di hook | Pindahkan ke babak Payoff; hook hanya menyimpan pertanyaan |
| **Dobel zona teks** | Ada layar yang memuat kata besar **dan** kalimat bawah yang mengatakan hal yang sama | Buang kalimat bawahnya. Satu zona teks per layar |
| **Objek generik** | Ada ikon clip-art di dalam lingkaran, rata tengah, diam | Ganti dengan potongan slide asli, atau objek besar yang keluar dari tepi bingkai |
| **Keterbacaan slide** | Teks slide yang sedang dibicarakan lebih pendek dari **3% tinggi bingkai** (±58 px pada 1920) | Zoom sampai terbaca. Slide 16:9 utuh di bingkai 9:16 hanya untuk konteks, maksimal 1,5 detik |

Cara cepat menguji keterbacaan: perkecil frame ke lebar **430 px** — ukuran tampil sebenarnya di ponsel — lalu baca. Tidak terbaca di situ berarti tidak terbaca di feed.

### 2c · Standar publikasi — sepuluh pemeriksaan isi dan strategi

Ditambahkan 6 Nov 2026 dari evaluasi video StockWaze ("Jangan tonjolkan 3 langkah sekaligus"): enam gerbang retensi lolos semua, tetapi video belum layak tayang karena **gagasan yang sama diulang tiga kali, jawaban bocor di detik 0–3, bahasanya kaku, dan tidak ada situasi yang dikenali penonton**. Gerbang teknis saja tidak cukup; video baru layak tayang kalau **butir 2, 2b, dan 2c semuanya lolos**.

Tiap baris dijawab LOLOS atau GAGAL **beserta detiknya**. Kolom kanan adalah perbaikan otomatis (butir 3), bukan pertanyaan ke Felix.

| # | Standar | Lolos kalau | Cara cek | Perbaikan otomatis kalau gagal |
|---|---|---|---|---|
| S1 | **Topik relatable** | Hook memuat situasi yang dikenali segmen (mis. "kamu baru bahas langkah 1, audiens sudah baca langkah 3"), bukan aturan abstrak. Kalimat janji satu kalimat masih benar | Baca hook dan kalimat janji dari Peran 1 | Ganti ke varian hook situasi yang **sudah ditulis** di Peran 2 (tiga varian); tulis ulang ketukan pertama |
| S2 | **Hook kuat** | Gerbang G1 lolos · terbaca tanpa suara ≤ 1,5 dtk · situasi/pertanyaan utuh sebelum detik 0,8 · **jawabannya tidak muncul** di hook | Lembar frame detik 0–3 + naskah | Pindahkan kata kunci jawaban ke Payoff; hook hanya menyimpan pertanyaan |
| S3 | **Kalimat sederhana, tanpa jargon** | Nol kata di daftar [CEK KATA] · satu kalimat satu gagasan, ≤ 7 kata per ketukan, kalimat utuh ≤ 12 kata · kata sehari-hari (tabel di bawah) | Baca seluruh naskah + subtitle terhadap daftar kata | Ganti kata, pecah kalimat; lewat rantai teks lagi (Peran 2 butir 4) |
| S4 | **Satu gagasan, satu adegan** | Tulis satu baris gagasan per adegan. Tidak ada gagasan inti yang dinyatakan lebih dari sekali (kata lain, kalimat lain, tetap dihitung) | Tabel adegan → gagasan | Buang adegan yang mengulang; payoff dan penutup maju, durasi dipadatkan |
| S5 | **Storytelling yang membangun kepercayaan** | Garis cerita "mengira → ternyata → jadi" terbaca dari Tension ke Payoff · ada **alasan** ("karena …"), bukan hanya perintah · bukti dari slide asli atau berlabel karangan · nol klaim hasil, nol cerita pengalaman karangan, narator tanpa "saya" palsu | Naskah + label di layar | Tambah satu kalimat alasan dari teks final carousel/dek; pasang label; hapus klaim |
| S6 | **Motion graphic menarik** | G2, G3, G4 lolos · pattern interrupt tiap 2–4,5 dtk · objek utama dari slide asli, nol ikon dalam lingkaran · satu zona teks per layar · **nol dua teks terbaca bersamaan > 0,2 dtk saat transisi** · teks slide yang dibicarakan ≥ 3% tinggi bingkai · **SFX sesuai butir 3c Peran 2 (sinkron ±0,1 dtk, ≤ 1 efek per 1,5 dtk, nol musik, narator tetap terdengar)** | Lembar frame; ambil frame tiap 0,2 dtk di sekitar tiap pergantian teks; uji 430 px | Perpendek crossfade, zoom ke bagian slide, ganti objek generik |
| S7 | **Retention optimal** | G1–G6 = 6/6 · payoff di 55–80% durasi · penutup menyambung ke hook (mancing putar ulang) | `ukur-retensi.py` + butir 2b | Sesuai tabel butir 2b |
| S8 | **Format Reels 9:16** | `cek-format.py` semua lolos: 1080×1920, 22–28 dtk, 24–60 fps, h264 + aac, audio ada dan tidak pecah, **suara narator V1–V4 (butir 3b Peran 2)** · area aman 14% atas dan 20% bawah kosong | `python video/_referensi-gaya/cek-format.py <file>.mp4` + lembar frame | Render ulang dengan parameter benar; geser teks dari area tertutup |
| S9 | **TOFU–MOFU–BOFU terarah** | Level, pilar, dan **satu CTA yang cocok levelnya** (TOFU kirim ke teman · MOFU simpan · BOFU DM kata kunci) tertulis dan sesuai isi · tangga menunjuk satu konten berikutnya · cocok dengan baris kalender (`claude/jadwal-kalender-konten.md` bagian 8) | Label di STATUS.md, CTA di layar, caption | Samakan CTA dengan level; satu CTA saja; tulis baris tangga di caption |
| S10 | **Uji nilai** | Setelah menonton, penonton bisa menyebut satu keputusan, satu alasan, dan satu hal yang bisa dikerjakan pada slide miliknya | Jawab tiga hal itu dari video, tertulis | Tambah babak Bukti atau instruksi di Penutup dari teks final |

**Kata sehari-hari (contoh, bukan daftar lengkap):** tonjolkan → terangkan / sorot · redupkan → buat redup · duplikat → gandakan · alur → langkah · hierarki → urutan penting · visual → tampilan · **"penonton"** untuk orang yang hadir di presentasi → **"audiens"** (supaya tidak tertukar dengan orang yang menonton Reels ini).

**Batas perbaikan otomatis.** Yang boleh diubah sendiri: kata, pemecahan kalimat, membuang adegan pengulang, memindahkan payoff, mengganti ke varian hook yang sudah ditulis, mengganti objek, mengatur ulang transisi, memasang label, menyamakan CTA. Yang **tidak** boleh diubah sendiri: topik, pilar, level, deck sumber, dan menambah klaim baru. Itu keputusan isi (butir 3).

### 3 · Perbaiki sendiri yang teknis — jangan tanya

Pilah tiap temuan dengan tabel "Tiga jenis keputusan" di `CLAUDE.md`:

- **Teknis dan pelanggaran standar** (gerbang G1–G6 gagal, keempat hal di butir 2b, **sepuluh standar di butir 2c** termasuk jargon, gagasan yang diulang, jawaban bocor di hook, hook tanpa situasi, CTA tidak cocok level; sinkron, area aman, ukuran huruf, transisi lebih dari satu jenis) → **perbaiki langsung**, tanpa bertanya, dalam batas yang tertulis di butir 2c. Naskah yang berubah wajib lewat rantai teks lagi (Peran 2 butir 4), lalu **suaranya dibuat ulang**: suara AI → Claude yang membuat ulang; suara yang direkam Felix → itu satu-satunya pertanyaan di butir 5 ("rekam ulang kalimat nomor …"). Memindahkan payoff dan membuang kalimat dobel termasuk teknis — itu memperbaiki struktur yang sudah disetujui, bukan mengubah isinya.
- **Isi atau selera** = memilih antara dua arah yang **sama-sama lolos** butir 2c (dua hook situasi yang sama kuat, warna aksen, pilihan deck sumber, ganti topik, ganti pilar atau level, menambah klaim) → jangan dikerjakan; **kumpulkan** untuk satu pertanyaan di butir 5. Pelanggaran standar bukan selera.
- **Batas putaran dan jaminan:** video **tidak diserahkan sebagai siap tayang** selama ada baris GAGAL. Putaran habis (3 untuk kode, 2 ekspor untuk CapCut) dan masih ada yang gagal → serahkan dengan tanda **BELUM LOLOS** beserta baris yang gagal, detiknya, dan apa yang sudah dicoba. Standar tidak pernah diturunkan diam-diam.

**Satu putaran = semua perbaikan teknis sekaligus.** Bukan satu perbaikan, lalu cek, lalu satu lagi.

| Editor | Satu putaran | Batas |
|---|---|---|
| **Kode** | perbaiki → render ulang **hanya adegan yang berubah** → ukur ulang → lihat frame | maks 3 putaran, **semuanya tanpa Felix** |
| **CapCut** | tulis semua perbaikan ke project sekaligus → minta **satu** ekspor → audit | **maks 2 ekspor dari Felix per video.** Sesudah ekspor kedua, sisa temuan teknis dicatat, bukan diminta ekspor ketiga |

Setiap putaran: **jalankan ulang `ukur-retensi.py` dan [CEK & PERBAIKI] dari awal tabel di butir 2 dan 2b Peran 3**, bukan cuma bagian yang diubah — revisi satu adegan sering menggeser sinkron adegan sesudahnya.

### 4 · Nomor versi

Satu nomor versi per file yang diserahkan ke Felix, bukan per putaran internal. Render percobaan di cabang kode tidak dinomori dan tidak dilaporkan satu-satu.

### 5 · Serahkan sekali, dengan satu pertanyaan paling banyak

Laporan akhir: file final · **kartu skor**: tiap baris G1–G6, empat hal butir 2b, S1–S10 dan F1–F6 (`cek-format.py`) dengan LOLOS/GAGAL, serta **putaran keberapa** tiap baris akhirnya lolos · satu baris per perbaikan yang sudah dikerjakan ("detik 7: dua teks bertabrakan → crossfade 0,15 dtk") · hasil uji gaya (lolos/gagal per baris) · lalu **satu** pertanyaan kalau ada temuan isi atau selera yang terkumpul:

> **Dua hal yang butuh keputusanmu:** (1) … (2) … — jawab nomornya, atau "final".

Tidak ada temuan isi atau selera → tidak ada pertanyaan. Langsung ke finalisasi.

### 6 · Evaluasi pasca-tayang (≥ 7 hari setelah Felix mengunggah)

Tarik metrik Reels lewat Windsor kalau tersambung (`media_reel_skip_rate`, `media_reel_avg_watch_time`, saves, shares); tidak tersambung → minta Felix angka dari Insights. Bandingkan dengan Reels sebelumnya, **satu variabel saja** (biasanya hook), isi baris di `claude/eksperimen-carousel-log.md`, **termasuk kolom Slot dan jam WIB** (`timestamp` + 7 jam). Hook dinilai dari skip rate dan watch time; jam dinilai dari reach pada umur sama — dua metrik terpisah (`claude/jadwal-kalender-konten.md` bagian 5). Aturan kejujuran sama: di bawah 8 posting = arah awal; reach kecil (< 50) tidak dinilai.

### 6b · Finalisasi

Catat satu baris di `video/_pilar-log.md`: tanggal, video, pilar, **level**, bentuk, sumber, jam tayang WIB dan slot.

Tayang **Kamis**, jam jangkar 19.30 atau pembanding 12.00 WIB sesuai rotasi (`claude/jadwal-kalender-konten.md`). **Selama Sprint 14 hari (10–23 Nov 2026): tayang Senin–Sabtu 19.30 WIB, slot dicatat "sprint", satu baris log per Reels dengan mekanisme hook (jadwal bagian 6c); syarat berhenti dibaca tiap Senin.** Serahkan pengingat unggah 15 menit sebelum jam itu; unggah lewat gerbang butir 7 atau Felix sendiri. Tayang ketiga (Minggu 19.30) hanya bila gerbang bagian 6 dokumen itu terpenuhi.

Caption memakai aturan Agent 1 Peran 4 (≤ 50 kata sebelum tagar, nol jargon, satu ajakan, 4–5 tagar) → [CEK KATA]. Serahkan file + caption.

**Unggah:** lewat gerbang butir 7 (Felix mengetik "unggah") atau Felix sendiri dari aplikasi Instagram.

Catat di `video/<nama>/STATUS.md` dan, kalau sumbernya carousel, di `carousel/<nomor>/STATUS.md`. Tambahkan satu baris ke `video/_pilar-log.md` (tanggal, video, pilar, bentuk, sumber).

### 7 · Gerbang unggah Reels — satu konfirmasi, satu tayang

**Larangan lama dicabut 6 Nov 2026** (keputusan Felix): Agent 6 boleh menayangkan Reels sendiri lewat `create_video_post`, **hanya** setelah Felix mengetik "unggah" di terminal sesi ini. Felix tetap boleh mengunggah sendiri dari aplikasi Instagram.

**Prasyarat, berurutan. Gagal satu → berhenti, laporkan sebabnya, dan serahkan file + caption untuk unggah manual.**
1. **Kartu skor semua LOLOS** (butir 2, 2b, 2c, dan `cek-format.py` semua lolos, termasuk V1–V4 suara). Ada baris BELUM LOLOS → unggah tidak ditawarkan.
2. **Caption final** lolos aturan Agent 1 Peran 4 (≤ 50 kata sebelum tagar, nol jargon, satu ajakan, 4–5 tagar), lolos [CEK KATA], dan CTA-nya sama dengan CTA di layar dan level kontennya.
3. **Slot.** Bandingkan dengan `claude/jadwal-kalender-konten.md`. `create_video_post` menayangkan **saat itu juga**, tanpa jadwal. Di luar jam slot hari itu → sebut selisihnya dan biarkan Felix memilih menunggu atau tayang sekarang.
4. **URL publik langsung ke file .mp4.** Instagram mengambil videonya dari URL, bukan dari komputer Felix. Syaratnya: MP4 atau MOV, ≤ 1 GB, 3 detik–15 menit, 9:16, bisa dibuka tanpa login. Sumber, urut yang dicoba: (a) tautan unduhan hasil `export-design` Canva bila videonya desain Canva · (b) **GitHub publik lewat `alat/unggah_media.py`** (`alur/unggah-media.md` bagian 3; keluar 0 = URL sudah terverifikasi), hosting lain yang Felix siapkan dicatat di `video/_hosting.md` · (c) tidak ada keduanya → langkah ini gagal, serahkan manual. **Verifikasi sebelum bertanya:** `curl -sI <url>` harus 200 dan bertipe `video/mp4` atau `application/octet-stream`. Tidak lolos → jangan bertanya "unggah".
5. **Cover.** Pakai `thumb_offset` (milidetik) yang menunjuk frame berisi hook utuh, atau `cover_url` JPEG. **Jangan frame pertama kalau frame itu hitam atau kosong** (video yang dibuka dari gelap punya frame 0 hitam).
6. **Tunjukkan rencana unggah ke Felix, lalu berhenti dan tunggu:** (a) empat frame dari file yang akan tayang · (b) caption persis, lengkap dengan tagar · (c) URL · (d) jam dan slot (A atau B) · (e) pilihan cover · (f) satu baris: "Setelah ini tayang di Instagram dan tidak bisa ditarik kembali. Lewat perintah ini tidak ada audio dari pustaka Instagram; kalau mau menambahkannya, unggah sendiri." Tutup dengan pertanyaan persis ini:

   > **Unggah Reels sekarang ke Instagram?** Balas "unggah" untuk memposting.

   **Hanya kata "unggah" di sini yang dihitung sebagai izin.** "Oke", "siap", "final", jawaban di butir 5, dan "jalan terus" bukan izin unggah. Felix diam → tidak diposting.
7. **Felix membalas "unggah"** → `execute_action` connector `instagram`, akun 17841464124677734, aksi `create_video_post` dengan `video_url`, `caption`, dan `thumb_offset` atau `cover_url`. `share_to_feed` tidak diubah (bawaan Instagram). Claude Code meminta izin sekali lagi lewat kotak izinnya; itu pengaman terakhir, bukan gangguan.
8. **Setelah tayang.** Reels perlu beberapa menit diproses. Tarik `media_permalink`, `media_caption`, dan `timestamp` terbaru lewat Windsor, cocokkan captionnya, kirim tautannya ke Felix, lalu catat: STATUS.md → **tayang** + jam WIB + slot, `video/_pilar-log.md`, dan baris di `claude/eksperimen-carousel-log.md`. **Hasilnya tidak jelas atau error → jangan langsung mengulang.** Tunggu beberapa menit, cek ulang apakah postingnya sudah ada; mengulang tanpa cek bisa membuat posting ganda. Masih tidak ada setelah pengecekan → tanyakan ke Felix, bukan mengulang diam-diam.

**Yang tetap tidak boleh:** mengunggah tanpa "unggah" dari Felix di sesi itu · tanpa melihat frame file yang akan tayang · video yang masih BELUM LOLOS · video dengan musik berhak cipta tertanam · memakai aksi Windsor lain (komentar, balas, hapus, story) tanpa Felix memintanya langsung. Satu "unggah" = satu posting.

---

## Peran 4 · Belajar dari revisi Felix

**Pemicu:** Felix selesai merapikan sendiri project CapCut-nya dan mengatakan begitu. Tidak dijalankan sendiri, dan tidak dijalankan untuk video yang Felix tidak sentuh.

### 1 · Ambil selisihnya

Bandingkan **salinan sebelum** (backup yang dibuat `/otomasi-capcut`) dengan project setelah Felix merevisi. Backup-nya tidak ada → berhenti; tanpa pembanding, yang tersisa cuma tebakan tentang apa yang berubah.

### 2 · Kelompokkan perubahannya

Tempo dan potongan · grading · gerakan dan zoom · teks layar dan subtitle · audio · urutan adegan.

### 3 · Pisahkan selera dari aturan

| Yang terlihat | Artinya |
|---|---|
| Perubahan yang sama muncul di **≥ 2 video** | Kandidat aturan. Tulis sebagai usulan |
| Muncul **sekali** | Selera untuk video itu. Catat di STATUS.md, jangan dijadikan aturan |
| Perubahan menabrak Langkah 0 | **Bukan aturan baru.** Laporkan sebagai temuan dan tanyakan |

Satu kali bukan pola. Menaikkan kejadian tunggal jadi aturan membuat skill ini pelan-pelan jadi kumpulan kebiasaan satu video.

### 4 · Usulkan, jangan tulis sendiri

Usulan ditulis ke `claude/usulan-skill-video.md`: apa yang diubah · bukti videonya yang mana · kalimat persis yang diusulkan masuk skill. Lalu:

> **Usulan mana yang dipakai?** Sebut nomornya, atau "tidak ada".

Felix menyetujui → baru skillnya diperbarui, lewat kartu usulan skill supaya dia yang menekan simpan. **Skill tidak pernah memperbarui dirinya sendiri tanpa persetujuan.**

### 5 · Yang tidak pernah boleh diusulkan untuk diubah

Langkah 0 fakta keras · area aman Reels · label usaha karangan dan ilustratif · nol klaim baru · nol wajah buatan mesin · nol lagu berhak cipta · grading tidak kena slide.

Ini bukan selera, dan revisi manual bukan alasan untuk melonggarkannya. Felix merevisi ke arah yang menabrak salah satunya → katakan apa adanya, lalu tanya. Itu satu-satunya jawaban yang jujur: dia mungkin punya alasan yang belum diketahui, atau mungkin lupa aturannya.
