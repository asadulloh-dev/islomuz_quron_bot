from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

namoz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Namoz nima?"),
            KeyboardButton(text="Poklanish")
        ],
        [
            KeyboardButton(text="Namozni o'rganamiz"),
            KeyboardButton(text="Namoz va taxorat kitobi")
        ],
        [
            KeyboardButton(text="Namoz vaqtlari"),
            KeyboardButton(text="Turli namozlar")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)

namoz_organamiz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Namozni qanday o'qiladi"),
            KeyboardButton(text="Bomdod")
        ],
        [
            KeyboardButton(text="Peshin"),
            KeyboardButton(text="Asr")
        ],
        [
            KeyboardButton(text="Shom"),
            KeyboardButton(text="Xufton")
        ],
        [
            KeyboardButton(text=""),
            KeyboardButton(text="Jamoat namozlari")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ]
)

turli_namozlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Vitr namozi"),
            KeyboardButton(text="Juma namozi")
        ],
        [
            KeyboardButton(text="Janoza namozi"),
            KeyboardButton(text="Hayit namozi")
        ],
        [
            KeyboardButton(text="Istisqo namozi"),
            KeyboardButton(text="Kusuf namozi")
        ],
        [
            KeyboardButton(text="Taroveh namozi"),
            KeyboardButton(text="Nafl namozlar")
        ],
        [
            KeyboardButton(text="Musofirning namozi"),
            KeyboardButton(text="Bemorning namozi")
        ],
        [
            KeyboardButton(text="Tilovat sajdasi"),
            KeyboardButton(text="Ibratli namozlar")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ]
)

namoz_video = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Erkaklar"),
            KeyboardButton(text="Ayollar")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)