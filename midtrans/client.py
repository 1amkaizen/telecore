# core_bot/midtrans/client.py

import httpx
import logging
import uuid
from typing import Optional

from core_bot.config import IS_MIDTRANS_SANDBOX

self.api_base = "https://app.sandbox.midtrans.com" if IS_MIDTRANS_SANDBOX else "https://app.midtrans.com"

logger = logging.getLogger(__name__)


class MidtransClient:
    
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

    def generate_order_id(self, prefix: str = "TX") -> str:
        return f"{prefix}-{uuid.uuid4().hex[:10].upper()}"

    def verify_signature_key(self, order_id: str, status_code: str, gross_amount: str, signature_key: str) -> bool:
        import hashlib
        raw = f"{order_id}{status_code}{gross_amount}{self.server_key}"
        calculated = hashlib.sha512(raw.encode()).hexdigest()
        return calculated == signature_key

