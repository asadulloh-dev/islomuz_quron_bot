from loader import dp

from aiogram.types import Message, CallbackQuery

from keyboards.default.menu_keyboard import menu, audio_quran
from keyboards.inline.quran_inline import  muhammadloiq_inline, abdulbosit_inline, mishari_inline, xasanxon_inline

#          3.QORILAR AUDIO QUR'ON
@dp.message_handler(text="Audio Qur'on")
async def audio_quron(mes: Message):
    await mes.answer("Audio Qur'on", reply_markup=audio_quran)


@dp.message_handler(text="Bosh menu")
async def bosh_menu(mes: Message):
    await mes.answer("Audio Qur'on", reply_markup=menu)


@dp.message_handler(text="Abdulbosit qori Qobilov")
async def abdulbosiit_qobilov(mes: Message):
    await mes.answer("Abdulbosit qori Qobilov qiroatlari: ", reply_markup=abdulbosit_inline)


@dp.callback_query_handler(text="ab1")
async def ab1(call: CallbackQuery):
    ab1 = [
        "https://t.me/abdulbosit_qobilov/3",
        "https://t.me/abdulbosit_qobilov/4",
        "https://t.me/abdulbosit_qobilov/5",
        "https://t.me/abdulbosit_qobilov/6",
        "https://t.me/abdulbosit_qobilov/7",
        "https://t.me/abdulbosit_qobilov/8",
        "https://t.me/abdulbosit_qobilov/9",
        "https://t.me/abdulbosit_qobilov/10",
    ]
    for url in ab1:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ab2")
async def ab(call: CallbackQuery):
    ab1 = [
        "https://t.me/abdulbosit_qobilov/11",
        "https://t.me/abdulbosit_qobilov/12",
        "https://t.me/abdulbosit_qobilov/13",
        "https://t.me/abdulbosit_qobilov/14",
        "https://t.me/abdulbosit_qobilov/15",
        "https://t.me/abdulbosit_qobilov/16",
        "https://t.me/abdulbosit_qobilov/17",
        "https://t.me/abdulbosit_qobilov/18",
    ]
    for url in ab1:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ab3")
async def ab(call: CallbackQuery):
    ab1 = [
        "https://t.me/abdulbosit_qobilov/19",
        "https://t.me/abdulbosit_qobilov/20",
        "https://t.me/abdulbosit_qobilov/21",
        "https://t.me/abdulbosit_qobilov/22",
        "https://t.me/abdulbosit_qobilov/23",
        "https://t.me/abdulbosit_qobilov/24",
        "https://t.me/abdulbosit_qobilov/25",
        "https://t.me/abdulbosit_qobilov/26",
    ]
    for url in ab1:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ab4")
async def ab(call: CallbackQuery):
    ab1 = [
        "https://t.me/abdulbosit_qobilov/27",
        "https://t.me/abdulbosit_qobilov/28",
        "https://t.me/abdulbosit_qobilov/29",
        "https://t.me/abdulbosit_qobilov/30",
        "https://t.me/abdulbosit_qobilov/31",
        "https://t.me/abdulbosit_qobilov/32",
        "https://t.me/abdulbosit_qobilov/33",
        "https://t.me/abdulbosit_qobilov/34",
    ]
    for url in ab1:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ab5")
async def ab(call: CallbackQuery):
    ab1 = [
        "https://t.me/abdulbosit_qobilov/35",
        "https://t.me/abdulbosit_qobilov/36",
        "https://t.me/abdulbosit_qobilov/37",
        "https://t.me/abdulbosit_qobilov/38",
        "https://t.me/abdulbosit_qobilov/39",
        "https://t.me/abdulbosit_qobilov/40",
        "https://t.me/abdulbosit_qobilov/41",
        "https://t.me/abdulbosit_qobilov/42",
    ]
    for url in ab1:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ab6")
async def ab(call: CallbackQuery):
    ab1 = [
        "https://t.me/abdulbosit_qobilov/43",
        "https://t.me/abdulbosit_qobilov/44",
        "https://t.me/abdulbosit_qobilov/45",
        "https://t.me/abdulbosit_qobilov/46",
        "https://t.me/abdulbosit_qobilov/47",
        "https://t.me/abdulbosit_qobilov/48",
        "https://t.me/abdulbosit_qobilov/49",
        "https://t.me/abdulbosit_qobilov/50",
    ]
    for url in ab1:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ab7")
async def ab(call: CallbackQuery):
    ab1 = [
        "https://t.me/abdulbosit_qobilov/51",
        "https://t.me/abdulbosit_qobilov/52",
        "https://t.me/abdulbosit_qobilov/53",
        "https://t.me/abdulbosit_qobilov/54",
        "https://t.me/abdulbosit_qobilov/55",
        "https://t.me/abdulbosit_qobilov/56",
        "https://t.me/abdulbosit_qobilov/57",
        "https://t.me/abdulbosit_qobilov/58",
    ]
    for url in ab1:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ab8")
async def ab(call: CallbackQuery):
    ab1 = [
        "https://t.me/abdulbosit_qobilov/59",
        "https://t.me/abdulbosit_qobilov/60",
        "https://t.me/abdulbosit_qobilov/61",
        "https://t.me/abdulbosit_qobilov/62",
        "https://t.me/abdulbosit_qobilov/63",
        "https://t.me/abdulbosit_qobilov/64",
        "https://t.me/abdulbosit_qobilov/65",
        "https://t.me/abdulbosit_qobilov/66",
    ]
    for url in ab1:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ab9")
