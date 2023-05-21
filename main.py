import config as cfg
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)
from db import Database
import functions as fc

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)
db = Database('database.db')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет')


@dp.message_handler()
async def mess(message: types.Message):
    answer_id = fc.recognize_questions(message.text, db.get_questions())
    await bot.send_message(message.from_user.id, db.get_answer(answer_id))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
