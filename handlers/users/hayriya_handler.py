from loader import dp

from aiogram.types import Message
from keyboards.default.hayriya_keyboard import hayriya_guruhlar


@dp.message_handler(text="💝 Hayriya")
async def ehson(mes: Message):
    text = "Ushbu bo'limda hayriya guruhlarining bog'lanmalari keltirilgan\n" \
           "Biz faqat dalolat qilamiz !!!"
    await mes.answer(text, reply_markup=hayriya_guruhlar)


@dp.message_handler(text="VAQF")
async def vaqf(mes: Message):
    text = """Vaqf hayriya jamoat fondining rasmiy sahifalari:
    
Veb sayt: www.vaqf.uz
Telegram: @vaqfuz,    @vaqfuzguruhi
Instagram: https://www.instagram.com/vaqfuzb
Facebook: https://www.facebook.com/vaqfuz
Xamkorlar uchun: +998951951610"""
    await mes.answer(text)


@dp.message_handler(text="Yurak Amri")
async def yurak_amri(mes: Message):
    text = """
Sardor Rahimxon boshchiligidagi Yurak Amri,
Ajr islom, 25+, 60 kabutar loyihalarining
ijtimoiy tarmoqdagi rasmiy sahifalari:

Yurak Amri: @YurakAmri_official
Ajr islom: @Ajr_islom            
YouTube: https://youtube.com/c/SardorRahimxon
Instagram: https://www.instagram.com/sardor_rahimxon_official/
https://www.instagram.com/yurak_amri_rasmiy/
Facebook: https://www.facebook.com/yurakamri_uz/"""
    await mes.answer(text)


@dp.message_handler(text="Sahovat Namangan")
async def saxovat_namangan(mes: Message):
    text = """"Sahovat Namangan" hayriya jamoat fondining 
ijtimoiy tarmoqdagi rasmiy sahifalari:

Telegram: @sahovat_namangan
Instagram: https://www.instagram.com/sahovatnamangan/
YouTube: https://www.youtube.com/c/SaxovatNamangan/
Facebook: https://www.facebook.com/pg/sahovatnamangan/"""
    await mes.answer(text)



@dp.message_handler(text="Mehrob himmati")
async def mehrob_himmati(mes: Message):
    text="""www.mehrob.uz sahifasi muassisi Shayx Sayyid
Rohmatulloh Termiziy tashabbusidagi «MEHROB HIMMATI»
hayriya fondining ijtimoiy tarmoqdagi rasmiy sahifalari:

Telegram: @mehrob_himmati
Instagram: https://www.instagram.com/mehrobhimmati.uz/"""
    await mes.answer(text)


@dp.message_handler(text="Mehrli qo'llar")
async def mehrli_qollar(mes: Message):
    text="""
"Mehrli qo'llar" hayriya fondining 
ijtimoiy tarmoqdagi rasmiy sahifalari:

Veb sayt: www.mehrli.uz
Telegram: @Mehrliqollar
Instagram: https://www.instagram.com/mehrliqollar/
YouTube: https://www.youtube.com/channel/UCC1UVnKvNG6hzz3-_Bjd8YA
Facebook: https://facebook.com/Mehrli.uz/
"""
    await mes.answer(text)


@dp.message_handler(text="Ezgu amal")
async def ezgu_amal(mes: Message):
    text="""
"Ezgu amal" hayriya fondining rasmiy sahifalari:

Veb sayt: ezguamal.org
Telegram: https://t.me/ezguamaluzb
Instagram: https://www.instagram.com/ezgu_amal/
Facebook: https://www.facebook.com/ezguamal
"""
    await mes.answer(text)