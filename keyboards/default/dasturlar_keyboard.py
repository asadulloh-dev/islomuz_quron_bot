from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

dasturlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Qur'onga oid"),
            KeyboardButton(text="Siyratga oid")
        ],
        [
            KeyboardButton(text="Namozga oid"),
            KeyboardButton(text="Arab tiliga oid")
        ],
        [
            KeyboardButton(text="Adabiyotlar"),
            KeyboardButton(text="Boshqalar")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)