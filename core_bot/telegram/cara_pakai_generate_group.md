## 📘 Dokumentasi: `generate_grup_markdown()` – Sistem Grup Telegram Dinamis

### 📂 Lokasi File

```
core_bot/
└── telegram/
    └── generate_group.py
```

---

## 🚀 Tujuan

Fungsi `generate_grup_markdown()` memungkinkan developer menampilkan daftar grup Telegram dalam format Markdown, **secara fleksibel dan dinamis**, berdasarkan konfigurasi di `.env`.

---

## ⚙️ Cara Kerja

Fungsi akan:

1. Membaca jumlah grup dari ENV (`GRUP_COUNT`)
2. Mengambil nama dan link setiap grup (`GRUP_1_NAMA`, `GRUP_1_LINK`, dst.)
3. Mengatur jumlah grup per baris (`GRUP_PER_BARIS`)
4. Mengembalikan teks Markdown yang siap ditampilkan di Telegram

---

## 🧩 Struktur ENV yang Dibutuhkan

```env
# Jumlah total grup
GRUP_COUNT=4

# Jumlah grup per baris (untuk layout horizontal)
GRUP_PER_BARIS=2

# Data grup (nama + link)
GRUP_1_NAMA=Diskusi Umum
GRUP_1_LINK=https://t.me/diskusi

GRUP_2_NAMA=Channel VIP
GRUP_2_LINK=https://t.me/vip

GRUP_3_NAMA=Kripto Pemula
GRUP_3_LINK=https://t.me/pemula

GRUP_4_NAMA=Signal Harian
GRUP_4_LINK=https://t.me/signal
```

> ⚠️ Semua `GRUP_{i}_NAMA` dan `GRUP_{i}_LINK` harus tersedia & valid untuk ditampilkan.

---

## 🧠 Integrasi di `config.py`

File `core_bot/config.py` akan mengatur parsing ENV ini:

```python
GROUP_COUNT = int(os.getenv("GRUP_COUNT", 6))
GROUP_PER_BARIS = int(os.getenv("GRUP_PER_BARIS", 3))

GRUP_LINKS = []
for i in range(1, GROUP_COUNT + 1):
    nama = os.getenv(f"GRUP_{i}_NAMA")
    link = os.getenv(f"GRUP_{i}_LINK")
    if nama and link:
        GRUP_LINKS.append({"nama": nama.strip(), "link": link.strip()})
```

---

## 🔧 Fungsi Utama

```python
# core_bot/telegram/generate_group.py

from core_bot import config

def generate_grup_markdown() -> str:
    grup_md_list = [f"[{g['nama']}]({g['link']})" for g in config.GRUP_LINKS]

    baris_md = []
    for i in range(0, len(grup_md_list), config.GROUP_PER_BARIS):
        baris = grup_md_list[i:i + config.GROUP_PER_BARIS]
        baris_md.append(" | ".join(baris))

    return "\n".join(baris_md)
```

---

## 📥 Contoh Pemakaian

### Di handler bot (`start.py` atau lainnya):

```python
from core_bot.telegram.generate_group import generate_grup_markdown

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    grup_links_md = generate_grup_markdown()
    welcome_text = (
        "👋 Selamat datang di Sayabot!\n\n"
        "📢 Gabung grup kami:\n"
        f"{grup_links_md}\n\n"
        "Silakan pilih menu di bawah ini:"
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown")
```

---

## 💡 Tips Tambahan

* Jika ingin **menampilkan grup dalam 1 kolom vertikal**, cukup set:

  ```env
  GRUP_PER_BARIS=1
  ```
* Jika ingin **menyembunyikan beberapa grup**, cukup kosongkan nama/link-nya di ENV atau kurangi `GRUP_COUNT`.

---

## 🧪 Output Contoh

Dengan konfigurasi:

```env
GRUP_COUNT=3
GRUP_PER_BARIS=2
```

Hasil:

```
[Diskusi Umum](https://t.me/diskusi) | [Channel VIP](https://t.me/vip)
[Kripto Pemula](https://t.me/pemula)
```

---

## 📌 Catatan

* Fungsi ini **tidak mencetak header seperti `🤝 Gabung Grup:`** — itu bisa ditambahkan secara fleksibel di proyek masing-masing.
* Semua data grup dikelola melalui `.env`, membuatnya sangat cocok untuk proyek multi-klien.

---

## ✅ Siap untuk Open Source

Modul ini telah dirancang agar:

* 💼 Cocok untuk multi-brand atau white-label bot
* 🔄 Mudah dikonfigurasi ulang di setiap proyek
* ☁️ Aman untuk digunakan di lingkungan deployment dengan `.env`

---

Kalau kamu setuju, ini bisa disimpan sebagai file dokumentasi:

```
core_bot/docs/telegram_group.md
```

