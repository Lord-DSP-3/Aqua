import time
import asyncio

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters
from pyrogram.types import Message

from Yukki import app, boot, botname
from Yukki.helpers import get_readable_time


@app.on_message(filters.command(["start"])& filters.private) 
async def on_start(_, message: Message):
    await message.reply_text(
        f"Pretty Much Nothing For Normies..."
    )
    return await message.reply_photo(photo="https://telegra.ph/file/df56751076ab5525b6d61.jpg")


@app.on_message(filters.command(["testdel"]))
async def testdel(_, message: Message):
    await asyncio.sleep(5)
    await message.delete()
    await message.reply_text(f"Look at sky \n Sky is Blue 💙")
