import requests
import os


class Yandex():
    _w_condition = {
        'clear': 'ясно',
        'partly-cloudy': 'малооблачно',
        'cloudy': 'облачно с проянениями',
        'overcast': 'пасмурно',
        'partly-cloudy-and-light-rain': 'небольшой дождь',
        'partly-cloudy-and-rain': 'дождь',
        'overcast-and-rain': 'сильный дождь',
        'overcast-thunderstorms-with-rain': 'сильный дождь, гроза',
        'cloudy-and-light-rain': 'небольшой дождь',
        'overcast-and-light-rain': 'небольшой дождь',
        'cloudy-and-rain': 'дождь',
        'overcast-and-wet-snow': 'дождь со снегом',
        'partly-cloudy-and-light-snow': 'небольшой снег',
        'partly-cloudy-and-snow': 'снег',
        'overcast-and-snow': 'снегопад',
        'cloudy-and-light-snow': 'небольшой снег',
        'overcast-and-light-snow': 'небольшой снег',
        'cloudy-and-snow': 'снег'}

    _w_part_name = {
        'night': 'Ночь',
        'morning': 'Утро',
        'day': 'День',
        'evening': 'Вечер'}

    def __init__(self):
        self.weather_token = os.environ['YWEATHER']

    def GetWeather(self):
        r = requests.get('https://api.weather.yandex.ru/v1/informers',
                         params={'lat': 53.9000000, 'lon': 27.5666700, 'lang': 'ru_RU'},
                         headers={'X-Yandex-API-Key': self.weather_token})
        if r.ok:
            r = r.json()
            now = f'**Сейчас**\n{self._w_condition[r["fact"]["condition"]]}\nТемпература: {r["fact"]["temp"]} \u2103 \nСкорость ветра: {r["fact"]["wind_speed"]} м/c'
            forecast = f'**Прогноз на {r["forecast"]["date"]}:**'
            for p in r['forecast']['parts']:
                forecast += f'\n\n_**{self._w_part_name[p["part_name"]]}**_:\n{self._w_condition[p["condition"]]}\nТемпература: {p["temp_avg"]} \u2103 \nСкорость ветра {p["wind_speed"]} м/с'
            ans = f'Подробный прогноз:<{r["info"]["url"]}>\n-----------------\n{now}\n-----------------\n{forecast}'
        else:
            ans = 'Произошла ошибка!'
        return ans
