from loader import dp

from aiogram.types import Message

@dp.message_handler(text="💌 Loyihani qo'llab-quvvatlash")
async def donate(mes: Message):
    await mes.answer("Agar ushbu botimiz sizga ma'qul kelgan bo'lsa botni ulashishingiz, loyiha muallifi haqqiga duo qilishingiz, agar qodir bo'lsangiz moddiy qo'llab quvvatlashingiz mumkin")
