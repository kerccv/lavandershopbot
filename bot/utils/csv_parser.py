import pandas as pd
import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

async def parse_and_insert_csv(file_path: str):
    df = pd.read_csv(file_path)
    conn = await asyncpg.connect(DATABASE_URL)
    await conn.execute("CREATE TABLE IF NOT EXISTS products (id SERIAL PRIMARY KEY, name TEXT, description TEXT, price NUMERIC, visible BOOLEAN DEFAULT TRUE)")
    for _, row in df.iterrows():
        await conn.execute("INSERT INTO products (name, description, price) VALUES ($1, $2, $3)", row['name'], row['description'], row['price'])
    await conn.close()
