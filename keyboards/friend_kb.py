from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

referal = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Получить реферальную ссылку", callback_data='referal')],
        [InlineKeyboardButton(text="Список моих друзей", callback_data='list_friends')],
        [InlineKeyboardButton(text="Мой баланс за друзей", callback_data='balance_friends')],
        [InlineKeyboardButton(text="Назад", callback_data='back')]
    ]
)