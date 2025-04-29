from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import logging
import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Стартовая клавиатура
start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb.add(KeyboardButton("Каталог"), KeyboardButton("Админ-панель"))

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=start_kb)

@dp.message_handler(lambda message: message.text == "Каталог")
async def catalog_handler(message: types.Message):
    await message.answer("Откройте мини-приложение: https://your-mini-app-url.com")

@dp.message_handler(lambda message: message.text == "Админ-панель")
async def admin_handler(message: types.Message):
    await message.answer("Функции админ-панели:
1. Загрузка CSV
2. Осмотр товаров (в разработке)")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
