#!/bin/bash

#############################################
# GURU AI - One-Command Installer (v2.0 IMPROVED)
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
MAGENTA='\033[0;35m'
NC='\033[0m' # No Color

# Banner
echo ""
echo -e "${CYAN}================================================${NC}"
echo -e "${CYAN}   GURU AI - One-Command Installer v2.0${NC}"
echo -e "${CYAN}   Guided Understanding Resource Unity${NC}"
echo -e "${MAGENTA}   ✨ IMPROVED VERSION AVAILABLE ✨${NC}"
echo -e "${CYAN}================================================${NC}"
echo ""
echo -e "${BLUE}Author: Anugrah Prahasta (@anugrahprahasta)${NC}"
echo -e "${BLUE}Version: 2.0.0 IMPROVED${NC}"
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
# Version Selection
#############################################
echo -e "${YELLOW}Choose GURU AI version to install:${NC}"
echo ""
echo -e "  ${GREEN}1.${NC} ${MAGENTA}IMPROVED VERSION${NC} (Recommended)"
echo -e "     ${CYAN}✓ 90%+ response consistency${NC}"
echo -e "     ${CYAN}✓ Automatic quality validation${NC}"
echo -e "     ${CYAN}✓ 50% faster, 66% cheaper${NC}"
echo -e "     ${CYAN}✓ Better prompt structure${NC}"
echo -e "     ${CYAN}✓ Quality scores displayed${NC}"
echo ""
echo -e "  ${GREEN}2.${NC} Original Version"
echo -e "     ${YELLOW}⚠️  45% structure adherence${NC}"
echo -e "     ${YELLOW}⚠️  No quality validation${NC}"
echo -e "     ${YELLOW}⚠️  Multi-agent overhead (slower)${NC}"
echo ""
read -p "$(echo -e ${CYAN}Select version [1/2] (default: 1): ${NC})" VERSION_CHOICE

USE_IMPROVED=true
MAIN_FILE="guru_ai_improved.py"

if [[ "$VERSION_CHOICE" == "2" ]]; then
    USE_IMPROVED=false
    MAIN_FILE="guru_ai.py"
    echo -e "${YELLOW}→ Original version selected${NC}"
else
    echo -e "${GREEN}→ IMPROVED version selected (Recommended!)${NC}"
fi
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
echo -e "${YELLOW}[1/7] Checking Python...${NC}"

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
echo -e "${YELLOW}[2/7] Setting up virtual environment...${NC}"

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
echo -e "${YELLOW}[3/7] Installing dependencies...${NC}"

if [ -f "requirements.txt" ]; then
    pip install --upgrade pip --quiet
    pip install -r requirements.txt --quiet
    echo -e "${GREEN}✓ Dependencies installed (requests, rich)${NC}"
else
    echo -e "${RED}❌ requirements.txt not found!${NC}"
    exit 1
fi

#############################################
# 4. Verify Improved Version Files
#############################################
if [ "$USE_IMPROVED" = true ]; then
    echo ""
    echo -e "${YELLOW}[4/7] Verifying IMPROVED version files...${NC}"

    MISSING_FILES=false

    if [ ! -f "guru_ai_improved.py" ]; then
        echo -e "${RED}❌ guru_ai_improved.py not found!${NC}"
        MISSING_FILES=true
    else
        echo -e "${GREEN}✓ guru_ai_improved.py found${NC}"
    fi

    if [ ! -f "response_validator.py" ]; then
        echo -e "${RED}❌ response_validator.py not found!${NC}"
        MISSING_FILES=true
    else
        echo -e "${GREEN}✓ response_validator.py found${NC}"
    fi

    if [ ! -f "improved_prompts.py" ]; then
        echo -e "${RED}❌ improved_prompts.py not found!${NC}"
        MISSING_FILES=true
    else
        echo -e "${GREEN}✓ improved_prompts.py found${NC}"
    fi

    if [ "$MISSING_FILES" = true ]; then
        echo ""
        echo -e "${RED}❌ Missing required files for IMPROVED version!${NC}"
        echo -e "${YELLOW}Please ensure all files are present or use original version.${NC}"
        exit 1
    fi

    # Test imports
    echo -e "${CYAN}Testing Python imports...${NC}"
    if $PYTHON_CMD -c "from response_validator import ResponseValidator; from improved_prompts import IMPROVED_SYSTEM_PROMPTS" 2>/dev/null; then
        echo -e "${GREEN}✓ All modules import successfully${NC}"
    else
        echo -e "${RED}❌ Module import failed!${NC}"
        echo -e "${YELLOW}There may be syntax errors in the improved files.${NC}"
        exit 1
    fi
