# telecore/settings/config_db.py

import logging
from telecore.supabase.client import SupabaseClient

logger = logging.getLogger(__name__)
supabase = SupabaseClient().client  # ⬅️ Tambahkan baris ini

def get_vip_price() -> int:
    try:
        result = supabase.table("Settings") \
                         .select("value") \
                         .eq("key", "vip_price") \
                         .execute()

        if result.data and len(result.data) > 0:
            return int(result.data[0]["value"])
        else:
            raise RuntimeError("vip_price tidak ditemukan di tabel Settings")

    except Exception as e:
        logger.exception(f"❌ Gagal ambil vip_price dari Supabase")
        raise RuntimeError(f"Gagal mengambil vip_price: {e}")

