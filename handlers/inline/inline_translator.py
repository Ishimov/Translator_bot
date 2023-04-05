from aiogram.types import InlineQuery

from loader import dp, bot
from translator.translator import get_translation_item

@dp.inline_handler()
async def inline_translator(inline_query: InlineQuery) -> None:
    item = await get_translation_item(inline_query)
    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item],
                                  cache_time=1)