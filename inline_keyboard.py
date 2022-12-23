from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

BTN_WEATHER = InlineKeyboardButton('Weather', callback_data='weather')


markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свою локацию ️', request_location=True)
)
markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)


WEATHER = InlineKeyboardMarkup()

