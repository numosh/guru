#!/bin/bash

#############################################
# GURU AI - One-Command Installer
# Author: Anugrah Prahasta (@anugrahprahasta)
# Easy setup untuk semua orang!
#############################################

set -e  # Exit on error

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Banner
echo ""
echo -e "${CYAN}================================================${NC}"
echo -e "${CYAN}   GURU AI - One-Command Installer${NC}"
echo -e "${CYAN}   Guided Understanding Resource Unity${NC}"
echo -e "${CYAN}================================================${NC}"
echo ""
echo -e "${BLUE}Author: Anugrah Prahasta (@anugrahprahasta)${NC}"
echo -e "${BLUE}Version: 1.0.0${NC}"
echo ""

# Detect OS
OS="$(uname -s)"
case "${OS}" in
    Linux*)     MACHINE=Linux;;
    Darwin*)    MACHINE=Mac;;
    CYGWIN*)    MACHINE=Windows;;
    MINGW*)     MACHINE=Windows;;
    *)          MACHINE="UNKNOWN:${OS}"
esac

echo -e "${CYAN}🖥️  Detected OS: ${MACHINE}${NC}"
echo ""

#############################################
# Installation Mode Selection
#############################################
echo -e "${YELLOW}Choose installation mode:${NC}"
echo -e "  ${GREEN}1.${NC} Global install (command: ${CYAN}guru${NC} from anywhere)"
echo -e "  ${GREEN}2.${NC} Local install (run from this directory only)"
echo ""
read -p "$(echo -e ${CYAN}Select mode [1/2]: ${NC})" INSTALL_MODE

GLOBAL_INSTALL=false
if [[ "$INSTALL_MODE" == "1" ]]; then
    GLOBAL_INSTALL=true
    echo -e "${GREEN}→ Global installation selected${NC}"
    echo ""
    echo -e "${YELLOW}⚠️  Note: Global install requires guru command in shell PATH${NC}"
    echo -e "${YELLOW}   Installer will create symlink to /usr/local/bin/guru${NC}"
    echo ""
    read -p "$(echo -e ${CYAN}Continue with global install? [Y/n]: ${NC})" -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]] && [[ ! -z $REPLY ]]; then
        echo -e "${YELLOW}Switching to local install...${NC}"
        GLOBAL_INSTALL=false
    fi
else
    echo -e "${GREEN}→ Local installation selected${NC}"
fi
echo ""

#############################################
# 1. Check Python
#############################################
echo -e "${YELLOW}[1/6] Checking Python...${NC}"

if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    echo -e "${GREEN}✓ Python3 found: ${PYTHON_VERSION}${NC}"
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
    MAJOR_VERSION=$(echo $PYTHON_VERSION | cut -d. -f1)
    if [ "$MAJOR_VERSION" -ge 3 ]; then
        echo -e "${GREEN}✓ Python found: ${PYTHON_VERSION}${NC}"
        PYTHON_CMD="python"
    else
        echo -e "${RED}❌ Python 3.7+ required, found Python ${PYTHON_VERSION}${NC}"
        echo -e "${YELLOW}Please install Python 3.7+ from: https://www.python.org/downloads/${NC}"
        exit 1
    fi
else
    echo -e "${RED}❌ Python not found!${NC}"
    echo -e "${YELLOW}Please install Python 3.7+ from: https://www.python.org/downloads/${NC}"
    exit 1
fi

#############################################
# 2. Create Virtual Environment
#############################################
echo ""
echo -e "${YELLOW}[2/6] Setting up virtual environment...${NC}"

if [ ! -d "venv" ]; then
    echo -e "${CYAN}Creating virtual environment...${NC}"
    $PYTHON_CMD -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${GREEN}✓ Virtual environment already exists${NC}"
fi

# Activate virtual environment
echo -e "${CYAN}Activating virtual environment...${NC}"
if [ "$MACHINE" = "Windows" ]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi
echo -e "${GREEN}✓ Virtual environment activated${NC}"

