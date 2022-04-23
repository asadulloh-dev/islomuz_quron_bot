from filters import IsPrivate
from loader import dp

from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import Command

from keyboards.default.darslar_keyboard import darslar, ruhiy_tarbiya


@dp.message_handler(IsPrivate(), text="🧑🏻‍🏫 Darslar")
async def darslar0(mes: Message):
    await mes.answer("Ushbu bo'limda ustozlarning ilmiy suhbat va darslaridan baxramand bo'lishingiz mumkin",
                     reply_markup=darslar)


@dp.message_handler(text="Ruhiy tarbiya")
async def ruhiy(mes: Message):
    await mes.answer(
        "Ushbu bo'limda shayx Muhammad Sodiq Muhammad Yusuf rohimahullohning Ramazon oyidagi Ruhiy tarbiya suhbatlaridan keltirilgan ",
        reply_markup=ruhiy_tarbiya)


@dp.message_handler(text="Poklanish (1-qism)")
async def poklanish1(mes: Message):
    await mes.answer("Ruhiy tarbiya darslari:\nhttps://youtube.com/playlist?list=PLys356tU5j5SFsAgtAzOK8OKH8SgLUvl3\n"
                     "Video shakli: https://youtube.com/playlist?list=PLi7SB6MZij7eyaXe_MwNYdDpX0GmUXSqV")
    audios = ["https://t.me/ruhiy_tarbiya_darslar/2",
              "https://t.me/ruhiy_tarbiya_darslar/3",
              "https://t.me/ruhiy_tarbiya_darslar/4",
              "https://t.me/ruhiy_tarbiya_darslar/6",
              "https://t.me/ruhiy_tarbiya_darslar/10",
              "https://t.me/ruhiy_tarbiya_darslar/14",
              "https://t.me/ruhiy_tarbiya_darslar/16",
              "https://t.me/ruhiy_tarbiya_darslar/18",
              "https://t.me/ruhiy_tarbiya_darslar/20",
              "https://t.me/ruhiy_tarbiya_darslar/22",
              "https://t.me/ruhiy_tarbiya_darslar/28",
              "https://t.me/ruhiy_tarbiya_darslar/30",
              "https://t.me/ruhiy_tarbiya_darslar/62",
              "https://t.me/ruhiy_tarbiya_darslar/63",
              "https://t.me/ruhiy_tarbiya_darslar/64",
              "https://t.me/ruhiy_tarbiya_darslar/65",
              "https://t.me/ruhiy_tarbiya_darslar/66",
              "https://t.me/ruhiy_tarbiya_darslar/67",
              "https://t.me/ruhiy_tarbiya_darslar/68"]

    for i in audios:
        await mes.answer_audio(i, caption="@islomuz_quron_bot")


@dp.message_handler(text="Poklanish (2-qism)")
async def poklanish2(mes: Message):
    audios = [
        "https://t.me/ruhiy_tarbiya_darslar/69",
        "https://t.me/ruhiy_tarbiya_darslar/70",
        "https://t.me/ruhiy_tarbiya_darslar/71",
        "https://t.me/ruhiy_tarbiya_darslar/72",
        "https://t.me/ruhiy_tarbiya_darslar/73",
        "https://t.me/ruhiy_tarbiya_darslar/74",
        "https://t.me/ruhiy_tarbiya_darslar/75",
        "https://t.me/ruhiy_tarbiya_darslar/76",
        "https://t.me/ruhiy_tarbiya_darslar/77",
        "https://t.me/ruhiy_tarbiya_darslar/78",
        "https://t.me/ruhiy_tarbiya_darslar/79",
        "https://t.me/ruhiy_tarbiya_darslar/80",
        "https://t.me/ruhiy_tarbiya_darslar/81",
        "https://t.me/ruhiy_tarbiya_darslar/82",
        "https://t.me/ruhiy_tarbiya_darslar/83",
        "https://t.me/ruhiy_tarbiya_darslar/84",
        "https://t.me/ruhiy_tarbiya_darslar/95",
    ]
    for i in audios:
        await mes.answer_audio(i, caption="@islomuz_quron_bot")


@dp.message_handler(text="Tiklanish (1-qism)")
async def tiklanish1(mes: Message):
    audios = [
        "https://t.me/ruhiy_tarbiya_darslar/96",
        "https://t.me/ruhiy_tarbiya_darslar/97",
        "https://t.me/ruhiy_tarbiya_darslar/98",
        "https://t.me/ruhiy_tarbiya_darslar/99",
        "https://t.me/ruhiy_tarbiya_darslar/100",
        "https://t.me/ruhiy_tarbiya_darslar/104",
        "https://t.me/ruhiy_tarbiya_darslar/105",
        "https://t.me/ruhiy_tarbiya_darslar/106",
        "https://t.me/ruhiy_tarbiya_darslar/109",
        "https://t.me/ruhiy_tarbiya_darslar/110",
        "https://t.me/ruhiy_tarbiya_darslar/111",
        "https://t.me/ruhiy_tarbiya_darslar/112",

    ]
    for i in audios:
        await mes.answer_audio(i, caption="@islomuz_quron_bot")


