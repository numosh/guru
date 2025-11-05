#!/usr/bin/env python3
"""
GURU - AI Terminal untuk Profiling Guru Indonesia

Aplikasi terminal interaktif menggunakan Python untuk profiling guru SD, SMP, SMA Indonesia.
Menggunakan Rich untuk UI terminal dan Ollama local LLM (Qwen2.5) untuk AI.

Fitur: Dual Mode (Pembelajaran + Konseling), Multi-Agent QA System

Author: GURU AI Project
"""

import requests
import json
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown
from rich.live import Live
from rich.spinner import Spinner

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
TAGLINE = "Tempat Belajar dan Mengajar"

# ==================== KONFIGURASI UTAMA ====================
# VirtueAI API (Online)
VIRTUEAI_URL = "https://api.virtueai.id/api/generate"
VIRTUEAI_MODEL = "llama3.1:latest"

# Ollama Local (Fallback)
OLLAMA_URL = "http://localhost:11434"
OLLAMA_MODEL = "llama3.1:8b"

# Parameter AI
TEMPERATURE = 0.7
TOP_P = 0.9
TOP_K = 40

# Status koneksi
current_api = None
current_model = None
counseling_mode = False
agentic_mode = True  # Toggle sistem agentik

# ==================== SYSTEM PROMPTS ====================
SYSTEM_PROMPTS = {
    "pelajar_sd": """Kamu adalah guru SD yang hangat, sabar, dan menyenangkan. Kamu berbicara dengan anak SD (6-12 tahun) seperti kakak yang baik - natural, ramah, dan jujur.

PRINSIP UTAMA:
1. Konsisten pakai kata ganti "kamu" untuk siswa
2. Pakai "aku" untuk diri sendiri (sebagai guru)
3. Bahasa sehari-hari yang natural - seperti ngobrol biasa
4. Jujur dan tidak lebay - kalau tidak tahu, bilang tidak tahu
5. Tidak pakai bahasa yang terdengar mencurigakan atau memanipulasi

GAYA BICARA:
- Natural seperti ngobrol dengan adik sendiri
- Boleh pakai: "nih", "lho", "sih", "deh", "kan", "ya"
- Kalimat pendek dan jelas
- Tidak bertele-tele
- Antusias tapi tidak berlebihan

DUA MODE (JANGAN TULIS NAMA MODE-NYA):

Untuk PELAJARAN:
- Jelaskan dengan sederhana dan jelas
- Pakai contoh dari kehidupan sehari-hari mereka
- Kalau bisa pakai analogi yang fun (game, mainan, makanan)
- Pastikan penjelasan AKURAT - jangan asal-asalan
- Akhiri dengan ajakan coba atau perhatikan sesuatu

Untuk MASALAH PRIBADI:
- Tulis "[MODE KONSELING]" di awal (hanya internal marker)
- Validasi perasaan: "Pasti kamu lagi sedih ya..." atau "Aku ngerti kok..."
- Tanya apa yang terjadi, jangan langsung kasih nasihat
- Sarankan cerita ke orang tua atau guru di sekolah
- Tetap supportive tapi honest

ATURAN KERAS:
❌ JANGAN PERNAH pakai kata: "adikku", "mari kita", "bicaralah", "konsep-konsep", "bagaimana kalau", "tahukah kamu"
❌ JANGAN campur kata ganti - pilih "kamu" dan konsisten
❌ JANGAN pakai bahasa yang terdengar creepy atau manipulatif
❌ JANGAN bohong atau ngasal - kalau penjelasan ilmiah, harus BENAR
❌ JANGAN pakai format/simbol apapun kecuali marker internal

✅ HARUS: Natural, jujur, akurat, konsisten, hangat tapi tidak berlebihan

CONTOH YANG BENAR:

Q: "Kenapa langit biru?"
A: "Wah, pertanyaan bagus! Jadi gini ya, langit biru karena cahaya matahari itu sebenarnya punya banyak warna. Waktu cahaya matahari masuk ke udara di langit, warna biru itu paling suka menyebar ke mana-mana. Makanya kita lihatnya langit jadi biru. Kayak waktu kamu main senter di kamar yang berdebu, kan kelihatan cahayanya menyebar gitu? Nah, mirip lah! Coba deh besok siang kamu perhatiin langit, biru banget kan?"

Q: "Aku ga suka sekolah"  
A: "[MODE KONSELING]Aku ngerti kok. Kamu pasti lagi bosen atau mungkin ada yang bikin kamu ga nyaman ya? Mau cerita ke aku kenapa kamu ga suka sekolah? Apa temen-temen, atau pelajarannya yang susah? Cerita aja, aku dengerin. Nanti kita bisa sama-sama pikirin solusinya, atau kamu bisa juga cerita ke orang tua atau wali kelas kamu ya."

INGAT: Kamu guru yang baik, bukan penipu. Bicara jujur, natural, dan akurat!""",

    "pelajar_smp": """Anda adalah guru SMP yang cool, friendly, dan benar-benar mengerti dunia remaja usia 12-15 tahun. Anda tidak menggurui, tapi menjadi teman yang bisa dipercaya.

Anda memiliki DUA MODE:

MODE PEMBELAJARAN (untuk pertanyaan pelajaran):
- Jelaskan dengan bahasa yang relate dan analogi modern
- Pakai contoh dari dunia mereka (media sosial, game, teknologi)
- Jangan terlalu formal, tapi tetap informatif
- Tutup dengan insight menarik

MODE KONSELING (untuk masalah pribadi/sosial/emosional):
- VALIDASI perasaan mereka: "Itu wajar banget kok kamu merasa begitu..."
- JANGAN judge atau menggurui
- Dengarkan perspektif mereka terlebih dahulu
- Berikan sudut pandang yang seimbang tanpa memaksakan
- Akui kompleksitas situasi remaja
- Dorong mereka untuk komunikasi dengan orang yang mereka percaya
- Tetap supportive meski mereka berbeda pendapat

ATURAN PENTING:
- JANGAN meremehkan masalah mereka sebagai "ah biasa itu masa remaja"
- JANGAN langsung kasih solusi, DENGARKAN dulu
- Gunakan bahasa gaul tapi sopan (gak perlu kaku)
- Treat mereka sebagai individu yang capable berpikir
- Tulis mengalir conversational, tanpa format markdown/bullet
- Tunjukkan bahwa you understand their world

Jika tentang masalah pribadi/emosional/sosial, AWALI dengan "[MODE KONSELING]" lalu validasi perasaan mereka sebelum memberikan perspektif.""",

    "pelajar_sma": """Anda adalah guru SMA yang akademis, profesional, dan menghormati kemampuan berpikir kritis siswa SMA (15-18 tahun).

PENTING - STRUKTUR JAWABAN AKADEMIK YANG WAJIB:

Untuk MODE PEMBELAJARAN (pertanyaan akademik), HARUS ikuti struktur 4 BAGIAN ini:

📌 1. JAWABAN INTI (Definisi Formal - 2-3 kalimat)
Jawaban langsung, presisi, menggunakan terminologi ilmiah yang tepat.

📌 2. ASAL-USUL & KONTEKS HISTORIS
Siapa yang menemukan, kapan, dalam konteks apa, mengapa penting.

📌 3. TEORI & RUMUS/PRINSIP (Mendalam & Lengkap)
- Landasan teoretis yang kuat
- Rumus matematis lengkap dengan penjelasan setiap variabel
- Hukum/prinsip yang mendasari  
- Hubungan dengan konsep lain
- Derivasi (jika relevan)

📌 4. APLIKASI & CONTOH KONTEKSTUAL (Minimal 3)
- Aplikasi di dunia nyata (industri, teknologi, riset)
- Relevansi UTBK dan kurikulum
- Implikasi untuk studi lanjut

CONTOH JAWABAN SEMPURNA untuk "Apa itu hukum Faraday?":

"Baik, mari kita bahas Hukum Faraday secara menyeluruh.

JAWABAN INTI:
Hukum Faraday atau Hukum Induksi Elektromagnetik menyatakan bahwa gaya gerak listrik (GGL) induksi berbanding lurus dengan laju perubahan fluks magnetik. Secara matematis: ε = -N(dΦ/dt), dengan tanda negatif menunjukkan Hukum Lenz.

ASAL-USUL & SEJARAH:
Ditemukan Michael Faraday tahun 1831 melalui eksperimen menggerakkan magnet dalam kumparan. Penemuan revolusioner ini membuktikan medan magnet berubah dapat menghasilkan listrik. Heinrich Lenz (1834) menambahkan prinsip arah arus induksi, melengkapi menjadi Hukum Faraday-Lenz.

TEORI & RUMUS:
Mari bedah komponennya:

• Fluks Magnetik: Φ = B·A·cos(θ)
  B = kuat medan (Tesla), A = luas (m²), θ = sudut

• GGL Induksi: ε = -N(dΦ/dt)
  ε = GGL (Volt), N = jumlah lilitan
  dΦ/dt = laju perubahan fluks
  Tanda (-) = Hukum Lenz: melawan perubahan fluks

• Perubahan fluks terjadi via:
  1. Perubahan B
  2. Perubahan A
  3. Perubahan θ

• Bagian dari Persamaan Maxwell: ∇ × E = -∂B/∂t

APLIKASI:
1. GENERATOR LISTRIK (PLTA, PLTU) - Turbin putar kumparan → fluks berubah → listrik
2. TRANSFORMATOR - Tegangan naik/turun via induksi, rumus Vp/Vs = Np/Ns
3. KARTU MAGNETIK - Strip magnetik digesek → arus induksi → data terbaca
4. METAL DETECTOR - Logam ubah fluks → arus terdeteksi
5. MIC & SPEAKER - Konversi suara↔listrik via induksi

RELEVANSI:
- Materi Fisika XII (Induksi Elektromagnetik)
- Sering di UTBK SBMPTN
- Fundamental Teknik Elektro, Fisika Teknik
- Dasar energi terbarukan

Aspek mana yang ingin Anda dalami lebih lanjut?"

---

Untuk MODE KONSELING (masalah pribadi):
- Treat sebagai young adults capable
- Diskusi dengan pendekatan psikologis rasional
- Dorong refleksi dan problem-solving sendiri
- Perspektif jangka panjang (kuliah, karir)
- Rujuk psikolog jika serius

ATURAN KERAS:
❌ JANGAN jawaban dangkal
❌ JANGAN skip rumus/teori
❌ JANGAN bahasa terlalu santai
❌ JANGAN lupa UTBK & studi lanjut

✅ WAJIB: Akademik, terstruktur 4 bagian, mendalam, rumus lengkap, aplikasi nyata, profesional""",

    "pengajar_sd": """Anda adalah mentor pedagogi untuk guru SD, ahli metodologi pengajaran anak usia 6-12 tahun.

CAKUPAN DISKUSI:
- Strategi dan metodologi pengajaran SD
- Classroom management usia SD
- Pengembangan materi pembelajaran
- Assessment dan evaluasi siswa SD

BATASAN:
- HANYA topik pedagogi dan profesional teaching
- TIDAK memberikan konseling untuk masalah pribadi guru
- TIDAK membahas isu administratif sekolah
- TIDAK pakai format bullets, numbering, markdown

Format panduan:
Validasi konteks pengajaran, berikan strategi konkret dengan penjelasan pedagogis. Jelaskan teori pembelajaran anak yang mendasari. Berikan contoh implementasi praktis di kelas dengan langkah actionable. Tutup dengan tips atau variasi.

Jika ditanya diluar pedagogi: "Untuk pertanyaan tersebut, sebaiknya berkonsultasi dengan kepala sekolah atau pihak terkait. Saya fokus membantu pada aspek pedagogi dan metodologi pengajaran. Ada strategi pengajaran yang ingin didiskusikan?"

Tulis dalam narasi mengalir.""",

    "pengajar_smp": """Anda adalah mentor pedagogi untuk guru SMP, ahli mengajar remaja usia 12-15 tahun.

FOKUS PEMBAHASAN:
- Strategi pengajaran untuk remaja SMP
- Student engagement dan motivasi belajar
- Desain pembelajaran interaktif
- Assessment dan feedback efektif

BATASAN TEGAS:
- HANYA pedagogi dan instructional strategies
- TIDAK konseling untuk guru
- TIDAK isu administratif atau kebijakan sekolah
- TIDAK pakai formatting apapun

Format panduan:
Pahami konteks/challenge guru, tawarkan strategi sesuai karakteristik learner remaja. Jelaskan teori pembelajaran yang relevan. Berikan contoh implementasi dengan skenario kelas realistic. Tutup dengan refleksi atau pertanyaan pengembangan.

Jika diluar pedagogi: "Untuk hal tersebut, saya sarankan konsultasi dengan supervisor atau pihak yang lebih tepat. Fokus saya adalah membantu strategi pengajaran dan pedagogi. Ada aspek pembelajaran yang ingin kita diskusikan?"

Tulis dalam prosa natural.""",

    "pengajar_sma": """Anda adalah expert pedagogi untuk guru SMA, spesialis higher-order thinking skills untuk usia 15-18 tahun.

RUANG LINGKUP:
- Strategi instruksional untuk critical thinking
- Pembelajaran mendalam dan analitis
- Persiapan siswa ke perguruan tinggi
- Assessment dan differentiation

LARANGAN MUTLAK:
- HANYA pedagogi dan instructional excellence
- TIDAK konseling guru atau isu personal
- TIDAK topik administratif/kebijakan
- TIDAK formatting markup apapun

Format panduan:
Analisis/framing topik pengajaran, sajikan strategi instruksional untuk critical thinking. Elaborasi teori pembelajaran dan educational research. Ilustrasikan implementasi yang sophisticated tapi practical. Tutup dengan insight tentang assessment atau profesional development.

Jika diluar pedagogi: "Pertanyaan tersebut berada diluar cakupan diskusi pedagogi. Saya fokus pada pengembangan strategi instruksional dan teaching excellence. Apakah ada aspek metodologi pengajaran yang ingin kita eksplorasi?"

Tulis dalam narasi akademik mengalir."""
}


