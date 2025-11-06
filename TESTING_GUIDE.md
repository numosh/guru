# 🧪 GURU AI - Comprehensive Testing Guide

## 🎯 Overview

This guide provides systematic tests to validate the improvements and compare old vs. new GURU AI systems.

---

## 📋 Pre-Test Setup

### **1. Install Dependencies**

```bash
cd guru
python3 -m pip install -r requirements.txt
```

### **2. Verify Files Exist**

```bash
ls -la | grep -E "(guru_ai.py|guru_ai_improved.py|response_validator.py|improved_prompts.py)"
```

Expected output:
```
guru_ai.py                  # Original
guru_ai_improved.py         # Improved
response_validator.py       # Validator
improved_prompts.py         # New prompts
```

### **3. Check AI Connectivity**

```bash
# Test VirtueAI
curl -X POST https://api.virtueai.id/api/generate \
  -H "Content-Type: application/json" \
  -d '{"model":"llama3.1:latest","prompt":"test","stream":false}'

# Or test Ollama (if offline)
curl http://localhost:11434/api/tags
```

---

## 🧪 TEST SUITE

### **Test 1: Consistency Test (Same Question)**

**Objective:** Measure response variability

**Steps:**
1. Run old version 5 times
2. Run new version 5 times
3. Compare consistency

**Test Case 1.1: SD - "Kenapa langit biru?"**

```bash
# Old system (run 5 times)
python3 guru_ai.py
# Select: 1 (Pelajar) → 1 (SD)
# Ask: "Kenapa langit biru?"
# Copy response → save to old_response_1.txt

# Repeat 5 times (old_response_1.txt to old_response_5.txt)
```

```bash
# New system (run 5 times)
python3 guru_ai_improved.py
# Select: 1 (Pelajar) → 1 (SD)
# Ask: "Kenapa langit biru?"
# Copy response → save to new_response_1.txt

# Repeat 5 times
```

**Expected Results:**

| System | Structure Similarity | Tone Consistency | Avg Length |
|--------|---------------------|------------------|------------|
| Old | 40-60% | Medium | Varies widely |
| New | 85-95% | High | 120-180 words |

**Pass Criteria:**
- ✅ New system has ≥80% structural similarity
- ✅ Tone is consistent across all 5 responses
- ✅ Length variance < 20%

---

### **Test 2: Forbidden Phrase Detection**

**Objective:** Validate that forbidden phrases are blocked

**Test Case 2.1: SD Forbidden Phrases**

```python
# Test script
from response_validator import ResponseValidator

validator = ResponseValidator("sd", "pelajar")

# Test cases
test_responses = [
    "Hai adikku yang manis!",  # ❌ Should fail
    "Mari kita belajar bersama",  # ❌ Should fail
    "Bagaimana kalau kita coba?",  # ❌ Should fail
    "Wah, pertanyaan bagus! Jadi gini ya...",  # ✅ Should pass
]

for response in test_responses:
    result = validator.validate_response(response)
    print(f"Response: {response[:30]}...")
    print(f"Score: {result['score']}")
    print(f"Issues: {result['issues']}")
    print()
```

**Expected Results:**
```
Response: Hai adikku yang manis!...
Score: 90  # -10 for forbidden phrase
Issues: ["Menggunakan frasa terlarang: 'adikku'"]

Response: Mari kita belajar bersama...
Score: 90
Issues: ["Menggunakan frasa terlarang: 'mari kita'"]

Response: Wah, pertanyaan bagus! Jadi...
Score: 100
Issues: []
```

**Pass Criteria:**
- ✅ All forbidden phrases detected
- ✅ Score reduction proportional to violations
- ✅ Clean responses score 100

---

### **Test 3: Markdown Removal**

**Objective:** Ensure NO markdown formatting in responses

**Test Case 3.1: Markdown Detection**

