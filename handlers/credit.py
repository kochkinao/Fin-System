from aiogram import types, F
import keyboards
from tg import dp

#Кредитные карты
@dp.callback_query(F.data.startswith('credit'))
async def credit_card(call: types.CallbackQuery):
    await call.message.edit_caption(caption=f"{call.from_user.full_name}, я рад, что ты решил выполнить это задание, ознакамливайся с необходимой и сразу после этого приступай к работе 😋\n<b>Возможный заработок в этом блоке: 10.100₽</b>\n\n"
                              f"<b>Целевое действие</b> - активация карты и выполненная покупка\n\n"
                              f"<b>НАЗВАНИЯ КОМПАНИЙ И ВАШ ЗАРАБОТОК</b>\n"
                              f"💰Росбанк (ЦД - покупка от 500р) -выплата 1800₽\n"
                              f"💰Свойбанк (ЦД - покупка от 50р) - выплата 1800₽\n"
                              f"💰Хоумбанк (ЦД - покупка от 500₽) - выплата 1600₽\n"
                              f"💰МТС (ЦД - покупка от 100р) - выплата 1000₽\n"
                              f"💰Газпром (ЦД - покупка от 100р) - выплата 1700₽ + 1500₽ от банка\n"
                              f"💰АК Барс (ЦД - покупка от 100р) - выплата 700₽", reply_markup=keyboards.go_credit_kb, parse_mode="HTML")