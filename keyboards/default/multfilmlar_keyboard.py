from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

multfilmlar = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="Qur'onda zikri kelgan insonlar qissasi")
        ],
        [
            KeyboardButton(text="Qur'onda zikri kelgan ayollar qissasi")
        ],
        [
            KeyboardButton(text="Qur'onda nomi kelgan jonzotlar")
        ],
        [
            KeyboardButton(text="Qur'onda kelgan ajoyibotlar")
        ],
        [
            KeyboardButton(text="Multfilmlarning barchasi")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)