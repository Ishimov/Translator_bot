from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineQuery

import uuid
import flag
from googletrans import Translator

from database.db_function import language_select

async def get_translation_item(inline_query: InlineQuery) -> InlineQueryResultArticle:

    text = inline_query.query or 'Введи текст...'
    tr = Translator()
    user_id = inline_query.from_user.id
    lang = await language_select(user_id=user_id)

    if lang == 'EN':
        flag_lang = flag.flag('gb')
    elif lang == 'KO':
        flag_lang = flag.flag('kr')
    else:
        flag_lang = flag.flag(lang)

    result = tr.translate(text, dest=lang)
    out = f'🇷🇺 {text}\n\n{flag_lang} {result.text}'
    output_content = InputTextMessageContent(out)

    item = InlineQueryResultArticle(input_message_content=output_content,
                                    id=str(uuid.uuid4()),
                                    title=result.text,
                                    description=lang)
    
    return item