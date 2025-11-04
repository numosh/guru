# 🗺️ ROADMAP - GURU AI

**Project:** AI Terminal untuk Profiling Guru Indonesia  
**Author:** @anugrahprahasta  
**Started:** 2025  
**Current Version:** 1.0.0

---

## 🎯 Vision & Mission

**Vision:**  
Menciptakan AI assistant pendidikan yang empati, akurat, dan accessible untuk semua kalangan pendidikan Indonesia.

**Mission:**
1. Menyediakan dukungan pembelajaran yang personalized untuk siswa SD/SMP/SMA
2. Memberikan guidance pedagogi untuk para pendidik
3. Mengintegrasikan mode konseling yang aman dan supportive
4. Membuat sistem yang bisa berjalan offline dengan model lokal

---

## 📍 Current Status: **Version 1.0 - Foundation**

### ✅ Completed Milestones

#### **Milestone 1: Core Foundation** ✅ (Nov 2025)
- [x] Basic terminal UI with Rich library
- [x] Dual API support (VirtueAI Online + Ollama Local fallback)
- [x] Role-based system (Pelajar/Pengajar)
- [x] Level-based prompts (SD/SMP/SMA)
- [x] System prompt engineering untuk setiap kombinasi
- [x] Error handling & timeout management
- [x] Beautiful ASCII logo & branding

#### **Milestone 2: Dual Mode System** ✅ (Nov 2025)
- [x] Mode Pembelajaran (akademik)
- [x] Mode Konseling (masalah pribadi/emosional)
- [x] Automatic mode detection
- [x] Visual indicators (color-coded panels)
- [x] Internal marker system `[MODE KONSELING]`
- [x] Empati-first approach untuk konseling

#### **Milestone 3: Multi-Agent QA** ✅ (Nov 2025)
- [x] Guru Muda (Primary Responder)
- [x] Guru Senior (Quality Checker dengan scoring 0-100)
- [x] Kepala Sekolah (Final Safety Approver)
- [x] Automatic revision untuk low-quality responses
- [x] Safety net untuk red flags (self-harm, abuse, dll)
- [x] Hierarchical validation system

#### **Milestone 4: Natural Language Optimization** ✅ (Nov 2025)
- [x] Konsisten kata ganti (kamu/aku) - no more mixing
- [x] Natural conversational tone untuk SD
- [x] Hapus bahasa yang creepy/manipulatif
- [x] Accuracy enforcement (no ngasal)
- [x] Remove visible markers dari output
- [x] Enhanced Guru Senior dengan criteria lebih ketat

---

## 🚀 Upcoming Milestones

### **Milestone 5: Model Optimization** 🎯 (Target: Q1 2026)

**Goal:** Membuat custom fine-tuned model yang lebih ringan dan optimal untuk use case GURU AI

**Tasks:**
- [ ] **Dataset Collection**
  - [ ] Kumpulkan 1000+ conversation examples (pembelajaran + konseling)
  - [ ] Annotate dengan quality scores
  - [ ] Balance dataset per level (SD/SMP/SMA)
  
- [ ] **Model Fine-tuning**
  - [ ] Fine-tune model kecil (1B-3B parameters) dengan dataset
  - [ ] Target models: Qwen2.5:1.5B, Llama3.2:1B, Phi-3-mini
  - [ ] Optimize untuk Indonesian language
  - [ ] Test accuracy vs current models
  
- [ ] **Model Compression**
  - [ ] Quantization ke 4-bit/8-bit untuk reduce size
  - [ ] Test performance dengan quantized models
  - [ ] Ensure quality tetap terjaga
  
- [ ] **Model Distribution**
  - [ ] Package model dalam format GGUF
  - [ ] Upload ke Hugging Face
  - [ ] Provide auto-download script
  - [ ] Documentation untuk model usage

**Success Criteria:**
- Model size < 2GB (untuk easy download)
- Response quality score ≥ 80/100 (sama atau lebih baik dari current)
- Inference speed < 5 detik per response
- Works offline 100%

---

### **Milestone 6: Enhanced Features** 🔮 (Target: Q2 2026)

**Goal:** Menambah fitur-fitur advanced untuk better user experience

**Tasks:**
- [ ] **Conversation History**
  - [ ] Save chat history per session
  - [ ] Resume previous conversation
  - [ ] Export conversation ke PDF/TXT
  
- [ ] **Subject-Specific Agents**
  - [ ] Math Teacher specialist
  - [ ] Science Teacher specialist
  - [ ] Language Teacher specialist
  - [ ] BK (Bimbingan Konseling) specialist
  
- [ ] **Analytics & Insights**
  - [ ] Track conversation topics
  - [ ] Quality score trends
  - [ ] Most asked questions
  - [ ] User satisfaction metrics
  
- [ ] **Voice Support**
  - [ ] Speech-to-Text input
  - [ ] Text-to-Speech output
  - [ ] Voice cloning untuk persona guru

---

### **Milestone 7: Community & Ecosystem** 🌍 (Target: Q3 2026)

**Goal:** Build komunitas dan ekosistem sekitar GURU AI

**Tasks:**
- [ ] **Plugin System**
  - [ ] Allow custom prompts/agents
  - [ ] Plugin marketplace
  - [ ] Community contributions
  
