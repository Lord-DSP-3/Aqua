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

@app.on_message(filters.command(["run"]))
async def run(client, message):
    await message.reply_text(f"Only For Authorised Users")
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFCz8BiqKWONbh60S0bp-mCUv3SLhNVCQACDgMAAmM1QEVoYvfpiYqB_SQE")
    @app.on_message(filters.command(["run"]))

async def run(client, message):

    await message.reply_text(f"Only For Authorised Users")

    await app.send_sticker(message.chat.id,"
   @app.on_message(filters.command(["run"]))

async def run(client, message):

    await message.reply_text(f"Only For Authorised Users")

    await app.send_sticker(message.chat.id,"