```python
from response_validator import ResponseValidator

validator = ResponseValidator("sma", "pelajar")

test_responses = [
    "**Ini bold text**",
    "# Header text",
    "- Bullet point",
    "1. Numbered list",
    "Ini `inline code`",
    "Ini text biasa tanpa formatting"
]

for response in test_responses:
    result = validator.validate_response(response)
    has_markdown = len([i for i in result['issues'] if 'markdown' in i.lower()]) > 0
    print(f"Response: {response}")
    print(f"Markdown detected: {has_markdown}")
    print(f"Cleaned: {result['cleaned_response']}")
    print()
```

**Expected Results:**
```
Response: **Ini bold text**
Markdown detected: True
Cleaned: Ini bold text

Response: # Header text
Markdown detected: True
Cleaned: Header text

Response: Ini text biasa tanpa formatting
Markdown detected: False
Cleaned: Ini text biasa tanpa formatting
```

**Pass Criteria:**
- ✅ All markdown detected
- ✅ Cleaned version has no formatting
- ✅ Text content preserved

---

### **Test 4: SMA Structure Enforcement**

**Objective:** Validate 4-part structure for SMA academic questions

**Test Case 4.1: Physics Question**

```bash
# Run improved system
python3 guru_ai_improved.py
# Select: 1 (Pelajar) → 3 (SMA)
# Ask: "Apa itu hukum Newton kedua?"
```

**Manual Validation Checklist:**

```
✓ BAGIAN 1: JAWABAN INTI
  - Has formal definition?
  - Uses scientific terminology?
  - 2-3 sentences?

✓ BAGIAN 2: ASAL-USUL & SEJARAH
  - Mentions Isaac Newton?
  - Historical context provided?

✓ BAGIAN 3: TEORI & RUMUS
  - Has formula: F = ma?
  - Explains each variable?
  - Theoretical foundation?

✓ BAGIAN 4: APLIKASI
  - At least 3 real-world examples?
  - Mentions UTBK relevance?
  - Study implications?
```

**Pass Criteria:**
- ✅ All 4 sections present
- ✅ Formula included with explanations
- ✅ Minimum 3 applications
- ✅ UTBK mentioned

---

### **Test 5: Counseling Mode Detection**

**Objective:** Validate empathy in counseling mode

**Test Case 5.1: SD Emotional Question**

```bash
# Run improved system
python3 guru_ai_improved.py
# Select: 1 (Pelajar) → 1 (SD)
# Ask: "Aku ga suka sekolah"
```

**Validation:**

```python
# Check response contains empathy keywords
empathy_keywords = ["ngerti", "mengerti", "wajar", "pasti", "merasa", "perasaan"]
judgmental_phrases = ["seharusnya", "salah kamu", "kenapa sih", "lebay"]

# Manual check:
# ✓ Has [MODE KONSELING] marker (internal)?
# ✓ Contains ≥2 empathy keywords?
# ✓ Has NO judgmental phrases?
# ✓ Panel shows GREEN color?
# ✓ Asks what happened (doesn't preach)?
```

**Expected Response Pattern:**
```
[Panel GREEN with 💚]

Aku ngerti kok. Kamu pasti lagi [validation]...

[Ask what happened - NO immediate advice]

[Empathetic response]

[Suggest talking to parents/teachers]
```

**Pass Criteria:**
- ✅ Detects counseling mode automatically
- ✅ ≥2 empathy keywords present
- ✅ NO judgmental language
- ✅ Green panel displayed
- ✅ Listens before advising

---

### **Test 6: Pronoun Consistency**

**Objective:** Ensure consistent pronoun usage

**Test Case 6.1: SD Pronoun Check**

```python
from response_validator import ResponseValidator

validator = ResponseValidator("sd", "pelajar")

test_response = """
Halo adik! Kamu pasti penasaran ya. Aku akan jelaskan...
"""

result = validator.validate_response(test_response)
pronoun_issues = [i for i in result['issues'] if 'kata ganti' in i.lower() or 'pronoun' in i.lower()]

print(f"Pronoun issues: {pronoun_issues}")
```

**Expected:**
- ❌ "adik" detected as forbidden
- ✅ "kamu" and "aku" allowed

**Pass Criteria:**
- ✅ Forbidden pronouns detected
- ✅ Allowed pronouns pass
- ✅ Consistency enforced

---

### **Test 7: Length Validation**

