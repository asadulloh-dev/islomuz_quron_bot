from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("zikr2", 'Tongi va kechki duolar'),
            types.BotCommand("zikr3", 'Duolar'),
            types.BotCommand("suhbat2", "Qur'on bilan tanishuv"),
            types.BotCommand("ramazon2", "Ramazon suhbatlari"),
            types.BotCommand("qalblarshifosi", "Qur'on qalblar shifosi")
        ]
    )
