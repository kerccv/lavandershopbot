import os
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

# Убедимся, что используется правильный URL
print(f"Подключаемся к БД по URL: {DATABASE_URL[:30]}...")  # Логируем для отладки

# Для Render PostgreSQL добавляем параметры
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "keepalives": 1,
        "keepalives_idle": 30,
        "keepalives_interval": 10,
        "keepalives_count": 5
    }
)

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(Text)
    photo_url = Column(String(255))
    is_active = Column(Boolean, default=True)  # Для управления видимостью

Session = sessionmaker(bind=engine)

def init_db():
    try:
        Base.metadata.create_all(engine)
        print("Таблицы успешно созданы")
    except Exception as e:
        print(f"Ошибка создания таблиц: {e}")