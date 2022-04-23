from loader import dp

from aiogram.types import Message
from keyboards.default.filmlar_keyboard import filmlar


@dp.message_handler(text="🎞 Islomiy Filmlar")
async def islomiyfilmlar(mes: Message):
    await mes.answer("Islomiy seriallar\n"
                     "Manba: @azoncinema"
                     "\nBoshqa serial va kinolar uchun: @azoncinema", reply_markup=filmlar)

@dp.message_handler(text="Umar ibn Hattob")
async def umar(mes: Message):
    await mes.answer(""" "Umar ibn Hattob" seriali
To'liq shaklda: https://t.me/islomiy_mediya/88    

HD formatda ko'rish uchun: https://t.me/azoncinema/140

@islomuz_quron_bot""")
    mediya = [
        "https://t.me/islomiy_mediya/88",
        "https://t.me/islomiy_mediya/89",
        "https://t.me/islomiy_mediya/90",
        "https://t.me/islomiy_mediya/91",
        "https://t.me/islomiy_mediya/92"
    ]
    for med in mediya:
        await mes.answer_video(med, caption="@islomuz_quron_bot")
    await mes.answer("Davomi: https://t.me/islomiy_mediya/88\n@islomuz_quron_bot")


@dp.message_handler(text="Umar ibn Abdulaziz")
async def ibnabdulaziz(mes: Message):
    await mes.answer("""
"Umar ibn Abdulaziz" seriali
To'liq shaklda: https://t.me/islomiy_mediya/151""")
    mediya = [
        "https://t.me/islomiy_mediya/151",
        "https://t.me/islomiy_mediya/152",
        "https://t.me/islomiy_mediya/153",
        "https://t.me/islomiy_mediya/154",
        "https://t.me/islomiy_mediya/155"
    ]
    for med in mediya:
        await mes.answer_video(med, caption="@islomuz_quron_bot")
    await mes.answer("Davomi: https://t.me/islomiy_mediya/151\n@islomuz_quron_bot")


@dp.message_handler(text="Olamga nur sochgan oy")
async def nuroy(mes: Message):
    await mes.answer("""
"Olamga nur sochgan oy" seriali
To'liq shaklda: https://t.me/islomiy_mediya/120""")
    mediya = [
        "https://t.me/islomiy_mediya/120",
        "https://t.me/islomiy_mediya/121",
        "https://t.me/islomiy_mediya/122",
        "https://t.me/islomiy_mediya/123",
        "https://t.me/islomiy_mediya/124"
    ]
    for med in mediya:
        await mes.answer_video(med, caption="@islomuz_quron_bot")
    await mes.answer("Davomi: https://t.me/islomiy_mediya/120\n@islomuz_quron_bot")


@dp.message_handler(text="Yunus Emro(Ishq safari)")
async def yunusemro(mes: Message):
    await mes.answer("""
"Yunus emro(Ishq safari)" seriali
To'liq shaklda: https://t.me/islomiy_mediya/391

HD formatda ko'rish uchun: https://t.me/azoncinema/10""")
    mediya = [
        "https://t.me/islomiy_mediya/391",
        "https://t.me/islomiy_mediya/392",
        "https://t.me/islomiy_mediya/393",
        "https://t.me/islomiy_mediya/394",
        "https://t.me/islomiy_mediya/395"
    ]
    for med in mediya:
        await mes.answer_video(med, caption="@islomuz_quron_bot")
    await mes.answer("Davomi: https://t.me/islomiy_mediya/391\n@islomuz_quron_bot")