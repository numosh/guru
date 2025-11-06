"""
Response Validator - GURU AI
Validasi dan perbaiki response AI untuk konsistensi kualitas

Author: GURU AI Enhancement Project
"""

import re
from typing import Dict, List, Tuple


class ResponseValidator:
    """Validator untuk memastikan kualitas dan konsistensi response AI"""

    # Daftar kata/frasa yang DILARANG berdasarkan level
    FORBIDDEN_PHRASES = {
        "sd": [
            "adikku", "anak kecil", "mari kita", "bicaralah",
            "konsep-konsep", "bagaimana kalau", "tahukah kamu",
            "mari belajar", "ayo kita", "sahabat kecilku",
            "bocah", "dik", "nak", "yuk kita"
        ],
        "smp": [
            "anak-anak", "adik-adik", "bocah",
            "kalian masih kecil", "nanti kalau sudah besar",
            "ah biasa itu masa remaja", "lebay deh"
        ],
        "sma": [
            "anak muda", "remaja labil", "masih hijau",
            "kalian belum ngerti", "nanti kalau sudah dewasa"
        ]
    }

    # Format markdown yang harus dihindari
    MARKDOWN_PATTERNS = [
        r'\*\*[^*]+\*\*',  # Bold
        r'__[^_]+__',      # Bold underscore
        r'\*[^*\n]+\*',    # Italic
        r'_[^_\n]+_',      # Italic underscore
        r'^#{1,6}\s',      # Headers
        r'```[\s\S]*?```', # Code blocks
        r'`[^`]+`',        # Inline code
        r'^\s*[-*+]\s',    # Bullet points
        r'^\s*\d+\.\s',    # Numbered lists
        r'\[([^\]]+)\]\([^\)]+\)',  # Links
    ]

    # Kata ganti yang harus konsisten
    PRONOUN_CONSISTENCY = {
        "sd": {
            "for_student": "kamu",
            "for_teacher": "aku",
            "forbidden": ["anda", "adik", "dik", "kalian"]
        },
        "smp": {
            "for_student": "kamu",
            "for_teacher": "aku",
            "forbidden": ["anda", "adik", "kalian"]
        },
        "sma": {
            "for_student": "anda/kamu",
            "for_teacher": "saya",
            "forbidden": ["adik", "dik"]
        }
    }

    def __init__(self, level: str, role: str):
        """
        Inisialisasi validator

        Args:
            level: Level pendidikan (sd/smp/sma)
            role: Role user (pelajar/pengajar)
        """
        self.level = level.lower()
        self.role = role.lower()

    def validate_response(self, response: str, is_counseling: bool = False) -> Dict:
        """
        Validasi response AI secara komprehensif

        Args:
            response: Response dari AI
            is_counseling: Apakah ini mode konseling

        Returns:
            Dict dengan score, issues, dan cleaned_response
        """
        issues = []
        score = 100

        # 1. Check forbidden phrases
        forbidden_issues = self._check_forbidden_phrases(response)
        if forbidden_issues:
            issues.extend(forbidden_issues)
            score -= len(forbidden_issues) * 10

        # 2. Check markdown formatting
        markdown_issues = self._check_markdown(response)
        if markdown_issues:
            issues.extend(markdown_issues)
            score -= len(markdown_issues) * 5

        # 3. Check pronoun consistency
        pronoun_issues = self._check_pronouns(response)
        if pronoun_issues:
            issues.extend(pronoun_issues)
            score -= len(pronoun_issues) * 8

        # 4. Check response length
        length_issue = self._check_length(response)
        if length_issue:
            issues.append(length_issue)
            score -= 5

        # 5. Check empathy (for counseling mode)
        if is_counseling and self.role == "pelajar":
            empathy_issues = self._check_empathy(response)
            if empathy_issues:
                issues.extend(empathy_issues)
                score -= len(empathy_issues) * 15

        # 6. Check structure (especially for SMA)
        if self.level == "sma" and self.role == "pelajar" and not is_counseling:
            structure_issues = self._check_sma_structure(response)
            if structure_issues:
                issues.extend(structure_issues)
                score -= 10

        # Clean response
        cleaned_response = self._clean_response(response)

        return {
            "score": max(0, score),  # Tidak boleh negatif
            "issues": issues,
            "cleaned_response": cleaned_response,
            "is_valid": score >= 70
        }

    def _check_forbidden_phrases(self, text: str) -> List[str]:
        """Check kata/frasa terlarang"""
        issues = []
        forbidden = self.FORBIDDEN_PHRASES.get(self.level, [])

        text_lower = text.lower()
        for phrase in forbidden:
            if phrase in text_lower:
                issues.append(f"Menggunakan frasa terlarang: '{phrase}'")

        return issues

    def _check_markdown(self, text: str) -> List[str]:
        """Check format markdown yang tidak diinginkan"""
        issues = []

        for pattern in self.MARKDOWN_PATTERNS:
            matches = re.findall(pattern, text, re.MULTILINE)
            if matches:
                issues.append(f"Menggunakan markdown formatting: {pattern}")

        return issues

    def _check_pronouns(self, text: str) -> List[str]:
        """Check konsistensi kata ganti"""
        issues = []
        rules = self.PRONOUN_CONSISTENCY.get(self.level, {})
        forbidden = rules.get("forbidden", [])

        text_lower = text.lower()
        for pronoun in forbidden:
            # Cek dengan word boundary
            pattern = r'\b' + re.escape(pronoun) + r'\b'
            if re.search(pattern, text_lower):
                issues.append(f"Menggunakan kata ganti terlarang: '{pronoun}'")

        return issues

    def _check_length(self, text: str) -> str:
        """Check panjang response"""
        word_count = len(text.split())

        if self.level == "sd":
            if word_count < 30:
                return "Response terlalu pendek untuk SD (minimal 30 kata)"
            elif word_count > 350:
                return "Response terlalu panjang untuk SD (maksimal 350 kata)"
        elif self.level == "smp":
            if word_count < 40:
                return "Response terlalu pendek untuk SMP (minimal 40 kata)"
            elif word_count > 500:
                return "Response terlalu panjang untuk SMP (maksimal 500 kata)"
        elif self.level == "sma":
            if word_count < 50:
                return "Response terlalu pendek untuk SMA (minimal 50 kata)"
            elif word_count > 1000:
                return "Response terlalu panjang untuk SMA (maksimal 1000 kata)"

        return ""

    def _check_empathy(self, text: str) -> List[str]:
        """Check empati dalam mode konseling"""
        issues = []
        text_lower = text.lower()

        # Keywords empati yang HARUS ada
        empathy_keywords = [
            "ngerti", "mengerti", "wajar", "valid", "pasti",
            "berat", "sulit", "merasa", "perasaan"
        ]

        # Check apakah ada minimal 2 empathy keywords
        found_keywords = sum(1 for kw in empathy_keywords if kw in text_lower)

        if found_keywords < 2:
            issues.append("Kurang empati - tidak ada validasi perasaan yang cukup")

        # Check frasa yang menghakimi (TIDAK BOLEH ada)
        judgmental_phrases = [
            "seharusnya", "harusnya kamu", "salah kamu",
            "kenapa sih", "cuma gitu aja", "lebay"
        ]

        for phrase in judgmental_phrases:
            if phrase in text_lower:
                issues.append(f"Terdengar menghakimi: '{phrase}'")

        return issues

    def _check_sma_structure(self, text: str) -> List[str]:
        """Check struktur 4 bagian untuk SMA akademik"""
        issues = []

        text_lower = text.lower()

        # Deteksi apakah ini pertanyaan sains atau sejarah/sosial
        is_science = any(kw in text_lower for kw in [
            "rumus", "persamaan", "matematis", "fisika", "kimia",
            "biologi", "energi", "gaya", "molekul", "atom"
        ])

        is_history = any(kw in text_lower for kw in [
            "pahlawan", "peristiwa", "perang", "kemerdekaan", "perjuangan",
            "sejarah", "tahun", "abad", "masa", "periode", "revolusi", "kolonial"
        ])

        # Check definition (sama untuk semua topik)
        has_definition = any(kw in text_lower for kw in ["adalah", "merupakan", "yaitu"])

        if is_science:
            # Untuk sains: butuh rumus/teori
            has_theory = any(kw in text_lower for kw in ["rumus", "teori", "prinsip", "hukum"])
            has_application = any(kw in text_lower for kw in ["aplikasi", "contoh", "digunakan", "teknologi"])

            if not (has_definition and has_theory and has_application):
                issues.append("Struktur SMA tidak lengkap - harus ada definisi, teori/rumus, dan aplikasi")

        elif is_history:
            # Untuk sejarah: butuh konteks historis dan analisis
            has_context = any(kw in text_lower for kw in [
                "konteks", "latar belakang", "kronologi", "peristiwa", "terjadi",
                "tanggal", "tahun", "masa", "periode", "abad"
            ])
            has_analysis = any(kw in text_lower for kw in [
                "pola", "prinsip", "analisis", "dampak", "pengaruh", "makna",
                "relevansi", "pelajaran", "signifikansi", "implikasi"
            ])

            if not (has_definition and has_context and has_analysis):
                issues.append("Struktur SMA tidak lengkap - harus ada gambaran umum, konteks historis, dan analisis mendalam")

        else:
            # Fallback: check umum (untuk topik lain)
            has_depth = any(kw in text_lower for kw in [
                "rumus", "teori", "prinsip", "hukum", "pola", "analisis",
                "konteks", "dampak", "pengaruh", "makna"
            ])
            has_application = any(kw in text_lower for kw in [
                "aplikasi", "contoh", "digunakan", "relevansi", "penerapan",
                "implementasi", "praktis", "manfaat"
            ])

            if not (has_definition and has_depth and has_application):
                issues.append("Struktur SMA tidak lengkap - harus ada definisi, pembahasan mendalam, dan relevansi/aplikasi")

        return issues

    def _clean_response(self, text: str) -> str:
        """Clean response dari formatting yang tidak diinginkan"""
        cleaned = text

        # Remove markdown bold
        cleaned = re.sub(r'\*\*([^*]+)\*\*', r'\1', cleaned)
        cleaned = re.sub(r'__([^_]+)__', r'\1', cleaned)

        # Remove markdown italic (hati-hati dengan formula matematika)
        # Hanya remove jika bukan dalam konteks matematika
        cleaned = re.sub(r'(?<![a-zA-Z0-9])\*([^*\n]+?)\*(?![a-zA-Z0-9])', r'\1', cleaned)

        # Remove headers
        cleaned = re.sub(r'^#{1,6}\s+', '', cleaned, flags=re.MULTILINE)

        # Remove code blocks
        cleaned = re.sub(r'```[a-z]*\n?', '', cleaned)
        cleaned = re.sub(r'```', '', cleaned)

        # Remove inline code
        cleaned = re.sub(r'`([^`]+)`', r'\1', cleaned)

        # Remove bullet points (tapi pertahankan dash di tengah kalimat)
        cleaned = re.sub(r'^\s*[-*+]\s+', '', cleaned, flags=re.MULTILINE)

        # Remove numbered lists
        cleaned = re.sub(r'^\s*\d+\.\s+', '', cleaned, flags=re.MULTILINE)

        # Remove [MODE KONSELING] marker
        cleaned = cleaned.replace("[MODE KONSELING]", "").strip()

        # Remove extra whitespace
        cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
        cleaned = cleaned.strip()

        return cleaned


def validate_and_improve(response: str, level: str, role: str, is_counseling: bool = False) -> Tuple[str, Dict]:
    """
    Validasi dan perbaiki response

    Args:
        response: Response asli dari AI
        level: Level pendidikan
        role: Role user
        is_counseling: Mode konseling atau tidak

    Returns:
        (cleaned_response, validation_report)
    """
    validator = ResponseValidator(level, role)
    result = validator.validate_response(response, is_counseling)

    return result["cleaned_response"], result