async def ab(call: CallbackQuery):
    ab1 = [
        "https://t.me/abdulbosit_qobilov/67",
        "https://t.me/abdulbosit_qobilov/68",
        "https://t.me/abdulbosit_qobilov/69",
        "https://t.me/abdulbosit_qobilov/70",
        "https://t.me/abdulbosit_qobilov/71",
        "https://t.me/abdulbosit_qobilov/72",
        "https://t.me/abdulbosit_qobilov/73",
        "https://t.me/abdulbosit_qobilov/74",
    ]
    for url in ab1:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ab10")
async def ab(call: CallbackQuery):
    ab1 = [
        "https://t.me/abdulbosit_qobilov/75",
        "https://t.me/abdulbosit_qobilov/76",
        "https://t.me/abdulbosit_qobilov/77",
        "https://t.me/abdulbosit_qobilov/78",
        "https://t.me/abdulbosit_qobilov/79",
        "https://t.me/abdulbosit_qobilov/80",
        "https://t.me/abdulbosit_qobilov/81",
        "https://t.me/abdulbosit_qobilov/82",
    ]
    for url in ab1:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ab11")
async def ab(call: CallbackQuery):
    ab1 = [
        "https://t.me/abdulbosit_qobilov/83",
        "https://t.me/abdulbosit_qobilov/84",
        "https://t.me/abdulbosit_qobilov/85",
        "https://t.me/abdulbosit_qobilov/86",
        "https://t.me/abdulbosit_qobilov/87",
        "https://t.me/abdulbosit_qobilov/88",
        "https://t.me/abdulbosit_qobilov/89",
        "https://t.me/abdulbosit_qobilov/90",
    ]
    for url in ab1:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ab12")
async def ab(call: CallbackQuery):
    ab1 = [
        "https://t.me/abdulbosit_qobilov/91",
        "https://t.me/abdulbosit_qobilov/92",
        "https://t.me/abdulbosit_qobilov/93",
        "https://t.me/abdulbosit_qobilov/94",
        "https://t.me/abdulbosit_qobilov/95",
        "https://t.me/abdulbosit_qobilov/96",
        "https://t.me/abdulbosit_qobilov/97",
        "https://t.me/abdulbosit_qobilov/98",
    ]
    for url in ab1:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ab13")
async def ab(call: CallbackQuery):
    ab1 = [
        "https://t.me/abdulbosit_qobilov/99",
        "https://t.me/abdulbosit_qobilov/100",
        "https://t.me/abdulbosit_qobilov/101",
        "https://t.me/abdulbosit_qobilov/102",
        "https://t.me/abdulbosit_qobilov/103",
        "https://t.me/abdulbosit_qobilov/104",
        "https://t.me/abdulbosit_qobilov/105",
        "https://t.me/abdulbosit_qobilov/106",
    ]
    for url in ab1:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ab14")
async def ab(call: CallbackQuery):
    ab1 = [
        "https://t.me/abdulbosit_qobilov/107",
        "https://t.me/abdulbosit_qobilov/108",
        "https://t.me/abdulbosit_qobilov/109",
        "https://t.me/abdulbosit_qobilov/110",
        "https://t.me/abdulbosit_qobilov/111",
        "https://t.me/abdulbosit_qobilov/112",
        "https://t.me/abdulbosit_qobilov/113",
        "https://t.me/abdulbosit_qobilov/114",
        "https://t.me/abdulbosit_qobilov/115",
        "https://t.me/abdulbosit_qobilov/116"
    ]
    for url in ab1:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.message_handler(text="Muhammadloiq qori")
async def muhammadloiq(mes: Message):
    await mes.answer("Muhammad Loiq qori qiroatlari: ", reply_markup=muhammadloiq_inline)


@dp.callback_query_handler(text="ml1")
async def ml(call: CallbackQuery):
    ml = [
        "https://t.me/muhammadloiq_qorii/8",
        "https://t.me/muhammadloiq_qorii/9",
        "https://t.me/muhammadloiq_qorii/10",
        "https://t.me/muhammadloiq_qorii/11",
        "https://t.me/muhammadloiq_qorii/12",
        "https://t.me/muhammadloiq_qorii/13",
        "https://t.me/muhammadloiq_qorii/14",
        "https://t.me/muhammadloiq_qorii/15",
    ]
    for url in ml:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ml2")
async def ml(call: CallbackQuery):
    ml = [
        "https://t.me/muhammadloiq_qorii/16",
        "https://t.me/muhammadloiq_qorii/17",
        "https://t.me/muhammadloiq_qorii/18",
        "https://t.me/muhammadloiq_qorii/19",
        "https://t.me/muhammadloiq_qorii/20",
        "https://t.me/muhammadloiq_qorii/21",
        "https://t.me/muhammadloiq_qorii/22",
        "https://t.me/muhammadloiq_qorii/23",
    ]
    for url in ml:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ml3")
async def ml(call: CallbackQuery):
    ml = [
        "https://t.me/muhammadloiq_qorii/24",
        "https://t.me/muhammadloiq_qorii/25",
        "https://t.me/muhammadloiq_qorii/26",
        "https://t.me/muhammadloiq_qorii/27",
        "https://t.me/muhammadloiq_qorii/28",
        "https://t.me/muhammadloiq_qorii/29",
        "https://t.me/muhammadloiq_qorii/30",
        "https://t.me/muhammadloiq_qorii/31",
    ]
    for url in ml:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ml4")
