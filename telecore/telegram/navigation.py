# telecore/telegram/navigation.py

from telegram import Update
from telegram.ext import ContextTypes
from .menus import make_menu

async def go_to_main_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    text: str = "🏠 *Menu Utama*",
    menu_rows: list[list[tuple[str, str]]] = None,
    parse_mode: str = "Markdown"
):
    """
    Kirim menu utama dengan teks dan struktur tombol yang bisa dikustom.
    Default pakai Markdown dan title "Menu Utama".
    """
    if not menu_rows:
        # Default jika tidak diberikan: aman untuk testing core
        menu_rows = [[("🔙 Kembali", "back")]]

    reply_markup = make_menu(menu_rows)

    if update.callback_query:
        await update.callback_query.message.edit_text(
            text=text,
            reply_markup=reply_markup,
            parse_mode=parse_mode
        )
    elif update.message:
        await update.message.reply_text(
            text=text,
            reply_markup=reply_markup,
            parse_mode=parse_mode
        )

