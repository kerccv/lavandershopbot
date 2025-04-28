from aiogram.types import (
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton,
    WebAppInfo
)

# Главное меню
def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🛍️ Каталог", web_app=WebAppInfo(url="https://lavandershopbot.onrender.com/static/index.html"))],
            [KeyboardButton(text="🔐 Админ-панель")]
        ],
        resize_keyboard=True
    )

# Админ-панель
def admin_panel():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📤 Загрузить CSV")],
            [KeyboardButton(text="👀 Просмотреть товары")],
            [KeyboardButton(text="🚪 Выйти")]
        ],
        resize_keyboard=True
    )

# Кнопка "Назад" в админке
def back_to_admin():
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="⬅️ Назад", callback_data="admin_back")]]
    )