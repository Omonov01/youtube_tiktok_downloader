from aiogram import types
from loader import dp,db,bot
from aiogram.dispatcher.filters import Text
from filters import IsPrivate
from data.config import ADMINS 



@dp.message_handler(IsPrivate(),text="/allusers", user_id=ADMINS)
async def add_channel(message:types.Message):
    try:
        for message.from_user.id in ADMINS:
             count = db.count_users()[0]
             msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
             await bot.send_message(chat_id=ADMINS, text=msg)
    except:
        await message.answer("Ro'yxatni ochib bo'madi")

