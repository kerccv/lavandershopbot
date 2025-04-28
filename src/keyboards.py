from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🛍️ Каталог", web_app=WebAppInfo(url="https://lavandershopbot.onrender.com/static/index.html"))],
            [KeyboardButton(text="🔐 Админ-панель")]
        ],
        resize_keyboard=True
    )

def admin_panel():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📤 Загрузить CSV")],
            [KeyboardButton(text="👀 Просмотреть товары")],
            [KeyboardButton(text="🚪 Выйти")]
        ],
        resize_keyboard=True
    )