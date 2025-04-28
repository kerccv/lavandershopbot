from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from src.config import ADMIN_SECRET
from keyboards import admin_panel, main_menu, back_to_admin
from utils.parser import parse_csv
from utils.db import Session, Product

admin_router = Router()

# Проверка секретного кода
@admin_router.message(F.text == "🔐 Админ-панель")
async def ask_admin_code(message: Message):
    await message.answer("🔑 Введите секретный код:", reply_markup=ReplyKeyboardRemove())

# Вход в админку
@admin_router.message(F.text == ADMIN_SECRET)
async def admin_login(message: Message):
    await message.answer("👨‍💻 Добро пожаловать в админ-панель!", reply_markup=admin_panel())

# Загрузка CSV
@admin_router.message(F.text == "📤 Загрузить CSV")
async def handle_csv(message: Message):
    await message.answer("📎 Отправьте CSV-файл с товарами:")

@admin_router.message(F.document)
async def process_csv(message: Message):
    file = await message.bot.get_file(message.document.file_id)
    await message.bot.download_file(file.file_path, "temp.csv")
    if await parse_csv("temp.csv"):
        await message.answer("✅ Товары успешно добавлены!", reply_markup=admin_panel())
    else:
        await message.answer("❌ Ошибка загрузки файла.")