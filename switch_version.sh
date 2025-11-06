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
