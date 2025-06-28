from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio

API_TOKEN = '8135937185:AAFyG-Ly0oyzpRKjcO9xTkCmqqNLVO7R_Cs'
CHANNEL_LINK = 'https://t.me/larisa_ortman'

# Обработка /start
async def start_handler(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}!\n"
        f"Пожалуйста, подпишись на наш канал 👉 {CHANNEL_LINK}"
    )

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    dp.message.register(start_handler, CommandStart())

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
