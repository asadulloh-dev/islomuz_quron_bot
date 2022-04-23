from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📖 Qur'on"),
            KeyboardButton(text="Hadis")
        ],
        [
            KeyboardButton(text="🕌 Namoz"),
            KeyboardButton(text="☪ Ro'za")
        ],
        [
            KeyboardButton(text="🤲 Duo va zikrlar"),
            KeyboardButton(text="🧑🏻‍🏫 Darslar")
        ],
        [
            KeyboardButton(text="📲 Dasturlar"),
            KeyboardButton(text="📚 Kitoblar")
        ],
        [
            KeyboardButton(text="📹 Multfilmlar"),
            KeyboardButton(text="🎞 Islomiy Filmlar")
        ],
        [
            KeyboardButton(text="✅ Foydali bo'lim"),
            KeyboardButton(text="💝 Hayriya")
        ],
        [
            KeyboardButton(text="💌 Loyihani qo'llab-quvvatlash")
        ]
    ],
    resize_keyboard=True
)

quron_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tafsiri Hilol"),
            KeyboardButton(text="O'zbek tilidagi ma'nolari tarjimasi")
        ],
        [
            KeyboardButton(text="Audio Qur'on"),
            KeyboardButton(text="Qur'on fazilatlari")
        ],
        [
            KeyboardButton(text="Bosh menu")

        ]
    ],
    resize_keyboard=True
)
uzb_quran =  ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Shayx Muhammad Sodiq Muhammad Yusuf"),
        ],
        [
            KeyboardButton(text="Afzal Rafiqov"),
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)


audio_quran = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Abdulbosit qori Qobilov"),
            KeyboardButton(text="Muhammadloiq qori")
        ],
        [
            KeyboardButton(text="Hasanxon Yahyo Abdulmajid"),
            KeyboardButton(text="Mishariy Al Afasiy")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)
