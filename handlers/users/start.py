import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters import IsPrivate
from keyboards.default.menu_keyboard import menu
from data.config import ADMINS

from loader import dp, db, bot

import logging


@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message):
    name = message.from_user.username
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=message.from_user.full_name,
                    email=f"@{name}")
    except sqlite3.IntegrityError:
        pass

    await message.answer(f"Assalomu alaykum va rohmatulloh, <b>{message.from_user.full_name}</b>!\n"
                         f"", reply_markup=menu)

    # Adminga xabar beramiz
    count = db.count_users()[0]

    msg = f"{message.from_user.username} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)
