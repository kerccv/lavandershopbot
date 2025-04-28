from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from src.routers import dp
from src.config import BOT_TOKEN, WEBHOOK_URL, WEB_SERVER_HOST, WEB_SERVER_PORT, WEBHOOK_PATH
from aiohttp import web
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)

async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)
    logger.info("Бот запущен через вебхук")

app = web.Application()
app.on_startup.append(on_startup)
SimpleRequestHandler(dp, bot).register(app, path=WEBHOOK_PATH)

if __name__ == "__main__":
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)