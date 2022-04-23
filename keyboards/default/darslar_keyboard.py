from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

darslar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ruhiy tarbiya"),
            KeyboardButton(text="Qur'on bilan tanishuv"),
        ],
        [
            KeyboardButton(text="Muallimi soniy"),
            KeyboardButton(text="Arab tili"),
        ],
        [
            KeyboardButton(text="Ramazon 2014"),
            KeyboardButton(text="Qur'on qalblar shifosi")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)

ruhiy_tarbiya = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Poklanish (1-qism)"),
            KeyboardButton(text="Poklanish (2-qism)")
        ],
        [
            KeyboardButton(text="Tiklanish (1-qism)"),
            KeyboardButton(text="Tiklanish (2-qism)")
        ],
        [
            KeyboardButton(text="Xulqlanish (1-qism)"),
            KeyboardButton(text="Xulqlanish (2-qism)")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]

    ],
    resize_keyboard=True
)
