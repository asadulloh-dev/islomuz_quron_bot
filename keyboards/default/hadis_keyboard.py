from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

hadis = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Hadis nima?"),
            KeyboardButton(text="Hadis ilmi lug'ati")
        ],
        [
            KeyboardButton(text="Muhaddislar"),
            KeyboardButton(text="")
        ],
        [
            KeyboardButton(text="Islomning madori bo'lgan hadislar")
        ],
        [
            KeyboardButton(text="Hadisi Qudsiy"),
            KeyboardButton(text="Hadislar to'plami")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)

muhaddislar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Imom Al Buxoriy"),
            KeyboardButton(text="Imom Muslim")
        ],
        [
            KeyboardButton(text="Imom at Termiziy"),
            KeyboardButton(text="Abu Dovud")
        ],
        [
            KeyboardButton(text="Nasoiy"),
            KeyboardButton(text="Ibn Moja")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)

hadis4 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-hadis"),
            KeyboardButton(text="2-hadis")
        ],
        [
            KeyboardButton(text="3-hadis"),
            KeyboardButton(text="4-hadis")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)