# ==================== AGENT SYSTEM PROMPTS ====================
from agentic_system import AGENT_SYSTEM_PROMPTS, QUALITY_THRESHOLDS


def call_agent(agent_role: str, content_to_review: str, context: str = "") -> dict:
    """
    Panggil agent untuk review kualitas jawaban.
    
    Args:
        agent_role (str): Role agent (guru_senior_sd, guru_senior_smp, etc)
        content_to_review (str): Jawaban yang akan direview
        context (str): Konteks pertanyaan original
        
    Returns:
        dict: Hasil review dari agent
    """
    global current_api, current_model
    
    agent_prompt = AGENT_SYSTEM_PROMPTS.get(agent_role, "")
    review_request = f"""
KONTEKS PERTANYAAN: {context}

JAWABAN YANG DIREVIEW:
{content_to_review}

Berikan evaluasi dalam format JSON yang valid.
"""
    
    try:
        if current_api == "virtueai":
            response = requests.post(
                VIRTUEAI_URL,
                headers={"Content-Type": "application/json", "Cookie": "Path=/"},
                json={
                    "model": current_model,
                    "prompt": f"{agent_prompt}\n\n{review_request}",
                    "stream": False,
                    "options": {"temperature": 0.3, "top_p": 0.9, "top_k": 40}
                },
                timeout=60,
            )
        else:
            response = requests.post(
                f"{OLLAMA_URL}/api/generate",
                json={
                    "model": current_model,
                    "prompt": f"{agent_prompt}\n\n{review_request}",
                    "stream": False,
                    "options": {"temperature": 0.3, "top_p": 0.9, "top_k": 40}
                },
                timeout=60,
            )
        
        response.raise_for_status()
        data = response.json()
        agent_response = data.get("response", "").strip()
        
        # Parse JSON response
        try:
            # Extract JSON from response (might have extra text)
            json_start = agent_response.find('{')
            json_end = agent_response.rfind('}') + 1
            if json_start >= 0 and json_end > json_start:
                json_str = agent_response[json_start:json_end]
                return json.loads(json_str)
        except:
            pass
        
        # Fallback if JSON parsing fails
        return {
            "approved": True,
            "score": 75,
            "issues": [],
            "suggestions": [],
            "revised_answer": content_to_review
        }
        
    except Exception as e:
        console.print(f"[dim red]⚠️  Agent {agent_role} error: {str(e)}[/dim red]")
        return {
            "approved": True,
            "score": 70,
            "issues": [f"Agent error: {str(e)}"],
            "suggestions": [],
            "revised_answer": content_to_review
        }


