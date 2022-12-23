BOT_API_TOKEN = '5883070708:AAHIcmhvLJ2IAeFohKWIloXskBWspdnduqw'
WEATHER_API_KEY = 'c54622bb40599128cd3970375148e1df'

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + WEATHER_API_KEY + '&units=metric'
)
