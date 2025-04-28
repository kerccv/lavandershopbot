import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import threading

from config import BOT_TOKEN
from handlers.admin import admin_router
from handlers.catalog import catalog_router

# Инициализация бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(admin_router)
dp.include_router(catalog_router)

# FastAPI приложение для webapp
app = FastAPI()

# Папка со статическими файлами
app.mount("/static", StaticFiles(directory="webapp"), name="static")


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Выбери действие:",
        reply_markup=await catalog_router.kb_main_menu()
    )

async def main():
    loop = asyncio.get_event_loop()
    threading.Thread(target=lambda: uvicorn.run(app, host="0.0.0.0", port=10000)).start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