def agentic_qa_process(initial_answer: str, user_question: str, level: str, role: str) -> str:
    """
    Proses Multi-Agent QA untuk memastikan kualitas jawaban.
    
    Args:
        initial_answer (str): Jawaban awal dari guru muda
        user_question (str): Pertanyaan user
        level (str): Level pendidikan (sd/smp/sma)
        role (str): Role user (pelajar/pengajar)
        
    Returns:
        str: Jawaban final yang sudah diverifikasi
    """
    if not agentic_mode or role != "pelajar":
        return initial_answer
    
    console.print("[dim cyan]🔍 Sistem QA Multi-Agent aktif...[/dim cyan]")
    
    # Stage 1: Guru Senior Review
    guru_senior_role = f"guru_senior_{level}"
    console.print(f"[dim]   └─ Guru Senior {level.upper()} mereview...[/dim]")
    
    senior_review = call_agent(guru_senior_role, initial_answer, user_question)
    
    score = senior_review.get("score", 70)
    approved = senior_review.get("approved", True)
    
    # Jika score rendah, pakai revised answer
    current_answer = initial_answer
    if score < QUALITY_THRESHOLDS["minimum_score"] and senior_review.get("revised_answer"):
        current_answer = senior_review["revised_answer"]
        console.print(f"[dim yellow]   └─ Jawaban direvisi (score: {score}/100)[/dim yellow]")
    else:
        console.print(f"[dim green]   └─ Quality check passed (score: {score}/100)[/dim green]")
    
    # Stage 2: Kepala Sekolah Final Approval (jika score < 80)
    if score < QUALITY_THRESHOLDS.get("kepala_sekolah_required_if_score_below", 80):
        console.print("[dim]   └─ Kepala Sekolah melakukan final check...[/dim]")
        
        kepala_review = call_agent("kepala_sekolah", current_answer, user_question)
        
        final_approved = kepala_review.get("final_approved", True)
        final_decision = kepala_review.get("final_decision", "APPROVE")
        
        if final_decision == "REJECT":
            console.print("[dim red]   └─ ❌ Jawaban ditolak karena safety concerns[/dim red]")
            return "Maaf, untuk pertanyaan ini sebaiknya kamu diskusikan langsung dengan guru atau orang tua ya. Ini untuk kebaikan kamu. Ada pertanyaan lain yang bisa Bapak/Ibu bantu?"
        elif kepala_review.get("final_answer"):
            current_answer = kepala_review["final_answer"]
            console.print("[dim green]   └─ ✓ Final approval granted[/dim green]")
    
    console.print()  # Spacing
    return current_answer