else
    echo ""
    echo -e "${YELLOW}[4/7] Skipping improved version verification...${NC}"
fi

#############################################
# 5. Create Global Command (Optional)
#############################################
if [ "$GLOBAL_INSTALL" = true ]; then
    echo ""
    echo -e "${YELLOW}[5/7] Installing globally...${NC}"

    # Create wrapper script that uses the selected version
    WRAPPER_SCRIPT="$(pwd)/guru"

    cat > "$WRAPPER_SCRIPT" << EOF
#!/bin/bash
# GURU AI Global Launcher
cd "$(pwd)"
source venv/bin/activate 2>/dev/null || source venv/Scripts/activate
python $MAIN_FILE "\$@"
EOF

    # Make wrapper executable
    chmod +x "$WRAPPER_SCRIPT"

    # Create symlink to /usr/local/bin
    if [ -w "/usr/local/bin" ]; then
        ln -sf "$WRAPPER_SCRIPT" /usr/local/bin/guru
        echo -e "${GREEN}✓ GURU AI installed globally${NC}"
        echo -e "${CYAN}   Symlink created: /usr/local/bin/guru → $WRAPPER_SCRIPT${NC}"
    else
        echo -e "${YELLOW}⚠️  Need sudo to create symlink in /usr/local/bin${NC}"
        sudo ln -sf "$WRAPPER_SCRIPT" /usr/local/bin/guru
        echo -e "${GREEN}✓ GURU AI installed globally (with sudo)${NC}"
        echo -e "${CYAN}   Symlink created: /usr/local/bin/guru → $WRAPPER_SCRIPT${NC}"
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
    echo -e "${YELLOW}[5/7] Skipping global installation...${NC}"
fi

#############################################
# 6. Check Internet Connection
#############################################
echo ""
echo -e "${YELLOW}[6/7] Checking connectivity...${NC}"

if curl -s --head --request GET https://api.virtueai.id > /dev/null 2>&1; then
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
    if ollama list 2>/dev/null | grep -q "llama3.1"; then
        echo -e "${GREEN}✓ Model llama3.1 already installed${NC}"
    else
        echo -e "${YELLOW}⚠️  Model llama3.1 not found${NC}"
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
# 7. Create Run Scripts
#############################################
echo ""
echo -e "${YELLOW}[7/7] Creating launchers...${NC}"

# Create quick run script for selected version
cat > run_guru.sh << EOF
#!/bin/bash
cd "\$(dirname "\$0")"
source venv/bin/activate 2>/dev/null || source venv/Scripts/activate
python $MAIN_FILE
EOF

chmod +x run_guru.sh

# Create Windows batch file
cat > run_guru.bat << EOF
@echo off
cd /d "%~dp0"
call venv\\Scripts\\activate
python $MAIN_FILE
pause
EOF

echo -e "${GREEN}✓ Launcher created (using $MAIN_FILE)${NC}"

# Create version switcher script
cat > switch_version.sh << 'EOF'
#!/bin/bash
echo "GURU AI - Version Switcher"
echo ""
echo "1. IMPROVED version (guru_ai_improved.py)"
echo "2. Original version (guru_ai.py)"
echo ""
read -p "Select version [1/2]: " choice

