# ⚡ Global Command Setup - GURU AI

## 🎯 Goal: Run `guru` from Anywhere

Seperti `copilot`, `git`, atau `npm` - ketik `guru` dan langsung jalan!

---

## 🚀 Installation Methods

### **Method 1: Auto Installer (Recommended)**

```bash
git clone https://github.com/numosh/guru.git
cd guru
chmod +x install.sh
./install.sh
```

**Pilih:** `1. Global install`

Installer akan:
- ✅ Setup virtual environment
- ✅ Install dependencies
- ✅ Install `guru` command globally
- ✅ Test connectivity

**Setelah install:**
```bash
# From anywhere in terminal:
guru
```

---

### **Method 2: Manual pip install**

```bash
cd guru
pip install -e .
```

**Test:**
```bash
guru --version  # (future feature)
guru            # Run application
```

---

### **Method 3: Add to PATH (Alternative)**

#### Linux / macOS

1. **Create symlink:**
```bash
cd guru
chmod +x guru
sudo ln -s "$(pwd)/guru" /usr/local/bin/guru
```

2. **Or add to PATH in shell config:**
```bash
# Add to ~/.bashrc or ~/.zshrc:
export PATH="$PATH:/path/to/guru"
```

3. **Reload shell:**
```bash
source ~/.bashrc  # or source ~/.zshrc
```

#### Windows

1. **Add to System PATH:**
   - Win + R → `sysdm.cpl`
   - Advanced → Environment Variables
   - Path → Edit → New
   - Add: `C:\path\to\guru`

2. **Or use batch file in system folder:**
```cmd
copy guru.bat C:\Windows\System32\
```

---

## 🧪 Testing Global Command

```bash
# From any directory:
cd ~
guru

# Should show GURU AI welcome screen
```

---

## 📦 How It Works

### **setup.py** - Python Package Setup
```python
entry_points={
    "console_scripts": [
        "guru=guru_ai:main",
    ],
}
```

Ini membuat command `guru` yang call `main()` dari `guru_ai.py`

### **guru** - Executable Entry Point
```python
#!/usr/bin/env python3
from guru_ai import main
main()
```

Standalone executable yang bisa jalan dengan `./guru`

---

## 🔧 Uninstall Global Command

### If installed with pip:
```bash
pip uninstall guru-ai-indonesia
```

### If using symlink:
```bash
sudo rm /usr/local/bin/guru
```

### If using PATH:
Remove the PATH entry from shell config.

---

## 💡 Advanced: Custom Alias

Kalau mau command lebih pendek atau custom:

```bash
# Add to ~/.bashrc or ~/.zshrc:
alias g='guru'
alias teach='guru'
alias belajar='guru'
```

Then:
```bash
g              # Run guru
teach          # Run guru
belajar        # Run guru
```

---

## 🌍 Multi-User Setup (Server/Lab Computer)

For system-wide installation (all users):

```bash
# Install globally for all users
sudo pip install -e /path/to/guru

# Or create system symlink
sudo ln -s /path/to/guru/guru /usr/local/bin/guru
sudo chmod +x /usr/local/bin/guru
```

Now any user can run:
```bash
guru
```

---

## 📊 Comparison with Other CLIs

| CLI Tool | Command | Install Method |
|----------|---------|----------------|
| **GitHub Copilot** | `copilot` | `npm install -g` |
| **Git** | `git` | System package manager |
| **Node.js** | `node` | Download installer |
| **Python** | `python` | Download installer |
| **GURU AI** | `guru` | `pip install -e .` |

---

## 🎓 Example Usage After Global Install

```bash
# Open terminal dari directory manapun
cd ~/Documents
guru

# Atau dari home
cd ~
guru

# Atau dari project lain
cd /path/to/other/project
guru
```

**Always works!** ✨

---

## 🐛 Troubleshooting

### Command not found
```bash
# Check if installed
pip list | grep guru

# Reinstall
cd guru
pip install -e . --force-reinstall
```

### Permission denied
```bash
# Linux/Mac:
sudo pip install -e .

# Or install for user only:
pip install -e . --user
```

### Wrong Python version
```bash
# Use specific Python version
python3.11 -m pip install -e .
```

### Virtual environment conflict
```bash
# Deactivate venv first
deactivate

# Install globally (outside venv)
pip install -e /path/to/guru
```

---

## 📚 Learn More

- [Python Entry Points](https://packaging.python.org/guides/distributing-packages-using-setuptools/#entry-points)
- [Console Scripts](https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html)
- [setup.py Guide](https://docs.python.org/3/distutils/setupscript.html)

---

**Made with ❤️ by Anugrah Prahasta (@anugrahprahasta)**

Now you can teach Indonesia, one `guru` command at a time! 🇮🇩🎓
