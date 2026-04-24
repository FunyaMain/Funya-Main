from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from services.database import fetchrow, execute

router = Router()


# 🔘 клавиатура профиля (только ЛС)
def profile_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔄 Обмен"), KeyboardButton(text="⛏ Копать")],
            [KeyboardButton(text="💧 Полить"), KeyboardButton(text="✋ Фап")]
        ],
        resize_keyboard=True
    )


# 👤 Профиль
@router.message(F.text.lower() == "профиль")
async def profile(message: Message):
    user = await fetchrow(
        "SELECT * FROM users WHERE id=$1",
        message.from_user.id
    )

    # если вдруг пользователя нет (на всякий случай)
    if not user:
        return await message.answer("❌ Сначала напиши /start в боте")

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


# 🔄 Обмен (кнопка)
@router.message(F.text == "🔄 Обмен")
async def exchange(message: Message):
    user = await fetchrow(
        "SELECT crystals FROM users WHERE id=$1",
        message.from_user.id
    )

    if not user:
        return await message.answer("❌ Сначала напиши /start в боте")

    if user["crystals"] < 1000:
        return await message.answer("❌ Недостаточно кристаллов")

    await execute(
        "UPDATE users SET crystals = crystals - 1000, pizza = pizza + 1 WHERE id=$1",
        message.from_user.id
    )

    await message.answer("🔄 Обмен\n\n💎 -1000\n🍕 +1")