async def ml(call: CallbackQuery):
    ml = [
        "https://t.me/muhammadloiq_qorii/32",
        "https://t.me/muhammadloiq_qorii/33",
        "https://t.me/muhammadloiq_qorii/34",
        "https://t.me/muhammadloiq_qorii/35",
        "https://t.me/muhammadloiq_qorii/36",
        "https://t.me/muhammadloiq_qorii/37",
        "https://t.me/muhammadloiq_qorii/38",
        "https://t.me/muhammadloiq_qorii/39",
    ]
    for url in ml:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ml5")
async def ml(call: CallbackQuery):
    ml = [
        "https://t.me/muhammadloiq_qorii/40",
        "https://t.me/muhammadloiq_qorii/41",
        "https://t.me/muhammadloiq_qorii/42",
        "https://t.me/muhammadloiq_qorii/43",
        "https://t.me/muhammadloiq_qorii/44",
        "https://t.me/muhammadloiq_qorii/45",
        "https://t.me/muhammadloiq_qorii/46",
        "https://t.me/muhammadloiq_qorii/47",
    ]
    for url in ml:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ml6")
async def ml(call: CallbackQuery):
    ml = [
        "https://t.me/muhammadloiq_qorii/48",
        "https://t.me/muhammadloiq_qorii/49",
        "https://t.me/muhammadloiq_qorii/50",
        "https://t.me/muhammadloiq_qorii/51",
        "https://t.me/muhammadloiq_qorii/52",
        "https://t.me/muhammadloiq_qorii/53",
        "https://t.me/muhammadloiq_qorii/54",
        "https://t.me/muhammadloiq_qorii/55",
    ]
    for url in ml:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ml7")
async def ml(call: CallbackQuery):
    ml = [
        "https://t.me/muhammadloiq_qorii/56",
        "https://t.me/muhammadloiq_qorii/57",
        "https://t.me/muhammadloiq_qorii/58",
        "https://t.me/muhammadloiq_qorii/59",
        "https://t.me/muhammadloiq_qorii/60",
        "https://t.me/muhammadloiq_qorii/61",
        "https://t.me/muhammadloiq_qorii/62",
        "https://t.me/muhammadloiq_qorii/63",
    ]
    for url in ml:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ml8")
async def ml(call: CallbackQuery):
    ml = [
        "https://t.me/muhammadloiq_qorii/64",
        "https://t.me/muhammadloiq_qorii/65",
        "https://t.me/muhammadloiq_qorii/66",
        "https://t.me/muhammadloiq_qorii/67",
        "https://t.me/muhammadloiq_qorii/68",
        "https://t.me/muhammadloiq_qorii/69",
        "https://t.me/muhammadloiq_qorii/70",
        "https://t.me/muhammadloiq_qorii/71",
    ]
    for url in ml:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ml9")
async def ml(call: CallbackQuery):
    ml = [
        "https://t.me/muhammadloiq_qorii/72",
        "https://t.me/muhammadloiq_qorii/73",
        "https://t.me/muhammadloiq_qorii/74",
        "https://t.me/muhammadloiq_qorii/75",
        "https://t.me/muhammadloiq_qorii/76",
        "https://t.me/muhammadloiq_qorii/77",
        "https://t.me/muhammadloiq_qorii/78",
        "https://t.me/muhammadloiq_qorii/79",
    ]
    for url in ml:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ml10")
async def ml(call: CallbackQuery):
    ml = [
        "https://t.me/muhammadloiq_qorii/80",
        "https://t.me/muhammadloiq_qorii/81",
        "https://t.me/muhammadloiq_qorii/82",
        "https://t.me/muhammadloiq_qorii/83",
        "https://t.me/muhammadloiq_qorii/84",
        "https://t.me/muhammadloiq_qorii/85",
        "https://t.me/muhammadloiq_qorii/86",
        "https://t.me/muhammadloiq_qorii/87",
    ]
    for url in ml:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ml11")
async def ml(call: CallbackQuery):
    ml = [
        "https://t.me/muhammadloiq_qorii/88",
        "https://t.me/muhammadloiq_qorii/89",
        "https://t.me/muhammadloiq_qorii/90",
        "https://t.me/muhammadloiq_qorii/91",
        "https://t.me/muhammadloiq_qorii/92",
        "https://t.me/muhammadloiq_qorii/93",
        "https://t.me/muhammadloiq_qorii/94",
        "https://t.me/muhammadloiq_qorii/95",
    ]
    for url in ml:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ml12")
async def ml(call: CallbackQuery):
    ml = [
        "https://t.me/muhammadloiq_qorii/96",
        "https://t.me/muhammadloiq_qorii/97",
        "https://t.me/muhammadloiq_qorii/98",
        "https://t.me/muhammadloiq_qorii/99",
        "https://t.me/muhammadloiq_qorii/100",
        "https://t.me/muhammadloiq_qorii/101",
        "https://t.me/muhammadloiq_qorii/102",
        "https://t.me/muhammadloiq_qorii/103",
    ]
    for url in ml:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ml13")
