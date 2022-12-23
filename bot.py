import logging
from dataclasses import dataclass

from aiogram import Bot, Dispatcher, executor, types

import config
import inline_keyboard
import messages
from sqliter import SQLighter

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot)

class Town:
    coords = None


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.bot.send_message(message.from_user.id, "Добро пожаловать!")


@dp.message_handler(commands=['weather'])
async def show_weather(message: types.Message):
    await message.answer(text=messages.weather(message.from_user['id']),
                         reply_markup=inline_keyboard.WEATHER)


@dp.message_handler(commands=['loca'])
async def loca(message: types.Message):
    await message.reply("Отправьте вашу геолокацию",
                        reply_markup=inline_keyboard.markup_request)


@dp.callback_query_handler(text='weather')
async def process_callback_weather(callback_query: types.CallbackQuery):

    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.weather(),
        reply_markup=inline_keyboard.WEATHER
    )


@dp.message_handler(content_types=["location"])
async def loca(message: types.Message):
    Town.coords = message.location
    if not SQLighter('db.db').subscriber_exists(message.from_user['id']):
        SQLighter('db.db').add_locator(message.from_user['id'], message.location['latitude'], message.location['longitude'])
    else:
        SQLighter('db.db').update_subscription(message.from_user['id'], message.location['latitude'], message.location['longitude'])




# @dataclass(slots=True, frozen=True)
# class Coordinates:
#     latitude: float
#     longitude: float
#
#
# def get_coordinates(town) -> Coordinates:
#     return Coordinates(latitude=town["latitude"], longitude=town["longitude"])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
