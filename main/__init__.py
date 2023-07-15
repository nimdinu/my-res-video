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
BOT_TOKEN = '5499781157:AAG75HAazC2254qlnPpszdQviCwcnz7a4OQ'
SESSION = 'BQBZbakAY0754StrKWn7regyOyZRpAziwcikWhGaZbg6spGk4606VVBi5-Ap0SvboMaNvcq2XWbz6uksFQ2mO1eABiv3DPx7nLkvH0edfgkEF7PkVegHxbMTE1Oiv6VEHC1fMlTN40RQhxBIO9L-M8AY9rHijHRoygYr6FhvG6XzSmWjmFfHj_wqqlKeaEo9ZnenUEXIam57FP4JrHfaS0DYN3XyfQdChPREklazy_dcODOtpBAzOUQUDzvnUv54ucxD_RIL1q_DmvOO3B9nKvjxpj2LLlKnw1q8WuhUu0GHFfmx7_423gXsezstU04cyqwVg1elDuqdEpf32_wi-jHPbsKIJAAAAABtVjAdAA'
FORCESUB = 'resvvfor'
AUTH = 1834364957

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