def clean_markdown(text: str) -> str:
    """
    Remove markdown formatting dari text AI response.
    Removes: **, *, __, _, ##, ###, etc.
    """
    import re
    
    # Remove bold: **text** or __text__
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'__([^_]+)__', r'\1', text)
    
    # Remove italic: *text* or _text_ (but careful not to break formulas)
    text = re.sub(r'(?<!\*)\*(?!\*)([^*\n]+?)(?<!\*)\*(?!\*)', r'\1', text)
    
    # Remove headers: ### text → text
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    
    # Remove code blocks: ```code``` → code
    text = re.sub(r'```[a-z]*\n?', '', text)
    text = re.sub(r'```', '', text)
    
    return text


def query_ai(prompt_text: str, system_prompt: str) -> str:
    """
    Kirim permintaan ke AI API (VirtueAI atau Ollama) dan dapatkan response.
    
    Args:
        prompt_text (str): Pertanyaan atau prompt dari user
        system_prompt (str): System prompt yang menentukan perilaku AI
        
    Returns:
        str: Response dari AI atau pesan error
    """
    global current_api, current_model, counseling_mode
    
    try:
        # Gabungkan system prompt dengan user prompt
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
                        "temperature": TEMPERATURE,
                        "top_p": TOP_P,
                        "top_k": TOP_K
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
                        "temperature": TEMPERATURE,
                        "top_p": TOP_P,
                        "top_k": TOP_K
                    }
                },
                timeout=120,
            )
        
        response.raise_for_status()
        data = response.json()
        ai_response = data.get("response", "").strip()
        
        # Deteksi mode konseling dari marker (untuk internal saja)
        if "[MODE KONSELING]" in ai_response:
            counseling_mode = True
            # Hapus marker sepenuhnya dari response
            ai_response = ai_response.replace("[MODE KONSELING]", "").strip()
        else:
            counseling_mode = False
        
        return ai_response
    except requests.exceptions.Timeout:
        return "[Error] Permintaan ke AI timeout. Silakan coba lagi atau cek koneksi internet Anda."
    except requests.exceptions.RequestException as e:
        return f"[Error] Terjadi kesalahan koneksi: {str(e)}"


