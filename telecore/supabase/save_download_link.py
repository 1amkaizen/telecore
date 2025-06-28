# telecore/supabase/save_download_link.py

import uuid
from datetime import datetime
from supabase import create_client
from telecore.config import SUPABASE_URL, SUPABASE_KEY, DOWNLOAD_BASE_URL

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def generate_token() -> str:
    return str(uuid.uuid4())

def save_download_link(user_id: int, ebook_key: str, base_url: str = None):
    token = generate_token()

    if base_url is None:
        base_url = DOWNLOAD_BASE_URL

    # Pastikan base_url tidak diakhiri slash ganda
    download_url = base_url.rstrip("/") + f"/{token}"
    now = datetime.utcnow().isoformat()

    data = {
        "user_id": user_id,
        "ebook_key": ebook_key,
        "download_url": download_url,
        "token": token,  # ✅ simpan token ke Supabase
        "used": False,
        "created_at": now,
    }

    result = supabase.table("DownloadLinks").insert(data).execute()
    return download_url if result.data else None

