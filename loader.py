from aiogram import Bot, Dispatcher
from core.config import TOKEN
from aiogram.enums import ParseMode

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