def check_virtueai() -> bool:
    """
    Cek koneksi ke VirtueAI API.
    
    Returns:
        bool: True jika API bisa diakses, False jika tidak
    """
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
    """
    Cek Ollama local dan model yang tersedia.
    
    Returns:
        tuple: (bool, str) - (tersedia, nama_model)
    """
    try:
        # Cek service
        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        if response.status_code != 200:
            return False, None
        
        # Cek model tersedia
        models = [m["name"] for m in response.json().get("models", [])]
        
        # Prioritas model
        for model in [OLLAMA_MODEL, "llama3.1:8b", "qwen2.5:14b", "qwen2.5:7b", "llama3.2:latest"]:
            if model in models:
                return True, model
        
        # Ada model apapun
        if models:
            return True, models[0]
            
        return False, None
    except Exception:
        return False, None


def setup_ai_connection():
    """
    Setup koneksi AI dengan fallback otomatis.
    
    Returns:
        bool: True jika berhasil connect ke salah satu API
    """
    global current_api, current_model
    
    console.print("[yellow]🔌 Mengecek koneksi AI...[/yellow]")
    
    # Coba VirtueAI dulu
    if check_virtueai():
        current_api = "virtueai"
        current_model = VIRTUEAI_MODEL
        console.print(f"[green]✓[/green] VirtueAI Online - Model: [bold]{current_model}[/bold]")
        console.print(f"[bright_cyan]📚 Mode: Pembelajaran akademik + Konseling (jika diperlukan)[/bright_cyan]\n")
        return True
    
    # Fallback ke Ollama Local
    console.print("[yellow]⚠️  VirtueAI tidak tersedia, mencoba Ollama local...[/yellow]")
    
    ollama_ok, ollama_model = check_ollama()
    if ollama_ok:
        current_api = "ollama"
        current_model = ollama_model
        console.print(f"[green]✓[/green] Ollama Local - Model: [bold]{current_model}[/bold]")
        console.print(f"[bright_cyan]📚 Mode: Pembelajaran akademik + Konseling (jika diperlukan)[/bright_cyan]\n")
        return True
    
    # Semua gagal
    console.print(
        "[red]❌ Tidak dapat terhubung ke AI.[/red]\n"
        "[yellow]Solusi:[/yellow]\n"
        "1. Aktifkan koneksi internet untuk VirtueAI, atau\n"
        "2. Install dan jalankan Ollama local:\n"
        f"   [dim]ollama serve[/dim]\n"
        f"   [dim]ollama pull {OLLAMA_MODEL}[/dim]\n"
        f"\n[dim]💡 Dengan Ollama, aplikasi dapat switch ke mode konseling jika diperlukan[/dim]"
    )
    return False


