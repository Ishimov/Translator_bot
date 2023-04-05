from aiogram.types import Message

from loader import dp

# Эхо хендлер, куда летят текстовые сообщения без указанного состояния или фильтра
@dp.message_handler(state=None)
async def bot_echo(message: Message) -> None:
   await message.answer(
      text=f"Эхо без состояния или фильтра.\nСообщение: {message.text}"
      )
