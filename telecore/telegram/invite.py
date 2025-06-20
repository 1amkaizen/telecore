# telecore/telegram/invite.py

import os
import logging
from telegram import Bot
from telecore.config import GROUP_VIP_ID

logger = logging.getLogger(__name__)


def get_group_vip_id() -> int:
    try:
        group_id = int(GROUP_VIP_ID)
        return group_id
    except (TypeError, ValueError):
        raise ValueError("❌ GROUP_VIP_ID tidak valid atau belum diatur di .env")


async def invite_user_to_group(bot: Bot, user_id: int):
    """
    Invite user ke grup VIP berdasarkan GROUP_VIP_ID dari env
    """
    group_id = get_group_vip_id()

    try:
        await bot.invite_chat_member(chat_id=group_id, user_id=user_id)
        logger.info(f"✅ User {user_id} berhasil diundang ke grup {group_id}")
    except Exception as e:
        logger.error(f"❌ Gagal invite user {user_id} ke grup {group_id}: {e}")
        raise

