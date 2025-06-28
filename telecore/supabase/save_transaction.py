# telecore/supabase/save_transaction.py


from datetime import datetime
from telecore.logging.logger import get_logger
from telecore.supabase.client import SupabaseClient

logger = get_logger("telecore.supabase.save_transaction")


def save_transaction(
    data: dict,
    *,
    table: str = "Transactions",
    client=None,
    raise_on_fail: bool = False,
) -> bool:
    """
    Menyimpan data transaksi ke Supabase (SYNC) dengan logging.
    Gunakan dengan run_in_executor() jika dipanggil dari kode async.
    """
    if "order_id" not in data or "user_id" not in data:
        raise ValueError("order_id dan user_id wajib diisi")

    data.setdefault("created_at", datetime.utcnow().isoformat())
    client = client or SupabaseClient().client

    try:
        response = client.table(table).insert(data).execute()
        if response.data:
            logger.info(
                f"📝 Transaksi {data['order_id']} disimpan ke tabel {table} | "
                f"user_id={data['user_id']}, username={data.get('username', '-')}, "
                f"gross_amount={data.get('gross_amount', '-')}"
            )
            return True
        else:
            logger.error(f"❌ Insert Supabase gagal tanpa exception: {response}")
            return False
    except Exception as e:
        logger.exception(f"❌ Gagal simpan transaksi ke {table}: {e}")
        if raise_on_fail:
            raise
        return False

