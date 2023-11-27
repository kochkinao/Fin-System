from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

personal_referal = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Пригласить друга 👨", callback_data='friend')],
        [InlineKeyboardButton(text="Назад", callback_data='back')]
    ]
)