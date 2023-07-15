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
SESSION = 'BQBZbakAwcwhY7SWliiLoM8OhajXHxIhk7RzKK4inlgjsrkZj2kTeD2j5wt1BvAC2ulrkALlb6BMj45QXyoXchDQw44MJbh2fRFmOBZ37XDEgq2Qxp4_K76JxJdP38xbYmia4_F_s8ARhUzhexZiw47Xb5OYTLJQjYk0YA1W8UINYrWQYU5DYSRmpghlQTLo-o6uVzMAfX7DO8nSzro0SFNkyZgFfvbfuYw04_fGDOUhv_0RHRyJ8h3dfn0cc9y0QlWOVivoynK52H0jU4hW0nxX8Di0FhR_hKZ5M0MlDDIyJUnPjKjWUms1Dv8OZMl-gAf0_hBO7NHq6BQytPruUgM0liIfQAAAAABtVjAdAA'
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
