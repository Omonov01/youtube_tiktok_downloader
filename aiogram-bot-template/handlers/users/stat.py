from aiogram import types
from loader import dp,db,bot
from aiogram.dispatcher.filters import Text
from filters import IsPrivate
from data.config import ADMINS 



@dp.message_handler(IsPrivate(),text="/allusers", user_id=ADMINS)
async def add_channel(message:types.Message):
    try:
        # print(message.from_user.id)
        # print(message)
        # for message.from_user.id in ADMINS:
        # print("id adminda bor")
        count = await db.count_users()
        # print("bazadan malumot olindi")
        msg = f"Bazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)
        # print("consolga userlar soni chiqarildi")
    except:
        await message.answer("Ro'yxatni ochib bo'madi")
