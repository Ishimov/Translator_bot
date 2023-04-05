from aiogram import Bot, Dispatcher
from config import bot_config
from utils.set_bot_commands import set_default_commands

bot = Bot(token=bot_config.BOT_TOKEN)
dp = Dispatcher(bot=bot)

async def on_startup(_):
    await set_default_commands(dp=dp)
    # await database_start()