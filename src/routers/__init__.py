from aiogram import Dispatcher
from .admin import admin_router
from .user import user_router

dp = Dispatcher()
dp.include_router(admin_router)
dp.include_router(user_router)