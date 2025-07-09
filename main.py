import asyncio
from core.config import ADMIN_ID
from aiogram import Bot
from loader import bot, dp
from handlers import admin, user
from core.database import create_table


async def starup_answer(bot: Bot):
    await bot.send_message(chat_id=ADMIN_ID, text="Bot ishga tushdi!")
    create_table()



async def main():
    dp.startup.register(starup_answer)

    dp.include_router(admin.router)
    dp.include_router(user.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
