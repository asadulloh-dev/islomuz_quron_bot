from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

quronga = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tafsiri Hilol", callback_data="Tafsiri Hilol")
        ],
        [
            InlineKeyboardButton(text="Qur'oni Karim", callback_data="qurondasturi")
        ],
        [
            InlineKeyboardButton(text="Quran Uzbek", callback_data="quranuzbek")
        ]
    ]
)

siyratga = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Payg'ambarlar qissasi", callback_data="payg'ambarlar")
        ],
        [
            InlineKeyboardButton(text="Saodat asri qissalari", callback_data="saodatasri")
        ],
        [
            InlineKeyboardButton(text="Oltin silsila", callback_data="oltinsilsila")
        ]
    ]
)

namozga = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Namoz", callback_data="namozdasturi")
        ],
        [
            InlineKeyboardButton(text="Muslim taqvim", callback_data="muslimtaqvim")
        ]
    ]
)

arabtiliga = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Arab alifbosi", callback_data="arabalifbosi"),
        ],
        [
            InlineKeyboardButton(text="Arab tilini o'rganaman", callback_data="araborganaman")
        ],
        [
            InlineKeyboardButton(text="Arab tili va tajvid", callback_data="arabtilivatajvid")
        ],
        [
            InlineKeyboardButton(text="Tartil", callback_data="tartil")
        ],
        [
            InlineKeyboardButton(text="Muallimi soniy", callback_data="muallimi soniy")
        ]
    ]
)

adabiyotlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Solihlar gulshani", callback_data="solihlargulshani")
        ],
        [
            InlineKeyboardButton(text="Hilol eBook", callback_data="hilolebook")
        ],
        [
            InlineKeyboardButton(text="Gunohi kabiralar", callback_data="gunohikabiralar")
        ]

    ]
)

boshqadasturlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Asmaul husna", callback_data="asmaulhusna"),
        ],
        [
            InlineKeyboardButton(text="Zikr ahlidan so'rang", callback_data="zikrahli")
        ],
        [
            InlineKeyboardButton(text="Zikr va duolar", callback_data="zikrvaduolar")
        ],
        [
            InlineKeyboardButton(text="Qirq hadisi qudsiy", callback_data="qirq")
        ],
        [
            InlineKeyboardButton(text="Olim bola", callback_data="olimbola"),
        ],
        [
            InlineKeyboardButton(text="Zukko bolajon", callback_data="zukko")
        ]
    ]
)