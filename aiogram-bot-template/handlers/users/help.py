from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from filters import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate(), CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - 🇺🇿 Botni ishga tushirish",
            "🇺🇸 Run the bot" ,
            "/help - 🇺🇿 Siz bu bot orqali Youtube tiktok platformalaridan video  yuklab olishingiz mumkin!",
                        "Buning uchun video  linkini yuborishingiz kerak",
                        "🇺🇸 You can download videos from Youtube, tiktok platform with this bot!",
                         "For this you need to send a video  link")
    
    await message.answer("\n".join(text))
