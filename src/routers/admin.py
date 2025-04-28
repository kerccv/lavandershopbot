from aiogram import Router, F
from aiogram.types import Message
from src.config import ADMIN_SECRET
from src.keyboards import admin_panel
from src.utils.parser import parse_csv

admin_router = Router()

@admin_router.message(F.text == "🔐 Админ-панель")
async def ask_admin_code(message: Message):
    await message.answer("🔑 Введите секретный код:")

@admin_router.message(F.text == ADMIN_SECRET)
async def admin_login(message: Message):
    await message.answer("👨‍💻 Вы вошли в админ-панель!", reply_markup=admin_panel())