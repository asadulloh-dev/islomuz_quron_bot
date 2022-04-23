from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

foydali_bolim = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Allohning 99 ismlari"),
            KeyboardButton(text="40 farz")
        ],
        [
            KeyboardButton(text="Islomning 5 ustuni"),
            KeyboardButton(text="Amallarning hukmlari")
        ],
        [
            KeyboardButton(text="Salovat"),
            KeyboardButton(text="Manbalar va foydali saytlar")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)