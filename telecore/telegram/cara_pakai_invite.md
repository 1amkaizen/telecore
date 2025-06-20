# 📘 Dokumentasi: `telecore.telegram.invite`

Modul ini digunakan untuk mengundang user Telegram ke **grup VIP** menggunakan metode `invite_chat_member`.
Nilai ID grup diambil secara dinamis dari environment variable `GROUP_VIP_ID`, sehingga **fleksibel dan reusable untuk banyak proyek.**

---

## 📂 Lokasi File

```
telecore/
└── telegram/
    └── invite.py
```

---

## 🧩 Fungsi

### 1. `get_group_vip_id() -> int`

Mengambil ID grup dari environment `GROUP_VIP_ID`, dan mengubahnya menjadi `int`.

#### ✅ Validasi:

* Jika tidak ditemukan atau tidak valid (bukan angka), akan melempar `ValueError`

#### 🔄 Contoh:

```python
group_id = get_group_vip_id()
```

---

### 2. `invite_user_to_group(bot: telegram.Bot, user_id: int)`

Mengundang user ke grup Telegram berdasarkan ID yang sudah dikonfigurasi.

| Parameter | Tipe           | Keterangan                              |
| --------- | -------------- | --------------------------------------- |
| `bot`     | `telegram.Bot` | Objek bot Telegram yang sedang berjalan |
| `user_id` | `int`          | Telegram user ID yang ingin diundang    |

#### 🚦 Behavior:

* Menggunakan `bot.invite_chat_member(chat_id, user_id)`
* Mencetak log jika berhasil atau gagal

#### 🔁 Return:

* Tidak mengembalikan nilai (`None`)
* Melempar `Exception` jika gagal mengundang

---

## 📝 Contoh Penggunaan

### ✅ Contoh di handler VIP setelah pembayaran:

```python
from telecore.telegram.invite import invite_user_to_group

# Misalnya setelah pembayaran berhasil
await invite_user_to_group(bot=context.bot, user_id=update.effective_user.id)
```

### ✅ Contoh di admin command manual:

```python
@admin_only
async def invite_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        target_id = int(context.args[0])
        await invite_user_to_group(bot=context.bot, user_id=target_id)
        await update.message.reply_text("✅ User berhasil diundang ke grup VIP.")
    except Exception as e:
        await update.message.reply_text(f"❌ Gagal mengundang user: {e}")
```

---

## 🔐 Konfigurasi Environment

Tambahkan ini di `.env` atau pada sistem environment kamu:

```env
GROUP_VIP_ID=-1001234567890
```

> Nilai harus berupa angka. Gunakan ID grup (bukan username link grup), dan pastikan bot sudah menjadi **admin** di grup tersebut.

---

## 🛡️ Error Handling

* Jika `GROUP_VIP_ID` tidak valid → raise `ValueError`
* Jika `bot.invite_chat_member` gagal (misalnya bot bukan admin, user sudah di grup, atau private) → raise `Exception`

---

## 🧪 Logging Otomatis

* ✅ **Jika sukses**:

  ```
  ✅ User 123456 berhasil diundang ke grup -1001234567890
  ```

* ❌ **Jika gagal**:

  ```
  ❌ Gagal invite user 123456 ke grup -1001234567890: [Error detail]
  ```

---

## 📎 Catatan Teknis

* Fungsi ini **tidak bisa invite user yang mengatur privasi tinggi** (misalnya tidak bisa ditambahkan langsung).
* Untuk memastikan invite berhasil, user harus **pernah mulai interaksi dengan bot** (via /start).


