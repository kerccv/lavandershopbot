from aiogram import Router

catalog_router = Router()  # Создаем экземпляр роутера

# Добавляем обработчики для каталога
@catalog_router.message(F.text == "🛍️ Каталог")
async def show_catalog(message: Message):
    await message.answer("Открываю каталог...")