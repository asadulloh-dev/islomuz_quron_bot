from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_keyb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Statistika"),
            KeyboardButton(text="Reklama")
        ],
        [
            KeyboardButton(text="Foydalanuvchilar"),
        ]
    ],
    resize_keyboard=True
)