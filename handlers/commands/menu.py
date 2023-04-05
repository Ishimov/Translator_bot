from aiogram.types import Message

from loader import dp
from keyboards.inline.inline_kb import menu_ikb


@dp.message_handler(commands=['menu'])
async def cmd_menu(msg: Message = None) -> None:
    await msg.answer(text='Основное меню бота:',
                     reply_markup=menu_ikb())