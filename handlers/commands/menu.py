from aiogram.types import Message

from loader import dp
from keyboards.inline.client import menu_ikb


@dp.message_handler(commands=['menu'])
async def cmd_menu(message: Message) -> None:
    await message.answer(text='Основное меню бота:',
                         reply_markup=menu_ikb())