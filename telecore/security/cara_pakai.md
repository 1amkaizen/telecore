# 📘 Dokumentasi: `telecore.security.admin`

Modul ini menyediakan fungsi untuk:

* Mengambil daftar admin dari environment (`ADMIN_ID`)
* Mengecek apakah `user_id` tertentu adalah admin

---

## 📂 Lokasi File

```
telecore/
└── security/
    └── admin.py
```

---

## 🧩 Dependensi

* `telecore.config.ADMIN_ID` harus tersedia, berupa string ID admin yang dipisahkan koma (`,`), misalnya:

```env
ADMIN_ID=12345678,98765432
```

---

## 🧠 Fungsi Utama

### 🔐 `get_admin_ids() -> list[int]`

Mengambil dan memvalidasi daftar admin dari `.env` (melalui `telecore.config.ADMIN_ID`).

#### Detail:

* Mengabaikan entri kosong atau non-digit
* Mengonversi string ke `int`
* Logging jika ada nilai yang tidak valid

#### Contoh:

```python
from telecore.security.admin import get_admin_ids

admin_ids = get_admin_ids()
print(admin_ids)  # Output: [12345678, 98765432]
```

---

### ✅ `is_admin(user_id: int) -> bool`

Cek apakah user dengan `user_id` tertentu termasuk dalam daftar admin.

#### Contoh:

```python
from telecore.security.admin import is_admin

if is_admin(update.effective_user.id):
    await update.message.reply_text("Kamu admin.")
else:
    await update.message.reply_text("Akses ditolak.")
```

---

## ✅ Contoh Implementasi di Bot Telegram

### Handler `/admin` untuk akses admin saja:

```python
from telegram import Update
from telegram.ext import ContextTypes
from telecore.security.admin import is_admin

async def admin_only_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if not is_admin(user_id):
        await update.message.reply_text("❌ Akses ditolak. Hanya admin yang boleh.")
        return

    await update.message.reply_text("✅ Selamat datang, Admin.")
```

---

## 🛑 Handling Error dan Validasi

* Jika `ADMIN_ID` tidak diatur → log warning.
* Jika isi `ADMIN_ID` tidak valid (misalnya huruf) → log per item.
* Jika `user_id` tidak dalam daftar → return `False`.

---

## 🔄 Kelebihan Desain

| Fitur                    | Keterangan                                    |
| ------------------------ | --------------------------------------------- |
| 🔄 **Reusable**          | Bisa digunakan di seluruh modul bot           |
| ⚙️ **Berdasarkan ENV**   | Tidak hardcoded, mudah diubah tanpa edit kode |
| 🔒 **Aman**              | Tidak expose info sensitif                    |
| 🧼 **Validasi internal** | Otomatis skip nilai yang tidak valid          |

---

## 📥 Tips .env untuk Multi-Admin

```env
ADMIN_ID=123456789,987654321,456789123
```

Akan dibaca sebagai:

```python
[123456789, 987654321, 456789123]
```

