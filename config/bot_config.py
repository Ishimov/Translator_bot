from dotenv import dotenv_values

BOT_TOKEN = dotenv_values('.env')['BOT_TOKEN']

DEFAULT_COMMANDS = (
    ('start', 'Запустить бота'),
    ('help', 'Доступные команды'),
    ('menu', 'Основное меню')
)