from loader import dp

from aiogram.types import Message

from keyboards.default.multfilmlar_keyboard import multfilmlar

@dp.message_handler(text="📹 Multfilmlar")
async def multfilm(mes: Message):
    await mes.answer("Multfilmlar bo'limi:\nManba: https://www.youtube.com/c/Portalislomuz",reply_markup=multfilmlar)


@dp.message_handler(text="Qur'onda zikri kelgan insonlar qissasi")
async def qzki(mes: Message):
    await mes.answer("Qur'onda zikri kelgan insonlar qissasi\nTo'liq holda: https://t.me/islomiy_mediya/582")
    await mes.answer_video("https://t.me/islomiy_mediya/583", caption="Davomi: https://t.me/islomiy_mediya/582")


@dp.message_handler(text="Qur'onda zikri kelgan ayollar qissasi")
async def qzka(mes: Message):
    await mes.answer("Qur'onda zikri kelgan ayollar qissasi\nTo'liq holda: https://t.me/islomiy_mediya/613")
    await mes.answer_video("https://t.me/islomiy_mediya/614", caption="Davomi: https://t.me/islomiy_mediya/613")
    await mes.answer_video("https://t.me/islomiy_mediya/615", caption="Davomi: https://t.me/islomiy_mediya/613")


@dp.message_handler(text="Qur'onda nomi kelgan jonzotlar")
async def qnkj(mes: Message):
    await mes.answer("Qur'onda zikri kelgan jonzotlar qissasi\nTo'liq holda: https://t.me/islomiy_mediya/499")
    await mes.answer_video("https://t.me/islomiy_mediya/520", caption="https://t.me/islomiy_mediya/499")


@dp.message_handler(text="Qur'onda kelgan ajoyibotlar")
async def qnkj(mes: Message):
    await mes.answer("Qur'onda kelgan ajoyibotlar qissasi\nTo'liq holda: https://t.me/islomiy_mediya/550")
    await mes.answer_video("https://t.me/islomiy_mediya/551", caption="Davomi: https://t.me/islomiy_mediya/550")


@dp.message_handler(text="Multfilmlarning barchasi")
async def barchamultiklar(mes: Message):
    await mes.answer("Barcha multfilmlar quyidagi dasturda mavjud")
    await mes.answer_document("https://t.me/Englishfor_IT/14", caption="Multfilmlar dasturi\n"
                                                                       "Android tizimi uchun\n"
                                                                       "@islomuz_quron_bot")