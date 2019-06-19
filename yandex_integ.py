import requests
import os

class Yandex():
    _w_condition={
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
        'overcast-and-light-snow':'небольшой снег',
        'cloudy-and-snow': 'снег'
    }

    _w_part_name={
        'night': 'Ночь',
        'morning': 'Утро',
        'day': 'День',
        'evening': 'Вечер'
    }
    def __init__(self):
        weather_token=os.environ['YWEATHER']

    def GetWeather(self):
        r=requests.get('https://api.weather.yandex.ru/v1/informers', params={'lat':53.9000000,'lon':27.5666700,'lang':'ru_RU'}, headers={'X-Yandex-API-Key':'7b62cc40-c157-4bd0-b526-b5c23f8e0496'})
        if r.ok:
            r=r.json()
            now='**Сейчас** {}\nТемпература: {}\nСкорость ветра: {}'.format(self._w_condition[r['fact']['condition']],{r['fact']['temp']},{r['fact']['wind_speed']})
            forecast='**Прогноз на {}:**'.format(r['forecast']['date'])
            for p in r['forecast']['parts']:
                forecast+='\n\n_{}_:\n{}\nТемпература: {}\nСкорость ветра {}'.format(self._w_part_name[p['part_name']], self._w_condition[p['condition']], p['temp_avg'], p['wind_speed'])
            ans='Подробный прогноз:<{}>\n-----------------\n{}\n-----------------\n{}'.format(r['info']['url'], now, forecast)
        else:
            ans='Произошла ошибка!'
        return ans
