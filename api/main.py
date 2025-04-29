from fastapi import FastAPI
import asyncpg
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products")
async def get_products():
    conn = await asyncpg.connect(os.getenv("DATABASE_URL"))
    rows = await conn.fetch("SELECT id, name, description, price FROM products WHERE visible = TRUE")
    await conn.close()
    return [{"id": r["id"], "name": r["name"], "description": r["description"], "price": float(r["price"])} for r in rows]
