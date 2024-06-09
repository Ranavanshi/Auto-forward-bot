"""
from config import Config
from config import LOGGER
from pyrogram import Client, __version__
import asyncio
BOT_USERNAME=Config.BOT_USERNAME

class User(Client):
    def __init__(self):
        super().__init__(
            Config.SESSION,
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            workers=10
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        if BOT_USERNAME:
            await User.send_message(self, chat_id=BOT_USERNAME, text="/forward")
        usr_bot_me = await self.get_me()
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
"""
from pyrogram import Client, __version__

from config import API_HASH, APP_ID, LOGGER, \
    SESSION


class User(Client):
    def __init__(self):
        super().__init__(
            "userbot",
            api_hash=API_HASH,
            api_id=API_ID,
            session_string=SESSION,
            workers=20
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        try: await self.export_session_string()
        except: pass
        usr_bot_me = await self.get_me()
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
