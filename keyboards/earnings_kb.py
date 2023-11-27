from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

earnings = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Дебетовые карты", callback_data='debit')],
        [InlineKeyboardButton(text="Кредитные карты", callback_data='credit')],
        [InlineKeyboardButton(text="Назад", callback_data='back')]
    ]
)