if [[ "$choice" == "1" ]]; then
    sed -i.bak 's/python guru_ai.py/python guru_ai_improved.py/' run_guru.sh
    sed -i.bak 's/python guru_ai.py/python guru_ai_improved.py/' guru 2>/dev/null || true
    echo "✓ Switched to IMPROVED version"
elif [[ "$choice" == "2" ]]; then
    sed -i.bak 's/python guru_ai_improved.py/python guru_ai.py/' run_guru.sh
    sed -i.bak 's/python guru_ai_improved.py/python guru_ai.py/' guru 2>/dev/null || true
    echo "✓ Switched to Original version"
else
    echo "Invalid choice"
fi
EOF

chmod +x switch_version.sh
echo -e "${GREEN}✓ Version switcher created (./switch_version.sh)${NC}"

#############################################
# Installation Complete!
#############################################
echo ""
echo -e "${GREEN}================================================${NC}"
echo -e "${GREEN}   ✅ Installation Complete!${NC}"
if [ "$USE_IMPROVED" = true ]; then
    echo -e "${MAGENTA}   ✨ IMPROVED VERSION INSTALLED ✨${NC}"
fi
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
    echo -e "${YELLOW}   Or run: python $MAIN_FILE${NC}"
else
    echo -e "${YELLOW}   ./run_guru.sh${NC}"
fi

echo ""

if [ "$USE_IMPROVED" = true ]; then
    echo -e "${CYAN}📊 IMPROVED Version Features:${NC}"
    echo -e "${GREEN}   ✓ 90%+ response consistency${NC}"
    echo -e "${GREEN}   ✓ Automatic quality validation (0-100 score)${NC}"
    echo -e "${GREEN}   ✓ No markdown formatting${NC}"
    echo -e "${GREEN}   ✓ Forbidden phrase blocking${NC}"
    echo -e "${GREEN}   ✓ 50% faster response time${NC}"
    echo -e "${GREEN}   ✓ 66% lower API costs${NC}"
    echo ""
fi

echo -e "${CYAN}📚 Documentation:${NC}"
if [ "$USE_IMPROVED" = true ]; then
    echo -e "${MAGENTA}   IMPROVEMENTS_SUMMARY.md - What's new (START HERE!)${NC}"
    echo -e "${YELLOW}   IMPROVEMENT_REPORT.md - Detailed analysis${NC}"
    echo -e "${YELLOW}   TESTING_GUIDE.md - Comprehensive tests${NC}"
    echo -e "${YELLOW}   MIGRATION_GUIDE.md - Version switching${NC}"
fi
echo -e "${YELLOW}   README.md - Getting started${NC}"
echo -e "${YELLOW}   MODE_KONSELING.md - Counseling mode info${NC}"
echo ""

echo -e "${CYAN}🔧 Utilities:${NC}"
echo -e "${YELLOW}   ./switch_version.sh - Switch between versions${NC}"
echo ""

# Auto-run option
echo ""
read -p "$(echo -e ${CYAN}Do you want to run GURU AI now? [Y/n]: ${NC})" -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]] || [[ -z $REPLY ]]; then
    echo ""
    echo -e "${GREEN}🚀 Starting GURU AI...${NC}"
    if [ "$USE_IMPROVED" = true ]; then
        echo -e "${MAGENTA}   (Using IMPROVED version)${NC}"
    fi
    echo ""

    if [ "$GLOBAL_INSTALL" = true ]; then
        # Use the global guru command
        guru
    else
        # Use python directly
        $PYTHON_CMD $MAIN_FILE
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

    if [ "$USE_IMPROVED" = true ]; then
        echo -e "${MAGENTA}💡 Tip: Read IMPROVEMENTS_SUMMARY.md to learn about new features!${NC}"
        echo ""
    fi
fi
