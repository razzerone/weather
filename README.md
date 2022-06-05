# weather

## О приложении

Это приложение предназначено для получения информации о погоде из коммандной строки. 
Приложение использует библиотеку "requests" и [AccuWeather API](https://developer.accuweather.com/).

Вы можете узнать как краткую информацию о погоде в вашем городе, так и подробную, 
включающую информацию об осадках, относительной влажности и т.п

## Начало работы

Зарегистрируйтесь на сайте [AccuWeather API](https://developer.accuweather.com/) и получите собственный API ключ.
Поместите его в переменную среды _API_KEY_ или внутрь файла _weather.py_ в переменную ```API_KEY``` в 9-ой строкею

*Важно! Для работы приложения необходим _python_ версии 3.6 и выше.*

Для получения справки введите в консоли 
```python3 weather.py --help```

Для получения краткой информации введите
```python3 weather.py название_вашего_города```

Для получения полной информации введите
```python3 weather.py название_вашего_города -e```
