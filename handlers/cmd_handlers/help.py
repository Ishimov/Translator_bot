from aiogram.types import Message

from loader import dp
from config.bot_config import DEFAULT_COMMANDS

@dp.message_handler(commands=['help'])
async def cmd_help(message: Message) -> None:
    text = [f'/{command} - {desk}' for command, desk in DEFAULT_COMMANDS]
    await message.answer(text="\n".join(text))