import handers, middlewares, filters
from loader import dp, db
from aiogram import executor



async def on_startup(dispatcher):
    await db.create_table()

async def on_shutdown(dispatcher):
    await db.conn.close()







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_shutdown=on_shutdown, on_startup=on_startup)