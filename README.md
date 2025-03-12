# 🎵 Python Music Player

## 📝 Deskripsi
Music Player ini adalah aplikasi berbasis Python dengan antarmuka grafis menggunakan Tkinter dan dukungan pemutaran musik dengan Pygame. Aplikasi ini memungkinkan pengguna untuk memutar lagu dalam format MP3 dari folder lokal, menampilkan animasi putaran vinyl, serta menampilkan progress bar lagu yang sedang dimainkan.

---

## 🚀 Fitur Utama
- 📂 Memuat lagu dari folder lokal.
- ▶️ Play/Pause lagu dengan animasi vinyl berputar.
- ⏭️ Navigasi lagu sebelumnya dan berikutnya.
- ⏳ Progress bar untuk melihat durasi dan melakukan seek lagu.
- 🎵 Menampilkan judul lagu yang sedang diputar.

---

## 🛠️ Teknologi yang Digunakan
- Python
- Tkinter (GUI)
- Pygame (Audio Player)
- PIL (Image Processing)
- Mutagen (MP3 Metadata)

---

## 📥 Instalasi
1. Pastikan Python telah terinstal di sistem Anda.
2. Install dependensi dengan perintah berikut:
   ```bash
   pip install pygame pillow mutagen
   ```
3. Jalankan program dengan perintah:
   ```bash
   python Music_Player.py
   ```

---

## 🐞 Kontribusi & Perbaikan Bug
Jika Anda menemukan bug atau ingin meningkatkan fungsionalitas aplikasi, berikut adalah beberapa area yang dapat diperbaiki:

- **Handling Error Saat Load Lagu:** Saat pengguna memilih folder tanpa MP3, tambahkan validasi agar aplikasi tidak crash.
- **Optimasi Seek Bar:** Implementasi saat seek masih bisa diperbaiki agar lebih akurat.
- **Peningkatan Rotasi Vinyl:** Saat lagu di-pause, terkadang animasi masih berjalan. Bisa diperbaiki dengan mekanisme yang lebih ketat.
- **Tambah Dukungan Format Lain:** Saat ini hanya mendukung MP3, bisa diperluas untuk mendukung format lain seperti WAV atau FLAC.

Jika ingin berkontribusi, silakan fork repository ini dan ajukan pull request!

---

## 📜 Lisensi
Proyek ini menggunakan lisensi MIT. Anda bebas mengembangkan dan menggunakan aplikasi ini untuk keperluan pribadi maupun komersial.

---

🎧 **Selamat menikmati musik Anda!**

