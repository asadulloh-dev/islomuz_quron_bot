from loader import dp

from aiogram.types import Message, CallbackQuery
from keyboards.inline.kitoblar_inline import kitoblar

@dp.message_handler(text="📚 Kitoblar")
async def kitob(mes: Message):
    await mes.answer("Kitoblar ro'yhati (pdf):", reply_markup=kitoblar)


@dp.callback_query_handler(text="mansur")
async def tarjimasi(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/86", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="qalblarshifosi")
async def qalblarsh(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/144", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="tariximuhammadiy")
async def tarixim(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/134", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="odobi")
async def odobi(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/38", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="korganmisiz")
async def sizpk(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/136", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="shamoiliy")
async def shamoili(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/142", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="qalblarkashfiyoti")
async def qalblark(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/67", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="abubakr")
async def abubakr(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/139", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="umar")
async def umar(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/74", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="taxoratvanamoz")
async def t_va_n(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/94", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="baxtiyoroila")
async def boila(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/98", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="birkunlari")
async def birkunlari(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/105", caption="@islomuz_quron_bot")


@dp.callback_query_handler(text="ismmanosi")
async def ismlar(call: CallbackQuery):
    await call.message.answer_document("")


@dp.callback_query_handler(text="abuhanifa")
async def abuhanifa(call: CallbackQuery):
    await call.message.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/39", caption="@islomuz_quron_bot")

#
# @dp.callback_query_handler(text="")
# async def(call: CallbackQuery):
#     await call.message.answer_document("")
#
#
# @dp.callback_query_handler(text="")
# async def(call: CallbackQuery):
#     await call.message.answer_document("")
#
