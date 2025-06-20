# 📘 Dokumentasi Pemakaian `MidtransClient`

## 🔧 Inisialisasi

```python
from telecore.config import MIDTRANS_SERVER_KEY
from telecore.midtrans.client import MidtransClient

midtrans = MidtransClient(server_key=MIDTRANS_SERVER_KEY)
```

> ⚙️ Sandbox/production otomatis berdasarkan `.env`:

```env
MIDTRANS_IS_SANDBOX=true  # → true untuk testing, false untuk production
```

---

## 1. 🔑 `generate_order_id(prefix: str = "TX") -> str`

Generate ID unik untuk transaksi:

```python
order_id = midtrans.generate_order_id("VIP")
# Contoh hasil: VIP-FEBA912C8A
```

---

## 2. 📱 `create_qris_payment(order_id: str, amount: int, customer: dict) -> dict`

Membuat pembayaran via **QRIS**:

```python
order_id = midtrans.generate_order_id("VIP")
customer = {
    "first_name": "Zen",
    "email": "zen@example.com",
    "phone": "081234567890"
}

payment = await midtrans.create_qris_payment(
    order_id=order_id,
    amount=50000,
    customer=customer
)
```

**Response JSON berisi:**

* `transaction_token`
* `redirect_url` (Snap)
* `actions` → berisi URL QR (untuk di-scan)

---

## 3. 🏦 `create_va_payment(order_id: str, amount: int, bank: str, customer: dict) -> dict`

Membuat pembayaran via **Virtual Account**:

```python
order_id = midtrans.generate_order_id("ECER")
customer = {
    "first_name": "Zen",
    "email": "zen@example.com",
    "phone": "081234567890"
}

va_payment = await midtrans.create_va_payment(
    order_id=order_id,
    amount=100000,
    bank="bca",  # Pilihan: bca, bni, bri, permata, dll
    customer=customer
)
```

**Response JSON berisi:**

* `va_number`
* `bank`
* `transaction_id`, `redirect_url`, dll

---

## 4. 🔐 `verify_signature_key(order_id: str, status_code: str, gross_amount: str, signature_key: str) -> bool`

Digunakan untuk **verifikasi signature dari webhook Midtrans**:

```python
is_valid = midtrans.verify_signature_key(
    order_id="VIP-XXXX123",
    status_code="200",
    gross_amount="50000",
    signature_key="dikirim_oleh_midtrans"
)

if not is_valid:
    raise Exception("❌ Signature tidak valid")
```

---

## ✅ Dependensi Lingkungan

Tambahkan ke `.env`:

```env
MIDTRANS_SERVER_KEY=your_server_key
MIDTRANS_IS_SANDBOX=true
```

---

## 📂 Struktur Terkait

```
telecore/
├── config.py                # Env config loader
└── midtrans/
    └── client.py           # MidtransClient class
```

---


