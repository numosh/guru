# 🤝 Contributing to GURU AI

Terima kasih ingin berkontribusi ke GURU AI! Setiap kontribusi sangat berarti untuk pendidikan Indonesia.

## 🎯 Ways to Contribute

### 1. **Code Contributions**
- Bug fixes
- New features
- Performance improvements
- Code refactoring
- Tests

### 2. **Documentation**
- Improve README
- Add tutorials
- Create examples
- Translate docs
- Fix typos

### 3. **Testing & Feedback**
- Test dengan students
- Report bugs
- Suggest features
- Share use cases
- Performance testing

### 4. **Data & AI**
- Contribute conversation data
- Help fine-tune models
- Improve prompts
- Benchmark tests
- Quality evaluation

### 5. **Community**
- Answer questions
- Help newcomers
- Share knowledge
- Spread awareness
- Organize events

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Git
- Basic understanding of AI/LLM
- Passion untuk pendidikan Indonesia! 🇮🇩

### Setup Development Environment

1. **Fork & Clone**
```bash
git clone https://github.com/YOUR_USERNAME/guru.git
cd guru
```

2. **Create Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run Application**
```bash
python guru_ai.py
```

---

## 📝 Development Workflow

### 1. Create Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

**Branch Naming:**
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation
- `refactor/` - Code refactoring
- `test/` - Tests

### 2. Make Changes
- Write clean code
- Follow Python PEP 8
- Add comments untuk code yang complex
- Keep functions small & focused

### 3. Test Your Changes
```bash
# Manual testing
python guru_ai.py

# Test different scenarios
# - Pelajar SD/SMP/SMA
# - Pembelajaran vs Konseling
# - Error handling
```

### 4. Commit Changes
```bash
git add .
git commit -m "feat: add voice input support"
```

**Commit Message Format:**
```
<type>: <subject>

<body> (optional)
```

**Types:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `style:` Formatting
- `refactor:` Code refactoring
- `test:` Tests
- `chore:` Maintenance

**Examples:**
```
feat: add conversation history
fix: resolve mode konseling detection bug
docs: update installation guide
refactor: improve system prompt struktur
```

### 5. Push & Create PR
```bash
git push origin feature/your-feature-name
```

Then create Pull Request on GitHub dengan:
- Clear title & description
- Screenshots (jika UI changes)
- Test results
- Related issues (jika ada)

---

## 🎨 Code Style Guidelines

### Python Code
```python
# Good ✅
def calculate_score(response: str, criteria: dict) -> int:
    """
    Calculate quality score untuk response.
    
    Args:
        response: AI response text
        criteria: Scoring criteria
        
    Returns:
        Score 0-100
    """
    score = 0
    for criterion, weight in criteria.items():
        score += evaluate_criterion(response, criterion) * weight
    return min(max(score, 0), 100)


# Bad ❌
def calc(r,c):
    s=0
    for x,y in c.items():s+=eval(r,x)*y
    return s
```

### System Prompts
```python
# Good ✅ - Clear, natural, specific
"""
Kamu adalah guru SD yang hangat dan sabar.

PRINSIP:
1. Konsisten pakai "kamu" untuk siswa
2. Pakai "aku" untuk diri sendiri
3. Bahasa sehari-hari yang natural

CONTOH:
"Wah, pertanyaan bagus! Jadi gini ya..."
"""

# Bad ❌ - Verbose, unclear, formal
"""
Anda adalah seorang pendidik tingkat Sekolah Dasar 
yang memiliki karakteristik sangat sabar dan 
menggunakan bahasa yang sesuai dengan tingkat 
perkembangan kognitif anak usia 6-12 tahun...
"""
```

---

## 🧪 Testing Guidelines

### Manual Testing Checklist

**Basic Functionality:**
- [ ] App starts without errors
- [ ] VirtueAI connection works
- [ ] Ollama fallback works
- [ ] Role selection works
- [ ] Level selection works

