#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiAFKBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiAFKBot/blob/master/LICENSE >
#
# All rights reserved.

import time

from pyrogram import filters
from pyrogram.types import Message

from Yukki import app, boot, botname
from Yukki.helpers import get_readable_time


@app.on_message(filters.command(["start", "ping"]))
async def on_start(_, message: Message):
    bot_uptime = int(time.time() - boot)
    Uptime = get_readable_time(bot_uptime)
    await message.reply_text(
        f"Pretty Much Nothing For Normies..."
    )
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFCz7xiqKSb-T2ZG9im-K7pMdlJ_kZSmQACNwIAAsuOSEX5bh5-Omr7jSQE")

@app.on_message(filters.command(["settings"]))
async def run(client, message):
    await message.reply_text(f"Only For Authorised Users")
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFCz8BiqKWONbh60S0bp-mCUv3SLhNVCQACDgMAAmM1QEVoYvfpiYqB_SQE")

@app.on_message(filters.command(["help"]))
async def run(client, message):
    await message.reply_text(f"Join 💚 @Anime_Gaming_Chat_Global 💛 if you need any help.")
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFCz-hiqK7ULTKZTWvsw5lVTf83G-ielgACbgIAAgnDSEVqYh91csOLqyQE")

@app.on_message(filters.command(["scan"]))
async def run(client, message):
    await message.reply_text(f"Only For Authorised Users")
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFC0AFiqLFq96XquupWkC3Wjww8cIo8HwACRAIAAtSXSEXU4M20BCBnFCQE")

@app.on_message(filters.command(["repo"]))
async def run(client, message):
    await message.reply_text(f"Look at sky \n Sky is Blue 💙")
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFC0AFiqLFq96XquupWkC3Wjww8cIo8HwACRAIAAtSXSEXU4M20BCBnFCQE")
    await message.reply_text(f"Now look at you \n There's No One Ugly as You 😝")
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFC0FZiqLivDE15hr0iUXXB3uLKkm4iGQACvQIAAm9fSEXTjPhY1VGe5SQE")
    await message.reply_text(f"I Really Think You should be in Zoo 😂")
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFC0FliqLkzC0-vr0HKeCxg-QfbH8IW0gACbgIAAgnDSEVqYh91csOLqyQE")
