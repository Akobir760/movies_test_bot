from aiogram import Router, types, F
from core.database import get_all_movies, get_movie_by_id
from keyboards.user import user_kb

router = Router()

@router.message(F.text == "/start")
async def start(msg: types.Message):
    await msg.answer("Botga xush kelibsiz!", reply_markup=user_kb)


@router.message(F.text == "📃 Kinolar ro'xati")
async def list_movies(msg: types.Message):
    kinolar = get_all_movies()
    if kinolar:
        text = "\n".join([f"{k[0]}. {k[1]}" for k in kinolar])
    else:
        text = "Hozircha kinolar mavjud emas."
    await msg.answer(text + "\n\nQaysi kino ID sini tanlasangiz, uni yuboring.")


@router.message(F.text.regexp(r"^\d+$"))
async def get_movie(msg: types.Message):
    kino = get_movie_by_id(int(msg.text))
    if kino:
        name, desc, file_id = kino
        await msg.answer_video(video=file_id, caption=f"<b>{name}</b>\n\n{desc}")
    else:
        await msg.answer("Bunday kino mavjud emas.")
