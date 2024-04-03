from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from main.config import TOKEN
from utils.database import Database


bot = Bot(token = "TOKEN")
storage = MemoryStorage()
db = Dispatcher(bot, storage=storage)
dp = Database()