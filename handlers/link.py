from aiogram import types, F
import keyboards
from tg import dp


@dp.callback_query(F.data.startswith('link_deb'))
async def l_deb(call: types.CallbackQuery):
    await call.message.edit_caption(caption="<b>Приступаем к заданию</b>\n\n"
                                    "https://clck.ru/36jgcC - Газпром\n\n"
                                    "https://clck.ru/36jggx - Открытие\n\n"
                                    "https://clck.ru/36jgh8 - ВТБ\n\n"
                                    "https://clck.ru/36jghQ - Промсвязьбанк\n\n"
                                    "https://clck.ru/36jgi5 - Хоумбанк\n\n"
                                    "https://clck.ru/36jgiB - Форабанк\n\n"
                                    "https://clck.ru/36jgiN - Ак Барс",
                                    parse_mode="HTML", reply_markup=keyboards.main_menu)


# Ссылки
@dp.callback_query(F.data.startswith('link_credit'))
async def l_credit(call: types.CallbackQuery):
    await call.message.edit_caption(caption="<b>Приступаем к заданию</b>\n\n"
                                    "https://clck.ru/36jgcC - Росбанк\n\n"
                                    "https://clck.ru/36jgds - Свой банк\n\n"
                                    "https://clck.ru/36jge4 - Хоум банк\n\n"
                                    "https://clck.ru/36jgeC - Открытие\n\n"
                                    "https://clck.ru/36jgeM - Совкомбанк\n\n",
                                    parse_mode="HTML", reply_markup=keyboards.main_menu)



