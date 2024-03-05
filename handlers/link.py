from aiogram import types, F
import keyboards
from tg import dp


@dp.callback_query(F.data.startswith('link_deb'))
async def l_deb(call: types.CallbackQuery):
    await call.message.edit_caption(caption="<b>Приступаем к заданию</b>\n\n"
                                    "https://clck.ru/39EWFB - ВТБ\n\n"
                                    "https://clck.ru/39EWJx - Газпром\n\n"
                                    "https://clck.ru/39EWNi - Ак Барс\n\n"
                                    "https://clck.ru/39EWRp - Хоум Банк\n\n"
                                    "https://clck.ru/39EWXe - Промсвязь Банк\n\n"
                                    "https://clck.ru/39EWaY - Фора Банк\n\n"
                                    "https://clck.ru/39EWee - Совком Банк\n\n"
                                    "https://clck.ru/39EWiU - ОТП Банк\n\n"
                                    "https://clck.ru/39EWnN - ВТБ Стикер\n\n",
                                    parse_mode="HTML", reply_markup=keyboards.main_menu)


# Ссылки
@dp.callback_query(F.data.startswith('link_credit'))
async def l_credit(call: types.CallbackQuery):
    await call.message.edit_caption(caption="<b>Приступаем к заданию</b>\n\n"
                                    "https://clck.ru/39EWu4 - Росбанк\n\n"
                                    "https://clck.ru/39EWvv - Газпромбанк\n\n"
                                    "https://clck.ru/39EWzA - МТС\n\n"
                                    "https://clck.ru/39EX4r - Хоум Банк\n\n"
                                    "https://clck.ru/39EX7A - Свой Банк\n\n"
                                    "https://clck.ru/39EX8k - Ак Барс",
                                    parse_mode="HTML", reply_markup=keyboards.main_menu)



