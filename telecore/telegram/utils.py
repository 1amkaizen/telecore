# telecore/telegram/utils.py



from telegram import Bot
from telegram.request import HTTPXRequest
from telecore.config import BOT_TOKEN
from telecore.logging.logger import get_logger

logger = get_logger("telecore.telegram.utils")

# Inisialisasi request default
telegram_request = HTTPXRequest()  # TANPA custom client

# Inisialisasi Bot dengan request custom
bot = Bot(token=BOT_TOKEN, request=telegram_request)

async def send_telegram_message(
    chat_id: int,
    text: str,
    parse_mode: str = "Markdown",
    reply_markup=None
):
    try:
        await bot.send_message(
            chat_id=chat_id,
            text=text,
            parse_mode=parse_mode,
            reply_markup=reply_markup
        )
        logger.info(f"✅ Pesan terkirim ke {chat_id}")
    except Exception as e:
        logger.warning(f"❌ Gagal kirim pesan ke {chat_id}: {e}")

