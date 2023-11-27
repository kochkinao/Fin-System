from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

pristupit_deb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Приступить", callback_data='pristupit_deb')],
        [InlineKeyboardButton(text="Главное меню", callback_data='main_menu')]
    ]
)

pristupit_credit = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Приступить", callback_data='pristupit_credit')],
        [InlineKeyboardButton(text="Главное меню", callback_data='main_menu')]
    ]
)