from loader import dp

from aiogram.types import Message, CallbackQuery

from keyboards.default.menu_keyboard import menu, quron_menu, uzb_quran
from keyboards.inline.quran_inline import tafsirihilol_audio1, tafsirihilol_audio2, tafsir, afzal_rafiqov_inline


#          QUR'ON BO'LIMI
@dp.message_handler(text="📖 Qur'on")
async def quron(mes: Message):
    await mes.answer("Qur'on bo'limi:", reply_markup=quron_menu)


#        1.TAFSIRI HILOL
@dp.message_handler(text="Tafsiri Hilol")
async def tafsiri_hilol(mes: Message):
    await mes.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/8", caption=""" <b>"Tafsiri Hilol" elektron dasturi
                                                                                                                  Muallif: Shayx Muhammad Sodiq Muhammad Yusuf

                                                                                                                  Nashriyot: @HilolNashr</b>
                                                                                                                  @islomuz_quron_bot""")

    await mes.answer("Tafsiri Hilol audio shakli", reply_markup=tafsir)


@dp.callback_query_handler(text="muqaddimahilol")
async def muqaddima(call: CallbackQuery):
    muqaddima = [
        "https://t.me/TAFSIRIXILOL/21",
        "https://t.me/TAFSIRIXILOL/22",
        "https://t.me/TAFSIRIXILOL/23",
        "https://t.me/TAFSIRIXILOL/24",
        "https://t.me/TAFSIRIXILOL/25",
        "https://t.me/TAFSIRIXILOL/26",
        "https://t.me/TAFSIRIXILOL/27",
        "https://t.me/TAFSIRIXILOL/28",
        "https://t.me/TAFSIRIXILOL/29",
        "https://t.me/TAFSIRIXILOL/30",
        "https://t.me/TAFSIRIXILOL/31",
    ]
    import datetime
    for url in muqaddima:
        await call.message.answer_audio(url, caption="Tafsiri Hilol audio shakli\n"
                                                     "Muallif: Shayx Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")



@dp.callback_query_handler(text="29pora")
async def pora29(call: CallbackQuery):
    pora29 = [
        "https://t.me/TAFSIRIXILOL/96",
        "https://t.me/TAFSIRIXILOL/95",
        "https://t.me/TAFSIRIXILOL/94",
        "https://t.me/TAFSIRIXILOL/93",
        "https://t.me/TAFSIRIXILOL/92",
        "https://t.me/TAFSIRIXILOL/91",
        "https://t.me/TAFSIRIXILOL/90",
        "https://t.me/TAFSIRIXILOL/89",
        "https://t.me/TAFSIRIXILOL/88",
        "https://t.me/TAFSIRIXILOL/76",
    ]
    for url in pora29:
        await call.message.answer_audio(url, caption="Tafsiri Hilol audio shakli\n"
                                                     "Muallif: Shayx Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="30pora")
async def pora30(call: CallbackQuery):
    pora30 = [
        "https://t.me/TAFSIRIXILOL/72",
        "https://t.me/TAFSIRIXILOL/71",
        "https://t.me/TAFSIRIXILOL/70",
        "https://t.me/TAFSIRIXILOL/69",
        "https://t.me/TAFSIRIXILOL/68",
        "https://t.me/TAFSIRIXILOL/67",
        "https://t.me/TAFSIRIXILOL/66",
        "https://t.me/TAFSIRIXILOL/65",
        "https://t.me/TAFSIRIXILOL/64",
        "https://t.me/TAFSIRIXILOL/63",
        "https://t.me/TAFSIRIXILOL/62",
        "https://t.me/TAFSIRIXILOL/61",
        "https://t.me/TAFSIRIXILOL/60",
        "https://t.me/TAFSIRIXILOL/59",
        "https://t.me/TAFSIRIXILOL/58",
        "https://t.me/TAFSIRIXILOL/57",
        "https://t.me/TAFSIRIXILOL/56",
        "https://t.me/TAFSIRIXILOL/55",
        "https://t.me/TAFSIRIXILOL/54",
        "https://t.me/TAFSIRIXILOL/53",
        "https://t.me/TAFSIRIXILOL/52",
        "https://t.me/TAFSIRIXILOL/51",
        "https://t.me/TAFSIRIXILOL/50",
        "https://t.me/TAFSIRIXILOL/49",
        "https://t.me/TAFSIRIXILOL/48",
        "https://t.me/TAFSIRIXILOL/47",
        "https://t.me/TAFSIRIXILOL/46",  #45 yo'q
        "https://t.me/TAFSIRIXILOL/44",
        "https://t.me/TAFSIRIXILOL/43",
        "https://t.me/TAFSIRIXILOL/42",
        "https://t.me/TAFSIRIXILOL/41",
        "https://t.me/TAFSIRIXILOL/40",
        "https://t.me/TAFSIRIXILOL/39",
        "https://t.me/TAFSIRIXILOL/38",
        "https://t.me/TAFSIRIXILOL/37",
        "https://t.me/TAFSIRIXILOL/36",
        "https://t.me/TAFSIRIXILOL/35"
    ]
    for url in pora30:
        await call.message.answer_audio(url, caption="Tafsiri Hilol audio shakli\n"
                                                     "Muallif: Shayx Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")




#        2.O'ZBEK TILIDAGI MA'NOLARI TARJIMASI
@dp.message_handler(text="O'zbek tilidagi ma'nolari tarjimasi")
async def tafsiri_hilol_audio(mes: Message):
    await mes.answer("O'zbek tilidagi ma'nolari tarjimasining audio shakli:", reply_markup=uzb_quran)


#        2.1. SHAYX MUHAMMAD SODIQ MUHAMMAD YUSUF
@dp.message_handler(text="Shayx Muhammad Sodiq Muhammad Yusuf")
async def shayx(ms: Message):
    await ms.answer("Shayx Muhammad Sodiq Muhammad Yusuf \nQur'oni Karim va o'zbek tilidagi ma'nolari tarjimasi",
                    reply_markup=tafsirihilol_audio1)


@dp.message_handler(text="Afzal Rafiqov")
async def afzal_rafiqov(mes: Message):
    await mes.answer("Afzal Rafiqov - Qur'oni Karim ma'nolari tarjimasi:", reply_markup=afzal_rafiqov_inline)


@dp.callback_query_handler(text="ar1")
async def ar1(call: CallbackQuery):
    ar1 = [
        "https://t.me/Rafiqov_Afzal/14",
        "https://t.me/Rafiqov_Afzal/15",
        "https://t.me/Rafiqov_Afzal/16",
        "https://t.me/Rafiqov_Afzal/17",
        "https://t.me/Rafiqov_Afzal/18",
        "https://t.me/Rafiqov_Afzal/19",
        "https://t.me/Rafiqov_Afzal/20",
        "https://t.me/Rafiqov_Afzal/21",
        "https://t.me/Rafiqov_Afzal/22",
    ]
    for url in ar1:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ar2")
async def ar2(call: CallbackQuery):
    ar2 = [
        "https://t.me/Rafiqov_Afzal/23",
        "https://t.me/Rafiqov_Afzal/24",
        "https://t.me/Rafiqov_Afzal/25",
        "https://t.me/Rafiqov_Afzal/26",
        "https://t.me/Rafiqov_Afzal/27",
        "https://t.me/Rafiqov_Afzal/28",
        "https://t.me/Rafiqov_Afzal/29",
        "https://t.me/Rafiqov_Afzal/30"
    ]
    for url in ar2:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")

@dp.callback_query_handler(text="ar3")
async def ar3(call: CallbackQuery):
    ar3 = [
        "https://t.me/Rafiqov_Afzal/31",
        "https://t.me/Rafiqov_Afzal/32",
        "https://t.me/Rafiqov_Afzal/33",
        "https://t.me/Rafiqov_Afzal/34",
        "https://t.me/Rafiqov_Afzal/35",
        "https://t.me/Rafiqov_Afzal/36",
        "https://t.me/Rafiqov_Afzal/37",
        "https://t.me/Rafiqov_Afzal/38"
    ]
    for url in ar3:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ar4")
async def ar4(call: CallbackQuery):
    ar4 = [
        "https://t.me/Rafiqov_Afzal/39",
        "https://t.me/Rafiqov_Afzal/40",
        "https://t.me/Rafiqov_Afzal/41",
        "https://t.me/Rafiqov_Afzal/42",
        "https://t.me/Rafiqov_Afzal/43",
        "https://t.me/Rafiqov_Afzal/44",
        "https://t.me/Rafiqov_Afzal/45",
        "https://t.me/Rafiqov_Afzal/46"
    ]
    for url in ar4:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ar5")
async def ar5(call: CallbackQuery):
    ar5 = [
        "https://t.me/Rafiqov_Afzal/47",
        "https://t.me/Rafiqov_Afzal/48",
        "https://t.me/Rafiqov_Afzal/49",
        "https://t.me/Rafiqov_Afzal/50",
        "https://t.me/Rafiqov_Afzal/51",
        "https://t.me/Rafiqov_Afzal/52",
        "https://t.me/Rafiqov_Afzal/53",
        "https://t.me/Rafiqov_Afzal/54"
    ]
    for url in ar5:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ar6")
async def ar6(call: CallbackQuery):
    ar6 = [
        "https://t.me/Rafiqov_Afzal/55",
        "https://t.me/Rafiqov_Afzal/56",
        "https://t.me/Rafiqov_Afzal/57",
        "https://t.me/Rafiqov_Afzal/58",
        "https://t.me/Rafiqov_Afzal/59",
        "https://t.me/Rafiqov_Afzal/60",
        "https://t.me/Rafiqov_Afzal/61",
        "https://t.me/Rafiqov_Afzal/62"
    ]
    for url in ar6:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")

@dp.callback_query_handler(text="ar7")
async def ar7(call: CallbackQuery):
    ar7 = [
        "https://t.me/Rafiqov_Afzal/114",
        "https://t.me/Rafiqov_Afzal/115",
        "https://t.me/Rafiqov_Afzal/116",
        "https://t.me/Rafiqov_Afzal/117",
        "https://t.me/Rafiqov_Afzal/118",
        "https://t.me/Rafiqov_Afzal/119",
        "https://t.me/Rafiqov_Afzal/120",
        "https://t.me/Rafiqov_Afzal/121"
    ]
    for url in ar7:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ar8")
async def ar8(call: CallbackQuery):
    ar8 = [
        "https://t.me/Rafiqov_Afzal/122",
        "https://t.me/Rafiqov_Afzal/123",
        "https://t.me/Rafiqov_Afzal/124",
        "https://t.me/Rafiqov_Afzal/125",
        "https://t.me/Rafiqov_Afzal/126",
        "https://t.me/Rafiqov_Afzal/127",
        "https://t.me/Rafiqov_Afzal/128",
        "https://t.me/Rafiqov_Afzal/129"
    ]
    for url in ar8:
        await call.message.answer_video(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ar9")
async def ar9(call: CallbackQuery):
    ar9 = [
        "https://t.me/Rafiqov_Afzal/130",
        "https://t.me/Rafiqov_Afzal/131",
        "https://t.me/Rafiqov_Afzal/132",
        "https://t.me/Rafiqov_Afzal/133",
        "https://t.me/Rafiqov_Afzal/134",
        "https://t.me/Rafiqov_Afzal/135",
        "https://t.me/Rafiqov_Afzal/136",
        "https://t.me/Rafiqov_Afzal/137"
    ]
    for url in ar9:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ar10")
async def ar10(call: CallbackQuery):
    ar10 = [
        "https://t.me/Rafiqov_Afzal/138",
        "https://t.me/Rafiqov_Afzal/139",
        "https://t.me/Rafiqov_Afzal/140",
        "https://t.me/Rafiqov_Afzal/141",
        "https://t.me/Rafiqov_Afzal/142",
        "https://t.me/Rafiqov_Afzal/143",
        "https://t.me/Rafiqov_Afzal/144",
        "https://t.me/Rafiqov_Afzal/145"
    ]
    for url in ar10:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ar11")
async def ar11(call: CallbackQuery):
    ar11 = [
        "https://t.me/Rafiqov_Afzal/146",
        "https://t.me/Rafiqov_Afzal/147",
        "https://t.me/Rafiqov_Afzal/148",
        "https://t.me/Rafiqov_Afzal/149",
        "https://t.me/Rafiqov_Afzal/150",
        "https://t.me/Rafiqov_Afzal/151",
        "https://t.me/Rafiqov_Afzal/152",
        "https://t.me/Rafiqov_Afzal/153"
    ]
    for url in ar11:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ar12")
async def ar12(call: CallbackQuery):
    ar12 = [
        "https://t.me/Rafiqov_Afzal/154",
        "https://t.me/Rafiqov_Afzal/155",
        "https://t.me/Rafiqov_Afzal/156",
        "https://t.me/Rafiqov_Afzal/157",
        "https://t.me/Rafiqov_Afzal/158",
        "https://t.me/Rafiqov_Afzal/159",
        "https://t.me/Rafiqov_Afzal/160",
        "https://t.me/Rafiqov_Afzal/161"
    ]
    for url in ar12:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ar13")
async def ar13(call: CallbackQuery):
    ar13 = [
        "https://t.me/Rafiqov_Afzal/162",
        "https://t.me/Rafiqov_Afzal/163",
        "https://t.me/Rafiqov_Afzal/164",
        "https://t.me/Rafiqov_Afzal/165",
        "https://t.me/Rafiqov_Afzal/166",
        "https://t.me/Rafiqov_Afzal/167",
        "https://t.me/Rafiqov_Afzal/168",
        "https://t.me/Rafiqov_Afzal/169"
    ]
    for url in ar13:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ar14")
async def ar14(call: CallbackQuery):
    ar14 = [
        "https://t.me/Rafiqov_Afzal/170",
        "https://t.me/Rafiqov_Afzal/171",
        "https://t.me/Rafiqov_Afzal/172",
        "https://t.me/Rafiqov_Afzal/173",
        "https://t.me/Rafiqov_Afzal/174",
        "https://t.me/Rafiqov_Afzal/175",
        "https://t.me/Rafiqov_Afzal/176",
        "https://t.me/Rafiqov_Afzal/177",
        "https://t.me/Rafiqov_Afzal/186"
    ]
    for url in ar14:
        await call.message.answer_audio(url, caption="@islomuz_quron_bot")



@dp.callback_query_handler(text="2qismga")
async def ikkinchiqisimga(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("2-qism", reply_markup=tafsirihilol_audio2)



@dp.callback_query_handler(text="1qismga")
async def ikkinchiqisimga(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("1-qism", reply_markup=tafsirihilol_audio1)


@dp.callback_query_handler(text="Bosh menu")
async def boshiga(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Bosh menu", reply_markup=menu)


@dp.callback_query_handler(text="quronbolimi")
async def quronbolimi(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Qur'on :", reply_markup=quron_menu)

#       2.1.1.FOTIHA
@dp.callback_query_handler(text="hilol1")
async def fotiha(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/18",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf"
                                            "\n@islomuz_quron_bot")
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="hilol2")
async def baqara(call: CallbackQuery):
    baqara = [
        "https://t.me/Quron_Tafsiri_30_pora/19",
        "https://t.me/Quron_Tafsiri_30_pora/20",
        "https://t.me/Quron_Tafsiri_30_pora/21",
        "https://t.me/Quron_Tafsiri_30_pora/22",
        "https://t.me/Quron_Tafsiri_30_pora/23",
        "https://t.me/Quron_Tafsiri_30_pora/24",
        "https://t.me/Quron_Tafsiri_30_pora/25",
        "https://t.me/Quron_Tafsiri_30_pora/26",
        "https://t.me/Quron_Tafsiri_30_pora/27",
        "https://t.me/Quron_Tafsiri_30_pora/28"
    ]
    for url in baqara:
        await call.message.answer_audio(url, caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf"
                                                     "\n@islomuz_quron_bot")
        await call.answer(cache_time=60)


@dp.callback_query_handler(text="hilol3")
async def oli_imron(call: CallbackQuery):
    oli_imron = [
        "https://t.me/Quron_Tafsiri_30_pora/29",
        "https://t.me/Quron_Tafsiri_30_pora/30",
        "https://t.me/Quron_Tafsiri_30_pora/31",
        "https://t.me/Quron_Tafsiri_30_pora/32"
    ]
    for url in oli_imron:
        await call.message.answer_audio(url, caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf"
                                                     "\n@islomuz_quron_bot")
        await call.answer(cache_time=60)


@dp.callback_query_handler(text="hilol4")
async def niso(call: CallbackQuery):
    niso = [
        "https://t.me/Quron_Tafsiri_30_pora/33",
        "https://t.me/Quron_Tafsiri_30_pora/34",
        "https://t.me/Quron_Tafsiri_30_pora/35",
        "https://t.me/Quron_Tafsiri_30_pora/36",
        "https://t.me/Quron_Tafsiri_30_pora/37",
        "https://t.me/Quron_Tafsiri_30_pora/38"
    ]
    for url in niso:
        await call.message.answer_audio(url, caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf"
                                                     "\n@islomuz_quron_bot")
        await call.answer(cache_time=60)


@dp.callback_query_handler(text="hilol5")
async def moida(call: CallbackQuery):
    moida = [
        "https://t.me/Quron_Tafsiri_30_pora/39",
        "https://t.me/Quron_Tafsiri_30_pora/40",
        "https://t.me/Quron_Tafsiri_30_pora/41",
        "https://t.me/Quron_Tafsiri_30_pora/42",
        "https://t.me/Quron_Tafsiri_30_pora/43",
    ]
    for url in moida:
        await call.message.answer_audio(url, caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf"
                                                     "\n@islomuz_quron_bot")
        await call.answer(cache_time=60)


@dp.callback_query_handler(text="hilol6")
async def anom(call: CallbackQuery):
    anom = [
        "https://t.me/Quron_Tafsiri_30_pora/50",
        "https://t.me/Quron_Tafsiri_30_pora/51",
        "https://t.me/Quron_Tafsiri_30_pora/52",
        "https://t.me/Quron_Tafsiri_30_pora/53",
        "https://t.me/Quron_Tafsiri_30_pora/54",
    ]
    for url in anom:
        await call.message.answer_audio(url, caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol7")
async def arof(call: CallbackQuery):
    arof = [
        "https://t.me/Quron_Tafsiri_30_pora/56",
        "https://t.me/Quron_Tafsiri_30_pora/57",
        "https://t.me/Quron_Tafsiri_30_pora/58",
        "https://t.me/Quron_Tafsiri_30_pora/59",
        "https://t.me/Quron_Tafsiri_30_pora/60",

    ]
    for url in arof:
        await call.message.answer_audio(url, caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol8")
async def anfol(call: CallbackQuery):
    anfol = [
        "https://t.me/Quron_Tafsiri_30_pora/79",
        "https://t.me/Quron_Tafsiri_30_pora/81",
    ]
    for url in anfol:
        await call.message.answer_audio(url, caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol9")
async def tavba(call: CallbackQuery):
    tavba = [
        "https://t.me/Quron_Tafsiri_30_pora/83",
        "https://t.me/Quron_Tafsiri_30_pora/95",
        "https://t.me/Quron_Tafsiri_30_pora/96",
        "https://t.me/Quron_Tafsiri_30_pora/97",
    ]
    for url in tavba:
        await call.message.answer_audio(url, caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol10")
async def yunus(call: CallbackQuery):
    yunus = [
        "https://t.me/Quron_Tafsiri_30_pora/98",
        "https://t.me/Quron_Tafsiri_30_pora/99",
        "https://t.me/Quron_Tafsiri_30_pora/100",
    ]
    for url in yunus:
        await call.message.answer_audio(url, caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol11")
async def hud(call: CallbackQuery):
    hud = [
        "https://t.me/Quron_Tafsiri_30_pora/101",
        "https://t.me/Quron_Tafsiri_30_pora/102",
        "https://t.me/Quron_Tafsiri_30_pora/103",
    ]
    for url in hud:
        await call.message.answer_audio(url, caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol12")
async def yusuf(call: CallbackQuery):
    yusuf = [
        "https://t.me/Quron_Tafsiri_30_pora/104",
        "https://t.me/Quron_Tafsiri_30_pora/105",
        "https://t.me/Quron_Tafsiri_30_pora/106",
    ]
    for url in yusuf:
        await call.message.answer_audio(url, caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol13")
async def rad(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/107",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol14")
async def ibrohim(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/108",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol15")
async def hijr(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/109",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/110",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol16")
async def nahl(call: CallbackQuery):
    nahl = [
        "https://t.me/Quron_Tafsiri_30_pora/111",
        "https://t.me/Quron_Tafsiri_30_pora/112",
        "https://t.me/Quron_Tafsiri_30_pora/113",
    ]
    for url in nahl:
        await call.message.answer_audio(url, caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol17")
async def isro(call: CallbackQuery):
    isro = [
        "https://t.me/Quron_Tafsiri_30_pora/114",
        "https://t.me/Quron_Tafsiri_30_pora/115",
        "https://t.me/Quron_Tafsiri_30_pora/116",
    ]
    for url in isro:
        await call.message.answer_audio(url, caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol18")
async def kahf(call: CallbackQuery):
    kahf = [
        "https://t.me/Quron_Tafsiri_30_pora/117",
        "https://t.me/Quron_Tafsiri_30_pora/118",
        "https://t.me/Quron_Tafsiri_30_pora/119",
    ]
    for url in kahf:
        await call.message.answer_audio(url, caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol19")
async def maryam(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/120",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/121",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol20")
async def toha(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/122",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/123",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol21")
async def anbiyo(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/124",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/125",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol22")
async def haj(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/126",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/127",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol23")
async def mominun(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/128",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/129",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/130",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")

@dp.callback_query_handler(text="hilol24")
async def nur(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/131",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/132",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol25")
async def furqon(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/133",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/134",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol26")
async def shuaro(call: CallbackQuery):
    shuaro = [
        "https://t.me/Quron_Tafsiri_30_pora/135",
        "https://t.me/Quron_Tafsiri_30_pora/136",
        "https://t.me/Quron_Tafsiri_30_pora/137",
        "https://t.me/Quron_Tafsiri_30_pora/138",
    ]
    for url in shuaro:
        await call.message.answer_audio(url, caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol27")
async def naml(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/139",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/140",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol28")
async def qosos(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/141",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/142",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol29")
async def ankabut(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/143",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/144",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")



@dp.callback_query_handler(text="hilol30")
async def rum(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/145",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/146",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol31")
async def luqmon(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/149",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol32")
async def sajda(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/151",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol33")
async def ahzob(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/152",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/153",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol34")
async def saba(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/149",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="hilol35")
async def fotir(call: CallbackQuery):
    await call.message.answer_audio("CQACAgIAAxkBAAEObr1iIJHBf0Ll7l1rXMKzAozEG0ywiQACthMAAtxKCUm9zQNH7YHdWyME",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h36")
async def yosin(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/155",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h37")
async def soffat(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/156",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h38")
async def sod(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/157",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h39")
async def zumar(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/158",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h40")
async def gofir(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/159",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h41")
async def fussilat(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/160",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h42")
async def shuro(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/161",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h43")
async def zuhruf(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/162",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h44")
async def duxon(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/163",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h45")
async def josiya(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/164",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h46")
async def ahqof(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/165",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h47")
async def muhammad(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/166",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h48")
async def fath(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/167",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h49")
async def hujurot(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/168",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h50")
async def qof(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/169",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h51")
async def zoriyot(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/170",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h52")
async def tur(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/171",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h53")
async def najm(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/172",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h54")
async def qamar(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/173",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h55")
async def rohman(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/174",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h56")
async def voqea(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/198",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h57")
async def hadid(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/199",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h58")
async def mujodala(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/200",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h59")
async def hashr(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/207",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h60")
async def mumtahana(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/208",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h61")
async def sof(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/209",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h62")
async def juma(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/210",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h63")
async def munofiqun(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/211",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h64")
async def tagobun(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/212",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h65")
async def taloq(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/213",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h66")
async def tahrim(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/214",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h67")
async def mulk(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/215",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h68")
async def qalam(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/217",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h69")
async def haqqo(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/218",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h70")
async def maorij(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/219",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h71")
async def nuh(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/220",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h72")
async def jin(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/221",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h73")
async def muzzammil(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/222",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h74")
async def muddassir(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/223",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h75")
async def qiyomat(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/224",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h76")
async def inson(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/225",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h77")
async def mursalot(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/226",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h78")
async def naba(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/227",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h79")
async def naziat(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/234",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h80")
async def abasa(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/235",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h81")
async def takvir(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/236",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h82")
async def infitor(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/237",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h83")
async def mutoffifiyn(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/238",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h84")
async def inshiqoq(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/239",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h85")
async def buruj(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/240",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h86")
async def toriq(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/241",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h87")
async def ala(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/242",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h88")
async def goshiya(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/243",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h89")
async def fajr(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/244",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h90")
async def balad(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/245",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h91")
async def shams(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/246",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h92")
async def layl(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/247",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h93")
async def zuho(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/248",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h94")
async def sharh(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/249",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h95")
async def tiyn(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/250",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h96")
async def alaq(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/251",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h97")
async def qadr(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/252",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h98")
async def bayyina(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/253",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h99")
async def zalzala(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/254",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h100")
async def adiyat(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/255",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h101")
async def qoriya(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/256",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h102")
async def takosur(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/257",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h103")
async def asr(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/258",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h104")
async def humaza(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/259",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h105")
async def fil(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/260",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h106")
async def quraysh(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/261",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h107")
async def maun(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/262",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h108")
async def kavsar(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/263",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h109")
async def kafirun(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/264",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h110")
async def nasr(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/265",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h111")
async def masad(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/266",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h112")
async def ihlos(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/275",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h113")
async def falaq(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/267",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")


@dp.callback_query_handler(text="h114")
async def nas(call: CallbackQuery):
    await call.message.answer_audio("https://t.me/Quron_Tafsiri_30_pora/268",
                                    caption="Muallif: Shayh Muhammad Sodiq Muhammad Yusuf\n@islomuz_quron_bot")






