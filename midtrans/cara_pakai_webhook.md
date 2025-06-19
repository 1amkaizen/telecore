## 📄 Dokumentasi `handle_midtrans_webhook`

### 📌 Tujuan

Fungsi fleksibel untuk menangani **webhook Midtrans** dari berbagai jenis transaksi (`VIP`, `ECER`, `SUB`, dll) dalam satu endpoint saja.

---

### ⚙️ Parameter Fungsi

```python
async def handle_midtrans_webhook(
    request: Request,
    supabase_client,               # Instance SupabaseClient
    transactions_table: str,       # Nama tabel transaksi di Supabase
    prefix_handler_map: dict       # Mapping prefix → fungsi callback async
)
```

---

### ✅ Alur Kerja

1. Menerima webhook dari Midtrans (format JSON)
2. Ambil `order_id` → ambil prefix-nya (misal: `VIP-xxxx`)
3. Ambil data transaksi dari tabel Supabase
4. Update transaksi dari Midtrans (`status`, `gross_amount`, dll)
5. Jalankan handler async sesuai prefix (jika status = `settlement`)

---

## 🧪 Contoh Implementasi di Project

### 🔹 `project_klien/routes/webhook_midtrans.py`

```python
from fastapi import APIRouter, Request
from core_bot.midtrans.webhook import handle_midtrans_webhook
from core_bot.supabase.client import SupabaseClient
from core_bot.config import SUPABASE_URL, SUPABASE_KEY

router = APIRouter()
supabase = SupabaseClient(SUPABASE_URL, SUPABASE_KEY)

# Definisikan handler prefix
async def handle_vip(body: dict, transaction: dict):
    user_id = transaction["user_id"]
    vip_since = body.get("settlement_time")
    await supabase.table("Users").update({
        "is_vip": True,
        "vip_since": vip_since
    }).eq("user_id", user_id).execute()
    print(f"✅ User {user_id} di-mark VIP.")

async def handle_ecer(body: dict, transaction: dict):
    user_id = transaction["user_id"]
    gross = body.get("gross_amount")
    print(f"💰 User {user_id} beli Solana eceran: Rp {gross}")

# Mapping prefix ke fungsi
prefix_handlers = {
    "VIP": handle_vip,
    "ECER": handle_ecer,
}

@router.post("/midtrans")
async def midtrans_webhook(request: Request):
    return await handle_midtrans_webhook(
        request=request,
        supabase_client=supabase,
        transactions_table="Transactions",
        prefix_handler_map=prefix_handlers
    )
```

---

### 📁 Struktur Direktori Minimal

```
project_klien/
├── routes/
│   └── webhook_midtrans.py  ✅
├── main.py                  ✅ mount router
```

---

## 📦 Kelebihan Pendekatan Ini

| Fitur                               | Ada? |
| ----------------------------------- | ---- |
| Hanya satu endpoint webhook         | ✅    |
| Bisa handle banyak tipe order       | ✅    |
| Tidak terikat ke `VIP`, `ECER` saja | ✅    |
| Handler per prefix modular & rapi   | ✅    |
| Bisa digunakan ulang di proyek lain | ✅    |

---

## 🧠 Penjelasan Maksud Kalimat :

> “Kalau kamu butuh juga template `handle_subscription`, atau `produk`, tinggal tambahkan saja di `prefix_handler_map`.”

Artinya:

* Misalkan kamu bikin `order_id` seperti `SUB-xxxxx` untuk langganan bulanan
* Atau `PROD-xxxxx` untuk jual produk digital
* Maka kamu cukup:

  * Buat **fungsi async baru** untuk handle `SUB` / `PROD`
  * Tambahkan ke `prefix_handler_map`

Jadi **cukup di sisi project klien-nya**, bukan di core. Contoh:

```python
async def handle_subscription(body: dict, trx: dict):
    # Hitung tanggal kadaluarsa, update langganan, dll
    ...
```

---

## 🔁 Kalau Jenis Langganan Berbeda (bulanan/tahunan/mingguan), Apakah Perlu Ubah Kode?

### ❌ Tidak perlu ubah core

### ✅ Kamu cukup kirim metadata di saat create payment (misal `subscription_type`)

Lalu di `handler_subscription()` kamu cek jenisnya:

```python
sub_type = trx.get("subscription_type")  # dari transaksi
if sub_type == "monthly":
    expired_at = today + timedelta(days=30)
elif sub_type == "weekly":
    expired_at = today + timedelta(days=7)
...
```

Jadi fleksibel — kamu kontrol penuh dari project klien/template.

---

## ✅ Kesimpulan

| Hal                                     | Dikerjakan di…          | Keterangan                              |
| --------------------------------------- | ----------------------- | --------------------------------------- |
| Webhook handler subscription            | **Project klien**       | Tambah fungsi `handle_subscription()`   |
| Logika expired/langganan (minggu/bulan) | **Project klien**       | Gunakan data dari transaksi             |
| Fungsi umum Midtrans                    | **Sudah di `core_bot`** | Tidak perlu diubah                      |
| Core perlu diubah?                      | ❌ Tidak                 | Kamu hanya pakai fungsi generiknya saja |

---

