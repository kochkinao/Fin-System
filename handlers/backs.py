from aiogram import types, F

import config
import keyboards
from tg import dp


@dp.callback_query(F.data.startswith('back2'))
async def back_l(call: types.CallbackQuery):
    try:
        await call.message.edit_caption(
            caption=f"{call.from_user.full_name}, я рад, что ты решил поделиться возможностью заработать со своими друзьями🤗\n\n"
                    "<b>Бонус за друзей:</b>\n"
                    "За каждого друга ты можешь получить 2000₽\n\n"
                    "У нас действует многоступенчатая система выплат\n"
                    "За каждое выполненное задание твоего друга ты получишь 200р\n"
                    "Считаются первые 10 выполненных заданий.\n\n"
                    "<b>Пояснение</b>\n"
                    "Друг выполнил 1 задание - выплата 200₽\n"
                    "Друг выполнил 3 задания - выплата 600₽\n"
                    "Друг выполнил 8 заданий - выплата 1600₽\n"
                    "<b>Выводить деньги можно только если друг выполнит 3+ заданий</b>\n\n"
                    "<b>Важно</b>\n"
                    "Грамотно выбирай своих друзей, при попытке обмана со стороны вашего друга, мы будем вынуждены заблокировать в нашей системе его и вас, без возможности вывести средства.\n\n"
                    "Этого не хочется ни нам, ни вам, поэтому, давайте жить дружно и честно😉",
            reply_markup=keyboards.referal,
            parse_mode="HTML")
    except Exception:
        await call.message.delete()


# Назад
@dp.callback_query(F.data.startswith('back'))
async def back_m(call: types.CallbackQuery):
    try:
        if call.from_user.id in config.ADMIN:
            await call.message.edit_caption(caption=f"Привет👋, {call.from_user.full_name}. "
                                                    f"Я - бот помощник по заработку денюжки на финансовых офферах и не только! 😊\n\n"
                                                    f"Следуй всем рекомендациям и получай выплаты!\n\n"
                                                    f"На данный момент выплаты производятся <b>только на карты Сбербанка!</b>",
                                            parse_mode="HTML", reply_markup=keyboards.admin_start_menu)
        else:
            await call.message.edit_caption(caption=f"Привет👋, {call.from_user.full_name}. "
                                                f"Я - бот помощник по заработку денюжки на финансовых офферах и не только! 😊\n\n"
                                                f"Следуй всем рекомендациям и получай выплаты!\n\n"
                                                f"На данный момент выплаты производятся <b>только на карты Сбербанка!</b>",
                                        parse_mode="HTML", reply_markup=keyboards.start_menu)
    except Exception:
        await call.message.delete()


# Главное меню
@dp.callback_query(F.data.startswith('main_menu'))
async def main_m(call: types.CallbackQuery):
    if call.from_user.id in config.ADMIN:
        await call.message.edit_caption(caption=f"Привет👋, {call.from_user.full_name}. "
                                                f"Я - бот помощник по заработку денюжки на финансовых офферах и не только! 😊\n\n"
                                                f"Следуй всем рекомендациям и получай выплаты!\n\n"
                                                f"На данный момент выплаты производятся <b>только на карты Сбербанка!</b>",
                                        parse_mode="HTML", reply_markup=keyboards.admin_start_menu)
    else:
        await call.message.edit_caption(caption=f"Привет👋, {call.from_user.full_name}. "
                                            f"Я - бот помощник по заработку денюжки на финансовых офферах и не только! 😊\n\n"
                                            f"Следуй всем рекомендациям и получай выплаты!\n\n"
                                            f"На данный момент выплаты производятся <b>только на карты Сбербанка!</b>",
                                    parse_mode="HTML", reply_markup=keyboards.start_menu)