**Objective:** Ensure responses are appropriately sized

**Test Case 7.1: Length Boundaries**

```python
from response_validator import ResponseValidator

# SD: 30-200 words
validator_sd = ResponseValidator("sd", "pelajar")

short_response = "Iya."  # 1 word
long_response = " ".join(["word"] * 250)  # 250 words
good_response = " ".join(["word"] * 100)  # 100 words

print("SHORT:", validator_sd._check_length(short_response))
print("LONG:", validator_sd._check_length(long_response))
print("GOOD:", validator_sd._check_length(good_response))
```

**Expected:**
```
SHORT: Response terlalu pendek untuk SD (minimal 30 kata)
LONG: Response terlalu panjang untuk SD (maksimal 200 kata)
GOOD:
```

**Pass Criteria:**
- ✅ Too short rejected
- ✅ Too long rejected
- ✅ Appropriate length accepted

---

### **Test 8: AI Parameter Optimization**

**Objective:** Verify optimized parameters reduce variability

**Test Case 8.1: Temperature Impact**

```python
# Compare old (temp=0.7) vs new (temp=0.3 for SMA)

import requests

prompt = "Jelaskan fotosintesis secara singkat"

# Old params
old_response = requests.post(url, json={
    "prompt": prompt,
    "options": {"temperature": 0.7}
})

# New params
new_response = requests.post(url, json={
    "prompt": prompt,
    "options": {"temperature": 0.3}
})

# Run 10 times each, measure standard deviation of response lengths
```

**Expected Results:**

| Parameter Set | Avg Length | Std Dev | Variability |
|---------------|------------|---------|-------------|
| Old (temp=0.7) | 185 | 42 | High |
| New (temp=0.3) | 178 | 18 | Low |

**Pass Criteria:**
- ✅ New params have <50% std dev of old
- ✅ Responses more consistent
- ✅ Quality maintained or improved

---

### **Test 9: Quality Score Accuracy**

**Objective:** Validate scoring system accuracy

**Test Case 9.1: Known Good Response**

```python
from response_validator import validate_and_improve

good_response = """
Wah, pertanyaan bagus! Jadi gini ya, langit biru karena cahaya matahari
itu sebenarnya punya banyak warna. Waktu cahaya matahari masuk ke udara
di langit, warna biru itu paling suka menyebar ke mana-mana. Makanya kita
lihatnya langit jadi biru. Coba deh besok siang kamu perhatiin langit!
"""

cleaned, report = validate_and_improve(good_response, "sd", "pelajar", False)

print(f"Score: {report['score']}")
print(f"Issues: {report['issues']}")
```

**Expected:**
```
Score: 100
Issues: []
```

**Test Case 9.2: Known Bad Response**

```python
bad_response = """
**Hai adikku!** Mari kita belajar bersama ya!

Langit itu biru karena... um... *cahaya*?

Bagaimana kalau kita coba eksperimen?
"""

cleaned, report = validate_and_improve(bad_response, "sd", "pelajar", False)

print(f"Score: {report['score']}")
print(f"Issues: {report['issues']}")
```

**Expected:**
```
Score: 55  # Multiple violations
Issues: [
    "Menggunakan frasa terlarang: 'adikku'",
    "Menggunakan frasa terlarang: 'mari kita'",
    "Menggunakan frasa terlarang: 'bagaimana kalau'",
    "Menggunakan markdown formatting: \\*\\*...",
    "Menggunakan markdown formatting: \\*...",
]
```

**Pass Criteria:**
- ✅ Good responses score 90-100
- ✅ Bad responses score <70
- ✅ All issues accurately detected

---

### **Test 10: End-to-End Comparison**

**Objective:** Overall system comparison

**Steps:**

1. **Prepare 20 test questions** (mix of academic + counseling)
2. **Run all through old system** - record responses
3. **Run all through new system** - record responses
4. **Manual quality assessment** by 3 reviewers
5. **Compare metrics**

**Test Questions:**

