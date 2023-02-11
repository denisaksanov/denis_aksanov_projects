#!venv/bin/pythonimport logging

# добавляем кнопку в массив с клавиаутуройgreet_kb.add(button_hi)
from aiogram import Bot, Dispatcher, executor, types
bot = Bot(token="5890375828:AAGnn54WQbFbYtI7ZLX0i_tMrBFSmafkBS4")
dp = Dispatcher(bot)
i = 1234567891234456789
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('Привет! 555')
button_2 = KeyboardButton('Привет1')
greet_kb = ReplyKeyboardMarkup()


greet_kb.add(button_hi)
greet_kb.add(button_2)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Тест', reply_markup=greet_kb)
@dp.message_handler()
async def cmd_text(message: types.Message):

    if message.text == "самая новая версия маенкрафта?":
        await  bot.send_message(message.from_user.id, "1.19.3", reply_markup=greet_kb)
    if message.text == "сколько лет учи.ру?":
        await  bot.send_message(message.from_user.id, "10 лет", reply_markup=greet_kb)
    #elif добавление новой команды    elif message.text == "hello":
        await  bot.send_message(message.from_user.id, "hi")
    elif message.text == "how_are_you?":
        await  bot.send_message(message.from_user.id, "i'm_fine!")
    elif message.text == "test1":
        await  bot.send_message(message.from_user.id, 'hi')
    elif message.text == "Умножить":



        global i
        i = i * 1234554354565675675456464678
        await bot.send_message(message.from_user.id, str(i))
    elif message.text == "Отнять":
        i = i - 2
        await bot.send_message(message.from_user.id, str(i))
    elif message.text == "Разделить":
        i = i / 2
        await bot.send_message(message.from_user.id, str(i))
    elif message.text == "4":
        i = i / (2+6)
        await bot.send_message(message.from_user.id, str(i))
    elif message.text == "3":
        i = i / (1000/10+40/4)
        await bot.send_message(message.from_user.id, str(i))
    elif message.text == "2":
        i = i / (1234567890-987654321+123456789952/3-22222*123)
        await bot.send_message(message.from_user.id, str(i))
    elif message.text == "разделить_сумму":
        i = i / (12*9999-11*10000)
        await bot.send_message(message.from_user.id, str(i))
    elif "прибавить" in message.text:
        i = i + 12134567899872123876338761287132123767
        await bot.send_message(message.from_user.id, str(i))
    # ЭТО САМАЯ ПОСЛЕДНЯЯ КОМАНДА ВСЕГДА    else:
        await  bot.send_message(message.from_user.id, "Не знаю , что на это ответить")

@dp.message_handler(commands="start")
async def with_hidden_link(message: types.Message):
    await bot.send_message(message.from_user.id,'текст')

if __name__ == "__main__":
    executor.start_polling(dp)
