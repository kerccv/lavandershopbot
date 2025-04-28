from aiogram import Router, types
from aiogram.filters import Command
from config import ADMIN_PASSWORD, PRODUCTS_FILE
import json
from services.parser import parse_csv

admin_router = Router()

@admin_router.message(Command("admin"))
async def admin_login(message: types.Message):
    await message.answer("Введи секретный код:")

@admin_router.message(lambda m: m.text == ADMIN_PASSWORD)
async def admin_menu(message: types.Message):
    await message.answer("Добро пожаловать в админку!\nОтправь CSV-файл с товарами.")

@admin_router.message(lambda m: m.document)
async def upload_csv(message: types.Message, document: types.Document):
    file = await message.bot.download(document)
    products = parse_csv(file)
    with open(PRODUCTS_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)
    await message.answer("✅ Товары загружены!")
