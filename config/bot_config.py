from dotenv import dotenv_values

BOT_TOKEN = dotenv_values('.env')['BOT_TOKEN']

DEFAULT_COMMANDS = (
    ('start', 'Запустить бота'),
    ('help', 'Доступные команды')
)

HELP_COMMAND = '''
<b>Cписок команд:</b>
<b>/start</b> - <em>запуск бота</em>
<b>/help</b> - <em>список команд</em>'''