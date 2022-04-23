from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

filmlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Umar ibn Hattob"),
            KeyboardButton(text="Umar ibn Abdulaziz")
        ],
        [
            KeyboardButton(text="Olamga nur sochgan oy"),
            KeyboardButton(text="Yunus Emro(Ishq safari)")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)