@dp.message_handler(text="Tiklanish (2-qism)")
async def tiklanish2(mes: Message):
    audios = [
        "https://t.me/ruhiy_tarbiya_darslar/113",
        "https://t.me/ruhiy_tarbiya_darslar/114",
        "https://t.me/ruhiy_tarbiya_darslar/116",
        "https://t.me/ruhiy_tarbiya_darslar/119",
        "https://t.me/ruhiy_tarbiya_darslar/124",
        "https://t.me/ruhiy_tarbiya_darslar/125",
        "https://t.me/ruhiy_tarbiya_darslar/126",
        "https://t.me/ruhiy_tarbiya_darslar/127",
        "https://t.me/ruhiy_tarbiya_darslar/128",
    ]
    for i in audios:
        await mes.answer_audio(i, caption="@islomuz_quron_bot")


@dp.message_handler(text="Xulqlanish (1-qism)")
async def xulqlanish1(mes: Message):
    audios = [
        "https://t.me/ruhiy_tarbiya_darslar/129",
        "https://t.me/ruhiy_tarbiya_darslar/130",
        "https://t.me/ruhiy_tarbiya_darslar/131",
        "https://t.me/ruhiy_tarbiya_darslar/132",
        "https://t.me/ruhiy_tarbiya_darslar/133",
        "https://t.me/ruhiy_tarbiya_darslar/134",
        "https://t.me/ruhiy_tarbiya_darslar/136",
        "https://t.me/ruhiy_tarbiya_darslar/137",
        "https://t.me/ruhiy_tarbiya_darslar/139",
        "https://t.me/ruhiy_tarbiya_darslar/142",
        "https://t.me/ruhiy_tarbiya_darslar/143",
        "https://t.me/ruhiy_tarbiya_darslar/145",
        "https://t.me/ruhiy_tarbiya_darslar/146",
        "https://t.me/ruhiy_tarbiya_darslar/147",
        "https://t.me/ruhiy_tarbiya_darslar/148",
        "https://t.me/ruhiy_tarbiya_darslar/149"
    ]
    for i in audios:
        await mes.answer_audio(i, caption="@islomuz_quron_bot")


@dp.message_handler(text="Xulqlanish (2-qism)")
async def xulqlanish2(mes: Message):
    audios = [
        "https://t.me/ruhiy_tarbiya_darslar/150",
        "https://t.me/ruhiy_tarbiya_darslar/151",
        "https://t.me/ruhiy_tarbiya_darslar/153",
        "https://t.me/ruhiy_tarbiya_darslar/154",
        "https://t.me/ruhiy_tarbiya_darslar/155",
        "https://t.me/ruhiy_tarbiya_darslar/156",
        "https://t.me/ruhiy_tarbiya_darslar/157",
        "https://t.me/ruhiy_tarbiya_darslar/161",
        "https://t.me/ruhiy_tarbiya_darslar/162",
        "https://t.me/ruhiy_tarbiya_darslar/165",
        "https://t.me/ruhiy_tarbiya_darslar/166",
        "https://t.me/ruhiy_tarbiya_darslar/167",
        "https://t.me/ruhiy_tarbiya_darslar/168"
    ]
    for i in audios:
        await mes.answer_audio(i, caption="@islomuz_quron_bot")


# 2.Qur'on bilan tanishuv

@dp.message_handler(text="Qur'on bilan tanishuv")
async def qbtanishuv(mes: Message):
    await mes.answer(
        "Ushbu bo'limda ustoz Hasanxon qori Yaxyo Abdulmajidning \"Qur'on bilan tanishuv\" Ramazon suxbatlaridan baxramand bo'lishingiz mumkin\nManba (YouTube): https://youtube.com/playlist?list=PLE0uv2eFBCH3pcRx63D7eCqkpbRYY96d3")
    tanishuv1 = [
        "https://t.me/islomiy_mediya/38",
        "https://t.me/islomiy_mediya/39",
        "https://t.me/islomiy_mediya/40",
        "https://t.me/islomiy_mediya/41",
        "https://t.me/islomiy_mediya/42",
        "https://t.me/islomiy_mediya/43",
        "https://t.me/islomiy_mediya/44",
        "https://t.me/islomiy_mediya/45",
        "https://t.me/islomiy_mediya/46",
        "https://t.me/islomiy_mediya/47",
        "https://t.me/islomiy_mediya/48",
        "https://t.me/islomiy_mediya/49",
        "https://t.me/islomiy_mediya/50",
    ]
    for i in tanishuv1:
        await mes.answer_video(i, caption="@islomiy_mediya\n@islomuz_quron_bot")
    await mes.answer("Davomi: /suhbat2")


