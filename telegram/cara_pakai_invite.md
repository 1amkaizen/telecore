### Fitur:

* Mengambil `GROUP_VIP_ID` dari `.env` (via `core_bot.config`)
* Validasi env kosong atau tidak valid
* Fungsi async untuk mengundang user

### Contoh Penggunaan:

```python
from telegram import Bot
from core_bot.telegram.invite import invite_user_to_group

# Misal dalam webhook atau handler selesai pembayaran VIP
await invite_user_to_group(bot, user_id)
```

Jika `GROUP_VIP_ID` kosong atau bukan angka, akan raise `ValueError`.
Kamu bisa pakai ini untuk semua jenis skenario: setelah /start, setelah bayar, dll — cukup panggil `invite_user_to_group`.

Kalau sudah oke, kita bisa lanjut ke core berikutnya. Mau ke sinyal trading, atau ke bagian langganan?

