from aiogram import types
from filters import IsGroup
from loader import dp,db
import asyncpg


@dp.message_handler(IsGroup())
async def add_person(message : types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)