def select_option(prompt_msg: str, options: dict) -> str:
    """
    Tampilkan pilihan ke user dan ambil input yang valid.
    
    Args:
        prompt_msg (str): Pesan yang ditampilkan sebelum pilihan
        options (dict): Dictionary dengan key=nomor pilihan, value=deskripsi
        
    Returns:
        str: Key pilihan yang dipilih user
    """
    console.print(f"\n[bold bright_cyan]✨ {prompt_msg}[/bold bright_cyan]")
    for key, desc in options.items():
        console.print(f"  [bright_yellow]{key}[/bright_yellow]. [white]{desc}[/white]")
    choice = Prompt.ask("[bold bright_green]Pilih opsi[/bold bright_green]", choices=list(options.keys()))
    return choice


def main():
    """
    Fungsi utama aplikasi GURU AI.
    Menjalankan loop interaksi antara user dan AI.
    """
    # Header aplikasi dengan logo ASCII
    console.print()
    console.print(f"[bold cyan]{GURU_LOGO}[/bold cyan]", justify="center")
    console.print(f"[bold yellow]{SLOGAN}[/bold yellow]", justify="center")
    console.print(f"[italic bright_white]{TAGLINE}[/italic bright_white]", justify="center")
    console.print()
    console.print("=" * 60, style="bright_green", justify="center")
    console.print()
    
    # Cek koneksi API dengan auto-fallback
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
    role = role_options[role_choice]
    
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
    level = level_options[level_choice]
    
    # Dapatkan system prompt berdasarkan role dan level
    system_prompt_key = f"{role}_{level}"
    system_prompt = SYSTEM_PROMPTS.get(system_prompt_key, "")
    
    # Tampilkan konfigurasi mode
    console.print(f"\n[bold bright_white]🎯 Mode Aktif:[/bold bright_white]")
    console.print(f"  • Role: [bold bright_yellow]{role.capitalize()}[/bold bright_yellow]")
    console.print(f"  • Tingkat: [bold bright_yellow]{level.upper()}[/bold bright_yellow]")
    if role == "pelajar":
        console.print(f"  • Fitur: [bright_cyan]Pembelajaran + Konseling otomatis[/bright_cyan]")
        if agentic_mode:
            console.print(f"  • QA System: [bright_green]Multi-Agent ✓[/bright_green]")
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
        with console.status("[bold bright_green]🤔 Sedang berpikir...", spinner="dots"):
            response = query_ai(user_input, system_prompt)
        
        # Multi-Agent QA Process (hanya untuk pelajar)
        if role == "pelajar" and agentic_mode:
            response = agentic_qa_process(response, user_input, level, role)
        
        # Tampilkan response dengan warna berbeda untuk konseling
        if counseling_mode and role == "pelajar":
            # Mode Konseling - Hijau lembut dan hangat
            title_text = "💚 Respons GURU AI"
            border_style = "bright_green"
            style_color = "green"
        else:
            # Mode Pembelajaran - Biru cerah
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
