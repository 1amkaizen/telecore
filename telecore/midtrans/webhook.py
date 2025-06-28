# telecore/midtrans/webhook.py

from django.http import HttpRequest
import json
import logging
from telecore.midtrans.client import MidtransClient
from telecore.config import MIDTRANS_SERVER_KEY

logger = logging.getLogger(__name__)
midtrans = MidtransClient()

async def handle_midtrans_webhook(
    request: HttpRequest,
    supabase_client,
    transactions_table: str,
    prefix_handler_map: dict
):
    try:
        body = json.loads(request.body)
    except Exception as e:
        logger.exception("❌ Gagal parsing body webhook")
        return {"message": "Invalid JSON"}

    order_id = body.get("order_id")
    if not order_id:
        return {"message": "order_id kosong"}

    prefix = order_id.split("-")[0]  # misalnya "VIP", "SUB", dsb

    # Ambil transaksi
    trx = supabase_client.table(transactions_table).select("*").eq("order_id", order_id).execute()
    transaction = trx.data[0] if trx.data else None

    if not transaction:
        return {"message": "Transaksi tidak ditemukan"}

    # Update transaksi
    supabase_client.table(transactions_table).update({
        "transaction_status": body.get("transaction_status"),
        "gross_amount": body.get("gross_amount"),
        "payment_type": body.get("payment_type"),
        "transaction_id": body.get("transaction_id"),
        "currency": body.get("currency"),
        "transaction_time": body.get("transaction_time"),
        "status_message": body.get("status_message"),
        "fraud_status": body.get("fraud_status"),
        "signature_key": body.get("signature_key"),
        "merchant_id": body.get("merchant_id"),
    }).eq("order_id", order_id).execute()

    # Jalankan handler jika status settlement
    handler = prefix_handler_map.get(prefix)
    if handler and body.get("transaction_status") == "settlement":
        await handler(body, transaction)

    return {"message": "OK"}

