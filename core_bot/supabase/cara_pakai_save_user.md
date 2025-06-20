# 📘 Dokumentasi: `save_user_to_db()`

Fungsi ini digunakan untuk menyimpan data user Telegram ke tabel `Users` di Supabase.
Disiapkan sebagai bagian dari modul `core_bot`, sehingga bisa digunakan ulang oleh berbagai proyek bot.

---

## 📦 Lokasi File

```
core_bot/
└── supabase/
    └── save_user.py
```

---

## 🔧 Fungsi

### `save_user_to_db(user_id: int, username: str, full_name: str) -> str`

### ✅ Tujuan:

Melakukan **upsert (insert/update)** data user ke tabel `Users` di Supabase.
Fungsi ini akan membuat log detail saat proses berlangsung, dan menghindari error karena `None`.

---

### 📥 Parameter

| Nama        | Tipe  | Keterangan                                              |
| ----------- | ----- | ------------------------------------------------------- |
| `user_id`   | `int` | ID user Telegram                                        |
| `username`  | `str` | Username Telegram (boleh kosong/None)                   |
| `full_name` | `str` | Nama lengkap gabungan dari `first_name` dan `last_name` |

---

### 📤 Return

| Tipe  | Isi                                                                                |
| ----- | ---------------------------------------------------------------------------------- |
| `str` | `"inserted"` / `"updated"` / `"already_exists"` (tergantung implementasi `upsert`) |

> Hasil disesuaikan dengan implementasi `SupabaseClient.upsert()`.

---

### ⚠️ Error Handling

* Jika terjadi error saat menyimpan, fungsi akan:

  * Log detail error menggunakan `logger.exception`
  * Melempar kembali exception agar bisa ditangani oleh handler pemanggil

---

### 📦 Contoh Penggunaan

```python
from core_bot.supabase.save_user import save_user_to_db

# Contoh di dalam handler Telegram
await save_user_to_db(
    user_id=update.effective_user.id,
    username=update.effective_user.username,
    full_name=f"{update.effective_user.first_name or ''} {update.effective_user.last_name or ''}".strip()
)
```

---

## 📝 Contoh Log

```bash
📝 [SAVE USER TO DB]
  - user_id   : 2116777065
  - username  : @iamkaizen
  - full_name : 1amKaiz3n
```

Jika gagal:

```bash
❌ Gagal menyimpan user ke Supabase:
Traceback (most recent call last):
...
```

---

## 🔐 Tabel Supabase

Pastikan kamu sudah punya tabel `Users` di Supabase dengan kolom:

* `user_id` (integer, primary key)
* `username` (text, nullable)
* `full_name` (text, nullable)

---

## ♻️ Reusabilitas

Fungsi ini bisa digunakan di:

* Handler `/start`
* Handler admin (cek user, VIP, dll)
* Fitur referral atau laporan
* Proyek bot lain (dengan `core_bot` sebagai dependensi)


