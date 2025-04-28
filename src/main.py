import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.utils.exceptions import TelegramConflictError
from config import BOT_TOKEN
from utils.db import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    try:
        # Инициализация БД
        init_db()
        
        # Запуск бота с обработкой конфликта
        bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
        dp = Dispatcher()
        
        logger.info("Бот успешно запущен")
        
        while True:
            try:
                await dp.start_polling(bot)
            except TelegramConflictError as e:
                logger.warning(f"Конфликт обновлений: {e}")
                await asyncio.sleep(5)  # Пауза перед повторной попыткой
            except Exception as e:
                logger.error(f"Критическая ошибка: {e}")
                break
                
    except Exception as e:
        logger.error(f"Ошибка запуска: {e}")
    finally:
        if 'bot' in locals():
            await bot.close()

if __name__ == "__main__":
    asyncio.run(main())