```
SD Academic:
1. Kenapa langit biru?
2. Bagaimana proses hujan?
3. Apa itu fotosintesis?

SD Counseling:
4. Aku ga suka sekolah
5. Temen-temen ga mau main sama aku
6. Aku takut sama guru

SMP Academic:
7. Apa itu ekosistem?
8. Jelaskan sistem peredaran darah
9. Bagaimana cara kerja internet?

SMP Counseling:
10. Temen-temen nge-bully aku
11. Aku bingung mau ikut ekskul apa
12. Nilai aku jelek terus

SMA Academic:
13. Apa itu hukum Newton kedua?
14. Jelaskan hukum Faraday
15. Bagaimana cara kerja sel volta?

SMA Counseling:
16. Aku bingung mau kuliah atau kerja
17. Aku stres mikirin UN
18. Aku ga tau passion aku apa

Pengajar:
19. Bagaimana mengajar perkalian kelas 2 SD?
20. Strategi engagement untuk SMP?
```

**Metrics to Compare:**

| Metric | Old System | New System | Target |
|--------|-----------|------------|---------|
| Avg quality score | 68/100 | ? | >85/100 |
| Forbidden phrase usage | 18% | ? | <3% |
| Markdown in responses | 35% | ? | <2% |
| Structure adherence | 45% | ? | >90% |
| Reviewer satisfaction | 6.2/10 | ? | >8.5/10 |
| Response time | 4.2s | ? | <2.5s |

**Pass Criteria:**
- ✅ New system scores ≥85/100 average
- ✅ <3% forbidden phrase usage
- ✅ <2% markdown formatting
- ✅ >90% structure adherence
- ✅ Reviewer satisfaction >8.5/10

---

## 📊 RESULTS TEMPLATE

```markdown
## Test Results Summary

**Date:** YYYY-MM-DD
**Tester:** Name
**Environment:** VirtueAI/Ollama + Model

### Test 1: Consistency
- Old variability: X%
- New variability: Y%
- Improvement: Z%
- Status: PASS/FAIL

### Test 2: Forbidden Phrases
- Detection accuracy: X%
- False positives: Y%
- Status: PASS/FAIL

[... continue for all tests ...]

### Overall Assessment
- Tests passed: X/10
- Critical failures: X
- Recommendation: APPROVE / NEEDS WORK / REJECT
```

---

## 🚀 Quick Test Script

```bash
#!/bin/bash
# quick_test.sh - Run automated tests

echo "🧪 GURU AI - Quick Test Suite"
echo "==============================="

# Test 1: Import check
echo "Test 1: Module imports..."
python3 -c "from response_validator import ResponseValidator; from improved_prompts import IMPROVED_SYSTEM_PROMPTS; print('✅ OK')"

# Test 2: Validator instantiation
echo "Test 2: Validator creation..."
python3 -c "from response_validator import ResponseValidator; v = ResponseValidator('sd', 'pelajar'); print('✅ OK')"

# Test 3: Forbidden phrase detection
echo "Test 3: Forbidden phrase detection..."
python3 << EOF
from response_validator import ResponseValidator
v = ResponseValidator("sd", "pelajar")
result = v.validate_response("Hai adikku!")
assert len(result['issues']) > 0, "Should detect forbidden phrase"
print("✅ OK")
EOF

# Test 4: Markdown detection
echo "Test 4: Markdown detection..."
python3 << EOF
from response_validator import ResponseValidator
v = ResponseValidator("sma", "pelajar")
result = v.validate_response("**Bold text**")
assert len([i for i in result['issues'] if 'markdown' in i.lower()]) > 0
print("✅ OK")
EOF

echo ""
echo "✅ All quick tests passed!"
```

---

## 💡 DEBUGGING TIPS

**If test fails:**

1. **Check dependencies:**
   ```bash
   python3 -m pip list | grep -E "(requests|rich)"
   ```

2. **Verify file integrity:**
   ```bash
   python3 -m py_compile response_validator.py
   python3 -m py_compile improved_prompts.py
   ```

3. **Test with verbose output:**
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

4. **Compare exact responses:**
   ```bash
   diff old_response.txt new_response.txt
   ```

---

**Ready to test? Start with the Quick Test Script, then run full suite!**
