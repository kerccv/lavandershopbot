import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("7313861292:AAEThP2eynTXlRxljyas9Gma_FPvGVVZhT8")
ADMIN_SECRET = os.getenv("1293forever")  # Секретный код для входа в админку
DATABASE_URL = "sqlite:///shop.db"        # Путь к SQLite (можно заменить на PostgreSQL)