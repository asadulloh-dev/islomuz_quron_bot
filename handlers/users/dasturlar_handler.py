from loader import dp

from aiogram.types import Message, CallbackQuery
from keyboards.default.dasturlar_keyboard import dasturlar
from keyboards.inline.dasturlar_inline import quronga, siyratga, namozga, adabiyotlar, boshqadasturlar, arabtiliga



# Dasturlar menu
@dp.message_handler(text="📲 Dasturlar")
async def kitoblar(mes: Message):
    await mes.answer("Dasturlar ro'yhati (apk):", reply_markup=dasturlar)


@dp.message_handler(text="Qur'onga oid")
async def qurandastur(mes: Message):
    await mes.answer("Qur'onga oid dasturlar: ", reply_markup=quronga)


@dp.message_handler(text="Siyratga oid")
async def siyrat(mes: Message):
    await mes.answer("Siyratga oid dasturlar: ", reply_markup=siyratga)


@dp.message_handler(text="Namozga oid")
async def namoz(mes: Message):
    await mes.answer("Namozga oid dasturlar: ", reply_markup=namozga)


@dp.message_handler(text="Arab tiliga oid")
async def arab(mes: Message):
    await mes.answer("Arab tiliga oid dasturlar: ", reply_markup=arabtiliga)


@dp.message_handler(text="Adabiyotlar")
async def adabiyotdastur(mes: Message):
    await mes.answer("Adabiyotlar (dasturlar): ", reply_markup=adabiyotlar)


@dp.message_handler(text="Boshqalar")
async def boshqalar(mes: Message):
    await mes.answer("Turli dasturlar: ", reply_markup=boshqadasturlar)





# 1.1 qur'onga oid dasturlar

@dp.callback_query_handler(text="Tafsiri Hilol")
async def thilol(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/112", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="qurondasturi")
async def qurondastur(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/10", caption="@islomuz_quron_bot")
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/30", caption="@islomuz_quron_bot")
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/32", caption="@islomuz_quron_bot")
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/34", caption="@islomuz_quron_bot")
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/46", caption="@islomuz_quron_bot")


# @dp.callback_query_handler(text="abdurahmonmushafi")
# async def abdurahmonm(call: CallbackQuery):
#     await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/115", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="quranuzbek")
async def uzquran(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/131", caption="@islomuz_quron_bot")



# 1.2 Siyrat
@dp.callback_query_handler(text="payg'ambarlar")
async def qissasi(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/81", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="saodatasri")
async def saodatasri(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/132", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="oltinsilsila")
async def oltinsilsila(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/113", caption="@islomuz_quron_bot")



# 1.3 Namozga oid
@dp.callback_query_handler(text="namozdasturi")
async def namozd(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/128", caption="@islomuz_quron_bot")
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/102", caption="@islomuz_quron_bot")
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/100", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="muslimtaqvim")
async def mtaqvim(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/103", caption="@islomuz_quron_bot")



# 1.4 Arab tiliga oid
@dp.callback_query_handler(text="arabalifbosi")
async def arabalifbosi(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/108", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="araborganaman")
async def araborganaman(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/109", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="arabtilivatajvid")
async def arabtilivatajvid(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/126", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="tartil")
async def tartil(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/104", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="muallimi soniy")
async def msoniy(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/219", caption="@islomuz_quron_bot")



# 1.5 Adabiyotlar
@dp.callback_query_handler(text="solihlargulshani")
async def solihlarg(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/125", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="hilolebook")
async def hiloebook(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/120", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="gunohikabiralar")
async def gkabiralar(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/175", caption="@islomuz_quron_bot")



# 1.6 Boshqa dasturlar
@dp.callback_query_handler(text="asmaulhusna")
async def asmaulhusna(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/118", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="zikrahli")
async def zikrahli(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/117", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="zikrvaduolar")
async def zikrvaduolar(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/116", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="qirq")
async def qirqhq(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/127", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="olimbola")
async def olimbola(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Englishfor_IT/11", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="zukko")
async def zukkobola(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/121", caption="@islomuz_quron_bot")


# @dp.callback_query_handler(text="")
# async def (call: CallbackQuery):
#     await call.message.answer_document("", caption="@islomuz_quron_bot")
#
#
# @dp.callback_query_handler(text="")
# async def (call: CallbackQuery):
#     await call.message.answer_document("", caption="@islomuz_quron_bot")
#
#
# @dp.callback_query_handler(text="")
# async def (call: CallbackQuery):
#     await call.message.answer_document("", caption="@islomuz_quron_bot")
#
#









