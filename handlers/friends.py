from aiogram import types, F
import keyboards
from tg import dp, db


#Получить реферальную ссылку
@dp.callback_query(F.data.startswith('referal'))
async def ref_link(call: types.CallbackQuery):
    await call.message.edit_caption(caption=f"Твоя реферальная ссылка👇\nhttps://t.me/Fin_System_bot?start={call.from_user.id}", reply_markup=keyboards.back2, parse_mode="HTML")


#Список моих друзей
@dp.callback_query(F.data.startswith('list_friends'))
async def l_friend(call: types.CallbackQuery):
    await call.message.edit_caption(caption=f"🫂 Всего рефералов: {db.get_referral(call.from_user.id)}", reply_markup=keyboards.back2, parse_mode="HTML")


#Список моих друзей
@dp.callback_query(F.data.startswith('balance_friends'))
async def b_friend(call: types.CallbackQuery):
    await call.message.edit_caption(caption=f"🤑 Всего заработано с рефералов: {db.get_friends_tasks(call.from_user.id)}₽",
                                    reply_markup=keyboards.back2, parse_mode="HTML")