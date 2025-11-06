#!/usr/bin/env python3
"""
GURU AI - IMPROVED VERSION
Versi perbaikan dengan validasi response dan prompt yang lebih terstruktur

Perbaikan utama:
1. Response validator untuk konsistensi
2. Prompt dengan template wajib
3. AI parameters yang dioptimalkan
4. Better error handling

Author: GURU AI Enhancement Project
"""

import requests
import json
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown

# Import modules perbaikan
from response_validator import ResponseValidator, validate_and_improve
from improved_prompts import IMPROVED_SYSTEM_PROMPTS, OPTIMIZED_AI_PARAMS
from historical_facts_db import retrieve_historical_facts, format_facts_for_prompt

console = Console()

# ==================== ASCII LOGO ====================
GURU_LOGO = """
 ██████╗ ██╗   ██╗██████╗ ██╗   ██╗
██╔════╝ ██║   ██║██╔══██╗██║   ██║
██║  ███╗██║   ██║██████╔╝██║   ██║
██║   ██║██║   ██║██╔══██╗██║   ██║
╚██████╔╝╚██████╔╝██║  ██║╚██████╔╝
 ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝
    @anugrahprahasta 2025
"""

SLOGAN = "Guided Understanding Resource Unity"
TAGLINE = "Tempat Belajar dan Mengajar - IMPROVED VERSION"

# ==================== KONFIGURASI UTAMA ====================
# VirtueAI API (Online)
VIRTUEAI_URL = "https://api.virtueai.id/api/generate"
VIRTUEAI_MODEL = "llama3.1:latest"

# Ollama Local (Fallback)
OLLAMA_URL = "http://localhost:11434"
OLLAMA_MODEL = "llama3.1:8b"

# Status koneksi
current_api = None
current_model = None
counseling_mode = False
current_level = None
current_role = None


def query_ai_improved(prompt_text: str, system_prompt: str, level: str, role: str) -> tuple:
    """
    Kirim permintaan ke AI dengan validasi otomatis dan RAG untuk fakta sejarah

    Args:
        prompt_text: Pertanyaan user
        system_prompt: System prompt
        level: Level pendidikan
        role: Role user

    Returns:
        (cleaned_response, validation_report, is_counseling)
    """
    global current_api, current_model, counseling_mode

    try:
        # Dapatkan AI parameters yang optimal
        prompt_key = f"{role}_{level}"
        ai_params = OPTIMIZED_AI_PARAMS.get(prompt_key, {
            "temperature": 0.5,
            "top_p": 0.9,
            "top_k": 40
        })

        # === RAG INTEGRATION: Retrieve historical facts if applicable ===
        historical_facts = retrieve_historical_facts(prompt_text)

        if historical_facts:
            # Inject facts into prompt
            facts_injection = format_facts_for_prompt(historical_facts)
            console.print("[dim cyan]📚 Menggunakan database fakta sejarah untuk akurasi...[/dim cyan]")

            # Enhanced prompt with facts
            full_prompt = f"""{system_prompt}

{facts_injection}

Pertanyaan: {prompt_text}

Jawaban:"""
        else:
            # Regular prompt without facts
            full_prompt = f"{system_prompt}\n\nPertanyaan: {prompt_text}\n\nJawaban:"

        if current_api == "virtueai":
            # VirtueAI API
            response = requests.post(
                VIRTUEAI_URL,
                headers={
                    "Content-Type": "application/json",
                    "Cookie": "Path=/"
                },
                json={
                    "model": current_model,
                    "prompt": full_prompt,
                    "stream": False,
                    "options": {
                        "temperature": ai_params.get("temperature", 0.5),
                        "top_p": ai_params.get("top_p", 0.9),
                        "top_k": ai_params.get("top_k", 40),
                        "num_predict": ai_params.get("max_tokens", 500)
                    }
                },
                timeout=120,
            )
        else:
            # Ollama Local API
            response = requests.post(
                f"{OLLAMA_URL}/api/generate",
                json={
                    "model": current_model,
                    "prompt": full_prompt,
                    "stream": False,
                    "options": {
                        "temperature": ai_params.get("temperature", 0.5),
                        "top_p": ai_params.get("top_p", 0.9),
                        "top_k": ai_params.get("top_k", 40),
                        "num_predict": ai_params.get("max_tokens", 500)
                    }
                },
                timeout=120,
            )

        response.raise_for_status()
        data = response.json()
        ai_response = data.get("response", "").strip()

        # Deteksi mode konseling
        is_counseling = "[MODE KONSELING]" in ai_response

        # VALIDASI OTOMATIS dengan Response Validator
        cleaned_response, validation_report = validate_and_improve(
            ai_response,
            level,
            role,
            is_counseling
        )

        # Update counseling mode global
        counseling_mode = is_counseling

        # Log jika ada issues
        if validation_report["issues"]:
            console.print(f"[dim yellow]⚠️  Quality issues detected ({validation_report['score']}/100):[/dim yellow]")
            for issue in validation_report["issues"][:3]:  # Show max 3 issues
                console.print(f"[dim yellow]   • {issue}[/dim yellow]")

        return cleaned_response, validation_report, is_counseling

    except requests.exceptions.Timeout:
        return "[Error] Permintaan ke AI timeout. Silakan coba lagi atau cek koneksi internet Anda.", {"score": 0, "issues": ["Timeout"]}, False
    except requests.exceptions.RequestException as e:
        return f"[Error] Terjadi kesalahan koneksi: {str(e)}", {"score": 0, "issues": [str(e)]}, False