async def ml(call: CallbackQuery):
    ml = [
        "https://t.me/muhammadloiq_qorii/104",
        "https://t.me/muhammadloiq_qorii/105",
        "https://t.me/muhammadloiq_qorii/106",
        "https://t.me/muhammadloiq_qorii/107",
        "https://t.me/muhammadloiq_qorii/108",
        "https://t.me/muhammadloiq_qorii/109",
        "https://t.me/muhammadloiq_qorii/110",
        "https://t.me/muhammadloiq_qorii/111",
    ]
    for url in ml:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ml14")
async def ml(call: CallbackQuery):
    ml = [
        "https://t.me/muhammadloiq_qorii/112",
        "https://t.me/muhammadloiq_qorii/113",
        "https://t.me/muhammadloiq_qorii/114",
        "https://t.me/muhammadloiq_qorii/115",
        "https://t.me/muhammadloiq_qorii/116",
        "https://t.me/muhammadloiq_qorii/117",
        "https://t.me/muhammadloiq_qorii/118",
        "https://t.me/muhammadloiq_qorii/119",
        "https://t.me/muhammadloiq_qorii/120",
        "https://t.me/muhammadloiq_qorii/121",
    ]
    for url in ml:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")






@dp.message_handler(text="Hasanxon Yahyo Abdulmajid")
async def hasanxon_yahyo(mes: Message):
    await mes.answer("Hasanxon qori qiroatlari: ", reply_markup=xasanxon_inline)


@dp.callback_query_handler(text="x1")
async def x(call: CallbackQuery):
    x = [
        "https://t.me/Xasanxonqori/462",
        "https://t.me/Xasanxonqori/463",
        "https://t.me/Xasanxonqori/464",
        "https://t.me/Xasanxonqori/465",
        "https://t.me/Xasanxonqori/466",
        "https://t.me/Xasanxonqori/467",
        "https://t.me/Xasanxonqori/468",
        "https://t.me/Xasanxonqori/469",
    ]
    for url in x:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="x2")
async def x(call: CallbackQuery):
    x = [
        "https://t.me/Xasanxonqori/470",
        "https://t.me/Xasanxonqori/471",
        "https://t.me/Xasanxonqori/472",
        "https://t.me/Xasanxonqori/473",
        "https://t.me/Xasanxonqori/474",
        "https://t.me/Xasanxonqori/475",
        "https://t.me/Xasanxonqori/476",
        "https://t.me/Xasanxonqori/477",
    ]
    for url in x:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")

@dp.callback_query_handler(text="x3")
async def x(call: CallbackQuery):
    x = [
        "https://t.me/Xasanxonqori/478",
        "https://t.me/Xasanxonqori/479",
        "https://t.me/Xasanxonqori/480",
        "https://t.me/Xasanxonqori/481",
        "https://t.me/Xasanxonqori/482",
        "https://t.me/Xasanxonqori/483",
        "https://t.me/Xasanxonqori/484",
        "https://t.me/Xasanxonqori/485",
    ]
    for url in x:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="x4")
async def x(call: CallbackQuery):
    x = [
        "https://t.me/Xasanxonqori/486",
        "https://t.me/Xasanxonqori/487",
        "https://t.me/Xasanxonqori/488",
        "https://t.me/Xasanxonqori/489",
        "https://t.me/Xasanxonqori/490",
        "https://t.me/Xasanxonqori/491",
        "https://t.me/Xasanxonqori/492",
        "https://t.me/Xasanxonqori/493",
    ]
    for url in x:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="x5")
async def x(call: CallbackQuery):
    x = [
        "https://t.me/Xasanxonqori/494",
        "https://t.me/Xasanxonqori/495",
        "https://t.me/Xasanxonqori/496",
        "https://t.me/Xasanxonqori/497",
        "https://t.me/Xasanxonqori/498",
        "https://t.me/Xasanxonqori/499",
        "https://t.me/Xasanxonqori/500",
        "https://t.me/Xasanxonqori/501",
    ]
    for url in x:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="x6")
async def x(call: CallbackQuery):
    x = [
        "https://t.me/Xasanxonqori/502",
        "https://t.me/Xasanxonqori/503",
        "https://t.me/Xasanxonqori/515",
        "https://t.me/Xasanxonqori/516",
        "https://t.me/Xasanxonqori/517",
        "https://t.me/Xasanxonqori/518",
        "https://t.me/Xasanxonqori/519",
        "https://t.me/Xasanxonqori/520",
    ]
    for url in x:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="x7")
async def x(call: CallbackQuery):
    x = [
        "https://t.me/Xasanxonqori/521",
        "https://t.me/Xasanxonqori/522",
        "https://t.me/Xasanxonqori/523",
        "https://t.me/Xasanxonqori/524",
        "https://t.me/Xasanxonqori/525",
        "https://t.me/Xasanxonqori/526",
        "https://t.me/Xasanxonqori/527",
        "https://t.me/Xasanxonqori/528",
    ]
    for url in x:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="x8")
async def x(call: CallbackQuery):
    x = [
        "https://t.me/Xasanxonqori/529",
        "https://t.me/Xasanxonqori/530",
        "https://t.me/Xasanxonqori/531",
        "https://t.me/Xasanxonqori/532",
        "https://t.me/Xasanxonqori/533",
        "https://t.me/Xasanxonqori/534",
        "https://t.me/Xasanxonqori/535",
        "https://t.me/Xasanxonqori/536",
    ]
    for url in x:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="x9")
