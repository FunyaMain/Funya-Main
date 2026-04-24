# main.py
import asyncio
from loader import dp, bot
from handlers import *

async def main():
    dp.include_router(start.router)
    dp.include_router(profile.router)
    dp.include_router(game.router)
    dp.include_router(bonus.router)
    dp.include_router(promo.router)
    dp.include_router(top.router)
    dp.include_router(chat_top.router)
    dp.include_router(bank.router)
    dp.include_router(donate_top.router)
    dp.include_router(tickets.router)
    dp.include_router(admin.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
