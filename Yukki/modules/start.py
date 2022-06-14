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
        f"Pretty Much Nothing For Normies \n Only AUTHORISED users..."
    )
    await app.send_sticker(message.chat.id,"CAACAgEAAxkBAAFCz5xiqJ8lua3WkPXNejoDnwKzJhahVgAC8QMAArrmQEWX3cjH0A_IbiQE")

@app.on_message(filters.command(["start", "ping"]))
async def start(client, message):
    await message.reply_text(
