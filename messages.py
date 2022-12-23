from bot import Town
from sqliter import SQLighter
from api_service import get_weather


def weather(user_id) -> str:
    res = SQLighter('db.db').take_pos(user_id)
    print(res)
    wthr = get_weather(res[0], res[1])
    return f''' В {wthr.location} Температура на улицe: {wthr.temperature}°C \n
    Ощущается, как: {wthr.temperature_feeling}°C  \n
    {wthr.wind_direction} ветер {wthr.wind_speed} м/c, {wthr.description}. \n
    Восход: {wthr.sunrise.strftime("%H:%M")} \n
    Закат: {wthr.sunset.strftime("%H:%M")}'''
