from aiogram import Bot, Dispatcher
from aiogram.utils.callback_data import CallbackData

from config import bot_config
from utils.set_bot_commands import set_bot_commands
from database.db_function import db_start

bot = Bot(token=bot_config.BOT_TOKEN)
dp = Dispatcher(bot=bot)

cb = CallbackData('ikb', 'action')

async def on_startup(_):
    await set_bot_commands(dp=dp)
    db_start()