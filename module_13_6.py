from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


API_TOKEN = "7919928556:AAF2H4yzW5Zkxon3hLlOnHekOdrCYMXNGa0"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
main_keyboard.add(button_calculate, button_info)

inline_keyboard = InlineKeyboardMarkup(row_width=1)
button_inline_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_inline_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_inline_calories, button_inline_formulas)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Я помогу рассчитать норму калорий.\nВыберите опцию ниже:",
                         reply_markup=main_keyboard)

@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    formula_message = (
        "Формула Миффлина-Сан Жеора:\n"
        "Для мужчин: 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) + 5\n"
        "Для женщин: 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) - 161"
    )
    await call.message.answer(formula_message)
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):

    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()

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
    await message.answer("Этот бот помогает рассчитать вашу норму калорий по введённым параметрам.\n"
                         "Нажмите 'Рассчитать', чтобы начать!")

@dp.message_handler()
async def unknown_command(message: types.Message):
    await message.answer("Неизвестная команда. Используйте кнопки меню.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

