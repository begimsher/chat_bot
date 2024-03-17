import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards import kb1, kb2

#Включаем логгирование
logging.basicConfig(level=logging.INFO)

#Создаём объект бота
bot = Bot(token=config.token)

#Диспетчер
dp = Dispatcher()


#Хэндлер на команду /start
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    print(message.chat)
    await message.answer(f'Привет, {name}', reply_markup=kb1)


#Хэндлер на команду /stop
@dp.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    print(message.chat)
    await message.answer(f'Пока, {name}')


#Хэндлер на команду /fox
@dp.message(Command('fox'))
@dp.message(Command('лиса'))
@dp.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    print(message.chat)
    await message.answer(f'Держи лису, {name}')


#Хэндлер на сообщения
@dp.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет-привет, {name}')
    elif 'пока' in msg_user:
        await message.answer(f'Пока-пока, {name}')
    elif 'ты кто' in msg_user:
            await message.answer_dice(emoji="🤖")
    elif 'лиса' in msg_user:
        await message.answer(f'Смотри что у меня есть, {name}', reply_markup=kb2)
    else:
        await message.answer(f'Я не знаю такого слова')

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())