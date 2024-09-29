import asyncio
import logging
from urllib.parse import unquote
from pyrogram import Client
from pyrogram.raw.types import RequestWebView

# Set up logger
logger = logging.getLogger(__name__)

class YourTelegramBot:
    def __init__(self, api_id, api_hash):
        self.client = Client("my_bot", api_id, api_hash)
        self.thread = 1  # Example thread identifier
        self.name = "YourBotName"

    async def get_tg_web_data(self):
        """
        Connects to the Telegram client, sends a WebView request to the bot 'BlumCryptoBot',
        and extracts the tgWebAppData from the returned URL.

        Returns:
            str: Extracted tgWebAppData if successful,
                 False if banned, or None in case of failure.
        """
        await self.client.connect()

        try:
            web_view = await self.client.invoke(RequestWebView(
                peer=await self.client.resolve_peer('BlumCryptoBot'),
                bot=await self.client.resolve_peer('BlumCryptoBot'),
                platform='android',
                from_bot_menu=False,
                url='https://telegram.blum.codes/'
            ))

            auth_url = web_view.url

        except Exception as err:
            logger.error(f"main | Thread {self.thread} | {self.name} | {err}")

            if 'USER_DEACTIVATED_BAN' in str(err):
                logger.error(f"login | Thread {self.thread} | {self.name} | USER BANNED")
                await self.client.disconnect()
                return False

            await self.client.disconnect()
            return None

        await self.client.disconnect()

        try:
            tg_web_app_data = unquote(
                string=unquote(
                    string=auth_url.split('tgWebAppData=')[1].split('&tgWebAppVersion')[0]
                )
            )
            return tg_web_app_data

        except (IndexError, KeyError):
            logger.error(f"main | Thread {self.thread} | {self.name} | Invalid URL format")
            return None

    async def run(self):
        data = await self.get_tg_web_data()
        print("Extracted Data:", data)

if __name__ == "__main__":
    # Replace these with your actual API credentials
    API_ID = ""  # Your API ID
    API_HASH = ""  # Your API Hash

    bot = YourTelegramBot(API_ID, API_HASH)
    
    # Run the bot
    asyncio.run(bot.run())
