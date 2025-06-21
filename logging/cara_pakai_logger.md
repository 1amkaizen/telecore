# 📘 Dokumentasi: `telecore.logging.logger`

Modul ini menyediakan logger siap pakai dengan **warna di terminal (colorlog)** untuk setiap modul kamu.
Logger ini cocok untuk debugging, monitoring event Telegram, API, Supabase, dan sebagainya.

---

## ✨ Fitur

* Warna otomatis sesuai level log (INFO = hijau, ERROR = merah, dll)
* Konsisten di semua file/module
* Tidak perlu inisialisasi global
* Tidak duplikatif (safe untuk import berulang)
* Tidak mengganggu log bawaan library lain (`httpx`, `telegram`, dll)

---

## 📂 Lokasi File

```
telecore/
└── logging/
    └── logger.py
```

---

## 📦 API

### `get_logger(name: str, level=logging.INFO) -> logging.Logger`

Membuat logger modular berwarna untuk file tertentu.

| Parameter | Tipe  | Keterangan                                   |
| --------: | ----- | -------------------------------------------- |
|    `name` | `str` | Nama unik untuk logger (biasanya path modul) |
|   `level` | `int` | Level log (default `logging.INFO`)           |

---

## 🔧 Contoh Penggunaan

### 1. Import `get_logger` di file Python-mu:

```python
from telecore.logging.logger import get_logger

logger = get_logger("telecore.supabase.save_user")
```

### 2. Gunakan seperti biasa:

```python
logger.info("User berhasil disimpan.")
logger.warning("Token hampir kadaluarsa.")
logger.error("Gagal memuat data dari Supabase.")
```

---

## 🎨 Output di Terminal

```bash
2025-06-20 09:00:00 [INFO] telecore.supabase.save_user: User berhasil disimpan.
2025-06-20 09:00:01 [WARNING] telecore.supabase.save_user: Token hampir kadaluarsa.
2025-06-20 09:00:02 [ERROR] telecore.supabase.save_user: Gagal memuat data dari Supabase.
```

> Warna tergantung level log: INFO = hijau, WARNING = kuning, ERROR = merah

---

## 🛠️ Tips

* Untuk nama logger, gunakan nama file/module:

  ```python
  get_logger(__name__)
  ```

  atau spesifik:

  ```python
  get_logger("handlers.user.start")
  ```

* Hindari membuat logger baru dalam loop (cukup satu kali per file).

* Tidak perlu inisialisasi `setup_global_logger()` jika hanya butuh warna di logger milikmu.

---

## 🚫 Yang Tidak Dilakukan oleh `get_logger()`

* **Tidak memodifikasi logger bawaan library lain** (`httpx`, `telegram`, dsb)
* **Tidak log ke file** (hanya ke console)
* **Tidak membuat konfigurasi global** (hanya lokal per modul)

---

## 🧩 Contoh Implementasi Nyata

```python
# handlers/users/start.py

from telecore.logging.logger import get_logger
logger = get_logger("handlers.users.start")

async def start(update, context):
    logger.info("User menjalankan /start")
```

