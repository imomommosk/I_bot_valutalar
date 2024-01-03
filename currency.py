import logging


from aiogram import Bot, Dispatcher, executor, types

import valyuta

API_TOKEN = '6741505062:AAGJCMOZah-bKRULhxobjKJT9dxQQZOlEIo'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "help"])
async def welcome_bot(message: types.Message):
    await message.reply("Assalom alaykum.\nBotimizga xush kelibsiz!\nCreated by Imomaddin")
    await message.answer(f"Hozir {valyuta.sana} sana bilan dollar kursi {valyuta.kurs} so'mga teng.")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)