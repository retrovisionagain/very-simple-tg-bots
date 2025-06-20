import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from weather_api import get_weather

# Загрузка переменных окружения
load_dotenv()

# Инициализация бота
bot = Bot(token=os.getenv('TG_BOT_TOKEN'))
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    text = (
        "🌤 Привет! Я погодный бот.\n"
        "Просто напиши название города, и я покажу текущую погоду!\n"
        "Например: \"Москва\" или \"London\""
    )
    await message.answer(text)

# Обработчик текстовых сообщений
@dp.message()
async def weather_handler(message: types.Message):
    city = message.text.strip()
    
    if not city:
        await message.answer("Пожалуйста, укажите город")
        return
    
    # Показываем "печатает..."
    await bot.send_chat_action(message.chat.id, "typing")
    
    # Получаем данные о погоде
    weather = get_weather(city)
    await message.answer(weather)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



