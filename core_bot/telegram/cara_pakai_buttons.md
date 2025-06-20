# 📘 Dokumentasi: `core_bot.telegram.buttons`

Modul ini menyediakan berbagai **template tombol (`InlineKeyboardMarkup`)** siap pakai untuk bot Telegram berbasis `python-telegram-bot`.

Dirancang agar modular, fleksibel, dan bisa digunakan ulang di berbagai proyek bot.

---

## 📂 Lokasi File

```
core_bot/
└── telegram/
    └── buttons.py
```

---

## 📦 Fungsi & API

### 1. `back_to_main_menu_button()`

Tombol kembali ke menu utama.

```python
back_to_main_menu_button()
```

💬 Output:

```
🔙 Kembali ke Menu Utama
(callback_data="back_to_main")
```

---

### 2. `join_vip_button()`

Tombol untuk ajakan Join VIP (lifetime).

```python
join_vip_button()
```

💬 Output:

```
🔥 Join VIP Lifetime
(callback_data="join_vip")
```

---

### 3. `confirm_cancel_buttons(confirm_cb="confirm", cancel_cb="cancel")`

Tombol dua opsi: ✅ Konfirmasi dan ❌ Batal.
Callback bisa dikustomisasi.

```python
confirm_cancel_buttons()
confirm_cancel_buttons(confirm_cb="yes", cancel_cb="no")
```

💬 Output:

```
✅ Konfirmasi  ❌ Batal
(callback_data: "confirm" & "cancel")
```

---

### 4. `refresh_button()`

Tombol untuk mengecek status, biasanya digunakan setelah pembayaran atau permintaan status.

```python
refresh_button()
```

💬 Output:

```
🔄 Cek Status
(callback_data="refresh_status")
```

---

### 5. `contact_admin_button()`

Tombol hubungi admin.

```python
contact_admin_button()
```

💬 Output:

```
📞 Kontak Admin
(callback_data="contact_admin")
```

---

### 6. `single_button(label: str, callback_data: str)`

Buat tombol tunggal dengan label dan callback custom.

```python
single_button("🔔 Notifikasi", "notif")
```

💬 Output:

```
🔔 Notifikasi
(callback_data="notif")
```

---

### 7. `multi_button(rows: list[list[tuple[str, str]]])`

Buat keyboard dari struktur nested list:

```python
multi_button([
    [("Option A", "a"), ("Option B", "b")],
    [("Cancel", "cancel")]
])
```

💬 Output:

```
Option A | Option B
Cancel
```

---

## 🎯 Contoh Penggunaan di Handler

```python
from core_bot.telegram.buttons import confirm_cancel_buttons

await update.message.reply_text(
    "Apakah kamu yakin ingin melanjutkan?",
    reply_markup=confirm_cancel_buttons("ya", "tidak")
)
```

---

## ♻️ Cocok Untuk:

* Bot edukasi, pembayaran, manajemen VIP
* Konfirmasi pembelian, akses sinyal, dan navigasi menu
* Kebutuhan kustom keyboard berbasis `callback_data`

---

## 🛠️ Tips Tambahan

* Callback yang kamu berikan akan dikirim ke handler `CallbackQueryHandler`
* Kombinasikan dengan `ConversationHandler` untuk flow interaktif
* Bisa digunakan juga di channel post (melalui `send_message(..., reply_markup=...)`)


