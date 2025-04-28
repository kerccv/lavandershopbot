from src.routers import dp  # Теперь импорт будет работать
from src.config import BOT_TOKEN
from aiogram import Bot
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from aiohttp import web

bot = Bot(token=BOT_TOKEN)
app = web.Application()
SimpleRequestHandler(dp, bot).register(app, path='/webhook')

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8000)