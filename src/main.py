from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.session.aiohttp import AiohttpSession
from config import BOT_TOKEN
from routers import user_router, catalog_router, admin_router

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML, session=AiohttpSession())
dp = Dispatcher()

dp.include_router(user_router)
dp.include_router(catalog_router)
dp.include_router(admin_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())