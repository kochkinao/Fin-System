from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Кол-во пользователей", callback_data='statistics'), InlineKeyboardButton(text="Рассылка", callback_data='newsletter')],
        [InlineKeyboardButton(text="Добавить 1 задачу", callback_data='done_task'), InlineKeyboardButton(text="Убрать 1 задачу", callback_data='fail_task')],
        [InlineKeyboardButton(text="Назад", callback_data='back')]
    ]
)