async def x(call: CallbackQuery):
    x = [
        "https://t.me/Xasanxonqori/537",
        "https://t.me/Xasanxonqori/538",
        "https://t.me/Xasanxonqori/539",
        "https://t.me/Xasanxonqori/540",
        "https://t.me/Xasanxonqori/548",
        "https://t.me/Xasanxonqori/549",
        "https://t.me/Xasanxonqori/550",
        "https://t.me/Xasanxonqori/551",
    ]
    for url in x:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="x10")
async def x(call: CallbackQuery):
    x = [
        "https://t.me/Xasanxonqori/552",
        "https://t.me/Xasanxonqori/553",
        "https://t.me/Xasanxonqori/554",
        "https://t.me/Xasanxonqori/555",
        "https://t.me/Xasanxonqori/556",
        "https://t.me/Xasanxonqori/557",
        "https://t.me/Xasanxonqori/558",
        "https://t.me/Xasanxonqori/559",
    ]
    for url in x:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="x11")
async def x(call: CallbackQuery):
    x = [
        "https://t.me/Xasanxonqori/560",
        "https://t.me/Xasanxonqori/561",
        "https://t.me/Xasanxonqori/562",
        "https://t.me/Xasanxonqori/563",
        "https://t.me/Xasanxonqori/564",
        "https://t.me/Xasanxonqori/565",
        "https://t.me/Xasanxonqori/566",
        "https://t.me/Xasanxonqori/567",
    ]
    for url in x:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="x12")
async def x(call: CallbackQuery):
    x = [
        "https://t.me/Xasanxonqori/568",
        "https://t.me/Xasanxonqori/569",
        "https://t.me/Xasanxonqori/570",
        "https://t.me/Xasanxonqori/571",
        "https://t.me/Xasanxonqori/572",
        "https://t.me/Xasanxonqori/573",
        "https://t.me/Xasanxonqori/574",
        "https://t.me/Xasanxonqori/575",
    ]
    for url in x:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="x13")
async def x(call: CallbackQuery):
    x = [
        "https://t.me/Xasanxonqori/576",
        "https://t.me/Xasanxonqori/577",
        "https://t.me/Xasanxonqori/583",
        "https://t.me/Xasanxonqori/584",
        "https://t.me/Xasanxonqori/585",
        "https://t.me/Xasanxonqori/586",
        "https://t.me/Xasanxonqori/587",
        "https://t.me/Xasanxonqori/588",
        "https://t.me/Xasanxonqori/589",
    ]
    for url in x:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="x14")
async def x(call: CallbackQuery):
    x = [
        "https://t.me/Xasanxonqori/590",
        "https://t.me/Xasanxonqori/591",
        "https://t.me/Xasanxonqori/592",
        "https://t.me/Xasanxonqori/593",
        "https://t.me/Xasanxonqori/594",
        "https://t.me/Xasanxonqori/595",
        "https://t.me/Xasanxonqori/596",
        "https://t.me/Xasanxonqori/597"
    ]
    for url in x:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")



# 3.4.Mishariy Roshid Al Afasiy
@dp.message_handler(text="Mishariy Al Afasiy")
async def al_afasiy(mes: Message):
    await mes.answer("Mishariy Roshid Al Afasiy qiroatlari:", reply_markup=mishari_inline)


@dp.callback_query_handler(text="m1")
async def m(call: CallbackQuery):
    m = [
        "https://t.me/Mishary_Roshid_Alafasiy1/4",
        "https://t.me/Mishary_Roshid_Alafasiy1/5",
        "https://t.me/Mishary_Roshid_Alafasiy1/6",
        "https://t.me/Mishary_Roshid_Alafasiy1/7",
        "https://t.me/Mishary_Roshid_Alafasiy1/8",
        "https://t.me/Mishary_Roshid_Alafasiy1/9",
        "https://t.me/Mishary_Roshid_Alafasiy1/10",
        "https://t.me/Mishary_Roshid_Alafasiy1/11",
    ]
    for url in m:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="m2")
async def m(call: CallbackQuery):
    m = [
        "https://t.me/Mishary_Roshid_Alafasiy1/12",
        "https://t.me/Mishary_Roshid_Alafasiy1/13",
        "https://t.me/Mishary_Roshid_Alafasiy1/14",
        "https://t.me/Mishary_Roshid_Alafasiy1/15",
        "https://t.me/Mishary_Roshid_Alafasiy1/16",
        "https://t.me/Mishary_Roshid_Alafasiy1/17",
        "https://t.me/Mishary_Roshid_Alafasiy1/18",
        "https://t.me/Mishary_Roshid_Alafasiy1/19",
    ]
    for url in m:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="m3")
async def m(call: CallbackQuery):
    m = [
        "https://t.me/Mishary_Roshid_Alafasiy1/20",
        "https://t.me/Mishary_Roshid_Alafasiy1/21",
        "https://t.me/Mishary_Roshid_Alafasiy1/22",
        "https://t.me/Mishary_Roshid_Alafasiy1/23",
        "https://t.me/Mishary_Roshid_Alafasiy1/24",
        "https://t.me/Mishary_Roshid_Alafasiy1/25",
        "https://t.me/Mishary_Roshid_Alafasiy1/26",
        "https://t.me/Mishary_Roshid_Alafasiy1/27",
    ]
    for url in m:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="m4")
