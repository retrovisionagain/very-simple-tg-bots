import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(city: str) -> str:
    api_key = os.getenv('WEATHER_TOKEN')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather = (
                f"🌡 Погода в {data['name']}:\n"
                f"• Температура: {data['main']['temp']}°C (ощущается как {data['main']['feels_like']}°C)\n"
                f"• Состояние: {data['weather'][0]['description'].capitalize()}\n"
                f"• Влажность: {data['main']['humidity']}%\n"
                f"• Ветер: {data['wind']['speed']} м/с"
            )
            return weather
        else:
            return f"🚫 Ошибка: {data['message']}"
            
    except Exception as e:
        return f"⚠️ Ошибка соединения: {str(e)}"