
import logging

# добавляем кнопку в массив с клавиаутуройgreet_kb.add(button_hi)
from aiogram import Bot, Dispatcher, executor, types
import pymysql
bot = Bot(token="5885555076:AAE0hX7WkcANQB5uAejWuE5buA_NiSXvl5w")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
i = 1234567891234456789

@dp.message_handler(commands=['start'])
async def cmd_test1(message: types.Message):
    await message.answer("Test1")
@dp.message_handler(commands="getPos")
async def cmd_getPos(message: types.Message):
    await message.answer("1tw7e6rvf7weftves7fysd8f7dbyf8dryfg8re7vg8e7gferhu87gtyg8u64oh7i")

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('Привет')

@dp.message_handler(commands=['create'])
async def cmd_create_user(message: types.Message):
    con=pymysql.connect(host="185.231.153.103", user="study", password="study123", database="egor")
    with con:
        cur=con.cursor()
        cur.execute("SELECT VERSION()")
        version = cur.fetchone()
        await bot.send_message(message.from_user.id, str(version[0]))
@dp.message_handler(commands=['show_user'])
async def cmd_show_user(message: types.Message):
    con = pymysql.connect(host="185.231.153.103", user="study", password="study123", database="egor")
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        for row in rows:
           await bot.send_message(message.from_user.id, f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")
users = {1,1}
@dp.message_handler(commands=['insert'])
async def cmd_insert(message: types.Message):
    users.add(message.from_user.id)
    await bot.send_message(message.from_user.id, "/n".join(f"* {user_id}" for user_id in users))

if __name__ == "__main__":
    executor.start_polling(dp)