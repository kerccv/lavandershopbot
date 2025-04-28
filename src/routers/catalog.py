from aiogram import Router, F
from aiogram.types import Message

# Создаем экземпляр роутера
catalog_router = Router(name="catalog_router")

# Обработчик кнопки "Каталог"
@catalog_router.message(F.text == "🛍️ Каталог")
async def show_catalog(message: Message):
    await message.answer("Открываю каталог...")