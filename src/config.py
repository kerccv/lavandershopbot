import os

# Явное указание токена (на время теста)
BOT_TOKEN = "7313861292:AAEThP2eynTXlRxljyas9Gma_FPvGVVZhT8"
ADMIN_SECRET = "1293forever"
DATABASE_URL = "postgresql://admin:z08MOdcHDvaIkTxVqX7HiagLj3sQJk12@dpg-d07r2cp5pdvs73ae65r0-a/shop_sov1"

# Проверка
if not BOT_TOKEN:
    raise ValueError("Токен бота не найден!")