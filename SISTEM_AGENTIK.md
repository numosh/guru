# Sistem Agentik Multi-Agent QA - GURU AI

## 🏫 Arsitektur Sistem

```
┌─────────────────────────────────────────────────────────┐
│                    USER QUESTION                        │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────┐
│  GURU MUDA (Primary Responder)                          │
│  - Generate jawaban awal                                │
│  - Mode: Pembelajaran atau Konseling                    │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────┐
│  GURU SENIOR (Quality Checker)                          │
│  - Verifikasi empati & tone                             │
│  - Cek akurasi konten                                   │
│  - Safety check                                         │
│  - Score: 0-100                                         │
│                                                         │
│  Threshold: Score ≥ 70 → Pass                           │
│             Score < 70 → Revisi jawaban                 │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ▼ (jika score < 80)
┌─────────────────────────────────────────────────────────┐
│  KEPALA SEKOLAH (Final Approver)                        │
│  - Final safety check                                   │
│  - Values alignment                                     │
│  - Professional boundaries                              │
│  - Legal & ethical validation                           │
│                                                         │
│  Decision: APPROVE / REVISE / REJECT                    │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────┐
│              FINAL ANSWER TO USER                       │
└─────────────────────────────────────────────────────────┘
```

## 👥 Agent Roles

### 1. **Guru Muda** (Primary Responder)
**Tugas:**
- Generate jawaban awal untuk siswa
- Detect mode (Pembelajaran vs Konseling)
- Follow system prompts sesuai level

**Karakteristik:**
- Fresh perspective
- Up-to-date dengan metode modern
- Enthusiastic tapi kadang kurang pengalaman

---

### 2. **Guru Senior** (Quality Checker)
**Tugas:**
- Review kualitas jawaban dari Guru Muda
- Scoring 0-100 berdasarkan kriteria
- Revisi jika diperlukan

**Kriteria Evaluasi:**

#### Untuk SD:
- ✅ Bahasa sesuai usia 6-12 tahun
- ✅ Empati jika mode konseling
- ✅ Tidak pakai kata meremehkan
- ✅ Akurasi informasi
- ✅ Safety (tidak trigger anxiety)

#### Untuk SMP:
- ✅ Relate dengan dunia remaja
- ✅ Tidak patronizing
- ✅ Validasi perasaan
- ✅ Tidak victim-blaming
- ✅ Encourage healthy coping

#### Untuk SMA:
- ✅ Respectful sebagai young adults
- ✅ Tidak condescending
- ✅ Multiple perspectives
- ✅ Dorong critical thinking
- ✅ Ethical guidance

**Scoring System:**
- **90-100:** Excellent - Luar biasa empati dan akurat
- **80-89:** Good - Baik, minor improvements
- **70-79:** Acceptable - Cukup, tapi bisa lebih baik
- **< 70:** Needs Revision - Harus diperbaiki

---

### 3. **Kepala Sekolah** (Final Approver)
**Tugas:**
- Final validation sebelum ke user
- Safety & ethics guardian
- Decision maker

**Final Check Criteria:**
1. **Safety First**
   - Tidak ada konten berbahaya
   - Tidak trigger trauma
   - Protect student welfare

2. **Values Alignment**
   - Sesuai nilai pendidikan Indonesia
   - Promote positive values
   - Cultural sensitivity

3. **Professional Boundaries**
   - Tidak overstep sebagai AI
   - Redirect ke manusia jika perlu
   - Acknowledge limitations

4. **Legal & Ethical**
   - Tidak melanggar kode etik guru
   - Responsible advice
   - Proper safeguarding

**Decision Tree:**
```
Score ≥ 80 → APPROVE (langsung ke user)
Score 70-79 → APPROVE dengan catatan
Score < 70 → REVISE (pakai revised answer)
Red Flags → REJECT (safety fallback message)
```

---

## 🔄 Flow Process

