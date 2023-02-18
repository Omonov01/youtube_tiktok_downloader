import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate
from data.config import ADMINS
from loader import dp,db,bot
import asyncpg

@dp.message_handler(IsPrivate(),CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
        print(user)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)
    await message.answer(f"Salom, {message.from_user.full_name}!\n 🇺🇿 Siz bu bot orqali Youtube, tiktok platformalaridan video yuklab olishingiz mumkin!\nBuning uchun video linkini yuborishingiz kerak! \n 🇺🇸 You can download videos  from Youtube , tiktok platforms with this bot!\nFor this you need to send a video link!")
