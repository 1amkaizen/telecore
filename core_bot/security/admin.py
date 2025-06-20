# core_bot/security/admin.py

import logging
from core_bot.config import ADMIN_ID  # Ambil dari config.py

logger = logging.getLogger(__name__)

def get_admin_ids() -> list[int]:
    """Ambil daftar admin ID dari config"""
    if not ADMIN_ID:
        logger.warning("⚠️ Config ADMIN_ID kosong.")
        return []

    admin_ids = []
    for uid in ADMIN_ID.split(","):
        uid = uid.strip()
        if uid.isdigit():
            admin_ids.append(int(uid))
        else:
            logger.warning(f"⚠️ ADMIN_ID tidak valid: {uid}")
    return admin_ids


def is_admin(user_id: int) -> bool:
    return user_id in get_admin_ids()

