import os
import logging
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

# Muat .env otomatis dari root project (naik max 3 tingkat)
def try_load_dotenv_from_project_root():
    import inspect
    frame = inspect.stack()[-1]
    caller_file = os.path.abspath(frame.filename)
    root_dir = os.path.dirname(caller_file)

    for _ in range(3):
        env_path = os.path.join(root_dir, ".env")
        if os.path.isfile(env_path):
            load_dotenv(dotenv_path=env_path)
            logger.info(f"✅ Loaded .env from: {env_path}")
            break
        root_dir = os.path.dirname(root_dir)

try_load_dotenv_from_project_root()


def require_env(var_name: str, cast=str, allow_empty=False):
    raw = os.getenv(var_name)
    if raw is None:
        logger.warning(f"⚠️ Environment variable '{var_name}' is not set.")
        return None
    if not allow_empty and raw.strip() == "":
        logger.warning(f"⚠️ Environment variable '{var_name}' is empty.")
        return None

    try:
        if cast == bool:
            return raw.lower() in ("1", "true", "yes", "on")
        elif cast == list:
            return [int(x.strip()) for x in raw.split(",") if x.strip()]
        elif cast == int:
            return int(raw)
        return cast(raw)
    except Exception as e:
        logger.error(f"❌ Failed to cast env '{var_name}' to {cast.__name__}: {e}")
        return None

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

DOWNLOAD_BASE_URL = require_env("DOWNLOAD_BASE_URL" )


# Grup Telegram (Fleksibel & Validated)
GROUP_COUNT = int(os.getenv("GRUP_COUNT", 6))
GROUP_PER_BARIS = int(os.getenv("GRUP_PER_BARIS", 3))

GRUP_LINKS = []
for i in range(1, GROUP_COUNT + 1):
    nama = os.getenv(f"GRUP_{i}_NAMA")
    link = os.getenv(f"GRUP_{i}_LINK")
    if nama and link:
        GRUP_LINKS.append({"nama": nama.strip(), "link": link.strip()})

