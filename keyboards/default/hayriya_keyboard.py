from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

hayriya_guruhlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="VAQF"),
            KeyboardButton(text="Yurak Amri")
        ],
        [
            KeyboardButton(text="Sahovat Namangan"),
            KeyboardButton(text="Mehrob himmati")
        ],
        [
            KeyboardButton(text="Mehrli qo'llar"),
            KeyboardButton(text="Ezgu amal")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)