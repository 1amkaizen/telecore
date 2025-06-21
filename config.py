import os

def require_env(var_name: str, cast=str, allow_empty=False):
    raw = os.getenv(var_name)
    if raw is None:
        raise ValueError(f"Environment variable '{var_name}' is required but not set.")

    if not allow_empty and raw.strip() == "":
        raise ValueError(f"Environment variable '{var_name}' cannot be empty.")

    try:
        if cast == bool:
            return raw.lower() in ("1", "true", "yes", "on")
        elif cast == list:
            return [int(x.strip()) for x in raw.split(",") if x.strip()]
        elif cast == int:
            return int(raw)
        return cast(raw)
    except Exception as e:
        raise ValueError(f"Environment variable '{var_name}' could not be cast to {cast.__name__}: {e}")


# Config utama
BOT_TOKEN = require_env("BOT_TOKEN")
WEBHOOK_URL = require_env("WEBHOOK_URL")
ADMIN_ID = require_env("ADMIN_ID", cast=list)
ADMIN_USERNAME = require_env("ADMIN_USERNAME")

SUPABASE_URL = require_env("SUPABASE_URL")
SUPABASE_KEY = require_env("SUPABASE_KEY")

MIDTRANS_CLIENT_KEY = require_env("MIDTRANS_CLIENT_KEY")
MIDTRANS_SERVER_KEY = require_env("MIDTRANS_SERVER_KEY")
MIDTRANS_IS_SANDBOX = require_env("MIDTRANS_IS_SANDBOX", cast=bool)

FAQ_LINK = require_env("FAQ_LINK")
GROUP_VIP_ID = require_env("GROUP_VIP_ID", cast=int)
GROUP_UMUM_ID = require_env("GROUP_UMUM_ID", cast=int)


# Grup Telegram (Fleksibel & Validated)
GROUP_COUNT = int(os.getenv("GRUP_COUNT", 6))
GROUP_PER_BARIS = int(os.getenv("GRUP_PER_BARIS", 3))

GRUP_LINKS = []
for i in range(1, GROUP_COUNT + 1):
    nama = os.getenv(f"GRUP_{i}_NAMA")
    link = os.getenv(f"GRUP_{i}_LINK")
    if nama and link:
        GRUP_LINKS.append({"nama": nama.strip(), "link": link.strip()})

