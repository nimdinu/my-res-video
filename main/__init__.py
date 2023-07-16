#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
# variables
API_ID = 5860777
API_HASH = 'a8595cffe5fca4cf19ea3f3334b4fe46'
BOT_TOKEN = '6185997244:AAFfufCPMdsXW9hhikuaf410XG2rCm5A6lQ'
SESSION = 'BQBZbakARZKYrFJyxvYPQHSMOOR5stpxR6dl18Wal2w5ak8lEIkJwEVL6J1zcctkKbDRzirqfYG98mQ9dBe5z4H9XndD9zhPf_5Yka27p5XAG73DLCszj1Xpv5YDREFPT6JnQiOkp2qRm_YanEHhXwuQ9x8XwPx99SKn1H9zP_pnsyYnCQ5yWrALAGKFmYProX1WbfpHhI6XgMHzyODZJt-tbzvqJ1u-yFHJCngeqpXx5VhwcgkpYDLFrQYB7sx-WBwdvY2Zw8_JF7Csiey6Hw3RQXTSK22NxKcWloTsjBSlhqXcJoFhfju0yA5hyVYM2c0Gslc76mAXNd9pCVW8-0OIoxrbWgAAAABtVjAdAA'
FORCESUB = 'resvvfor'
AUTH = 1834364957

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException as er:
    print("Userbot Error ! Have you added SESSION while deploying??")
    print(er)
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
