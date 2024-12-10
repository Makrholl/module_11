from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "000"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler()
async def all_messages(message: types.Message):
    print("Введите команду /start, чтобы начать общение.")
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == '__main__':
    # Запуск бота
    print("Bot is running...")
    executor.start_polling(dp, skip_updates=True)

