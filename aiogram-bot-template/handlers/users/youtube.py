from aiogram import types
from loader import dp
from pytube import YouTube
from aiogram.dispatcher.filters import Text
from filters import IsPrivate
import os
from data.config import BOT_LINKS

@dp.message_handler(IsPrivate(),Text(contains='youtu.be',ignore_case=True))
@dp.message_handler(IsPrivate(),Text(contains='youtube.com',ignore_case=True))
async def download_youtube_video(msg:types.Message):
    if not os.path.exists('youtube'):
        os.makedirs('youtube')
    link = msg.text
    try:
        yt = YouTube(link)
        messege = await msg.answer("Please wait...")
        stream = yt.streams.filter(progressive=True,file_extension='mp4')
        stream.get_highest_resolution().download(f"./youtube",f"{msg.chat.id}_{yt.title}")
        with open(f"./youtube/{msg.chat.id}_{yt.title}","rb") as video:
            await messege.delete()
            await msg.answer_video(video,caption = f'Video downloaded by {BOT_LINKS}')
            os.remove(f"./youtube/{msg.chat.id}_{yt.title}")
    except:
        await msg.answer("Invalid link !Please send again valid link! Or Huge video size")