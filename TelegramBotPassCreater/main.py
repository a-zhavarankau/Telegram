from tg_bot_config import tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message):
    await message.answer("Hello! Write a length of the password, but no more 20")


@dp.message_handler(commands=["info"])
async def start_command(message):
    await message.answer("Author: Aliaksandr Zhavarankau")


@dp.message_handler()
async def get_password(message: types.Message):
    try:
        passlength = int(message.text)
        if passlength > 20 or passlength <= 0:
            await message.reply("Incorrect password length")
        else:
            a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            b = "abcdefghijklmnopqrstuvwxyz"
            c = "0123456789"
            d = "!@#$%^&*()_+-=,.?\|`~[]{}"
            all = a + b + c + d
            password = "".join(random.sample(all, passlength ))
            await message.answer(f"Your password: {password}")
    except ValueError as e:
        print(f"[ERROR MSG]", *e.args)
        await message.reply("Enter a number from 1 to 20")


if __name__ == "__main__":
    executor.start_polling(dp)


