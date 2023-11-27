from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

get_link_deb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Получить ссылки", callback_data='link_deb')],
        [InlineKeyboardButton(text="Главное меню", callback_data='main_menu')]
    ]
)

get_link_credit = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Получить ссылки", callback_data='link_credit')],
        [InlineKeyboardButton(text="Главное меню", callback_data='main_menu')]
    ]
)