import asyncio
from aiogram.dispatcher import filters
from aiogram import types

from aiogram.utils import exceptions, executor
import asyncio
import logging
log = logging.getLogger('broadcast')
from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(filters.IDFilter(user_id=ADMINS),
        content_types=[
            types.ContentType.PHOTO,
            #types.ContentType.DOCUMENT,
            types.ContentType.TEXT,
            # types.ContentType.AUDIO,
            # types.ContentType.VOICE,
            types.ContentType.VIDEO
        ]
    )


async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    count = 0
    try:
        for user in users:
            user_id = user[3]
            print(user_id)
            try:
                await message.copy_to(chat_id=user_id,reply_markup=message)
            except:
                pass
            count += 1
            print(count)
            await asyncio.sleep(0.5)
            print("a")
        #await message.a(chat_id=ADMINS[0], text=f"reklama {count} ta userga junatildi")
        print("b")
    finally:
        await bot.send_message(chat_id=ADMINS, text=f"reklama {count} ta userga junatildi")
