import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "7313861292:AAEThP2eynTXlRxljyas9Gma_FPvGVVZhT8")
ADMIN_SECRET = os.getenv("ADMIN_SECRET", "1293forever")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:z08MOdcHDvaIkTxVqX7HiagLj3sQJk12@dpg-d07r2cp5pdvs73ae65r0-a/shop_sov1")

# Webhook settings
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://lavandershopbot.onrender.com/webhook")
WEBHOOK_PATH = "/webhook"
WEB_SERVER_HOST = "0.0.0.0"
WEB_SERVER_PORT = os.getenv("PORT", "8000")