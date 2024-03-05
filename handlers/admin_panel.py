from aiogram import types, F
import keyboards
from tg import dp, db, bot
from state import UserState
from aiogram.fsm.context import FSMContext


@dp.callback_query(F.data.startswith('admin_panel'))
async def admin_panel_func(call: types.CallbackQuery):
    await call.message.edit_caption(
        caption="Приветствую, Босс 🧐\n"
                "<b>Немного описания для того, чтобы ты не забыл:</b>\n\n"
                "<b>Кол-во пользователей</b> - вывод количества всех пользователей\n\n"
                "<b>Рассылка</b> - отправка всем пользователям твоего <b>текстового сообщения</b>\n"
                "<i>Можно отправить только текст. Видео, документы, кружки и т.п - <b>НЕТ</b></i>\n\n"
                "<b>Добавить/Убрать 1 задачу</b> - по факту выполнения задачи ты нажмешь эту кнопку и человеку добавится/уберется 1 выполненная задача\n"
                "<i>Нужна больше для работы с рефералами</i>\n\n", reply_markup=keyboards.admin_panel, parse_mode="HTML")


#Статистика
@dp.callback_query(F.data.startswith('statistics'))
async def statistics_func(call: types.CallbackQuery):
    await call.message.answer(f"Всего пользователей: <b>{db.all_users()}</b>", parse_mode="HTML")


#Рассылка
@dp.callback_query(F.data.startswith('newsletter'))
async def newsletter_text(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Отправь сообщение, которое необходимо отправить👇")
    await state.set_state(UserState.newsletter_wait_msg)


@dp.message(UserState.newsletter_wait_msg)
async def newsletter_func(msg: types.Message, state: FSMContext):
    users = db.get_user()
    fail = 0
    for row in users:
        try:
            await bot.send_message(row[0], msg.text)
        except:
            fail += 1
    await msg.answer("Рассылка отправлена\n"
                     f"Не доставлено из-за блокировки бота: {fail}")
    await state.clear()


#Добавить 1 задачу
@dp.callback_query(F.data.startswith('done_task'))
async def done_task(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Отправь ID пользователя👇")
    await state.set_state(UserState.done_task_wait_id)


@dp.message(UserState.done_task_wait_id)
async def newsletter_func(msg: types.Message, state: FSMContext):
    if msg.text.isdigit():
        db.add_task(int(msg.text))
        await msg.answer("Успешно")
        await state.clear()
    else:
        await msg.answer('Ты должен ввести число 😌')


#Убрать 1 задачу
@dp.callback_query(F.data.startswith('fail_task'))
async def done_task(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Отправь ID пользователя👇")
    await state.set_state(UserState.fail_task_wait_id)


@dp.message(UserState.fail_task_wait_id)
async def newsletter_func(msg: types.Message, state: FSMContext):
    if msg.text.isdigit():
        db.delete_task(int(msg.text))
        await msg.answer("Успешно")
        await state.clear()
    else:
        await msg.answer('Ты должен ввести число 😌')


#Изменить Дебетовые карты
@dp.callback_query(F.data.startswith('edit deb'))
async def done_task(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Отправь ID пользователя👇")
    await state.set_state(UserState.fail_task_wait_id)