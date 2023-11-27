from aiogram.fsm.state import State, StatesGroup


class UserState(StatesGroup):
    newsletter_wait_msg = State()
    done_task_wait_id = State()
    fail_task_wait_id = State()