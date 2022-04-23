from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

hadis_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Al Jomi' As Sahih", callback_data="jomisahih")
        ],
        [
            InlineKeyboardButton(text="Oltin silsila", callback_data="oltinsilsila")
        ]
    ]
)