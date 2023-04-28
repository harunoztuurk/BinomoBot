import asyncio
import logging
import json

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from datetime import datetime, timedelta

from BinomoBot.telegram_bot.create_bot import bot
from BinomoBot.telegram_bot.utils.database import UsersDatabase

users = UsersDatabase()


async def welcome(message: types.Message):
    await bot.send_message(message.chat.id, 'hello!')
    if not users.if_user_exists(message.from_user.id):
        users.create_new_user(message.from_user.id)
        await send_every_10_minutes()


async def send_statistic(message: types.Message):
    await bot.send_photo()


async def send_every_10_minutes():
    while True:
        for user_id in users.get_all_users():
            await bot.send_message(user_id[0], 'work')
        await asyncio.sleep(3)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(welcome, commands=['start', 'help'])
