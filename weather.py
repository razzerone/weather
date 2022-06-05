import argparse
import json
import os
from datetime import datetime

import requests as requests

API_KEY = os.getenv('WEATHER_API_KEY')
LANGUAGE = 'ru-ru'


def get_weather_data(city_id: int, city_name: str, e=False) -> str:
    resp = requests.get(
        f'http://dataservice.accuweather.com/currentconditions/v1/{city_id}',
        params={
            'apikey': API_KEY,
            'language': LANGUAGE,
            'details': e
        }
    )

    resp_json = json.loads(resp.content)[0]

    if not e:
        return (
            f'В данный момент в городе {city_name} '
            f'{resp_json["WeatherText"].lower()}, '
            f'температура {resp_json["Temperature"]["Metric"]["Value"]}'
        )

    time = datetime.strptime(
        resp_json['LocalObservationDateTime'][:-6],
        '%Y-%m-%dT%H:%M:%S'
    )

    precipitation = resp_json["PrecipitationType"]["Localized"] \
        if resp_json["HasPrecipitation"] \
        else 'Без осадков'

    return (
        f'Город {city_name}, время {time.strftime("%H:%M:%S")}, '
        f'{resp_json["WeatherText"].lower()}\n{precipitation}\n\n'
        f'Температура: {resp_json["Temperature"]["Metric"]["Value"]}\n'
        f'Ощущается как: '
        f'{resp_json["RealFeelTemperature"]["Metric"]["Value"]}\n'
        f'Температура в тени: '
        f'{resp_json["RealFeelTemperatureShade"]["Metric"]["Value"]}\n\n'
        f'Ветер {resp_json["Wind"]["Direction"]["Localized"]}, '
        f'{resp_json["Wind"]["Speed"]["Metric"]["Value"]} км/ч\n'
        f'Порывы до {resp_json["WindGust"]["Speed"]["Metric"]["Value"]}\n\n'
        f'Относительная влажность: {resp_json["RelativeHumidity"]}%\n'
    )


def get_city_id(city: str) -> int:
    resp = requests.get(
        'http://dataservice.accuweather.com/locations/v1/cities/search',
        params={
            'apikey': API_KEY,
            'q': city,
            'language': LANGUAGE,
        }
    )

    return json.loads(resp.content)[0]['Key']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'city',
        type=str,
        help=(
            'Город, в котором хотите узнать погоду. \n'
            'При пустом аргументе используется последний введенный.'
        )
    )
    parser.add_argument(
        '-e', '--extended',
        action='store_true',
        help='Позволяет получить расширенную информацию о погоде.'
    )

    args = parser.parse_args()

    print(get_weather_data(get_city_id(args.city), args.city, e=args.extended))


if __name__ == '__main__':
    main()
