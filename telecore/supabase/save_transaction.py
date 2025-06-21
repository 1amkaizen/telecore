# telecore/supabase/save_transaction.py

from telecore.supabase.client import SupabaseClient
from datetime import datetime
from telecore.logging.logger import get_logger

logger = get_logger("telecore.supabase.save_transaction")

supabase = SupabaseClient().client


async def save_transaction(data: dict, *, table: str = "Transactions") -> None:
    """
    Simpan transaksi ke Supabase.

    Args:
        data (dict): Data transaksi dari Midtrans.
        table (str): Nama tabel. Default: "Transactions".
    """

    if "order_id" not in data or "user_id" not in data:
        raise ValueError("order_id dan user_id wajib diisi")

    data.setdefault("created_at", datetime.utcnow().isoformat())

    try:
        supabase.table(table).insert(data).execute()

        logger.info(
            f"📝 Transaksi {data['order_id']} disimpan ke tabel {table} | "
            f"user_id={data['user_id']}, username={data.get('username', '-')}, "
            f"gross_amount={data.get('gross_amount', '-')}"
        )

    except Exception:
        logger.exception(f"❌ Gagal simpan transaksi ke {table}")
        raise

