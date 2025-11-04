#!/bin/bash

# GURU AI - Startup Script
# Script untuk menjalankan aplikasi GURU AI dengan pengecekan otomatis

echo "================================================"
echo "   GURU AI - AI Terminal Guru Indonesia"
echo "   Guided Understanding Resource Unity"
echo "================================================"
echo ""

# Cek apakah Python terinstall
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 tidak ditemukan. Silakan install Python 3.7+ terlebih dahulu."
    exit 1
fi

echo "✓ Python3 ditemukan: $(python3 --version)"

# Cek apakah virtual environment ada
if [ ! -d "venv" ]; then
    echo ""
    echo "📦 Virtual environment tidak ditemukan."
    echo "🔨 Membuat virtual environment..."
    python3 -m venv venv
fi

# Aktivasi virtual environment
echo "🔄 Mengaktifkan virtual environment..."
source venv/bin/activate

# Install dependencies jika belum
if ! python3 -c "import rich" &> /dev/null; then
    echo ""
    echo "📦 Installing dependencies..."
    pip install -q -r requirements.txt
    echo "✓ Dependencies terinstall"
fi

# Cek koneksi internet
echo ""
echo "🔍 Mengecek koneksi internet..."
if ping -c 1 google.com &> /dev/null; then
    echo "✓ Koneksi internet aktif"
else
    echo "⚠️  Tidak ada koneksi internet. Aplikasi memerlukan koneksi untuk mengakses VirtueAI API."
fi

# Jalankan aplikasi
echo ""
echo "================================================"
echo "🚀 Memulai GURU AI..."
echo "================================================"
echo ""

python3 guru_ai.py

# Deactivate virtual environment setelah selesai
deactivate
