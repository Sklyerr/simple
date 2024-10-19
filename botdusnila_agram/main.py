import asyncio
import logging

from aiogram import Bot, Dispatcher

from handlers import router
from config import config


bot = Bot(token = config.token.get_secret_value())
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level = logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")