import sys

sys.dont_write_bytecode = True

import asyncio

from handlers.handlers import router
from config import bot, dp
from database.database import initialize_database

async def main():
    await initialize_database()

    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())