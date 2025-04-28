from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
import logging

logger = logging.getLogger(__name__)

# Инициализация
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(Text)
    photo_url = Column(String(255))
    is_active = Column(Boolean, default=True)

def init_db():
    """Синхронная инициализация БД"""
    try:
        engine = create_engine(DATABASE_URL)
        logger.info(f"Подключение к БД: {DATABASE_URL[:30]}...")
        Base.metadata.create_all(engine)
        logger.info("Таблицы успешно созданы")
        return True
    except Exception as e:
        logger.error(f"Ошибка БД: {e}")
        return False