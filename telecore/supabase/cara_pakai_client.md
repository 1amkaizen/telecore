# 📘 Dokumentasi: `SupabaseClient`

Modul ini menyediakan class `SupabaseClient` untuk berinteraksi dengan database Supabase via REST API.
Dirancang agar **ringan, fleksibel, dan cocok untuk proyek bot Telegram berbasis Python**.

---

## 📂 Lokasi File

```
telecore/
└── supabase/
    └── client.py
```

---

## 🔧 Kebutuhan

Sebelum menggunakan class ini, pastikan variabel environment berikut telah diatur:

* `SUPABASE_URL` → URL project Supabase
* `SUPABASE_KEY` → API Key (service role disarankan)

---

## 🏗️ Kelas: `SupabaseClient`

### ➕ Inisialisasi

```python
client = SupabaseClient()
```

Secara otomatis akan:

* Membuat koneksi ke Supabase
* Menyimpan `base_url` dan `key`
* Siap digunakan untuk upsert data

---

## 📦 Fungsi dan Parameter

### 1. `upsert(table: str, data: dict) -> str`

Melakukan upsert (insert atau update jika duplikat) ke tabel Supabase.

| Parameter | Tipe   | Keterangan               |
| --------- | ------ | ------------------------ |
| `table`   | `str`  | Nama tabel di Supabase   |
| `data`    | `dict` | Data yang ingin disimpan |

**Return:**

* `"success"` → jika berhasil insert/update
* `"already_exists"` → jika data sudah ada (HTTP 409)
* Akan `raise Exception` jika error lainnya

**Contoh:**

```python
await client.upsert("Users", {
    "user_id": 123,
    "username": "zen",
    "full_name": "Zen Micin"
})
```

---

### 2. `upsert_vip_user(user_id: int, username: str, full_name: str) -> str`

Shortcut untuk menyimpan user baru dengan struktur khusus `is_vip`.

**Isi default:**

* `is_vip`: `False`
* `vip_since`: `None`
* `created_at`: waktu UTC sekarang

**Contoh:**

```python
await client.upsert_vip_user(123, "zen", "Zen Micin")
```

---

### 3. `upsert_custom_user(data: dict, table="Users") -> str`

Alternatif fleksibel untuk menyimpan user dengan struktur custom.

**Contoh:**

```python
await client.upsert_custom_user({
    "user_id": 123,
    "role": "admin",
    "last_login": "2025-06-20T09:00:00Z"
})
```

---

## 🖨️ Log Otomatis

Menggunakan `colorlog` untuk log detail:

| Event                 | Level    | Contoh Log                               |
| --------------------- | -------- | ---------------------------------------- |
| Data sudah ada (409)  | INFO     | `ℹ️ Data already exists in table Users.` |
| Error selain 409      | ERROR    | `❌ Error upsert to Users: ...`           |
| Gagal konek saat init | CRITICAL | `❌ Gagal menghubungkan ke Supabase: ...` |

---

## 🛡️ Error Handling

* Melempar `Exception` jika status kode bukan 200/201/409
* Bisa langsung `try/except` di pemanggil luar

```python
try:
    await client.upsert("Users", {...})
except Exception as e:
    logger.error(f"Gagal simpan: {e}")
```

---

## 🧩 Cocok Digunakan Untuk

* Handler `/start` untuk menyimpan user
* Bot VIP langganan
* Admin panel untuk update status user
* General-purpose bot yang pakai Supabase REST API

---

## 🧪 Contoh Implementasi

```python
from telecore.supabase.client import SupabaseClient

client = SupabaseClient()

await client.upsert("Users", {
    "user_id": 123456789,
    "username": "zen",
    "full_name": "Zen Micin"
})
```


