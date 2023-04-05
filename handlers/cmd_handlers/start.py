from aiogram.types import Message

from loader import dp

@dp.message_handler(commands=['start'])
async def cmd_help(message: Message) -> None:
    await message.answer(
        text=f'Добро пожаловать, {message.from_user.full_name}!'
        )