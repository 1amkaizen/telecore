import os
from dotenv import load_dotenv

load_dotenv()

def str_to_bool(value: str) -> bool:
    return str(value).lower() in ("true", "1", "yes")

def str_to_list(value: str) -> list:
    return [x.strip() for x in value.split(",") if x.strip()]

# ===== BASIC CONFIG =====
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# ===== ADMIN CONFIG =====
ADMIN_ID = [int(x) for x in os.getenv("ADMIN_ID", "").split(",") if x.strip().isdigit()]
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "")

# ===== SUPABASE CONFIG =====
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# ===== MIDTRANS CONFIG =====
MIDTRANS_CLIENT_KEY = os.getenv("MIDTRANS_CLIENT_KEY")
MIDTRANS_SERVER_KEY = os.getenv("MIDTRANS_SERVER_KEY")
MIDTRANS_IS_SANDBOX = str_to_bool(os.getenv("MIDTRANS_IS_SANDBOX", "true"))

# ===== GROUP CONFIG =====
GROUP_VIP_ID = int(os.getenv("GROUP_VIP_ID", "-1"))
GROUP_UMUM_ID = int(os.getenv("GROUP_UMUM_ID", "-1"))

# ===== LINK TAMBAHAN =====
FAQ_LINK = os.getenv("FAQ_LINK", "")

# ===== OPSIONAL: GRUP LAINNYA (jika ingin looping/akses dinamis) =====
GRUP_LIST = []
for i in range(1, 7):
    nama = os.getenv(f"GRUP_{i}_NAMA")
    link = os.getenv(f"GRUP_{i}_LINK")
    if nama and link:
        GRUP_LIST.append({
            "nama": nama,
            "link": link
        })

# ===== VALIDASI WAJIB =====
required_vars = [
    BOT_TOKEN, SUPABASE_URL, SUPABASE_KEY,
    MIDTRANS_SERVER_KEY, MIDTRANS_CLIENT_KEY
]

if any(v is None or v == "" for v in required_vars):
    raise RuntimeError("❌ ENV tidak lengkap. Harap cek .env kamu.")


