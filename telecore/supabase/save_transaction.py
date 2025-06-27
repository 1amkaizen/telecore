# telecore/supabase/save_transaction.py

from telecore.supabase.client import SupabaseClient
from datetime import datetime
from telecore.logging.logger import get_logger

logger = get_logger("telecore.supabase.save_transaction")

def save_transaction(
    data: dict,
    *,
    table: str = "Transactions",
    client=None,
    raise_on_fail: bool = False,
) -> bool:
    """
    Menyimpan data transaksi ke Supabase dengan logging.
    """
    if "order_id" not in data or "user_id" not in data:
        raise ValueError("order_id dan user_id wajib diisi")

    data.setdefault("created_at", datetime.utcnow().isoformat())

    client = client or SupabaseClient().client

    try:
        response = client.table(table).insert(data).execute()
        if hasattr(response, "status_code") and response.status_code not in [200, 201]:
            raise Exception(f"Kode status bukan 200/201: {response.status_code}")

        logger.info(
            f"📝 Transaksi {data['order_id']} disimpan ke tabel {table} | "
            f"user_id={data['user_id']}, username={data.get('username', '-')}, "
            f"gross_amount={data.get('gross_amount', '-')}"
        )
        return True

    except Exception as e:
        logger.exception(f"❌ Gagal simpan transaksi ke {table}: {e}")
        if raise_on_fail:
            raise
        return False

