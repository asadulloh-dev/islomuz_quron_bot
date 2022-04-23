import asyncio
import sqlite3

from aiogram.dispatcher.filters import Command

from keyboards.default.admin_keyboard import admin_keyb

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(Command('adminstart'), user_id=ADMINS)
async def admstart(mes: types.Message):
    await mes.answer("Admin panel", reply_markup=admin_keyb)


@dp.message_handler(text="Foydalanuvchilar", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    for user in users:
        await message.answer(user)


@dp.message_handler(text="reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    rek_mes = message.reply_to_message.message_id
    n = 0
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        try:
            await bot.forward_message(chat_id=user_id, from_chat_id=735024727, message_id=rek_mes)
            await asyncio.sleep(0.1)
            n += 1
        except:
            pass
    await message.answer(f"Ushbu xabar {n} ta foydalanuvchiga yetib bordi.")


@dp.message_handler(text="Statistika", user_id=ADMINS)
async def stat(mes: types.Message):
    users = db.select_all_users()

    await mes.answer(f"Ushbu botda {len(users)} foydalanuvchi bor")


@dp.message_handler(text="Qo'shish", user_id=ADMINS)
async def add_us(mes: types.Message):
    id_name = list(mes.reply_to_message.text.split())
    id_raqam = int(id_name[0])
    name = id_name[1]
    if len(id_name) == 3:
        email = id_name[2]
    else:
        email = None

    try:
        db.add_user(id_raqam, name, email)
    except sqlite3.IntegrityError:
        pass
    await mes.answer(f"{id_raqam} raqamli {name} {email}")


@dp.message_handler(text="/cleanesdatabases", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")


@dp.message_handler(text="IDLAR", user_id=ADMINS)
async def ids(mes: types.Message):
    users = db.select_all_users()
    for user in users:
        await mes.answer(user[0])


@dp.message_handler(text="USERNAMES")
async def userns(mes: types.Message):
    users = db.select_all_users()
    for user in users:
        try:
            await mes.answer(user[2])
        except:
            await mes.answer("None")