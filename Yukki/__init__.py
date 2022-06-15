import asyncio
import time

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pyrogram import Client

import config

loop = asyncio.get_event_loop()
boot = time.time()

mongo = MongoClient(config.MONGO_DB_URI)
db = mongo.AFK

botid = 0
botname = ""

SUDOERS = config.SUDO_USER

app = Client(
    ":YukkiAFKBot:",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)


async def initiate_bot():
    global botid, botname
    await app.start()
    getme = await app.get_me()
    botid = getme.id
    if getme.last_name:
        botname = getme.first_name + " " + getme.last_name
    else:
        botname = getme.first_name


loop.run_until_complete(initiate_bot())
