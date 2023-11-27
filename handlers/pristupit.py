from aiogram import types, F
import keyboards
from tg import dp


# Приступить
@dp.callback_query(F.data.startswith('pristupit_credit'))
async def pristupit_call(call: types.CallbackQuery):
    await call.message.edit_caption(caption="<b>Теперь краткая пошаговая инструкция по последующим действиям</b>\n\n"
                                    "1. Переходите по ссылке на витрину\n"
                                    "2. Оставляете заявки <b>только на те продукты, которые в списке!!!</b>\n"
                                    "3. Затем получаете карту и делаете ЦД\n"
                                    "4. ЦД нужно выполнять только покупками в оффлайн и интернет магазинах\n"
                                    "5. После выполненного ЦД присылаете необходимые скрины в поддержку бота и получаете выплату\n\n"
                                    "Если все понятно, <b>ЖМИ</b> на ссылку ниже и приступай к работе😏\n",
                                    reply_markup=keyboards.get_link_credit, parse_mode="HTML")


@dp.callback_query(F.data.startswith('pristupit_deb'))
async def pristupit_call(call: types.CallbackQuery):
    await call.message.edit_caption(caption="<b>Теперь краткая пошаговая инструкция по последующим действиям</b>\n\n"
                                    "1. Переходите по ссылке на витрину\n"
                                    "2. Оставляете заявки <b>только на те продукты, которые в списке!!!</b>\n"
                                    "3. Затем получаете карту и делаете ЦД\n"
                                    "4. ЦД нужно выполнять только покупками в оффлайн и интернет магазинах\n"
                                    "5. После выполненного ЦД присылаете необходимые скрины в поддержку бота и получаете выплату\n\n"
                                    "Если все понятно, <b>ЖМИ</b> на ссылку ниже и приступай к работе😏\n",
                                    reply_markup=keyboards.get_link_deb, parse_mode="HTML")
