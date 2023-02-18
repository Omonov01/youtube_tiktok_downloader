import asyncio
from aiogram.dispatcher import filters
from aiogram import types

from aiogram.utils import exceptions, executor
import asyncio
import logging
log = logging.getLogger('broadcast')
from data.config import ADMINS
from loader import dp, db, bot

async def send_message_to_users_handler(user_id,text) :
    try:
        print("a")
        await bot.an(user_id,text,message_id=bot.id)
    except exceptions.BotBlocked:
        logging.error(f"Target [ID:{user_id}]: blocked by user")
    except exceptions.ChatNotFound:
        logging.error(f"Target [ID:{user_id}]: invalid user ID")
    except exceptions.RetryAfter as e:
        logging.error(f"Target [ID:{user_id}]: Flood limit is exceeded. " f"Sleep {e.timeout} seconds.")
        await asyncio.sleep(e.timeout)
        return await bot.send_message(user_id, text)  # Recursive call
    except exceptions.UserDeactivated:
        logging.error(f"Target [ID:{user_id}]: user is deactivated")
    except exceptions.TelegramAPIError:
        logging.exception(f"Target [ID:{user_id}]: failed")
    else:
        logging.info(f"Target [ID:{user_id}]: success")
        return True
    return False

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
            await message.copy_to(chat_id=user_id)
            count += 1
            await asyncio.sleep(0.5)
        await bot.send_message(chat_id=ADMINS, text=f"reklama {count} ta userga junatildi")
    finally:
        await bot.send_message(chat_id=ADMINS, text=f"reklama {count} ta userga junatildi")