# Mode Konseling - GURU AI

## 🎯 Fitur Dual Mode untuk Pelajar

GURU AI memiliki kemampuan **automatic mode switching** untuk role pelajar:

### 📚 Mode Pembelajaran (Default)
Aktif ketika pelajar bertanya tentang:
- Mata pelajaran (matematika, IPA, bahasa, dll)
- Pengetahuan umum akademik
- Tips belajar dan study skills

**Tampilan:** Panel magenta biasa

### 💚 Mode Konseling (Otomatis)
Aktif ketika pelajar bertanya tentang:
- Masalah pribadi atau emosional
- Isu sosial (teman, keluarga, dll)
- Dilema atau kebingungan hidup
- Karir dan masa depan (SMA)

**Tampilan:** Panel hijau (💚) dengan border bright_green

## 🔄 Cara Kerja

1. **Deteksi Otomatis**: AI mendeteksi jenis pertanyaan
2. **Internal Marker**: AI menyisipkan `[MODE KONSELING]` sebagai marker (tidak ditampilkan ke user)
3. **Visual Indicator**: System mendeteksi marker dan ubah warna panel:
   - 💚 **Hijau** = Mode Konseling
   - 🎓 **Biru** = Mode Pembelajaran
4. **Empati & Support**: AI memberikan dukungan emosional yang sesuai usia

## 📝 Contoh

### Pelajar SMA bertanya masalah pribadi:

```
Anda: Kenapa saya harus sekolah? Saya merasa tidak semangat

╭─ Respons GURU AI - 💚 Mode Konseling ─────────────────────╮
│ 💚 Mode Konseling Aktif 💚                                │
│                                                            │
│ Terima kasih sudah berbagi perasaanmu. Kehilangan         │
│ semangat itu hal yang wajar dialami, dan kamu tidak       │
│ sendirian dalam merasakannya.                             │
│                                                            │
│ Banyak siswa mengalami fase seperti ini, terutama ketika  │
│ rutinitas terasa monoton atau tujuan terasa kabur. Yang   │
│ penting adalah kamu mau mengakui perasaan ini dan mencari │
│ cara untuk kembali menemukan makna...                     │
╰────────────────────────────────────────────────────────────╯
```

### Pelajar SD bertanya pelajaran:

```
Anda: Kenapa air bisa mendidih?

╭─ Respons GURU AI ──────────────────────────────────────────╮
│ Halo adik! Wah, pertanyaan yang bagus!                    │
│                                                            │
│ Jadi begini ya, air itu mendidih karena panasnya api      │
│ membuat air jadi sangat-sangat panas sampai dia berubah   │
│ jadi uap. Seperti kalau kamu mandi air hangat, ada uapnya │
│ kan? Nah kalau panasnya lebih kuat lagi, airnya jadi      │
│ gelembung-gelembung dan menguap ke udara...               │
╰────────────────────────────────────────────────────────────╯
```

## ⚠️ Batasan Mode Konseling

### Mode konseling TIDAK untuk:
- Kasus yang memerlukan profesional (psikolog/psikiater)
- Krisis mental health yang serius
- Situasi berbahaya atau emergency

### AI akan menyarankan:
- Bicara dengan orang tua
- Konsultasi guru BK
- Mencari bantuan profesional jika diperlukan

## 🔧 Pengaturan

Mode konseling **otomatis aktif** untuk semua role pelajar (SD, SMP, SMA).

Untuk role **pengajar**: Tetap fokus pedagogi, tidak ada mode konseling.

## 💡 Tips Penggunaan

1. **Jujur dengan perasaan** - AI tidak menghakimi
2. **Berikan konteks** - Ceritakan situasinya
3. **Terbuka untuk saran** - AI akan memberikan perspektif yang seimbang
4. **Follow up jika perlu** - Tanyakan lebih lanjut jika butuh klarifikasi

---

**Catatan:** Mode konseling adalah dukungan awal. Untuk isu serius, selalu konsultasi dengan profesional yang qualified.
