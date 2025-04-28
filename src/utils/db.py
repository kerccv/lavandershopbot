from sqlalchemy import create_engine
from config import DATABASE_URL  # Импорт URL из .env

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)  # Таблицы создадутся автоматически