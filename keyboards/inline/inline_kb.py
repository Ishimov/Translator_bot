from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import cb

def menu_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Настройки бота',
                              callback_data=cb.new('settings')),
        InlineKeyboardButton(text='Туториал',
                             callback_data=cb.new('tutorial'))],
        [InlineKeyboardButton(text='Установленный язык',
                              callback_data=cb.new('lang_ust'))]
    ])
    return ikb

def settings_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Язык',
                              callback_data=cb.new('language')),
        InlineKeyboardButton(text='<< Назад',
                             callback_data=cb.new('back_settings_menu'))]
    ])
    return ikb

def langauge_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='EN',
                              callback_data=cb.new('lang_EN')),
        InlineKeyboardButton(text='FR',
                             callback_data=cb.new('lang_FR')),
        InlineKeyboardButton(text='IT',
                             callback_data=cb.new('lang_IT'))],
        [InlineKeyboardButton(text='DE',
                              callback_data=cb.new('lang_DE')),
        InlineKeyboardButton(text='KO',
                             callback_data=cb.new('lang_KO')),
        InlineKeyboardButton(text='TR',
                             callback_data=cb.new('lang_TR'))],
        [InlineKeyboardButton(text='<< Назад',
                             callback_data=cb.new('back_language_settings'))]
    ])
    return ikb