### Normal Flow (Score tinggi):
```
1. User bertanya
2. Guru Muda jawab
3. Guru Senior review → Score 85
4. APPROVED → Langsung ke user
```

### Revision Flow (Score rendah):
```
1. User bertanya
2. Guru Muda jawab (kurang empati)
3. Guru Senior review → Score 65
4. Guru Senior revisi jawaban
5. Kepala Sekolah review → APPROVE
6. Revised answer → Ke user
```

### Rejection Flow (Red flags):
```
1. User bertanya (self-harm indication)
2. Guru Muda jawab
3. Guru Senior → flag safety issue
4. Kepala Sekolah → REJECT
5. Safe fallback message:
   "Untuk pertanyaan ini sebaiknya diskusikan 
    dengan guru/orang tua ya..."
```

---

## 🎯 Contoh Proses

### Case 1: Pertanyaan Akademik SD
```
User: "Kenapa langit biru?"

Guru Muda:
"Halo adik! Langit berwarna biru karena cahaya 
matahari yang dipantulkan oleh udara..."

Guru Senior Review:
{
  "approved": true,
  "score": 88,
  "issues": [],
  "suggestions": ["Sudah bagus, empati cukup"]
}

→ APPROVED, langsung ke user
```

### Case 2: Konseling SMP (Perlu Revisi)
```
User: "Saya tidak punya teman"

Guru Muda:
"Ah biasa itu, nanti juga dapat teman kok."

Guru Senior Review:
{
  "approved": false,
  "score": 55,
  "issues": ["Meremehkan perasaan", "Tidak empati"],
  "revised_answer": "Aku mengerti perasaanmu. 
  Merasa sendirian itu berat banget. Perasaanmu 
  valid kok..."
}

Kepala Sekolah: APPROVE revised answer

→ User dapat jawaban yang sudah direvisi
```

### Case 3: Safety Concern (REJECT)
```
User: "Saya ingin bunuh diri"

Guru Muda: (mencoba memberi dukungan)

Guru Senior: Flag mental health crisis

Kepala Sekolah Review:
{
  "final_approved": false,
  "final_decision": "REJECT",
  "reason": "Mental health emergency - require 
  professional intervention"
}

→ User dapat:
"Maaf, untuk pertanyaan ini sangat penting 
kamu bicara langsung dengan orang tua, guru BK, 
atau hubungi hotline kesehatan mental 119 ext 8. 
Kamu tidak sendirian dan ada yang ingin membantu."
```

---

## ⚙️ Configuration

### Thresholds
```python
QUALITY_THRESHOLDS = {
    "minimum_score": 70,           # Min untuk pass
    "excellent_score": 90,          # Excellent quality
    "kepala_sekolah_required_if_score_below": 80,
    "max_revision_attempts": 2
}
```

### Toggle
```python
agentic_mode = True  # Set False untuk disable QA
```

---

## 📊 Benefits

1. **Quality Assurance**: Jawaban selalu direview sebelum ke user
2. **Safety Net**: Cegah jawaban yang tidak empati atau berbahaya
3. **Continuous Improvement**: Guru Senior belajar dari pattern
4. **Accountability**: Multi-layer validation
5. **Trust**: User dapat jawaban yang sudah terverifikasi

---

## 🔧 Technical Implementation

**File:** `agentic_system.py`
- Agent system prompts
- Quality thresholds
- Evaluation criteria

**Integration:** `guru_ai.py`
- `call_agent()` - Call specific agent
- `agentic_qa_process()` - Orchestrate multi-agent flow
- Integrated in main query loop

---

## 💡 Future Enhancements

1. **Feedback Loop**: Agents learn from user satisfaction
2. **Specialization**: More specialized agents (Math Teacher, BK, etc)
3. **Analytics**: Track quality scores over time
4. **User Rating**: Allow users to rate answers
5. **Escalation Path**: Automatic escalation for serious issues

---

**Note:** Sistem agentik hanya aktif untuk role **pelajar**. Role pengajar tetap direct response tanpa multi-agent QA.
