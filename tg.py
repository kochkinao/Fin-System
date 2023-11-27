from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
import asyncio, config, logging
from db import Database

logging.basicConfig(level=logging.INFO)

bot = Bot(config.token, disable_web_page_preview=True)
dp = Dispatcher()
db = Database('database.db')


async def main():
    from handlers import dp
    try:
        await bot(DeleteWebhook(drop_pending_updates=True))
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')