import time
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters
from pyrogram.types import Message

from Yukki import app, boot, botname
from Yukki.helpers import get_readable_time


@app.on_message(filters.command(["start"])) 
async def on_start(_, message: Message):
    await message.reply_text(
        f"Pretty Much Nothing For Normies..."
    )
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFCz7xiqKSb-T2ZG9im-K7pMdlJ_kZSmQACNwIAAsuOSEX5bh5-Omr7jSQE")

@app.on_message(filters.command(["settings"])& filters.private)
async def run(client, message):
    await message.reply_text(f"Only For Authorised Users")


@app.on_message(filters.command(["help"]))
async def run(client, message):
    await message.reply_text(f"If you need any help join \n💚 @Anime_Gaming_Chat_Global 💛")
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFCz-hiqK7ULTKZTWvsw5lVTf83G-ielgACbgIAAgnDSEVqYh91csOLqyQE")

@app.on_message(filters.command(["scan"])& filters.private)
async def run(client, message):
    await message.reply_text(f"Only For Authorised Users")

@app.on_message(filters.command(["repo"])& filters.private)
async def run(client, message):
    await message.reply_text(f"Look at sky \n Sky is Blue 💙")
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFC0AFiqLFq96XquupWkC3Wjww8cIo8HwACRAIAAtSXSEXU4M20BCBnFCQE")
    await message.reply_text(f"Now look at you \n There's No One Ugly as You 😝")
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFC0FZiqLivDE15hr0iUXXB3uLKkm4iGQACvQIAAm9fSEXTjPhY1VGe5SQE")
    await message.reply_text(f"I Really Think You should be in the Zoo 😂")
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFC0FliqLkzC0-vr0HKeCxg-QfbH8IW0gACbgIAAgnDSEVqYh91csOLqyQE")
    await message.reply_text(f"Don't worry I'll be there too 🥺")
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFC0F9iqLoP10v9cGFlNDYlvMkf5EJcHgACDgIAApwgSUXoPrEi4_q4tyQE")
    await message.reply_text(f"But Laughing at you!!! ")
    await app.send_sticker(message.chat.id,"CAACAgUAAxkBAAFC0GJiqLqM2c0OK0MM45QaNtMwYlpU9AACuwUAAg2iqVdfW2GdjZSKYSQE")
    await message.reply_text(f"Ask for repo again And \n I will hit you with a shoe 🌝")
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFC0GZiqLubtDfUiSZOCibf8BS7LzsnuwACSgMAAlopSEUBme_jF0ul2yQE")
    await message.reply_text(f"If i do... \n Please You don't Cry ")
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFC0GxiqLzmpch1zZbA87pClhIrqg1jGgACxwMAAs72QEUySsl-a4Af0CQE")
    await message.reply_text(f"And GOOD BYE ! 🎋💕")
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFC0G9iqL0J8n28bWQS4_U3ziLujmHOoAACXgIAAm53SEW3PHkJlNtQ9iQE")

@app.on_message(filters.command(["ping"]))
async def on_start(_, message: Message):
    bot_uptime = int(time.time() - boot)
    Uptime = get_readable_time(bot_uptime)
    await message.reply_text(
        f"{botname} is alive and working good.\n\nUptime : {Uptime}"
    )
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFC3hNiqaNlV1mevOdOu1jDjAsSRWgBGQACtwIAAuYuSEV3tv6QBNjZvSQE")
