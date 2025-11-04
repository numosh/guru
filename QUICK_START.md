# ⚡ Quick Start - GURU AI

## 🎯 Install & Run dalam 2 Cara

### 🌍 Option 1: Global Command (Recommended)

**Install sekali, pakai selamanya dari mana saja!**

```bash
git clone https://github.com/numosh/guru.git
cd guru
./install.sh
```

**Pilih:** `1. Global install`

**Setelah install, dari directory manapun:**
```bash
guru
```

**That's it!** ✨

---

### 📁 Option 2: Local Install

**Hanya bisa dijalankan dari folder guru**

```bash
git clone https://github.com/numosh/guru.git
cd guru
./install.sh
```

**Pilih:** `2. Local install`

**Run dari folder guru:**
```bash
cd guru
./run_guru.sh  # Linux/Mac
run_guru.bat   # Windows
```

---

## 🚀 Comparison

| Feature | Global Install | Local Install |
|---------|----------------|---------------|
| **Command** | `guru` (anywhere) | `./run_guru.sh` (in folder) |
| **Convenience** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Setup** | Same | Same |
| **Portability** | ✅ Works everywhere | ❌ Folder-specific |
| **Updates** | Auto via git pull | Auto via git pull |

**Recommendation:** Use Global Install! 🌟

---

## 📱 What You'll See

```
╔═══════════════════════════════════════════════════╗
║  GURU AI - AI Terminal Guru Indonesia             ║
║  Guided Understanding Resource Unity              ║
║     @anugrahprahasta 2025                         ║
╚═══════════════════════════════════════════════════╝

🔌 Mengecek koneksi AI...
✓ VirtueAI Online - Model: llama3.1:latest

✨ Bagaimana Anda menggunakan aplikasi ini?
  1. Pelajar (siswa/siswi yang belajar)
  2. Pengajar (guru/mentor)
Pilih opsi [1/2]: _
```

---

## 💡 Usage Examples

### For Students (Pelajar)

**Learning Mode:**
```
💭 Anda: Kenapa langit biru?

🎓 Respons GURU AI (Biru)
Wah, pertanyaan bagus! Jadi gini ya, langit biru karena 
cahaya matahari punya banyak warna. Waktu cahaya masuk 
ke udara, warna biru paling suka menyebar. Makanya kita 
lihat langit jadi biru...
```

**Counseling Mode:**
```
💭 Anda: Saya tidak suka matematika

💚 Respons GURU AI (Hijau - Konseling)
Aku ngerti kok. Matematika emang bisa bikin pusing ya. 
Mau cerita kenapa kamu ga suka? Apa karena susah, atau 
mungkin cara ngajarnya yang bikin bingung?
```

### For Teachers (Pengajar)

```
💭 Anda: Strategi mengajar perkalian untuk SD kelas 2?

🎓 Respons GURU AI
Untuk kelas 2 SD, gunakan pendekatan konkret-visual. 
Mulai dengan manipulatif seperti kelereng atau balok. 
Contoh: 3 × 4 bisa divisualisasikan sebagai 3 kelompok 
yang masing-masing berisi 4 kelereng...
```

---

## ⚙️ System Requirements

**Minimal:**
- Python 3.7+
- 100MB free space
- Internet connection OR Ollama

**Recommended:**
- Python 3.9+
- 5GB free space (untuk Ollama model)
- Ollama installed (for offline mode)

---

## 🆘 Common Issues

**`guru: command not found`**
```bash
# Reinstall globally
cd guru
pip install -e .
```

**Permission denied**
```bash
chmod +x install.sh
./install.sh
```

**No AI backend available**
```bash
# Install Ollama
brew install ollama  # Mac
# or download from ollama.ai

# Pull model
ollama pull llama3.1:8b
```

---

## 📚 Learn More

- 📖 [Full Documentation](README.md)
- 🌍 [Global Command Setup](GLOBAL_COMMAND.md)
- 🗺️ [Roadmap](ROADMAP.md)
- 🤝 [Contributing](CONTRIBUTING.md)

---

## 🚀 Ready to Start?

```bash
git clone https://github.com/numosh/guru.git
cd guru
./install.sh
```

**Choose: 1 (Global)**

**Then from anywhere:**
```bash
guru
```

**Selamat menggunakan GURU AI! 🎉**

---

Made with ❤️ by **Anugrah Prahasta** (@anugrahprahasta)

"Mencerdaskan Indonesia, Satu Command at a Time" 🇮🇩🎓
