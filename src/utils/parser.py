import pandas as pd
from src.utils.db import Session, Product

def parse_csv(file_path: str):
    try:
        df = pd.read_csv(file_path)
        session = Session()
        for _, row in df.iterrows():
            product = Product(
                name=row['name'],
                price=row['price'],
                description=row['description'],
                photo_url=row['photo_url']
            )
            session.add(product)
        session.commit()
        return True
    except Exception as e:
        print(f"Ошибка: {e}")
        return False