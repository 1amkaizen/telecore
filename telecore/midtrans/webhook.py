# telecore/midtrans/webhook.py

from fastapi import Request
from telecore.midtrans.client import MidtransClient
from telecore.config import MIDTRANS_SERVER_KEY
import logging

logger = logging.getLogger(__name__)
#midtrans = MidtransClient(server_key=MIDTRANS_SERVER_KEY)
midtrans = MidtransClient()


async def handle_midtrans_webhook(
    request: Request,
    supabase_client,
    transactions_table: str,
    prefix_handler_map: dict
):
    body = await request.json()
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
        # dll
    }).eq("order_id", order_id).execute()

    # Jalankan handler berdasarkan prefix
    handler = prefix_handler_map.get(prefix)
    if handler and body.get("transaction_status") == "settlement":
        await handler(body, transaction)

    return {"message": "OK"}

