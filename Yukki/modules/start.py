import time
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
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFCz7xiqKSb-T2ZG9im-K7pMdlJ_kZSmQACNwIAAsuOSEX5bh5-Omr7jSQE")

@app.on_message(filters.command(["settings"])& filters.private)
async def run(client, message):
    await message.reply_text(f"Only For Authorised Users")


@app.on_message(filters.command(["help"]))
async def run(client, message):
    await message.reply_text(f"⛑️Promote me as Admin in group.\n⌱Only 'delete messesge' rights required.\n\n💚Usage of Afk command:\n/afk \n/afk Reason \n/afk (reply to a sticker) \n/afk (reply to a sticker) Reason \n/afk (reply to a image) \n/afk (reply to a image) Reason\n\n💛Others:\n/ping  - To see bot Uptime \n/repo  - Source code \n\n\n📜 ⌱ UCO PROJECT")
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFCz-hiqK7ULTKZTWvsw5lVTf83G-ielgACbgIAAgnDSEVqYh91csOLqyQE")

@app.on_message(filters.command(["scan"])& filters.private)
async def run(client, message):
    await message.reply_text(f"Only For Authorised Users")

@app.on_message(filters.command(["repo"])& filters.private)
async def run(client, message):
    await asyncio.sleep(3)
    await message.delete()
    await message.reply_text(f"Look at sky \n Sky is Blue 💙")


@app.on_message(filters.command(["ping"]))
async def on_start(_, message: Message):
    bot_uptime = int(time.time() - boot)
    Uptime = get_readable_time(bot_uptime)
    await message.reply_text(
        f"{botname} is alive and working good.\n\nUptime : {Uptime}"
    )
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFC3hNiqaNlV1mevOdOu1jDjAsSRWgBGQACtwIAAuYuSEV3tv6QBNjZvSQE")
