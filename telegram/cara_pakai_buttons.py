## 🧪 Contoh Pakai di Project

```python
from core_bot.telegram.buttons import confirm_cancel_buttons

await update.message.reply_text(
    "Yakin ingin bayar sekarang?",
    reply_markup=confirm_cancel_buttons()
)
```

Atau tombol dinamis:

```python
from core_bot.telegram.buttons import multi_button

reply_markup = multi_button([
    [("Scalping", "signal_scalping"), ("Swing", "signal_swing")],
    [("🔙 Kembali", "back_to_main")]
])
```

---

## ✅ Keunggulan Pendekatan Ini

* **Fleksibel** → bisa buat tombol custom pakai `single_button()` dan `multi_button()`
* **Reusable** → cukup 1 import untuk semua bot
* **Rapi** → gak perlu define ulang tombol dasar tiap kali bikin bot

---
