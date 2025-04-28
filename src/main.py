from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import BOT_TOKEN
from utils.db import init_db
from routers import user_router, catalog_router, admin_router

# Инициализация бота
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Регистрация роутеров
dp.include_router(user_router)
dp.include_router(catalog_router)
dp.include_router(admin_router)

# Обработчик команды /start
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать в магазин!")

async def on_startup():
    """Функция инициализации при запуске"""
    await init_db()  # Создаем таблицы в БД
    print("Бот запущен и готов к работе")

async def on_shutdown():
    """Функция очистки при выключении"""
    print("Бот выключается")

async def main():
    # Запускаем процессы
    await on_startup()
    
    # Запускаем бота
    try:
        await dp.start_polling(bot)
    finally:
        await on_shutdown()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())