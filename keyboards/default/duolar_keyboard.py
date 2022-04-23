from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

duolar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tongi va kechki zikrlar")
        ],
        [
            KeyboardButton(text="Qur'onda kelgan duolar")
        ],
        [
            KeyboardButton(text="Sunnatda kelgan duolar")
        ],
        [
            KeyboardButton(text="Duolar kitobi")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)