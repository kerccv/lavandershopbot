import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config import BOT_TOKEN
from utils.db import init_db  # Импорт синхронной функции

# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    try:
        # 1. Проверка токена
        if not BOT_TOKEN:
            raise ValueError("Токен бота не установлен!")
        
        # 2. Инициализация БД (синхронный вызов)
        logger.info("Инициализация базы данных...")
        init_db()  # Теперь это синхронная функция
        
        # 3. Запуск бота
        bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
        dp = Dispatcher()
        
        logger.info("Бот успешно запущен")
        await dp.start_polling(bot)
        
    except Exception as e:
        logger.error(f"Ошибка при запуске: {e}")
    finally:
        if 'bot' in locals():
            await bot.close()

if __name__ == "__main__":
    asyncio.run(main())