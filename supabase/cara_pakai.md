# **cara pakai `SupabaseClient` versi fleksibel & modular** 

```
project_klien/
├── main.py
├── .env
└── requirements.txt

micin_core/
├── config.py
└── supabase/
    └── client.py
```

---

## ✅ 1. **Isi `.env` kamu di project:**

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-service-role-key
```

---

## ✅ 2. **Import & Gunakan di Project**

```python
from micin_core.supabase.client import SupabaseClient

supabase = SupabaseClient()
```

---

## 💡 **Opsi 1: Pakai fungsi default `upsert_vip_user()`**

```python
await supabase.upsert_vip_user(
    user_id=12345678,
    username="zen_dev",
    full_name="Zen Developer"
)
```

Field-nya otomatis:

```json
{
  "user_id": 12345678,
  "username": "zen_dev",
  "full_name": "Zen Developer",
  "is_vip": false,
  "vip_since": null,
  "created_at": "..."
}
```

---

## 💡 **Opsi 2: Pakai fungsi fleksibel `upsert()`**

```python
data = {
    "telegram_id": 12345678,
    "nama": "Zen",
    "status_pelanggan": "aktif",
    "tanggal_join": "2025-06-19"
}
await supabase.upsert("Pelanggan", data)
```

---

## 💡 **Opsi 3: Pakai `upsert_custom_user()`**

```python
user_data = {
    "user_id": 99999,
    "username": "botuser",
    "extra_info": "testing"
}
await supabase.upsert_custom_user(user_data)
```

---


## 📘 **Panduan Lengkap Pemakaian `SupabaseClient` (Core)**

### 🔧 Kelas: `SupabaseClient`

Dibuat untuk menyederhanakan interaksi dengan Supabase via REST API (`httpx`), tanpa perlu kamu mikirin header, error code, dll.

---

## 🔹 1. Fungsi: `upsert(table: str, data: dict)`

### ✅ Gunakan ini kalau:

* **Tabel dan kolomnya bebas**
* Project klien **punya struktur berbeda-beda**

### 📥 Parameter:

* `table`: nama tabel Supabase
* `data`: dictionary field dan value

### 🧠 **Syarat minimal Supabase-nya:**

* Tabel `table` sudah dibuat di Supabase
* Kolom sesuai dengan `data.keys()`
* Tidak wajib ada `primary key`, tapi **disarankan ada 1 kolom unique** (misal: `user_id`) biar `merge-duplicates` berfungsi

### 📌 Contoh Penggunaan:

```python
from micin_core.supabase.client import SupabaseClient

supabase = SupabaseClient()

data = {
    "telegram_id": 12345678,
    "nama": "Zen",
    "level": "basic",
    "join_date": "2025-06-19"
}

await supabase.upsert("Pengguna", data)
```

### 🧩 Contoh Struktur Tabel di Supabase:

| telegram\_id | nama | level | join\_date |
| ------------ | ---- | ----- | ---------- |
| 12345678     | Zen  | basic | 2025-06-19 |

> **Catatan:** pastikan kolom `telegram_id` ada di Supabase dengan constraint `unique`, kalau mau pakai `merge-duplicates`.

---

## 🔹 2. Fungsi: `upsert_vip_user(...)`

### ✅ Gunakan ini kalau:

* Kamu sedang membangun **bot VIP dengan skema standar Micin**
* Struktur tabel-nya tetap seperti default

### 🔧 Field yang dikirim:

```python
{
  "user_id": ...,          # int
  "username": ...,         # str
  "full_name": ...,        # str
  "is_vip": False,         # bool
  "vip_since": None,       # str (isoformat)
  "created_at": now        # str (isoformat)
}
```

### 📌 Contoh Penggunaan:

```python
await supabase.upsert_vip_user(
    user_id=987654,
    username="micin_trader",
    full_name="Trader Sukses"
)
```

### 🧩 Contoh Struktur Tabel Supabase:

| user\_id | username      | full\_name    | is\_vip | vip\_since | created\_at          |
| -------- | ------------- | ------------- | ------- | ---------- | -------------------- |
| 987654   | micin\_trader | Trader Sukses | false   | NULL       | 2025-06-19T03:22:00Z |

> ❗ Pastikan kamu sudah buat kolom-kolom di atas di tabel `Users`.

---

## 💡 **Tips Implementasi:**

* Buat dokumentasi internal (atau README di `micin_core`) tentang:

  * Struktur tabel yang disarankan
  * Contoh `data` per tabel
* Kalau field dynamic, kamu bisa tambah validasi `pydantic` untuk cek schema sebelum dikirim (opsional)

---

## 📌 Kesimpulan

| Fungsi              | Untuk siapa     | Fleksibel? | Perlu struktur tetap? |
| ------------------- | --------------- | ---------- | --------------------- |
| `upsert()`          | Semua project   | ✅ Ya       | ❌ Tidak               |
| `upsert_vip_user()` | Bot VIP standar | ❌ Tidak    | ✅ Ya (`user_id`, dst) |

---


