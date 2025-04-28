from aiogram import Router, F
from aiogram.types import Message
from keyboards import main_menu

user_router = Router()

@user_router.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer(
        "👋 Добро пожаловать в магазин!",
        reply_markup=main_menu()
    )