from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

go_deb_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Начать 💵", callback_data='go_deb')],
        [InlineKeyboardButton(text="Главное меню", callback_data='main_menu')]
    ]
)

go_credit_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Начать 💵", callback_data='go_credit')],
        [InlineKeyboardButton(text="Главное меню", callback_data='main_menu')]
    ]
)