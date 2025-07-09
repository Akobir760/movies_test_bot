from aiogram import Router
from aiogram.fsm.state import State, StatesGroup
router = Router()

class MovieAdd(StatesGroup):
    name = State()
    desc = State()
    file = State()

class MovieEdit(StatesGroup):
    id = State()
    new_name = State()

class MovieDelete(StatesGroup):
    id = State()