# telecore/telegram/menus.py

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from typing import List, Tuple

ButtonRow = List[Tuple[str, str]]  # List tombol per baris

def make_menu(rows: List[ButtonRow]) -> InlineKeyboardMarkup:
    """
    Buat inline menu fleksibel.

    rows: list tombol dalam bentuk:
        [
            [("Text Tombol 1", "callback_data_1")],                   # Baris 1 (1 tombol)
            [("Text A", "cb_a"), ("Text B", "cb_b")],                 # Baris 2 (2 tombol)
            [("A", "a"), ("B", "b"), ("C", "c")]                      # Baris 3 (3 tombol)
        ]
    """
    keyboard = [
        [InlineKeyboardButton(text, callback_data=callback_data) for text, callback_data in row]
        for row in rows
    ]
    return InlineKeyboardMarkup(keyboard)

