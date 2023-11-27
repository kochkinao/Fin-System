from aiogram import types, F
import keyboards
from tg import dp


# Начать 💵
@dp.callback_query(F.data.startswith('go_credit'))
async def go_call(call: types.CallbackQuery):
    await call.message.edit_caption(
        caption="<b><i>Перед началом работы вам необходимо ознакомиться с указанной ниже информацией</i></b>\n\n"
        "<b>Суть задания</b>\n"
        "Вам необходимо перейти по ссылке, которую пришлю вам я на наш сайт, далее перейти на сайт компании, заказать карту и выполнить ЦД по каждой карте😉\n\n"
        "<b>ОБЯЗАТЕЛЬНЫЕ условия</b>\n"
        "- Вы не должны были быть клиентом банка до этого\n"
        "- Без выполнения ЦД мы не сможем вам выплатить\n\n"
        "<b>Отчетность</b>\n"
        "После заказа карты и выполнения ЦД вам необходимо нам прислать:\n"
        "1. Скриншот заказа карты по нашей ссылке\n"
        "2. Фото полученной пластиковой карты\n"
        "3. Скриншот из ЛК, на котором будет видна сделанная вами трата на необходимую сумму\n\n"
        "<i>При нажатии на кнопку ниже, вы соглашаетесь с нашими правилами</i>",
        reply_markup=keyboards.pristupit_credit, parse_mode="HTML")


@dp.callback_query(F.data.startswith('go_deb'))
async def go_call(call: types.CallbackQuery):
    await call.message.edit_caption(
        caption="<b><i>Перед началом работы вам необходимо ознакомиться с указанной ниже информацией</i></b>\n\n"
        "<b>Суть задания</b>\n"
        "Вам необходимо перейти по ссылке, которую пришлю вам я на наш сайт, далее перейти на сайт компании, заказать карту и выполнить ЦД по каждой карте😉\n\n"
        "<b>ОБЯЗАТЕЛЬНЫЕ условия</b>\n"
        "- Вы не должны были быть клиентом банка до этого\n"
        "- Без выполнения ЦД мы не сможем вам выплатить\n\n"
        "<b>Отчетность</b>\n"
        "После заказа карты и выполнения ЦД вам необходимо нам прислать:\n"
        "1. Скриншот заказа карты по нашей ссылке\n"
        "2. Фото полученной пластиковой карты\n"
        "3. Скриншот из ЛК, на котором будет видна сделанная вами трата на необходимую сумму\n\n"
        "<i>При нажатии на кнопку ниже, вы соглашаетесь с нашими правилами</i>", reply_markup=keyboards.pristupit_deb,
        parse_mode="HTML")
