# keyboards/reply.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def profile_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔄 Обмен"), KeyboardButton(text="⛏ Копать")],
            [KeyboardButton(text="💧 Полить"), KeyboardButton(text="✋ Фап")]
        ],
        resize_keyboard=True
    )
