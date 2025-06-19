# core_bot/supabase/client.py

import httpx
import logging
from datetime import datetime
from supabase import create_client, Client
from micin_core.config import SUPABASE_URL, SUPABASE_KEY

logger = logging.getLogger(__name__)


class SupabaseClient:
    def __init__(self):
        try:
            self.client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
            self.base_url = SUPABASE_URL
            self.key = SUPABASE_KEY
        except Exception as e:
            raise RuntimeError(f"❌ Gagal menghubungkan ke Supabase: {e}")

    async def upsert(self, table: str, data: dict) -> str:
        """Fungsi umum untuk upsert ke tabel mana pun"""
        headers = {
            "apikey": self.key,
            "Authorization": f"Bearer {self.key}",
            "Content-Type": "application/json",
            "Prefer": "resolution=merge-duplicates"
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/rest/v1/{table}",
                headers=headers,
                json=[data]  # Supabase expects a list of records
            )

        if response.status_code == 409:
            logger.info(f"ℹ️ Data already exists in table {table}.")
            return "already_exists"

        if response.status_code not in (200, 201):
            logger.error(f"❌ Error upsert to {table}: {response.text}")
            raise Exception(f"Supabase error: {response.status_code} - {response.text}")

        return "success"

    async def upsert_vip_user(self, user_id: int, username: str, full_name: str):
        """Upsert user ke tabel 'Users' dengan skema standar bot Micin"""
        data = {
            "user_id": user_id,
            "username": username or "",
            "full_name": full_name or "",
            "is_vip": False,
            "vip_since": None,
            "created_at": datetime.utcnow().isoformat()
        }
        return await self.upsert("Users", data)

    async def upsert_custom_user(self, data: dict, table="Users"):
        """Upsert data user dengan struktur bebas ke tabel yang ditentukan"""
        return await self.upsert(table, data)

