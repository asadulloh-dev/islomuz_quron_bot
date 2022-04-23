from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kitoblar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Qur'oni Karim ma'nolari tarjimasi A.Mansur", callback_data="mansur")
        ],
        [
            InlineKeyboardButton(text="Qur'on qalblar shifosi", callback_data="qalblarshifosi")
        ],
        [
            InlineKeyboardButton(text="Tarixi Muhammadiy", callback_data="tariximuhammadiy")
        ],
        [
            InlineKeyboardButton(text="Musulmonning odobi", callback_data="odobi")
        ],
        [
            InlineKeyboardButton(text="Siz payg'ambarni ko'rganmisiz", callback_data="korganmisiz")
        ],
        [
            InlineKeyboardButton(text="Shamoili Muhammadiy", callback_data="shamoiliy")
        ],
        [
            InlineKeyboardButton(text="Qalblar kashfiyoti.Imom G'azzoliy", callback_data="qalblarkashfiyoti")
        ],
        [
            InlineKeyboardButton(text="Hazrati Abu Bakr Siddiq", callback_data="abubakr")
        ],
        [
            InlineKeyboardButton(text="Hazrati Umar ibn Xattob", callback_data="umar")
        ],
        [
            InlineKeyboardButton(text="Taxorat va Namoz", callback_data="taxoratvanamoz")
        ],
        [
            InlineKeyboardButton(text="Baxtiyor oila", callback_data="baxtiyoroila")
        ],
        [
            InlineKeyboardButton(text="Rosululloh alayhisalomning bir kunlari", callback_data="birkunlari")
        ],
        [
            InlineKeyboardButton(text="Musnadi Abu Hanifa", callback_data="abuhanifa")
        ]
    ]
)