# 📦 Installation Guide - GURU AI

## 🎯 Easiest Way: One-Command Install

### Linux / macOS

```bash
git clone https://github.com/numosh/guru.git
cd guru
chmod +x install.sh
./install.sh
```

### Windows (PowerShell)

```powershell
git clone https://github.com/numosh/guru.git
cd guru
bash install.sh
```

Atau download ZIP dari GitHub, extract, lalu double-click `install.sh`

---

## 🔧 What the Installer Does

1. ✅ **Check Python** - Memastikan Python 3.7+ terinstall
2. ✅ **Setup Virtual Environment** - Isolasi dependencies
3. ✅ **Install Dependencies** - `pip install requests rich`
4. ✅ **Check Connectivity** - Test VirtueAI & Ollama
5. ✅ **Download Model (Optional)** - Ollama llama3.1:8b
6. ✅ **Create Launchers** - Scripts untuk easy run
7. ✅ **Auto-Run** - Langsung jalankan aplikasi

---

## 📋 Prerequisites

### Minimum Requirements

- **Python 3.7+** (Python 3.9+ recommended)
- **Internet Connection** ATAU **Ollama installed**
- **2GB Free Space** (jika download Ollama model)
- **Terminal/Command Prompt**

### Operating Systems

- ✅ Linux (Ubuntu, Debian, Fedora, dll)
- ✅ macOS (10.14+)
- ✅ Windows 10/11 (with Git Bash or WSL)

---

## 🚀 Running GURU AI

Setelah installation:

### Linux / macOS
```bash
./run_guru.sh
```

### Windows
```cmd
run_guru.bat
```

Atau activate venv manual:
```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
python guru_ai.py
```

---

## 🌐 AI Backend Options

GURU AI support 2 backends:

### Option 1: VirtueAI (Online)
- ✅ No installation needed
- ✅ Always up-to-date
- ✅ Fast inference
- ❌ Requires internet

### Option 2: Ollama (Offline)
- ✅ 100% offline
- ✅ Privacy (data stays local)
- ✅ Free forever
- ❌ Requires ~5GB disk space

**Best Practice:** Install Ollama sebagai fallback!

---

## 📥 Installing Ollama (Optional but Recommended)

### macOS
```bash
brew install ollama
ollama serve &
ollama pull llama3.1:8b
```

### Linux
```bash
curl -fsSL https://ollama.ai/install.sh | sh
ollama serve &
ollama pull llama3.1:8b
```

### Windows
1. Download dari: https://ollama.ai
2. Install
3. Run: `ollama pull llama3.1:8b`

---

## 🐛 Troubleshooting

### Python not found
```bash
# Install Python
# Ubuntu/Debian:
sudo apt install python3 python3-pip python3-venv

# macOS:
brew install python3

# Windows:
# Download dari python.org
```

### Permission denied (Linux/Mac)
```bash
chmod +x install.sh
chmod +x run_guru.sh
```

### Module not found
```bash
# Activate venv first
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### VirtueAI & Ollama both unavailable
```bash
# Check internet
ping google.com

# Or install Ollama for offline mode
# See section above
```

### Ollama model download fails
```bash
# Check disk space
df -h  # Linux/Mac
# Need ~5GB free

# Retry download
ollama pull llama3.1:8b

# Or use smaller model
ollama pull qwen2.5:1.5b  # ~1GB
```

---

## 🔄 Updating GURU AI

```bash
cd guru
git pull origin main
pip install -r requirements.txt --upgrade
```

---

## 🗑️ Uninstalling

```bash
cd guru
rm -rf venv  # Remove virtual environment
cd ..
rm -rf guru  # Remove entire directory
```

Untuk Ollama:
```bash
# macOS
brew uninstall ollama

# Linux
sudo rm /usr/local/bin/ollama
rm -rf ~/.ollama

# Windows
# Uninstall via Control Panel
```

---

## 💡 Tips

### Faster Installation
```bash
# Use --quiet flag
pip install -r requirements.txt --quiet
```

### Use Different Python Version
```bash
# Specify python version
python3.11 -m venv venv
```

### Share Installation
```bash
# Copy entire guru directory to USB/cloud
# Run on any computer with Python installed
# No need to reinstall!
```

### Offline Installation
1. Install on computer with internet
2. Copy entire `guru/` directory
3. Copy to offline computer
4. Requires Ollama with pre-downloaded model

---

## 📞 Need Help?

- 📖 Read [README.md](README.md)
- 🐛 Check [GitHub Issues](https://github.com/numosh/guru/issues)
- 💬 Ask in [Discussions](https://github.com/numosh/guru/discussions)
- 📧 Email: [TBD]

---

**Installation should take less than 5 minutes! 🚀**

Made with ❤️ by Anugrah Prahasta
