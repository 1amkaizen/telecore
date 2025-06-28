# telecore/midtrans/client.py


import httpx
import logging
import uuid
import hashlib
from typing import Optional
from telegram import User
from telecore.config import MIDTRANS_SERVER_KEY, MIDTRANS_IS_SANDBOX

logger = logging.getLogger(__name__)


class MidtransClient:
    def __init__(self):
        self.server_key = MIDTRANS_SERVER_KEY
        self.auth = (self.server_key, "")
        self.api_base = "https://app.sandbox.midtrans.com" if MIDTRANS_IS_SANDBOX else "https://app.midtrans.com"

    async def create_qris_payment(self, order_id: str, amount: int, customer: dict) -> dict:
        url = f"{self.api_base}/snap/v1/transactions"
        headers = {"Content-Type": "application/json"}
        payload = {
            "transaction_details": {
                "order_id": order_id,
                "gross_amount": amount
            },
            "payment_type": "qris",
            "qris": {},
            "customer_details": customer
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(url, auth=self.auth, headers=headers, json=payload)

        if response.status_code != 201:
            logger.error(f"Midtrans QRIS error: {response.text}")
            raise Exception("Gagal membuat pembayaran QRIS")

        return response.json()

    async def create_va_payment(self, order_id: str, amount: int, bank: str, customer: dict) -> dict:
        url = f"{self.api_base}/v2/charge"
        headers = {"Content-Type": "application/json"}
        payload = {
            "payment_type": "bank_transfer",
            "transaction_details": {
                "order_id": order_id,
                "gross_amount": amount
            },
            "bank_transfer": {
                "bank": bank
            },
            "customer_details": customer
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(url, auth=self.auth, headers=headers, json=payload)

        if response.status_code != 201:
            logger.error(f"Midtrans VA error: {response.text}")
            raise Exception("Gagal membuat pembayaran Virtual Account")

        return response.json()

    @staticmethod
    def generate_order_id(prefix: str = "TX") -> str:
        return f"{prefix}-{uuid.uuid4().hex[:10].upper()}"

    @staticmethod
    def get_customer_from_user(user: User) -> dict:
        return {
            "first_name": user.full_name,
            "email": f"{user.username or user.id}@example.com"
        }

    def verify_signature_key(self, order_id: str, status_code: str, gross_amount: str, signature_key: str) -> bool:
        raw = f"{order_id}{status_code}{gross_amount}{self.server_key}"
        calculated = hashlib.sha512(raw.encode()).hexdigest()
        return calculated == signature_key
    async def create_snap_payment(
        self, order_id: str, amount: int, customer: dict, enabled_payments: Optional[list] = None) -> dict:
        url = f"{self.api_base}/snap/v1/transactions"
        headers = {"Content-Type": "application/json"}
        payload = {
            "transaction_details": {
                "order_id": order_id,
                "gross_amount": amount
            },
            "customer_details": customer,
        }
        if enabled_payments:
            payload["enabled_payments"] = enabled_payments

        async with httpx.AsyncClient() as client:
            response = await client.post(url, auth=self.auth, headers=headers, json=payload)

        if response.status_code != 201:
            logger.error(f"Midtrans Snap error: {response.text}")
            raise Exception("Gagal membuat pembayaran Snap")

        data = response.json()
        return {
            "redirect_url": data.get("redirect_url"),
            "token": data.get("token"),
            "midtrans_response": data  # ← tambahan ini
        }