async def m(call: CallbackQuery):
    m = [
        "https://t.me/Mishary_Roshid_Alafasiy1/28",
        "https://t.me/Mishary_Roshid_Alafasiy1/29",
        "https://t.me/Mishary_Roshid_Alafasiy1/30",
        "https://t.me/Mishary_Roshid_Alafasiy1/31",
        "https://t.me/Mishary_Roshid_Alafasiy1/32",
        "https://t.me/Mishary_Roshid_Alafasiy1/33",
        "https://t.me/Mishary_Roshid_Alafasiy1/34",
        "https://t.me/Mishary_Roshid_Alafasiy1/35",
    ]
    for url in m:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="m5")
async def m(call: CallbackQuery):
    m = [
        "https://t.me/Mishary_Roshid_Alafasiy1/36",
        "https://t.me/Mishary_Roshid_Alafasiy1/37",
        "https://t.me/Mishary_Roshid_Alafasiy1/38",
        "https://t.me/Mishary_Roshid_Alafasiy1/39",
        "https://t.me/Mishary_Roshid_Alafasiy1/40",
        "https://t.me/Mishary_Roshid_Alafasiy1/41",
        "https://t.me/Mishary_Roshid_Alafasiy1/42",
        "https://t.me/Mishary_Roshid_Alafasiy1/43",
    ]
    for url in m:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="m6")
async def m(call: CallbackQuery):
    m = [
        "https://t.me/Mishary_Roshid_Alafasiy1/44",
        "https://t.me/Mishary_Roshid_Alafasiy1/45",
        "https://t.me/Mishary_Roshid_Alafasiy1/46",
        "https://t.me/Mishary_Roshid_Alafasiy1/47",
        "https://t.me/Mishary_Roshid_Alafasiy1/48",
        "https://t.me/Mishary_Roshid_Alafasiy1/49",
        "https://t.me/Mishary_Roshid_Alafasiy1/50",
        "https://t.me/Mishary_Roshid_Alafasiy1/51",
    ]
    for url in m:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="m7")
async def m(call: CallbackQuery):
    m = [
        "https://t.me/Mishary_Roshid_Alafasiy1/52",
        "https://t.me/Mishary_Roshid_Alafasiy1/53",
        "https://t.me/Mishary_Roshid_Alafasiy1/54",
        "https://t.me/Mishary_Roshid_Alafasiy1/55",
        "https://t.me/Mishary_Roshid_Alafasiy1/56",
        "https://t.me/Mishary_Roshid_Alafasiy1/57",
        "https://t.me/Mishary_Roshid_Alafasiy1/58",
        "https://t.me/Mishary_Roshid_Alafasiy1/59",
    ]
    for url in m:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="m8")
async def m(call: CallbackQuery):
    m = [
        "https://t.me/Mishary_Roshid_Alafasiy1/60",
        "https://t.me/Mishary_Roshid_Alafasiy1/61",
        "https://t.me/Mishary_Roshid_Alafasiy1/62",
        "https://t.me/Mishary_Roshid_Alafasiy1/63",
        "https://t.me/Mishary_Roshid_Alafasiy1/64",
        "https://t.me/Mishary_Roshid_Alafasiy1/65",
        "https://t.me/Mishary_Roshid_Alafasiy1/66",
        "https://t.me/Mishary_Roshid_Alafasiy1/67",
    ]
    for url in m:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="m9")
async def m(call: CallbackQuery):
    m = [
        "https://t.me/Mishary_Roshid_Alafasiy1/68",
        "https://t.me/Mishary_Roshid_Alafasiy1/69",
        "https://t.me/Mishary_Roshid_Alafasiy1/70",
        "https://t.me/Mishary_Roshid_Alafasiy1/71",
        "https://t.me/Mishary_Roshid_Alafasiy1/72",
        "https://t.me/Mishary_Roshid_Alafasiy1/73",
        "https://t.me/Mishary_Roshid_Alafasiy1/74",
        "https://t.me/Mishary_Roshid_Alafasiy1/75",
    ]
    for url in m:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="m10")
async def m10(call: CallbackQuery):
    m10 = [
        "https://t.me/Mishary_Roshid_Alafasiy1/76",
        "https://t.me/Mishary_Roshid_Alafasiy1/77",
        "https://t.me/Mishary_Roshid_Alafasiy1/78",
        "https://t.me/Mishary_Roshid_Alafasiy1/79",
        "https://t.me/Mishary_Roshid_Alafasiy1/80",
        "https://t.me/Mishary_Roshid_Alafasiy1/81",
        "https://t.me/Mishary_Roshid_Alafasiy1/82",
        "https://t.me/Mishary_Roshid_Alafasiy1/83",
    ]
    for url in m10:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="m11")
async def m(call: CallbackQuery):
    m = [
        "https://t.me/Mishary_Roshid_Alafasiy1/84",
        "https://t.me/Mishary_Roshid_Alafasiy1/85",
        "https://t.me/Mishary_Roshid_Alafasiy1/86",
        "https://t.me/Mishary_Roshid_Alafasiy1/87",
        "https://t.me/Mishary_Roshid_Alafasiy1/88",
        "https://t.me/Mishary_Roshid_Alafasiy1/89",
        "https://t.me/Mishary_Roshid_Alafasiy1/90",
        "https://t.me/Mishary_Roshid_Alafasiy1/91",
    ]
    for url in m:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="m12")
