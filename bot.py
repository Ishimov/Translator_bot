from loader import dp, on_startup
import handlers
from aiogram import executor


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup
    )
