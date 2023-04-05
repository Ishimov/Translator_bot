from config.bot_config import DEFAULT_COMMANDS
from aiogram.types import BotCommand
from aiogram import Dispatcher

async def set_bot_commands(dp: Dispatcher) -> None:
    await dp.bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )