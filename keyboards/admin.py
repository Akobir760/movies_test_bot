from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎬 Kino qo'shish")],
        [KeyboardButton(text="✏️ Kinoni tahrirlash")],
        [KeyboardButton(text="🗑️ Kinoni o'chirish")],
    ],
    resize_keyboard=True
)
