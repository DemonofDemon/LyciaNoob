import requests
import rapidjson as json
from PIL import Image
import os
import asyncio
import re
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)

import logging

from telegram import Update, ForceReply

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)




#vars

API_ID=2114829
TOKEN="1688991183:AAE5Y2HIroqZKRRggWci4ofkdevdEnMf4ec"
API_HASH="e90ddf1f46ac58ee0c267eff1e0548de",

#initiators

telethn = TelegramClient("lycia", API_ID, API_HASH)



messageprivate = '''
Hi, I'm Anime Quotes Bot, We also have group Management Bots.
'''

messagegroup = '''
Hi, I'm Anime Quotes bot, We also have Group Management Bots.
'''



async def start(_, message):
    self = await anime.get_me()
    busername = self.username
    if message.chat.type != "private":
        await message.reply_text(messagegroup)
        return
    else:
        buttons = [[InlineKeyboardButton("Shinobu", url="https://t.me/TheShinobuRobot"),
                    ]]
        await message.reply_text(messageprivate, reply_markup=InlineKeyboardMarkup(buttons))



def quote(_, message):
    quote = requests.get("https://animechan.vercel.app/api/random").json()
    message.reply_text('`'+quote['quote']+'`\n '+quote['anime']+' (In '+quote['character']+')')


print(
    """
Please Follow Minato👀✨
""" 
)

def main() -> None:
	updater = Updater("TOKEN")
	dispatcher = updater.dispatcher
	
	
	dispatcher.add_handler(CommandHandler("start", start))
	dispatcher.add_handler(CommandHandler("quote", quote))
	updater.start_polling
	updater.idle

if __name__ == "__main__":
	main.()
	telethn.start(bot_token=TOKEN)

__name__ == "__main__"