def check_virtueai() -> bool:
    """Cek koneksi ke VirtueAI API"""
    try:
        response = requests.post(
            VIRTUEAI_URL,
            headers={
                "Content-Type": "application/json",
                "Cookie": "Path=/"
            },
            json={
                "model": VIRTUEAI_MODEL,
                "prompt": "test",
                "stream": False,
                "options": {"temperature": 0.7}
            },
            timeout=10,
        )
        return response.status_code == 200
    except Exception:
        return False


def check_ollama() -> tuple:
    """Cek Ollama local dan model yang tersedia"""
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        if response.status_code != 200:
            return False, None

        models = [m["name"] for m in response.json().get("models", [])]

        for model in [OLLAMA_MODEL, "llama3.1:8b", "qwen2.5:14b", "qwen2.5:7b", "llama3.2:latest"]:
            if model in models:
                return True, model

        if models:
            return True, models[0]

        return False, None
    except Exception:
        return False, None


def setup_ai_connection():
    """Setup koneksi AI dengan fallback otomatis"""
    global current_api, current_model

    console.print("[yellow]🔌 Mengecek koneksi AI...[/yellow]")

    # Coba VirtueAI dulu
    if check_virtueai():
        current_api = "virtueai"
        current_model = VIRTUEAI_MODEL
        console.print(f"[green]✓[/green] VirtueAI Online - Model: [bold]{current_model}[/bold]")
        console.print(f"[bright_cyan]📚 IMPROVED VERSION - Enhanced quality & consistency[/bright_cyan]\n")
        return True

    # Fallback ke Ollama Local
    console.print("[yellow]⚠️  VirtueAI tidak tersedia, mencoba Ollama local...[/yellow]")

    ollama_ok, ollama_model = check_ollama()
    if ollama_ok:
        current_api = "ollama"
        current_model = ollama_model
        console.print(f"[green]✓[/green] Ollama Local - Model: [bold]{current_model}[/bold]")
        console.print(f"[bright_cyan]📚 IMPROVED VERSION - Enhanced quality & consistency[/bright_cyan]\n")
        return True

    # Semua gagal
    console.print(
        "[red]❌ Tidak dapat terhubung ke AI.[/red]\n"
        "[yellow]Solusi:[/yellow]\n"
        "1. Aktifkan koneksi internet untuk VirtueAI, atau\n"
        "2. Install dan jalankan Ollama local:\n"
        f"   [dim]ollama serve[/dim]\n"
        f"   [dim]ollama pull {OLLAMA_MODEL}[/dim]\n"
    )
    return False


def select_option(prompt_msg: str, options: dict) -> str:
    """Tampilkan pilihan ke user dan ambil input yang valid"""
    console.print(f"\n[bold bright_cyan]✨ {prompt_msg}[/bold bright_cyan]")
    for key, desc in options.items():
        console.print(f"  [bright_yellow]{key}[/bright_yellow]. [white]{desc}[/white]")
    choice = Prompt.ask("[bold bright_green]Pilih opsi[/bold bright_green]", choices=list(options.keys()))
    return choice


