# telecore/supabase/save_user.py

import logging
from telecore.supabase.client import SupabaseClient

from telecore.logging.logger import get_logger

logger = get_logger("telecore.supabase.save_user")

supabase_client = SupabaseClient()

async def save_user_to_db(user_id: int, username: str, full_name: str) -> str:
    try:
        sanitized_data = {
            "user_id": user_id,
            "username": username or "",
            "full_name": full_name or "",
        }
        logger.info("\n📝 [SAVE USER TO DB]\n"
                    f"  - user_id   : {user_id}\n"
                    f"  - username  : @{username or '-'}\n"
                    f"  - full_name : {full_name or '-'}")

        result = await supabase_client.upsert("Users", sanitized_data)
        return result

    except Exception as e:
        logger.exception(f"❌ Gagal menyimpan user ke Supabase:\n{e}")
        raise
