from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean  # Добавили Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
import logging

# Настройка логгирования
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def get_engine():
    """Создает и возвращает подключение к БД с обработкой ошибок"""
    try:
        logger.info(f"Подключаемся к БД: {DATABASE_URL[:30]}...")  # Логируем начало подключения
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
        logger.info("Подключение к БД успешно установлено")
        return engine
    except Exception as e:
        logger.error(f"Ошибка подключения к БД: {e}")
        raise

Base = declarative_base()
engine = get_engine()
Session = sessionmaker(bind=engine)

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(Text)
    photo_url = Column(String(255))
    is_active = Column(Boolean, default=True, nullable=False)  # Теперь Boolean импортирован корректно

def init_db():
    """Инициализирует БД, создает таблицы"""
    try:
        Base.metadata.create_all(engine)
        logger.info("Таблицы БД успешно созданы")
    except Exception as e:
        logger.error(f"Ошибка при создании таблиц БД: {e}")
        raise

def add_product(name: str, price: int, description: str, photo_url: str):
    """Добавляет новый товар в БД"""
    session = Session()
    try:
        product = Product(
            name=name,
            price=price,
            description=description,
            photo_url=photo_url
        )
        session.add(product)
        session.commit()
        logger.info(f"Добавлен товар: {name}")
        return product
    except Exception as e:
        session.rollback()
        logger.error(f"Ошибка при добавлении товара: {e}")
        raise
    finally:
        session.close()
