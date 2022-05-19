from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData




keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Базовый'),
            KeyboardButton(text='Голд')
        ],
        [
            KeyboardButton(text='Премиум')
        ]
    ],
    resize_keyboard=True
)

cb = CallbackData('buy','id', 'name', 'price' )

keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Base', callback_data='buy:0:base:1000'),
            InlineKeyboardButton(text='Gold', callback_data='buy:1:gold:2000'),
        ],[
            InlineKeyboardButton(text='Premium', callback_data='buy:2:premium:5000'),
            ]
    ],
    resize_keyboard=True

)