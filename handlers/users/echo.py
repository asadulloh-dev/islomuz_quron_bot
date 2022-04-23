from aiogram import types
from aiogram.types import ContentTypes
from filters import IsPrivate

from loader import dp


# Echo bot
@dp.message_handler(IsPrivate(), state=None)
async def bot_echo(message: types.Message):
    await message.answer("<b>❌ Noto'gri matn kiritdingiz! !!!</b>\n"
                         "Yordam uchun: /help")


@dp.message_handler(IsPrivate(), content_types=ContentTypes.ANY)
async def bot_error(message: types.Message):
    await message.answer("<b>❌ Foydalanuvchi bunday narsalar yubormang iltimos!</b>\n"
                         "Yordam: /help")
