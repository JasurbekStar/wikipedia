import asyncio
import logging
import sys,os

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import wikipedia
wikipedia.set_lang("uz")
load_dotenv()
API = os.getenv("API")
dp = Dispatcher()


@dp.message(Command("start"))
async def command_start(message: Message) -> None:
    await message.answer(f"salom , {html.bold(message.from_user.full_name)}!")


@dp.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    await message.answer(f"sizga qanday yordam bera olaman")


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        msg=await message.answer("👀")
        await message.answer(f"{wikipedia.summary(message.text)}")
        await msg.delete()
    except:
        await message.answer("Topilmadi")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
