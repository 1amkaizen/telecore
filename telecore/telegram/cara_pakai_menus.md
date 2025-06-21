# 📘 Dokumentasi: `telecore.telegram.menus`

Modul ini menyediakan fungsi fleksibel `make_menu()` untuk membuat **inline keyboard Telegram** dalam bentuk grid sesuai kebutuhan.

---

## 📂 Lokasi File

```
telecore/
└── telegram/
    └── menus.py
```

---

## 🧩 Tipe Data

```python
ButtonRow = List[Tuple[str, str]]
```

Tipe alias untuk satu baris tombol:

* `Tuple[str, str]`: pasangan (`label`, `callback_data`)
* `ButtonRow`: list dari beberapa tombol dalam satu baris

---

## 🔧 Fungsi

### `make_menu(rows: List[ButtonRow]) -> InlineKeyboardMarkup`

Membuat inline keyboard dengan bentuk bebas: 1 tombol per baris, 2 kolom, 3 kolom, dll.

| Parameter | Tipe                | Keterangan                                                         |
| --------- | ------------------- | ------------------------------------------------------------------ |
| `rows`    | `List[List[Tuple]]` | List dari baris tombol. Setiap baris berisi tuple label & callback |

**Return:** `InlineKeyboardMarkup`

---

## 📥 Struktur Input

```python
[
    [("Tombol A", "a")],                             # Baris 1, 1 kolom
    [("B", "b"), ("C", "c")],                        # Baris 2, 2 kolom
    [("D", "d"), ("E", "e"), ("F", "f")]             # Baris 3, 3 kolom
]
```

---

## 📤 Contoh Penggunaan

### ✅ 1. Menu Sederhana 1 kolom

```python
from telecore.telegram.menus import make_menu

menu = make_menu([
    [("🔍 Cek Status", "status")],
    [("📘 Edukasi Gratis", "edukasi")],
    [("❌ Keluar", "cancel")]
])
await update.message.reply_text("Pilih menu:", reply_markup=menu)
```

---

### ✅ 2. Menu 2 tombol per baris

```python
menu = make_menu([
    [("📘 Edukasi", "edukasi"), ("💰 Beli Solana", "ecer")],
    [("❓ Bantuan", "bantuan"), ("🔥 Join VIP", "vip")]
])
```

---

### ✅ 3. Menu dinamis dari database

```python
options = [("📚 Materi A", "materi_a"), ("📚 Materi B", "materi_b")]
menu = make_menu([options])  # 1 baris, 2 kolom

await update.callback_query.edit_message_text("Pilih materi:", reply_markup=menu)
```

---

## 🧪 Integrasi Umum di Handler

```python
from telegram.ext import CallbackQueryHandler
from telecore.telegram.menus import make_menu

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu = make_menu([
        [("✅ Konfirmasi", "confirm"), ("❌ Batal", "cancel")]
    ])
    await update.message.reply_text("Konfirmasi pilihan:", reply_markup=menu)

handler = CommandHandler("menu", menu_handler)
```

---

## 🎯 Kelebihan

* ✅ **Fleksibel:** Bisa 1, 2, atau 3 tombol per baris
* ✅ **Reusable:** Cocok digunakan untuk banyak jenis flow menu
* ✅ **Clean:** Tidak perlu repot manual pakai `InlineKeyboardButton` per baris

---

## 🛠️ Tips Tambahan

* `callback_data` harus pendek (max 64 byte), cocok untuk kode atau flag.
* Bisa digunakan untuk **navigasi antar halaman**, seperti: `("⏮️ Prev", "page_1")`, `("⏭️ Next", "page_3")`.

---

## 🔄 Perbandingan dengan Langsung Pakai InlineKeyboardMarkup

Tanpa `make_menu()`:

```python
InlineKeyboardMarkup([
    [InlineKeyboardButton("A", callback_data="a")],
    [InlineKeyboardButton("B", callback_data="b"), InlineKeyboardButton("C", callback_data="c")]
])
```

Dengan `make_menu()`:

```python
make_menu([
    [("A", "a")],
    [("B", "b"), ("C", "c")]
])
```

Lebih pendek, bersih, dan mudah dinamis!


