from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from filters import IsPrivate

from loader import dp


@dp.message_handler(CommandHelp(), IsPrivate())
async def bot_help(message: types.Message):
    text = ("Yordam: \n"
            "Botni ishga tushirish: /start\n\n"
            "Taklif va murojaatlar: @Asadulloha_bot")

    await message.answer(text)
