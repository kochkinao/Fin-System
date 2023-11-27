from aiogram import types, F
import keyboards
from tg import dp

#Кредитные карты
@dp.callback_query(F.data.startswith('credit'))
async def credit_card(call: types.CallbackQuery):
    await call.message.edit_caption(caption=f"{call.from_user.full_name}, я рад, что ты решил выполнить это задание, ознакамливайся с необходимой и сразу после этого приступай к работе 😋\n<b>Возможный заработок в этом блоке: 14.823₽</b>\n\n"
                              f"<b>Целевое действие</b> - активация карты и выполненная покупка\n\n"
                              f"<b>НАЗВАНИЯ КОМПАНИЙ И ВАШ ЗАРАБОТОК</b>\n"
                              f"💰Росбанк (цд - покупка от 500р) -выплата 2500\n"
                              f"💰Свойбанк(цд -активация и первая транзакция) - выплата 1900₽\n"
                              f"💰Хоумбанк(цд - покупка от 500₽) - выплата 1600₽\n"
                              f"💰Открытие (цд -активация и первая транзакция) - выплата 1200₽\n"
                              f"💰Совкомбанк(цд -выдача карты) -  выплата 1000₽\n", reply_markup=keyboards.go_credit_kb, parse_mode="HTML")