- [ ] **Multi-platform**
  - [ ] Web interface
  - [ ] Mobile app (Android/iOS)
  - [ ] Desktop app (Electron)
  - [ ] API service
  
- [ ] **Collaboration Features**
  - [ ] Multi-user classroom mode
  - [ ] Teacher dashboard
  - [ ] Parent monitoring (opt-in)
  
- [ ] **Content Library**
  - [ ] Curated learning materials
  - [ ] Video explanations
  - [ ] Interactive exercises
  - [ ] Gamification

---

## 📊 Technical Roadmap

### Phase 1: Foundation (DONE ✅)
```
Terminal App
    ↓
VirtueAI API (Online)
    ↓ (fallback)
Ollama Local (Offline)
    ↓
llama3.1:8b / qwen2.5
```

### Phase 2: Optimization (Q1 2026)
```
Terminal App
    ↓
Custom Fine-tuned Model (GGUF)
    ↓
guru-id-1.5b (< 2GB)
    ↓
100% Offline
```

### Phase 3: Distribution (Q2 2026)
```
Terminal + Web + Mobile
    ↓
Cloud Service (Optional)
    ↓
Local-First Architecture
    ↓
Hugging Face Model Hub
```

### Phase 4: Ecosystem (Q3 2026)
```
Plugin System + API
    ↓
Community Contributions
    ↓
Multi-Platform Deployment
    ↓
Global Education Network
```

---

## 🎓 Model Strategy

### Current Models (v1.0)
| Model | Size | Use Case | Status |
|-------|------|----------|--------|
| llama3.1:latest | ~4.7GB | VirtueAI Online | ✅ Active |
| llama3.1:8b | ~4.7GB | Ollama Local | ✅ Fallback |
| qwen2.5:7b | ~4.4GB | Alternative | ✅ Tested |

### Target Models (v2.0 - Q1 2026)
| Model | Size | Parameters | Target |
|-------|------|------------|--------|
| guru-id-sd | ~1GB | 1.5B | SD-optimized |
| guru-id-smp | ~1.2GB | 1.8B | SMP-optimized |
| guru-id-sma | ~1.5GB | 2.5B | SMA-optimized |
| guru-id-unified | ~2GB | 3B | All levels |

**Fine-tuning Strategy:**
1. Base: Qwen2.5-1.5B-Instruct atau Llama3.2-1B
2. Dataset: 1000+ Indonesian education conversations
3. Training: LoRA fine-tuning
4. Quantization: Q4_K_M atau Q8_0
5. Validation: Human eval + auto metrics

---

## 💡 Innovation Goals

### Short Term (Q1 2026)
- **Lighter & Faster:** Model < 2GB yang bisa di-download semua orang
- **Better Quality:** Fine-tuned specifically untuk education Indonesia
- **Full Offline:** 100% bisa jalan tanpa internet
- **Easy Setup:** One-command installation

### Mid Term (Q2 2026)
- **Specialist Agents:** Math, Science, Language experts
- **Voice Interaction:** Ngobrol pakai suara
- **Smart History:** Context-aware dari chat sebelumnya
- **Multi-modal:** Text + gambar untuk explain concepts

### Long Term (Q3 2026)
- **Collaborative Learning:** Connect students with peers
- **Teacher Tools:** Dashboard untuk monitor & guide
- **Adaptive Learning:** AI yang belajar dari interaction patterns
- **Global Reach:** Multi-language support (English, Malay, dll)

---

## 🤝 Community Involvement

### How to Contribute

**For Developers:**
1. Fork repository
2. Create feature branch
3. Submit PR dengan description jelas
4. Follow coding standards

**For Educators:**
1. Test dengan students
2. Report feedback & issues
3. Suggest improvements
4. Share success stories

**For Data Scientists:**
1. Help dengan model fine-tuning
2. Contribute training data
3. Optimize prompts
4. Benchmark performance

**For Everyone:**
1. Star ⭐ repository
2. Share dengan teman-teman
3. Report bugs
4. Spread the word!

---

## 📈 Success Metrics

### v1.0 (Current)
- [x] Terminal app functional
- [x] Dual mode working
- [x] Multi-agent QA active
- [x] Natural language untuk SD
- [x] Safe for students

### v2.0 (Q1 2026 Target)
- [ ] Custom model < 2GB
- [ ] 1000+ downloads
- [ ] Quality score ≥ 85/100
- [ ] 100% offline capable
- [ ] 10+ community contributors

### v3.0 (Q3 2026 Target)
- [ ] 10,000+ active users
- [ ] Multi-platform support
- [ ] Plugin ecosystem
- [ ] International recognition
- [ ] Self-sustaining community

---

## 🙏 Acknowledgments

- **VirtueAI** - API support
- **Ollama** - Local LLM infrastructure
- **Qwen & Llama Teams** - Base models
- **Rich Library** - Beautiful terminal UI
- **Indonesian Education Community** - Feedback & support

---

## 📞 Contact & Links

- **GitHub:** https://github.com/numosh/guru
- **Author:** @anugrahprahasta
- **Email:** [TBD]
- **Discord:** [TBD]
- **Documentation:** See README.md

---

**Last Updated:** 2025-01-04  
**Version:** 1.0.0  
**Status:** 🟢 Active Development

---

**"Mencerdaskan Indonesia, Satu Percakapan AI at a Time"** 🇮🇩🎓