async def m(call: CallbackQuery):
    m = [
        "https://t.me/Mishary_Roshid_Alafasiy1/92",
        "https://t.me/Mishary_Roshid_Alafasiy1/93",
        "https://t.me/Mishary_Roshid_Alafasiy1/94",
        "https://t.me/Mishary_Roshid_Alafasiy1/95",
        "https://t.me/Mishary_Roshid_Alafasiy1/96",
        "https://t.me/Mishary_Roshid_Alafasiy1/97",
        "https://t.me/Mishary_Roshid_Alafasiy1/98",
        "https://t.me/Mishary_Roshid_Alafasiy1/99",
    ]
    for url in m:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="m13")
async def m(call: CallbackQuery):
    m = [
        "https://t.me/Mishary_Roshid_Alafasiy1/100",
        "https://t.me/Mishary_Roshid_Alafasiy1/101",
        "https://t.me/Mishary_Roshid_Alafasiy1/102",
        "https://t.me/Mishary_Roshid_Alafasiy1/103",
        "https://t.me/Mishary_Roshid_Alafasiy1/104",
        "https://t.me/Mishary_Roshid_Alafasiy1/105",
        "https://t.me/Mishary_Roshid_Alafasiy1/106",
        "https://t.me/Mishary_Roshid_Alafasiy1/107",
    ]
    for url in m:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="m14")
async def m(call: CallbackQuery):
    m = [
        "https://t.me/Mishary_Roshid_Alafasiy1/108",
        "https://t.me/Mishary_Roshid_Alafasiy1/109",
        "https://t.me/Mishary_Roshid_Alafasiy1/110",
        "https://t.me/Mishary_Roshid_Alafasiy1/111",
        "https://t.me/Mishary_Roshid_Alafasiy1/112",
        "https://t.me/Mishary_Roshid_Alafasiy1/113",
        "https://t.me/Mishary_Roshid_Alafasiy1/114",
        "https://t.me/Mishary_Roshid_Alafasiy1/115",
        "https://t.me/Mishary_Roshid_Alafasiy1/116",
        "https://t.me/Mishary_Roshid_Alafasiy1/117",
    ]
    for url in m:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")