#############################################
# 3. Install Dependencies
#############################################
echo ""
echo -e "${YELLOW}[3/6] Installing dependencies...${NC}"

if [ -f "requirements.txt" ]; then
    pip install --upgrade pip --quiet
    pip install -r requirements.txt --quiet
    echo -e "${GREEN}✓ Dependencies installed (requests, rich)${NC}"
else
    echo -e "${RED}❌ requirements.txt not found!${NC}"
    exit 1
fi

#############################################
# 3.5. Global Installation (Optional)
#############################################
if [ "$GLOBAL_INSTALL" = true ]; then
    echo ""
    echo -e "${YELLOW}[4/6] Installing globally...${NC}"
    
    # Get the full path to guru executable
    GURU_PATH="$(pwd)/guru"
    
    # Make guru executable
    chmod +x guru
    
    # Create symlink to /usr/local/bin (requires sudo)
    if [ -w "/usr/local/bin" ]; then
        ln -sf "$GURU_PATH" /usr/local/bin/guru
        echo -e "${GREEN}✓ GURU AI installed globally${NC}"
        echo -e "${CYAN}   Symlink created: /usr/local/bin/guru → $GURU_PATH${NC}"
    else
        echo -e "${YELLOW}⚠️  Need sudo to create symlink in /usr/local/bin${NC}"
        sudo ln -sf "$GURU_PATH" /usr/local/bin/guru
        echo -e "${GREEN}✓ GURU AI installed globally (with sudo)${NC}"
        echo -e "${CYAN}   Symlink created: /usr/local/bin/guru → $GURU_PATH${NC}"
    fi
    
    # Verify installation
    if command -v guru &> /dev/null; then
        echo -e "${GREEN}✓ Verified: 'guru' command is now available!${NC}"
    else
        echo -e "${RED}⚠️  Warning: 'guru' command not found in PATH${NC}"
        echo -e "${YELLOW}   You may need to restart your terminal or run: hash -r${NC}"
    fi
else
    echo ""
    echo -e "${YELLOW}[4/6] Skipping global installation...${NC}"
fi

#############################################
# 4. Check Internet Connection
#############################################
echo ""
echo -e "${YELLOW}[5/6] Checking connectivity...${NC}"

if curl -s --head --request GET https://api.virtueai.id > /dev/null; then
    echo -e "${GREEN}✓ VirtueAI API accessible (Online mode available)${NC}"
    VIRTUEAI_OK=true
else
    echo -e "${YELLOW}⚠️  VirtueAI API not accessible${NC}"
    VIRTUEAI_OK=false
fi

# Check Ollama (local fallback)
if command -v ollama &> /dev/null; then
    echo -e "${GREEN}✓ Ollama found (Local mode available)${NC}"
    OLLAMA_OK=true
    
    # Check if llama3.1:8b is available
    if ollama list | grep -q "llama3.1:8b"; then
        echo -e "${GREEN}✓ Model llama3.1:8b already installed${NC}"
    else
        echo -e "${YELLOW}⚠️  Model llama3.1:8b not found${NC}"
        read -p "$(echo -e ${CYAN}Do you want to download llama3.1:8b now? [y/N]: ${NC})" -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            echo -e "${CYAN}Downloading llama3.1:8b (this may take a while ~4.7GB)...${NC}"
            ollama pull llama3.1:8b
            echo -e "${GREEN}✓ Model downloaded successfully${NC}"
        else
            echo -e "${YELLOW}⚠️  You can download later with: ollama pull llama3.1:8b${NC}"
        fi
    fi
else
    echo -e "${YELLOW}⚠️  Ollama not found${NC}"
    OLLAMA_OK=false
fi

echo ""
if [ "$VIRTUEAI_OK" = true ] || [ "$OLLAMA_OK" = true ]; then
    echo -e "${GREEN}✓ At least one AI backend available!${NC}"
