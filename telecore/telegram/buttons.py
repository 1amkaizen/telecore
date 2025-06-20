# telecore/telegram/buttons.py

from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def back_to_main_menu_button():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Kembali ke Menu Utama", callback_data="back_to_main")]
    ])

def join_vip_button():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔥 Join VIP Lifetime", callback_data="join_vip")]
    ])

def confirm_cancel_buttons(confirm_cb="confirm", cancel_cb="cancel"):
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✅ Konfirmasi", callback_data=confirm_cb),
            InlineKeyboardButton("❌ Batal", callback_data=cancel_cb)
        ]
    ])

def refresh_button():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 Cek Status", callback_data="refresh_status")]
    ])

def contact_admin_button():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📞 Kontak Admin", callback_data="contact_admin")]
    ])

def single_button(label: str, callback_data: str):
    """Tombol custom 1 kolom"""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(label, callback_data=callback_data)]
    ])

def multi_button(rows: list[list[tuple[str, str]]]):
    """
    Contoh input:
    [
        [("Option A", "opt_a"), ("Option B", "opt_b")],
        [("Cancel", "cancel")]
    ]
    """
    keyboard = [
        [InlineKeyboardButton(label, callback_data=cb) for label, cb in row]
        for row in rows
    ]
    return InlineKeyboardMarkup(keyboard)

