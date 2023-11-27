from aiogram import types, F
from aiogram.filters import CommandStart

import config
from config import photo
import keyboards
from tg import dp, bot, db



@dp.message(CommandStart())
async def start(msg: types.Message):
    if not db.user_exists(msg.from_user.id):  # Если пользователь не зарегистрирован
        message = msg.text
        referrer_id = str(message[7:])
        if str(referrer_id) != "":  # Если он зашел по реферальной ссылке
            if str(referrer_id) != str(msg.from_user.id):  # Если реферальная ссылка не его
                db.add_user(msg.from_user.id, referrer_id)
                try:
                    await bot.send_message(referrer_id, '👾 По твоей ссылке зарегистрировался новый пользователь!')
                except:
                    pass
            else:
                db.add_user(msg.from_user.id)
        else:
            db.add_user(msg.from_user.id)
    try:
        db.set_user_name(msg.from_user.full_name, msg.from_user.id)
    except:
        pass
    if msg.from_user.id in config.ADMIN:
        await bot.send_photo(msg.from_user.id, photo, caption=f"Привет, {msg.from_user.full_name}👋\n"
                                                              f"Я - бот помощник по заработку денюжки на финансовых офферах и не только! 😊\n\n"
                                                              f"Следуй всем рекомендациям и получай выплаты!\n\n"
                                                              f"На данный момент выплаты производятся <b>только на карты Сбербанка!</b>",
                             parse_mode="HTML", reply_markup=keyboards.admin_start_menu)
    else:
        await bot.send_photo(msg.from_user.id, photo, caption=f"Привет, {msg.from_user.full_name}👋\n"
                                                              f"Я - бот помощник по заработку денюжки на финансовых офферах и не только! 😊\n\n"
                                                              f"Следуй всем рекомендациям и получай выплаты!\n\n"
                                                              f"На данный момент выплаты производятся <b>только на карты Сбербанка!</b>",
                             parse_mode="HTML", reply_markup=keyboards.start_menu)


# Заработок 💰
@dp.callback_query(F.data.startswith('earnings'))
async def earnings_call(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=keyboards.earnings)


# Правила работы 📕
@dp.callback_query(F.data.startswith('rules'))
async def earnings_call(call: types.CallbackQuery):
    await call.message.edit_caption(caption="❗<b>ПРАВИЛА БОТА</b>❗️\n\n"
                                            "- <b>ЗАПРЕЩЕНО</b> Спамить в лс администраторам с просьбой выплатить деньги, ждите, всех обработают в порядке очереди\n\n"
                                            "- Любая попытка обмана администраторов, или же, обычных пользователей приведет к мгновенной блокировке и изгнанию из наших сервисов, чатов\n\n"
                                            "- В некоторых случаях нам нужны будут от вас ваши личные данные, мы обязуемся, что они будут использованы только в тех местах и компаниях, о которых мы вам расскажем и вы будете в курсе\n\n"
                                            "Правила обновляются по мере развития проекта и компании. Контакт для связи - @prosto_gleb2\n\n"
                                            "Режим работы : С 11:00 по МСК до 18:00 по МСК",
                                    reply_markup=keyboards.back,
                                    parse_mode="HTML")


# Поддержка 🆘
@dp.callback_query(F.data.startswith('personal'))
async def earnings_call(call: types.CallbackQuery):
    if call.from_user.username is not None:
        username = f"@{call.from_user.username}"
    else:
        username = call.from_user.full_name
    await call.message.edit_caption(
        caption=f"👤 <b>Пользователь:</b> {username}\n🆔 <b>ID: </b>{call.from_user.id}\n🫂 Всего рефералов: {db.get_referral(call.from_user.id)}\n📈 Выполнено задач: {db.get_task_user(call.from_user.id)}",
        reply_markup=keyboards.personal_referal, parse_mode="HTML")


# Ответы на вопросы ❓
@dp.callback_query(F.data.startswith('answer_question'))
async def earnings_call(call: types.CallbackQuery):
    await call.message.answer(
        f"{call.from_user.full_name}, ниже ты можешь посмотреть на часто задаваемые нам вопросы😉\n"
        "<b>1. Мне меньше 18 лет, я смогу заработать?</b>\n"
        "<i>- Нет, только 18+ могут оформить продукты в боте и получить выплату за них</i>\n\n"
        "<b>2. Выплата 1000р, а покупку нужно на 1000р сделать, в чем профит?</b>\n"
        "<i>- Трата по карте может быть совершена по вашим самым обычным тратам, которые вы и так потратите с карты, не советуем использовать сервисы чаевых</i>\n\n"
        "<b>3. Я все оформил, как заработать больше?</b>\n"
        "<i>- Напишите в поддержку нашего бота и вам подскажут больше информации</i>\n\n"
        "<b>4. У меня есть все эти карты, когда обновление офферов будет?</b>\n"
        "<i>- В ближайшее время, мы вас уведомим о появлении новых😏</i>\n\n"
        "<b>5. Я все скинул поддержке, когда будут выплаты?</b>\n"
        "<i>- Прочитайте правила этого бота, там описан процесс выплат со сроками. Если они нарушаются - пишите по контакту в разделе 'Правила'</i>\n\n"
        "<b>6. Мне не нравится ваш бот и ваши выплаты, я буду делать сам через пп</b>\n"
        "<i>- Мы не запрещаем вам работать самостоятельно. Наши выплаты зависят от пп и не всегда они боту придут. Но вам они придут гарантированно. За этот риск бот берет себе от 20 до 50 процентов в зависимости от оффера</i>\n\n"
        "<b>7. Вы обманываете людей! Да вы, да я...!</b>\n"
        "<i>- ...бан</i>\n\n"
        "Ну а теперь, ты сможешь ознакомиться поближе с каждым заданием и понять его суть, <b>жми</b> на интересующий тебя раздел ниже и запоминай😉",
        reply_markup=keyboards.back, parse_mode="HTML", disable_notification=True)


# Пригласить друга 👨
@dp.callback_query(F.data.startswith('friend'))
async def earnings_call(call: types.CallbackQuery):
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


@dp.callback_query(F.data.startswith('leader_board'))
async def earnings_call(call: types.CallbackQuery):
    user = list(db.get_all_task_user())
    for i in range(1, 10)
        print(i)
        task_num = sorted(user)[len(sorted(user))-i][0]
        id_num = sorted(user)[len(sorted(user))-i][1]
        name_num = sorted(user)[len(sorted(user))-i][1]
    print(sorted(user))