**Pembelajaran Mode:**
- [ ] Answers accurate
- [ ] Language appropriate untuk level
- [ ] Examples relevant
- [ ] No formatting issues

**Konseling Mode:**
- [ ] Empathy present
- [ ] No judgment
- [ ] Safe recommendations
- [ ] Redirects when needed

**Multi-Agent QA:**
- [ ] Guru Senior scores properly
- [ ] Kepala Sekolah approves/rejects correctly
- [ ] Revisions improve quality
- [ ] Safety checks work

---

## 📚 Documentation Standards

### Code Comments
```python
# Good ✅
# Detect counseling mode from internal marker
if "[MODE KONSELING]" in response:
    counseling_mode = True

# Bad ❌
# Check if konseling
if "[MODE KONSELING]" in response:
```

### Docstrings
```python
# Good ✅
def query_ai(prompt: str, system_prompt: str) -> str:
    """
    Send query to AI API dan get response.
    
    Args:
        prompt: User question
        system_prompt: System instructions for AI
        
    Returns:
        AI response text atau error message
        
    Raises:
        RequestException: Jika API call fails
    """
    pass

# Bad ❌
def query_ai(prompt, system_prompt):
    """Query AI"""
    pass
```

---

## 🐛 Bug Reports

**Good Bug Report Template:**
```markdown
## Bug Description
Clear description of the bug

## Steps to Reproduce
1. Run `python guru_ai.py`
2. Select "Pelajar" → "SD"
3. Ask "kenapa langit biru"
4. Error appears

## Expected Behavior
Should explain dengan bahasa sederhana

## Actual Behavior
[Paste error message or screenshot]

## Environment
- OS: macOS 14.1
- Python: 3.11.5
- Model: llama3.1:8b
- Version: 1.0.0

## Additional Context
[Any other info]
```

---

## 💡 Feature Requests

**Good Feature Request Template:**
```markdown
## Feature Description
Add voice input support

## Problem It Solves
Students bisa interact dengan voice, lebih natural

## Proposed Solution
Integrate Whisper untuk speech-to-text

## Alternatives Considered
- Google Speech API (need internet)
- Azure Speech (paid)

## Additional Context
See issue #123 untuk related discussion
```

---

## 🎓 Learning Resources

### For Beginners
- [Python Basics](https://docs.python.org/3/tutorial/)
- [Git Tutorial](https://git-scm.com/docs/gittutorial)
- [Rich Library](https://rich.readthedocs.io/)

### For AI/LLM
- [Ollama Documentation](https://ollama.ai/docs)
- [Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- [LLM Fine-tuning](https://huggingface.co/docs/transformers/training)

### For Education
- [Pedagogi Indonesia](https://gtk.kemdikbud.go.id/)
- [Psikologi Anak](https://www.apa.org/topics/child-development)

---

## ✅ Pull Request Checklist

Before submitting PR, pastikan:

- [ ] Code works dan tested manually
- [ ] No breaking changes (atau documented)
- [ ] Code follows style guidelines
- [ ] Comments added untuk complex logic
- [ ] Documentation updated (jika perlu)
- [ ] Commit messages clear
- [ ] Branch up to date dengan main
- [ ] PR description complete

---

## 🏆 Recognition

Contributors akan di-credit di:
- README.md (Contributors section)
- Release notes
- Special thanks dalam updates

Top contributors might get:
- Collaborator access
- Feature requests priority
- Early access ke new versions
- Swag (future!) 🎁

---

## 📞 Questions?

- **GitHub Issues:** https://github.com/numosh/guru/issues
- **GitHub Discussions:** https://github.com/numosh/guru/discussions
- **Email:** [Contact maintainer]

---

## 📄 License

By contributing, you agree bahwa contributions akan di-license under the same license sebagai project (MIT License).

---

**Thank you untuk contribute ke GURU AI! Together kita bisa buat education better untuk Indonesia! 🇮🇩🎓**
