from aiogram.types import CallbackQuery

from loader import dp, bot, cb
from keyboards.inline.client import settings_ikb, langauge_ikb, menu_ikb
from database.db_function import edit_profile, language_select


@dp.callback_query_handler(cb.filter(action='settings'))
async def call_settings(callback: CallbackQuery):
    await bot.edit_message_text(chat_id=callback.message.chat.id,
                                text=f'Ваши настройки, {callback.message.chat.first_name}',
                                message_id=callback.message.message_id,
                                reply_markup=settings_ikb())


@dp.callback_query_handler(cb.filter(action='tutorial'))
async def call_tutorial(callback: CallbackQuery):
    await callback.answer('Tutorial')


@dp.callback_query_handler(cb.filter(action='lang_ust'))
async def call_lang_ust(callback: CallbackQuery):
    await callback.answer(await language_select(callback.from_user.id))


@dp.callback_query_handler(cb.filter(action='language'))
async def call_language(callback: CallbackQuery):
    await bot.edit_message_text(chat_id=callback.message.chat.id,
                                text='Выберете язык для перевода:',
                                message_id=callback.message.message_id,
                                reply_markup=langauge_ikb())
    

@dp.callback_query_handler(cb.filter(action='back_language_settings'))
async def call_back_language(callback: CallbackQuery):
    await call_settings(callback)


@dp.callback_query_handler(cb.filter(action='back_settings_menu'))
async def call_back_settings(callback: CallbackQuery):
    await bot.edit_message_text(chat_id=callback.message.chat.id,
                                text='Основное меню:',
                                message_id=callback.message.message_id,
                                reply_markup=menu_ikb())


@dp.callback_query_handler(lambda callback: 'lang_' in callback.data)
async def call_language_selection(callback: CallbackQuery):
    await edit_profile(callback.from_user.id, callback.data[9:])
    await callback.answer(f'Выбран {callback.data[9:]} язык!')

