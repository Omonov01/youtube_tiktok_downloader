from aiogram import types
from filters import IsGroup
from loader import dp
from aiogram.dispatcher.filters import Text
from tiktok_downloader import snaptik
import os
from data.config import BOT_LINKS


@dp.message_handler(IsGroup(),Text(contains="tiktok.com",ignore_case=True))
async def text(message: types.Message):
    if not os.path.exists('tiktok'):
        os.makedirs('tiktok')
    video_url = message.text
    try:
        msg = await message.answer("Please wait...")
        snaptik(video_url).get_media()[0].download(f"./tiktok/result_{message.from_user.id}.mp4")
        path = f'./tiktok/result_{message.from_user.id}.mp4'
        with open(f'./tiktok/result_{message.from_user.id}.mp4', 'rb') as file:
            await msg.delete()
            await message.answer_video(video=file,caption=f"Video downloaded by {BOT_LINKS}")
        os.remove(path)
    except Exception as e:
        await message.answer("Invalid link! Please send valid link")