#          4.QUR'ON FAZILATLARI
@dp.message_handler(text="Qur'on fazilatlari")
async def quron_fazilatlari(mes: Message):
    text = """Usmon roziyallohu anhudan rivoyat qilinadi:
"Payg‘ambarimiz sollallohu alayhi vasallam:
<b>"Sizlarning eng yaxshilaringiz Qur’onni o‘rganib,
boshqalarga ham o‘rgatadiganlaringizdir"</b>, dedilar".
(Imom Buxoriy rivoyati).\n\n"""
    text += """Abu Usoma al-Bohiliy roziyallohu anhudan rivoyat qilinadi:
"Rasululloh sollallohu alayhi vasallam:
<b>"Qur’onni tilovat qilinglar. Chunki Qiyomat kuni
o‘qigan egasiga u shafoatchi bo‘lib keladi"</b>, dedilar".
(Imom Muslim rivoyati)

@islomuz_quron_bot"""
    await mes.answer(text)
    text = """<b>1. «Умматимнинг энг шарафлиси ҳомилул қуръон ва кечаси қоим бўлувчиларидир».[1]

2. «Қуръон бойликдир, ундан сўнг фақирлик йўқ, ундан бошқа бойлик ҳам йўқ».[2]

3. «Қуръон қиёмат куни ўз соҳибини шафоат қилади...»[3]

4. «Қуръон қиёмат куни қабр ёрилганда ўз соҳибига юзи оппоқ киши каби йўлиқиб: «Мени танидингми?» дейди. У: «Йўқ», деб жавоб беради. Қуръон: «Мен кундузлари чанқатган, тунларингни бедор қилган ҳамроҳинг Қуръонман. Ҳар бир тижоратчи ўз тижорати ортидадир. Мен эса бугун сенинг ортингдаман», дейди. Сўнг унга мулк ўнг томонидан, абадийлик чап томонидан берилиб, бошига виқор тожи кийдирилади ва ота-онасига бу дунёнинг бутун қиймати ҳам унга тенг келмайдиган кийим кийдирилади. Улар «Буни нима сабабдан кийдик?» деб ҳайрон бўлганларида, уларга: «Фарзандингиз Қуръонни қўлга киритгани учун», дейилади. Сўнг унга: «Ўқи ва жаннат даражалари ва боғларида кўтарил», дейилади.  У тез ўқийдими, секин ўқийдими, модомики ўқир экан, кўтарилиб бораверади»[4].

5. «Расулуллоҳ соллаллоҳу алайҳи васаллам:  «Инсонлар ичида Аллоҳнинг хос бандалари бор», дедилар. «Улар кимлар?» деб сўрадилар. У зот: «Қуръон аҳли Аллоҳнинг аҳли ва хос бандаларидир», деб жавоб бердилар».[5] Мунавий: «Қуръон аҳли» Қуръонни тадаббур қилиб, унга амал қилишни лозим тутганлардир», деган.

6. «Мусулмон қарияни, маъсият билан ҳаддидан ошмаган ҳомилул қуръон(қори)ни ва одил султонни ҳурмат қилиш Аллоҳни улуғлашдандир».[6] Фойда: «Ҳаддидан ошмаган», яъни тажвид ва ҳарфларни адо қилишдан ёки айрим бидъатчилар каби маъносини ботил таъвил қилишдан, тиловатдан ва қироатини пухта қилиб, маъноларини тушунган ҳолда унга амал қилишдан юз ўгирмаган.

7. «Исо ибн Марям алайҳиссаломнинг олдиларидан бир аёл ўтаётиб: «Сенга ҳомиладор бўлган қорин ва сени эмизган кўкрак нақадар яхши!» деди. Шунда Исо алайҳиссалом: «Йўқ, балки ким Қуръон ўқиб, унга амал қилса, нақадар яхши!» дедилар»[7].

8. «Осмон эшиклари беш нарса учун очилади: Қуръон қироати, ҳужум қилганларга қарши туриш, ёмғир ёғиши, мазлумнинг дуоси ва азон учун.

9. Беш нарса ибодатдандир: Мусҳафга назар солиш, Каъбага назар солиш, ота-онага назар солиш, замзамга назар солиш – булар хатоларни ўчиради – ва олимнинг юзига назар солиш»[8].</b>
"""
    await mes.answer(text)


    text = """<b>10. «Сизларнинг энг яхшиларингиз Қуръонни ўрганиб, уни ўргатганларингиздир»[9]. Танбеҳ: Агар «Бу ривоятларга кўра муқрий (Қуръон ўргатувчи) оламнинг фозили бўлмиш фақиҳдан афзал экан-да», дейилса, биз айтамизки: «Йўқ, чунки бу ердаги мухотоб (тингловчилар) фақиҳ бўлганлар. Уларнинг тили бўлгани учун Қуръоннинг маъноларини шундоқ ҳам тушунганлар. Фиқҳ уларнинг қон-қонларига сингиб кетган. Ким ўшалардек бўлса, уларнинг жумласига киради. Аммо фақат қори ёки Қуръон ўқитувчи бўлиб, ўқиётган нарсасининг маъносидан ҳеч нарсани тушунмаса, бундан эмас.

11. Абу Зарр розияллоҳу анҳудан ривоят қилинади: «Мен: «Эй Аллоҳнинг Расули, менга насиҳат қилинг», дедим. У зот: «Тақво қилгин. Чунки у барча ишларнинг бошидир», дедилар. Мен: «Яна қўшимча қилинг», дедим. У зот: «Қуръон тиловатини лозим тут. Чунки у ерда нур, осмонда сен учун захирадир», дедилар»[10].

12. «Ким Аллоҳ ва Расули уни яхши кўришини хоҳласа, қарасин, агар Қуръонни яхши кўрса, демак, Аллоҳ ва Расули уни яхши кўради»[11].

13. «Ким фарзандига Қуръонни қараб ўқишни ўргатса, аввалу охир қилган гуноҳлари кечирилади. Ким унга ёдлатса, қиёмат куни Аллоҳ таоло уни тўлин ой суратида юборади ва фарзандига «Ўқи», дейди. Ҳар бир оятни ўқиган сайин, то ёдлаган жойининг охирига етгунича Аллоҳ азза ва жалла отасининг даражасини кўтараверади»[12].

14. «Қуръонни ёдлаб, ҳалолни ҳалол, ҳаромни ҳаром деб билса, Аллоҳ уни жаннатга киритади ва оиласидан дўзахга ҳукм қилинган ўнтасини шафоат қилишига имкон беради»[13].

15. «Ким Қуръон ўқиса, у ўз ичида нубувватни ҳосил қилган бўлади (яъни нубувват хислати ва илмини қамраб олган бўлади), фақат унга ваҳий қилинмаган, холос. Қуръон соҳиби ичида Аллоҳнинг каломи бўла туриб, ўзига ўхшаган (соҳиби Қуръон) билан урушмаслиги ва жоҳил билан жоҳиллик қилмаслиги лозим. Балки у гўзал ва комил бўлиб юриши лозим. Чунки унинг ичида ва қалбида Аллоҳ таолонинг каломи бор»[14].

16. «Эй Али, Қуръонни ўрганиб, уни ўргатгин. Шунда вафот қилсанг, худди инсонлар Аллоҳнинг Байтини тавоф қилганлари каби фаришталар қабринг атрофини тавоф қиладилар»[15].

17. «Соҳиби Қуръонга «Ўқи ва кўтарил, дунёда ўқиганинг каби ўқи! Сенинг манзилинг охирги ўқиган оятинг бўлган жойдир» дейилади»[16]. Танбеҳ: Ҳофиз Ибн Ҳажар: «Бу хабар Қуръонни ёдлаган қориларга хос, мусҳафдан ўқийдиганлар учун эмас. Шунинг учун уларнинг жаннатдаги даражалари ёдлаганларининг турлича бўлиши билан фарқ қилади», деганлар.

Оиша розияллоҳу анҳо айтадилар: «Жаннат даражаларининг сони Қуръони Карим оятларининг ададичадир»[17]. Ким тўла ёдласа, жаннатнинг энг баланд даражасига эга бўлади. Ким бир бўлагини ёдласа, даражаси шунга яраша бўлади, шу шарт биланки, ўқиган нарсасига амал қилувчи ва тадаббур қилувчи бўлсин.

Суютий айтадилар: «Қуръони Каримнинг жаннатда ўқилиши Қуръони Каримнинг хусусиятларидандир. Зеро, бошқа китоблар хусусида бунга ўхшаш ривоятлар ворид бўлмаган». Бу даражалар Қуръонга амал қилган қорилар учундир. Чунки у кунда ҳеч ким бир оят ҳам тиловат қилишга қодир бўлмайди, амал қилган бўлса, мустасно[18].

@islomuz_quron_bot</b>
"""

    await mes.answer(text)
