from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Заработок 💰", callback_data='earnings')],
        [InlineKeyboardButton(text="Правила работы 📕", callback_data='rules')],
        [InlineKeyboardButton(text="Личный кабинет ℹ️", callback_data='personal')],
        [InlineKeyboardButton(text="Ответы на вопросы ❓", callback_data='answer_question')],
        [InlineKeyboardButton(text='Пригласить друга 👨', callback_data='friend')],
        [InlineKeyboardButton(text='Leader Board 📈', callback_data='leader_board')]

    ]
)

admin_start_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Заработок 💰", callback_data='earnings')],
        [InlineKeyboardButton(text="Правила работы 📕", callback_data='rules')],
        [InlineKeyboardButton(text="Личный кабинет ℹ️", callback_data='personal')],
        [InlineKeyboardButton(text="Ответы на вопросы ❓", callback_data='answer_question')],
        [InlineKeyboardButton(text='Пригласить друга 👨', callback_data='friend')],
        [InlineKeyboardButton(text='Leader Board 📈', callback_data='leader_board')],
        [InlineKeyboardButton(text='Админ панель 👾', callback_data='admin_panel')]
    ]
)