else
    echo -e "${RED}❌ No AI backend available!${NC}"
    echo ""
    echo -e "${YELLOW}Please either:${NC}"
    echo -e "${YELLOW}  1. Connect to internet (for VirtueAI), OR${NC}"
    echo -e "${YELLOW}  2. Install Ollama for offline mode:${NC}"
    echo ""
    if [ "$MACHINE" = "Mac" ]; then
        echo -e "${CYAN}  brew install ollama${NC}"
        echo -e "${CYAN}  ollama serve &${NC}"
        echo -e "${CYAN}  ollama pull llama3.1:8b${NC}"
    elif [ "$MACHINE" = "Linux" ]; then
        echo -e "${CYAN}  curl -fsSL https://ollama.ai/install.sh | sh${NC}"
        echo -e "${CYAN}  ollama serve &${NC}"
        echo -e "${CYAN}  ollama pull llama3.1:8b${NC}"
    else
        echo -e "${CYAN}  Download from: https://ollama.ai${NC}"
    fi
    echo ""
    echo -e "${YELLOW}Then run this installer again.${NC}"
    exit 1
fi

#############################################
# 5. Create Run Script
#############################################
echo ""
echo -e "${YELLOW}[6/6] Creating launcher...${NC}"

# Create quick run script
cat > run_guru.sh << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
source venv/bin/activate 2>/dev/null || source venv/Scripts/activate
python guru_ai.py
EOF

chmod +x run_guru.sh

# Create Windows batch file
cat > run_guru.bat << 'EOF'
@echo off
cd /d "%~dp0"
call venv\Scripts\activate
python guru_ai.py
pause
EOF

echo -e "${GREEN}✓ Launcher created${NC}"

#############################################
# Installation Complete!
#############################################
echo ""
echo -e "${GREEN}================================================${NC}"
echo -e "${GREEN}   ✅ Installation Complete!${NC}"
echo -e "${GREEN}================================================${NC}"
echo ""
echo -e "${CYAN}🚀 To run GURU AI:${NC}"
echo ""

if [ "$GLOBAL_INSTALL" = true ]; then
    echo -e "${YELLOW}   From anywhere in terminal:${NC}"
    echo -e "${GREEN}   guru${NC}"
    echo ""
    echo -e "${YELLOW}   If 'guru' not found, restart terminal or run:${NC}"
    echo -e "${CYAN}   hash -r${NC}"
    echo ""
    echo -e "${YELLOW}   Or use launchers:${NC}"
fi

if [ "$MACHINE" = "Windows" ]; then
    echo -e "${YELLOW}   Double-click: run_guru.bat${NC}"
    echo -e "${YELLOW}   Or run: python guru_ai.py${NC}"
else
    echo -e "${YELLOW}   ./run_guru.sh${NC}"
    echo -e "${YELLOW}   Or: ./run.sh${NC}"
fi

echo ""
echo -e "${CYAN}📚 Documentation:${NC}"
echo -e "${YELLOW}   README.md - Getting started${NC}"
echo -e "${YELLOW}   ROADMAP.md - Future plans${NC}"
echo -e "${YELLOW}   CONTRIBUTING.md - How to contribute${NC}"
echo ""

# Auto-run option
echo ""
read -p "$(echo -e ${CYAN}Do you want to run GURU AI now? [Y/n]: ${NC})" -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]] || [[ -z $REPLY ]]; then
    echo ""
    echo -e "${GREEN}🚀 Starting GURU AI...${NC}"
    echo ""
    
    if [ "$GLOBAL_INSTALL" = true ]; then
        guru
    else
        $PYTHON_CMD guru_ai.py
    fi
else
    echo ""
    echo -e "${CYAN}You can run GURU AI anytime with:${NC}"
    
    if [ "$GLOBAL_INSTALL" = true ]; then
        echo -e "${GREEN}   guru${NC}"
    else
        if [ "$MACHINE" = "Windows" ]; then
            echo -e "${YELLOW}   run_guru.bat${NC}"
        else
            echo -e "${YELLOW}   ./run_guru.sh${NC}"
        fi
    fi
    echo ""
fi
