# handlers/profile.py
from aiogram import Router, F
from aiogram.types import Message
from services.database import fetchrow
from keyboards.reply import profile_kb

router = Router()

@router.message(F.text.lower() == "профиль")
async def profile(message: Message):
    user = await fetchrow(
        "SELECT * FROM users WHERE id=$1",
        message.from_user.id
    )

    text = f"""
👤 {message.from_user.first_name}
ID: {message.from_user.id}

💎 Кристаллы: {user['crystals']}
🍕 Пицца: {user['pizza']}
🧴 Крем для фапа: {user['cream']}
🌵 Кактус: {user['cactus']} см
✋ Фап: {user['fap']}

💱 1000 💎 = 1 🍕
"""

    await message.answer(text, reply_markup=profile_kb())
