#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 1735265
API_HASH = '3d35e17cfbbe90c1bc69baf97cd52016'
BOT_TOKEN = '6329273158:AAH6OVMPuo4Xtvz1jFTmNf6tOhqDqeR5Zbs'
SESSION = 'BQAaemEAjWsifkL8X-y36O_ospvAXoAbSQlJFMrc5ZpwcOwLj18bs_cpSNwQehNDzXAwI_0_ZA5INwTFn4IcEy92LvlIN9GFbDyQcJ7CWTtm32EclxUQCNpUON6YZrWffxq5oZoaTjoNPqX2gyi77MLvGsVuyAQR5jEmq8zBKzhO6aE2D8fQNUNmUvl9STFYANWya8Yx2O2F-0Q2xF190OSVWMrBR6IDtsPZ4IQuKRZyObpYHO5vCsJ5E6kS4KEkfeXRjRvndRYOvgROQx2qusQWftU3R2dBL650Z3LkmEbAG48gZ4MNuhEpD1AR4yBtN3EiJU1XzWAA-PulF9QHbyRPrFP2qAAAAABCl0-TAA'
FORCESUB = 'nimbackup'
AUTH = 1117212563

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
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
