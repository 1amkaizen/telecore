
```
core_bot/
├── telegram/
│   ├── buttons.py        # Fungsi bikin tombol-tombol Telegram
│   ├── menus.py          # Fungsi generate menu (VIP, utama, dll)
│   └── utils.py          # Fungsi validasi, format, dll
├── supabase/
│   └── client.py         # Class koneksi + helper Supabase
├── midtrans/
│   ├── client.py         # Create payment QRIS, cek status
│   └── signature.py      # Fungsi hash signature callback
├── models/
│   ├── user.py           # Pydantic model user
│   └── transaction.py    # Pydantic model transaksi
```

