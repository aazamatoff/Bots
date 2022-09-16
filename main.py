import logging
from aiogram import Bot, Dispatcher,executor,types
import wikipedia

token = '5726520398:AAEQ1o7EZP9h_08XBGZ5gk1zfpBFY8Qo_UU'
logging.basicConfig(level=logging.INFO)
wikipedia.set_lang('uz')


bot = Bot(token)
ab = Dispatcher(bot)


@ab.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Nima gap")


@ab.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply('help')


@ab.message_handler()
async def sendWiki(message: types.Message):
    try:
        s = wikipedia.summary(message.text)
        await message.answer(s)
    except:
        await message.answer('Mavjut emas')

if __name__ == '__main__':
    executor.start_polling(ab,skip_updates=True)