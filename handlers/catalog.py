from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import PRODUCTS_FILE, WEBAPP_URL
import json

catalog_router = Router()

async def kb_main_menu():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🛒 Каталог", web_app=types.WebAppInfo(url=WEBAPP_URL))],
        ]
    )
    return kb
