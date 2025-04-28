import pandas as pd
from pathlib import Path
from utils.db import add_product

async def parse_csv(file_path: str):
    try:
        df = pd.read_csv(file_path)
        for _, row in df.iterrows():
            add_product(
                name=row["name"],
                price=row["price"],
                description=row["description"],
                photo_url=row["photo_url"]
            )
        return True
    except Exception as e:
        print(f"Ошибка: {e}")
        return False