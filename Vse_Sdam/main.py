from aiogram import F, Dispatcher, Bot, types
from aiogram.filters import Command, CommandStart

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State, default_state
from aiogram.filters import StateFilter 
from aiogram.types import Message,ReplyKeyboardRemove

import keyboards
import asyncio

bot = Bot('forgot to add .env :)')
dp = Dispatcher()

lessons = ['Алгебра', 'Геометрия', 'Биология', 'География', 'Физика', 'История']

class Form(StatesGroup):
    choose_class = State()
    choose_work_type = State()
    choose_lesson = State()
    choose_variant = State()

#---------------------------------------------------------------------------------------------------#

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        text=f'Привет {message.from_user.full_name}, с помощью этого бота вы можете:\n\n'
        '[🔍👀 Находить почти все ответы на все возможные проверочные работы в одном месте.]\n\n'
        '[📆💨 Ответы обновляются благодаря тг каналам и сообществам.]\n\n'
        '[💎💰 Платный контент почти отсутвует,как ни как эту ответы вы можете найти сами если постараетесь 😙.]\n\n'
        '[🗄🗂 Исходный код бота выложен по этой ссылке: ... ]\n\n'
        'Напишите /otveti и мы приступим.\n\n'
        'Для отмены действия напишите /cancel или просто "отмена".\n\n' 
    )

@dp.message(Command('otveti'))
async def start_cmd(message: Message, state: FSMContext):
    await state.set_state(Form.choose_class)
    await message.answer('Выберите класс:', reply_markup=keyboards.kb_classes)

@dp.message(Form.choose_class, F.text.in_(['7', '8']))
async def process_7_8_class(message: Message, state: FSMContext):
    await state.update_data(chosen_class=message.text)
    await state.set_state(Form.choose_work_type)
    await message.answer('Выберите тип работы:', reply_markup=keyboards.kb_works_vpr_only)

@dp.message(Form.choose_class, F.text.in_(['9']))
async def process_9_class(message: Message, state: FSMContext):
    await state.update_data(chosen_class=message.text)
    await state.set_state(Form.choose_work_type)
    await message.answer('Выберите тип работы:', reply_markup=keyboards.kb_works_oge_vpr)

@dp.message(Form.choose_class, F.text.in_(['10', '11']))
async def process_10_11_class(message: Message, state: FSMContext):
    await state.update_data(chosen_class=message.text)
    await state.set_state(Form.choose_work_type)
    await message.answer('Выберите тип работы:', reply_markup=keyboards.kb_works_ege_vpr)

@dp.message(Form.choose_work_type, F.text.in_(['ВПР', 'ОГЭ', 'ЕГЭ']))
async def process_work_type(message: Message, state: FSMContext):
    await state.update_data(work_type=message.text)
    await state.set_state(Form.choose_lesson)
    await message.answer('Выберите предмет:', reply_markup=keyboards.kb_lessons)

@dp.message(Form.choose_lesson, F.text.in_(lessons))
async def process_lesson(message: Message, state: FSMContext):
    await state.update_data(chosen_lesson=message.text)
    await state.set_state(Form.choose_variant)
    await message.answer('Выберите вариант заданий:', reply_markup=keyboards.kb_var)

@dp.message(Form.choose_variant, F.text.in_(['1 вариант', '2 вариант']))
async def process_variant(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(
        f"Вы выбрали:\n"
        f"Класс: {data.get('chosen_class', 'не указан')}\n"
        f"Тип работы: {data.get('work_type', 'не указан')}\n"
        f"Предмет: {data.get('chosen_lesson', 'не указан')}\n"
        f"Вариант: {message.text}\n\n"
        f"Ответы будут здесь...",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()

@dp.message(StateFilter(None),Command(commands=['cancel']))
@dp.message(default_state,F.text.lower() == 'отмена')
async def cancel_nostate(message:Message,state:FSMContext):
    await state.set_data({})
    await message.answer(text='Пока вы ничего не выбрали',reply_markup=ReplyKeyboardRemove())

@dp.message(Command(commands=['cancel']))
@dp.message(F.text.lower() == 'отмена')
async def cancel(message:Message,state:FSMContext):
    await state.clear()
    await message.answer(text='Действие отменено',reply_markup=ReplyKeyboardRemove())

@dp.message(Command('🎲'))
async def dice(message:Message):
    await message.answer('🎲')

#------------------------------------------------------------------------------------#

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
