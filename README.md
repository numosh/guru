# GURU - AI Terminal untuk Profiling Guru Indonesia

```
 ██████╗ ██╗   ██╗██████╗ ██╗   ██╗
██╔════╝ ██║   ██║██╔══██╗██║   ██║
██║  ███╗██║   ██║██████╔╝██║   ██║
██║   ██║██║   ██║██╔══██╗██║   ██║
╚██████╔╝╚██████╔╝██║  ██║╚██████╔╝
 ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ 
```

**Guided Understanding Resource Unity**  
*Tempat Belajar dan Mengajar*

Aplikasi terminal interaktif menggunakan Python untuk profiling guru SD, SMP, SMA Indonesia dengan AI menggunakan VirtueAI GLM4.

## 🎯 Fitur Utama

1. **Role-based System**: Pelajar atau Pengajar
2. **Level Pendidikan**: SD, SMP, atau SMA
3. **System Prompt Kompleks**: Jawaban ramah, naratif, dan mudah dimengerti untuk setiap kombinasi role dan level
4. **Dual Mode (Pelajar)**: Otomatis switch antara Mode Pembelajaran dan Mode Konseling
5. **Struktur Jawaban Natural**: Tanpa simbol formatting, murni narasi mengalir
5. **VirtueAI Integration**: Menggunakan API VirtueAI dengan model GLM4
6. **Konfigurasi Fleksibel**: Temperature, top_p, top_k dapat dikonfigurasi
7. **Error Handling**: Menangani timeout dan error koneksi dengan baik
8. **UI Menarik**: Logo ASCII dan tampilan terminal yang cantik dengan Rich library
9. **100% Bahasa Indonesia**: Semua output dalam bahasa Indonesia

## 📋 Prasyarat

1. **Python 3.7+**
2. **Salah satu dari:**
   - **Koneksi Internet** - Untuk VirtueAI API (prioritas utama), atau
   - **Ollama Local** - Install dari [ollama.ai](https://ollama.ai) sebagai fallback
     ```bash
     ollama serve
     ollama pull llama3.1:8b
     ```

## 🚀 Instalasi

1. Clone atau download repository ini
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Cara Penggunaan

### Cara Cepat (Recommended):
```bash
./run.sh
```

Script `run.sh` akan otomatis:
- ✅ Cek instalasi Python
- ✅ Membuat virtual environment
- ✅ Install dependencies
- ✅ Cek koneksi internet
- ✅ Menjalankan aplikasi

### Cara Manual:
```bash
python guru_ai.py
```

Atau:
```bash
chmod +x guru_ai.py
./guru_ai.py
```

## 🎮 Alur Penggunaan

1. Aplikasi akan menampilkan welcome screen
2. Pilih role: Pelajar (1) atau Pengajar (2)
3. Pilih tingkat pendidikan: SD (1), SMP (2), atau SMA (3)
4. Mulai bertanya atau berdiskusi dengan AI
5. Ketik `quit` atau `exit` untuk keluar

## ⚙️ Konfigurasi

Edit bagian konfigurasi di `guru_ai.py`:

```python
# VirtueAI API (Online - Prioritas Utama)
VIRTUEAI_URL = "https://api.virtueai.id/api/generate"
VIRTUEAI_MODEL = "llama3.1:latest"

# Ollama Local (Fallback jika offline)
OLLAMA_URL = "http://localhost:11434"
OLLAMA_MODEL = "llama3.1:8b"

# Parameter AI
TEMPERATURE = 0.7    # Kreativitas (0.0-1.0)
TOP_P = 0.9          # Nucleus sampling
TOP_K = 40           # Top-K sampling
```

**Auto-Fallback:** Aplikasi otomatis akan mencoba VirtueAI dulu. Jika gagal, akan fallback ke Ollama local.

## 📝 Contoh Interaksi

### Untuk Pelajar SD:
```
Anda: Kenapa langit berwarna biru?

GURU AI:
Halo adik! Wah, pertanyaan yang bagus sekali!

Jadi begini ya, langit itu sebenarnya berwarna biru karena cahaya matahari yang bermain-main dengan udara di atas kita. Kalau kamu lihat cahaya matahari itu kan kelihatan putih ya? Nah, sebenarnya cahaya putih itu terdiri dari banyak sekali warna, seperti pelangi!

Kenapa biru? Karena warna biru itu suka sekali bertebaran ke mana-mana ketika cahaya matahari masuk ke udara. Seperti kalau kamu lempar bola kecil-kecil, bola biru itu lebih suka lompat-lompat ke segala arah dibanding bola merah yang lebih tenang.

Coba deh besok kalau siang hari cerah, adik lihat langit sambil bayangin cahaya matahari lagi bermain dengan udara! Keren kan?
```

### Untuk Pengajar SMA:
```
Anda: Bagaimana cara mengajar konsep integral yang efektif?

GURU AI:
Terima kasih sudah bertanya! Mengajar integral memang perlu pendekatan yang thoughtful karena ini adalah transisi besar dari pemikiran aljabar ke kalkulus.

Saya sarankan mulai dengan membangun intuisi geometris terlebih dahulu. Ajak siswa melihat integral sebagai cara menghitung luas daerah yang tidak beraturan, bukan langsung masuk ke rumus. Gunakan tools seperti GeoGebra atau Desmos untuk visualisasi interaktif area di bawah kurva. Biarkan mereka bereksperimen dengan fungsi sederhana dan lihat bagaimana luas berubah.

Dari perspektif pedagogis, ini sejalan dengan teori konstruktivisme dimana siswa membangun pemahaman dari konkret ke abstrak. Ketika mereka sudah comfortable dengan konsep luas, baru introduce notasi sigma dan limit untuk formalisasi matematis.

Untuk implementasinya, berikan project autentik seperti menghitung volume botol air mineral menggunakan integral volume rotasi. Atau analisis data real seperti konsumsi listrik dari grafik daya terhadap waktu. Ini membuat mereka see the point kenapa belajar integral.

Yang penting, jangan terburu-buru ke teknik integrasi yang kompleks sebelum konsep fundamental benar-benar solid.
```

## 🛠️ Troubleshooting

**Tidak bisa terhubung ke AI:**
- Aplikasi akan otomatis fallback ke Ollama local jika VirtueAI tidak tersedia
- Pastikan salah satu tersedia: koneksi internet ATAU Ollama local

**VirtueAI offline:**
- Install Ollama: `brew install ollama` (Mac) atau download dari [ollama.ai](https://ollama.ai)
- Jalankan: `ollama serve`
- Pull model: `ollama pull llama3.1:8b`

**Timeout error:**
- Pastikan koneksi internet stabil (jika pakai VirtueAI)
- Coba lagi beberapa saat kemudian

## 📦 Struktur Kode

- `guru_ai.py` - Main application file
- `requirements.txt` - Python dependencies
- `README.md` - Dokumentasi utama
- `MODE_KONSELING.md` - Panduan mode konseling
- `CONTOH_RESPONSE.md` - Contoh response yang baik vs buruk

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan buat pull request atau issue untuk perbaikan dan fitur baru.

## 📄 Lisensi

Open source - gunakan dengan bebas untuk tujuan pendidikan.

## 👨‍💻 Author

GURU AI Project - AI Terminal untuk Profiling Guru Indonesia

---

**Selamat menggunakan GURU AI! 🎓🇮🇩**
