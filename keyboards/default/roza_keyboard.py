from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

roza = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ramazon 2022")
        ],
        [
            KeyboardButton(text="Ro'za nima?"),
            KeyboardButton(text="Ro'zaning shartlari")
        ],
        [
            KeyboardButton(text="Ro'zaning turlari"),
            KeyboardButton(text="Ro'zaning niyati")
        ],
        [
            KeyboardButton(text="Saharlik va iftorlik"),
            KeyboardButton(text="Ro'zaning mustahablari")
        ],
        [
            KeyboardButton(text="Ro'zaning buzilish xollari"),
            KeyboardButton(text="Tutish makruh bo'lgan kunlar")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)