from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

API_TOKEN = "000"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
keyboard.add(button_calculate, button_info)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):

    await message.answer("Привет! Я помогу рассчитать норму калорий. Нажмите 'Рассчитать', чтобы начать!",
                         reply_markup=keyboard)

@dp.message_handler(text='Рассчитать')
async def set_age(message: types.Message):

    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):

    await state.update_data(age=message.text)
    await message.answer("Введите свой рост (в см):")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):

    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес (в кг):")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):

    await state.update_data(weight=message.text)

    data = await state.get_data()

    try:
        age = int(data['age'])
        growth = int(data['growth'])
        weight = int(data['weight'])

        calories = 10 * weight + 6.25 * growth - 5 * age + 5

        await message.answer(f"Ваша норма калорий: {calories:.2f} ккал/день.")
    except ValueError:
        await message.answer("Ошибка ввода данных. Пожалуйста, начните заново и введите корректные числа.")

    await state.finish()

@dp.message_handler(text='Информация')
async def information_handler(message: types.Message):

    await message.answer("Этот бот помогает рассчитать вашу норму калорий по введенным параметрам. Нажмите 'Рассчитать', чтобы начать.")

@dp.message_handler()
async def unknown_message(message: types.Message):

    await message.answer("Неизвестная команда. Используйте кнопки 'Рассчитать' или 'Информация'.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

