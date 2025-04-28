from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

# Сначала создаем Base
Base = declarative_base()

# Затем определяем модели
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(Text)
    photo_url = Column(String(255))

# И только потом создаем engine и сессии
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def init_db():
    """Создает таблицы при первом запуске"""
    Base.metadata.create_all(engine)

def add_product(name: str, price: int, description: str, photo_url: str):
    """Добавляет товар в БД"""
    session = Session()
    product = Product(name=name, price=price, description=description, photo_url=photo_url)
    session.add(product)
    session.commit()
    session.close()