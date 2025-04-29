from aiogram import types
from aiogram.dispatcher.filters import Command
from bot.utils.csv_parser import parse_and_insert_csv
import os

@Command("upload_csv")
async def upload_csv(message: types.Message):
    if not message.document:
        return await message.reply("Пожалуйста, отправьте CSV файл.")
    file_path = f"data/{message.document.file_name}"
    await message.document.download(destination_file=file_path)
    await parse_and_insert_csv(file_path)
    await message.reply("CSV файл обработан и товары добавлены.")