def main():
    """Fungsi utama aplikasi GURU AI IMPROVED"""
    global current_level, current_role

    # Header aplikasi
    console.print()
    console.print(f"[bold cyan]{GURU_LOGO}[/bold cyan]", justify="center")
    console.print(f"[bold yellow]{SLOGAN}[/bold yellow]", justify="center")
    console.print(f"[italic bright_white]{TAGLINE}[/italic bright_white]", justify="center")
    console.print()
    console.print("=" * 60, style="bright_green", justify="center")
    console.print()

    # Cek koneksi API
    if not setup_ai_connection():
        return

    # Pilih role user
    role_options = {"1": "pelajar", "2": "pengajar"}
    role_choice = select_option(
        "Bagaimana Anda menggunakan aplikasi ini?",
        {
            "1": "Pelajar (siswa/siswi yang belajar)",
            "2": "Pengajar (guru/mentor)"
        }
    )
    current_role = role_options[role_choice]

    # Pilih level pendidikan
    level_options = {"1": "sd", "2": "smp", "3": "sma"}
    level_choice = select_option(
        "Pilih tingkat pendidikan:",
        {
            "1": "SD (Sekolah Dasar)",
            "2": "SMP (Sekolah Menengah Pertama)",
            "3": "SMA (Sekolah Menengah Atas)"
        }
    )
    current_level = level_options[level_choice]

    # Dapatkan improved system prompt
    system_prompt_key = f"{current_role}_{current_level}"
    system_prompt = IMPROVED_SYSTEM_PROMPTS.get(system_prompt_key, "")

    # Tampilkan konfigurasi mode
    console.print(f"\n[bold bright_white]🎯 Mode Aktif:[/bold bright_white]")
    console.print(f"  • Role: [bold bright_yellow]{current_role.capitalize()}[/bold bright_yellow]")
    console.print(f"  • Tingkat: [bold bright_yellow]{current_level.upper()}[/bold bright_yellow]")
    console.print(f"  • Version: [bold bright_green]IMPROVED with Auto-Validation ✓[/bold bright_green]")
    if current_role == "pelajar":
        console.print(f"  • Fitur: [bright_cyan]Pembelajaran + Konseling otomatis[/bright_cyan]")
        console.print(f"  • Quality: [bright_green]Response validator aktif ✓[/bright_green]")
    console.print(f"\n[dim italic]💬 Ketik 'quit' atau 'exit' untuk keluar.[/dim italic]\n")

    # Loop interaksi utama
    while True:
        # Ambil input dari user
        user_input = Prompt.ask("[bold bright_cyan]💭 Anda[/bold bright_cyan]").strip()

        # Cek perintah keluar
        if user_input.lower() in ["quit", "exit", "keluar"]:
            console.print(Panel(
                "Terima kasih sudah menggunakan GURU AI. Sampai jumpa! 👋",
                style="bold green"
            ))
            break

        # Skip jika input kosong
        if not user_input:
            continue

        # Tampilkan loading indicator
        with console.status("[bold bright_green]🤔 Sedang berpikir dan memvalidasi...", spinner="dots"):
            response, validation_report, is_counseling = query_ai_improved(
                user_input,
                system_prompt,
                current_level,
                current_role
            )

        # Tampilkan quality score jika ada issues
        if validation_report["score"] < 90 and validation_report["score"] > 0:
            console.print(f"[dim]Quality Score: {validation_report['score']}/100[/dim]")

        # Tampilkan response dengan warna berbeda untuk konseling
        if is_counseling and current_role == "pelajar":
            title_text = "💚 Respons GURU AI - Mode Konseling"
            border_style = "bright_green"
            style_color = "green"
        else:
            title_text = "🎓 Respons GURU AI"
            border_style = "bright_cyan"
            style_color = "cyan"

        console.print(Panel(
            response,
            title=f"[bold]{title_text}[/bold]",
            title_align="left",
            style=style_color,
            border_style=border_style,
            padding=(1, 2)
        ))
        console.print()


if __name__ == "__main__":
    main()