@dp.message_handler(Command('suhbat2'), IsPrivate())
async def qbtanishuv2(mes: Message):
    tanishuv2 = [
        "https://t.me/islomiy_mediya/51",
        "https://t.me/islomiy_mediya/52",
        "https://t.me/islomiy_mediya/53",
        "https://t.me/islomiy_mediya/54",
        "https://t.me/islomiy_mediya/55",
        "https://t.me/islomiy_mediya/56",
        "https://t.me/islomiy_mediya/57",
        "https://t.me/islomiy_mediya/58",
        "https://t.me/islomiy_mediya/59",
        "https://t.me/islomiy_mediya/60",
        "https://t.me/islomiy_mediya/61",
        "https://t.me/islomiy_mediya/62",
        "https://t.me/islomiy_mediya/63",
        "https://t.me/islomiy_mediya/64",
        "https://t.me/islomiy_mediya/65",
    ]
    for i in tanishuv2:
        await mes.answer_video(i, caption="@islomy_mediya\n@islomuz_quron_bot")

    # 3.Muallimi soniy


@dp.message_handler(text="Muallimi soniy")
async def muallimis(mes: Message):
    await mes.answer("""
<b>
Ushbu kanal orqali ustozimiz 
Shayx Alijon qorining rasmiy kanallari orqali
"Muallimi soniy" va boshqa darslaridan baxramand bo'lishingiz mumkin

Usmon roziyallohu anhudan rivoyat qilinadi:
"Payg‘ambarimiz sollallohu alayhi vasallam:
<b>"Sizlarning eng yaxshilaringiz Qur’onni o‘rganib, boshqalarga ham o‘rgatadiganlaringizdir"</b>, dedilar".
(Imom Buxoriy rivoyati).

@Alquranuz
@Quron_ahlidan

@islomuz_quron_bot 
</b>""")
    await mes.answer("https://t.me/QURON_AHLIDAN/1351")


# 4. Arab tili
@dp.message_handler(text="Arab tili")
async def arabtili(mes: Message):
    text = """
<b>
Quyidagi kanallar orqali arab tilini o'rganishingiz mumkin:

www.arabic.uz
@arabicuz_nahv        (Nahv-sarf kanali)
@arabicuz_nahv_test   (testlar)
@arabicuz             (hikmat kanali)
@arabicuz_bot         (hikmat boti)
@Arabicuz_Media_bot   (media boti)
@arabicuz_nahv_hikmat (hikmatlar sharhi)

@islomuz_quron_bot
</b>"""
    await mes.answer(text)
    await mes.answer_video("https://t.me/arabicuz_nahv/2923", caption="""
@arabic_nahv kanalidagi darsliklar qo'llanmasi

@islomuz_quron_bot""")


@dp.message_handler(text="Ramazon 2014")
async def ramazon2014(mes: Message):
    await mes.answer("Shayx Muhammad Sodiq Muhammad Yusuf rohimahullohning ramazon oyidagi suhbatlari:")
    audios = [
        "https://t.me/ruhiy_tarbiya_darslar/172",
        "https://t.me/ruhiy_tarbiya_darslar/173",
        "https://t.me/ruhiy_tarbiya_darslar/174",
        "https://t.me/ruhiy_tarbiya_darslar/175",
        "https://t.me/ruhiy_tarbiya_darslar/176",
        "https://t.me/ruhiy_tarbiya_darslar/177",
        "https://t.me/ruhiy_tarbiya_darslar/178",
        "https://t.me/ruhiy_tarbiya_darslar/179",
        "https://t.me/ruhiy_tarbiya_darslar/181",
        "https://t.me/ruhiy_tarbiya_darslar/182",
    ]
    for i in audios:
        await mes.answer_audio(i, caption="@islomuz_quron_bot")
    await mes.answer("Davomi: /ramazon2")


@dp.message_handler(Command('ramazon2'), IsPrivate())
async def ramazon20142(mes: Message):
    audios = [
        "https://t.me/ruhiy_tarbiya_darslar/183",
        "https://t.me/ruhiy_tarbiya_darslar/184",
        "https://t.me/ruhiy_tarbiya_darslar/185",
        "https://t.me/ruhiy_tarbiya_darslar/186",
        "https://t.me/ruhiy_tarbiya_darslar/187",
        "https://t.me/ruhiy_tarbiya_darslar/188",
        "https://t.me/ruhiy_tarbiya_darslar/189",
        "https://t.me/ruhiy_tarbiya_darslar/190",
        "https://t.me/ruhiy_tarbiya_darslar/191",
        "https://t.me/ruhiy_tarbiya_darslar/192",
    ]
    for i in audios:
        await mes.answer_audio(i, caption="@islomuz_quron_bot")
    await mes.answer("Davomi: /ramazon3")


