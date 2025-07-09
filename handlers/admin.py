from aiogram import  types, F
from core.config import ADMIN_ID
from keyboards.admin import admin_kb
from core.database import add_movie, update_movie_name, delete_movie
from aiogram.fsm.context import FSMContext
from handlers.states import MovieAdd, MovieDelete, MovieEdit, router
from handlers.user import list_movies


@router.message(F.text == "/admin")
async def admin_start(msg: types.Message):
    if msg.from_user.id == ADMIN_ID:
        await msg.answer("Admin panelga xush kelibsiz", reply_markup=admin_kb)
    else:
        await msg.answer("Siz admin emassiz!")


@router.message(F.text == "🎬 Kino qo'shish")
async def add_movie_start(msg: types.Message, state: FSMContext):
    await msg.answer("Kino nomini yuboring:")
    await state.set_state(MovieAdd.name)


@router.message(MovieAdd.name)
async def add_movie_name(msg: types.Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer("Kino tavsifini yozing:")
    await state.set_state(MovieAdd.desc)


@router.message(MovieAdd.desc)
async def add_movie_desc(msg: types.Message, state: FSMContext):
    await state.update_data(desc=msg.text)
    await msg.answer("Kino faylini (video) yuboring:")
    await state.set_state(MovieAdd.file)


@router.message(MovieAdd.file, F.video)
async def add_movie_file(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    add_movie(data["name"], data["desc"], msg.video.file_id)
    await msg.answer("Kino muvaffaqiyatli qo'shildi!")
    await state.clear()


@router.message(F.text == "✏️ Kinoni tahrirlash")
async def edit_start(msg: types.Message, state: FSMContext):
    await list_movies(msg)
    await state.set_state(MovieEdit.id)


@router.message(MovieEdit.id)
async def edit_get_id(msg: types.Message, state: FSMContext):
    if msg.text.isdigit():
        await state.update_data(id=int(msg.text))
        await msg.answer("Yangi nomini yuboring:")
        await state.set_state(MovieEdit.new_name)


@router.message(MovieEdit.new_name)
async def edit_set_name(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    update_movie_name(data["id"], msg.text)
    await msg.answer("Kino nomi yangilandi!")
    await state.clear()


@router.message(F.text == "🗑️ Kinoni o'chirish")
async def delete_start(msg: types.Message, state: FSMContext):
    await list_movies(msg)
    await state.set_state(MovieDelete.id)


@router.message(MovieDelete.id)
async def delete_movie_handler(msg: types.Message, state: FSMContext):
    if msg.text.isdigit():
        delete_movie(int(msg.text))
        await msg.answer("Kino o'chirildi!")
        await state.clear()
