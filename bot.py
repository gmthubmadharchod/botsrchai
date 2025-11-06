import asyncio
import sys

# Fix for Python 3.10+ on Windows/RDP: Create event loop before importing Pyrogram
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Ensure event loop exists before importing Pyrogram
try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

from pyrogram import Client
from pyrogram.types import BotCommand
from config import API_ID, API_HASH, BOT_TOKEN

class Bot(Client):

    def __init__(self):
        super().__init__(
            "idfinderpro",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="IdFinderPro"),
            workers=100,  # Increased workers for better concurrency
            sleep_threshold=10,
            max_concurrent_transmissions=10,  # Allow multiple simultaneous uploads/downloads
            no_updates=False,
            takeout=False
        )

      
    async def start(self):
            
        await super().start()
        
        # Set bot commands menu
        await self.set_bot_commands([
            BotCommand("start", "Start the bot"),
            BotCommand("help", "Get help guide"),
            BotCommand("login", "Login with Telegram"),
            BotCommand("logout", "Logout account"),
            BotCommand("settings", "Forward settings"),
            BotCommand("batch", "Batch download"),
            BotCommand("premium", "Premium membership info"),
            BotCommand("redeem", "Redeem premium code"),
            BotCommand("cancel", "Cancel download")
        ])
        
        print('='*50)
        print('RESTRICTED CONTENT DOWNLOAD BOT STARTED')
        print('Made by: Surya (@tataa_sumo)')
        print('Channel: @idfinderpro')
        print('='*50)

    async def stop(self, *args):

        await super().stop()
        print('Bot Stopped Bye')

Bot().run()