@dp.message_handler(Command('ramazon3'), IsPrivate())
async def ramazon20143(mes: Message):
    audios = [
        "https://t.me/ruhiy_tarbiya_darslar/193",
        "https://t.me/ruhiy_tarbiya_darslar/194",
        "https://t.me/ruhiy_tarbiya_darslar/195",
        "https://t.me/ruhiy_tarbiya_darslar/198",
        "https://t.me/ruhiy_tarbiya_darslar/199",
        "https://t.me/ruhiy_tarbiya_darslar/200",
        "https://t.me/ruhiy_tarbiya_darslar/201"
    ]
    for i in audios:
        await mes.answer_audio(i, caption="@islomuz_quron_bot")


# 6.Qur'on qalblar shifosi
@dp.message_handler(text="Qur'on qalblar shifosi")
async def qalblarshifosi(mes: Message):
    await mes.answer(
        "Ustoz Shayx Alijon qori hafizahullohning \"Qur'on qalblar shifosi\" nomli suhbatlaridan baxramand bo'ling\n"
        "Manba(Rasmiy kanal): @Alquranuz\n"
        "\n@islomuz_quron_bot")
    await mes.answer_video("https://t.me/islomiy_mediya/70", caption="""
Alijon qori Fayzulla Maxdum oʻgʻli:
Qurʼon sari qilingan safar

Davomi: /qalblarshifosi

@islomuz_quron_bot""")


@dp.message_handler(Command('qalblarshifosi'), IsPrivate())
async def qalblarsh(mes: Message):
    await mes.answer_video("https://t.me/islomiy_mediya/66", caption="""
1.Qur'on qalb shifosi - Tajvid ilmi nima? (1-qism)

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/67", caption="""
    1.Qur'on qalb shifosi - Tajvid ilmi nima? (2-qism)

    Shayx Alijon qori

    Rasmiy kanal: @Alquranuz

    @islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/68", caption="""
2.Qur’on qalb shifosi - 10 xil qiroat hamda qiroat imomlari haqida (1-qism)

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/69", caption="""
2.Qur’on qalb shifosi - 10 xil qiroat hamda qiroat imomlari haqida (2-qism)

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/71", caption="""
3.Qur’on qalb shifosi - Qur’onni o’rganayotgan azizlarimizga tavsiya va maslahatlar 

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/72", caption="""
4.Qur’on qalb shifosi - Ubay ibn Kaa’b: Allohdan hadya olgan sahobiy

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/73", caption="""
5.Qur’on qalb shifosi: Imom Nofe’-tanasidan mushk ifori taralgan alloma!

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/74", caption="""
6.Qur’on qalb shifosi: Imom Hamza Habib azzayyad rahimahullohning karomati

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/75", caption="""
7.Qur’on qalb shifosi: Ibn Omir ad-Dimashqiy-bir vaqtda o’n ming talabaga ta’lim bergan alloma

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/76", caption="""
8.Qur’on qalb shifosi: Qiroat ilmida ijoza berish tartibi (1-qism)

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/77", caption="""
8.Qur’on qalb shifosi: Qiroat ilmida ijoza berish tartibi (2-qism)

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/78", caption="""
9.Qur’on qalb shifosi: Qur’on ta’limi uslublari (1-qism)

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/79", caption="""
9.Qur’on qalb shifosi: Qur’on ta’limi uslublari (2-qism)

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/80", caption="""
9.Qur’on qalb shifosi: Qur’on ta’limi uslublari (3-qism)

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/81", caption="""
9.Qur’on qalb shifosi: Qur’on ta’limi uslublari (4-qism)

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/82", caption="""
10. Qur’on qalb shifosi: Ijoza nima?

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/83", caption="""
11. Qurʼon qalb shifosi: Ijoza olish shartlari

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/84", caption="""
12. Qurʼon qalb shifosi: Qiroat ijozasi tafsilotlari

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/85", caption="""
13. Qurʼon qalb shifosi: Qurʼonni jamlagan sahobalardan biri

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/86", caption="""
14. Qurʼon qalb shifosi: Qurʼonga xizmat qilgan buyuklar

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")

    await mes.answer_video("https://t.me/islomiy_mediya/87", caption="""
15. Qurʼon qalb shifosi: Yetti qiroatni jamlagan koʻzi ojiz alloma

Shayx Alijon qori

Rasmiy kanal: @Alquranuz

@islomuz_quron_bot""")
