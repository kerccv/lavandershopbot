from aiogram import Router
from aiogram.types import Message
from src.keyboards import main_menu

user_router = Router()

@user_router.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer("👋 Добро пожаловать!", reply_markup=main_menu())