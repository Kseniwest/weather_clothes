import pyowm

owm = pyowm.OWM('fad3c79357435c636262961765050837',language = 'ru')

place = input('В каком городе\стране?: ')
observation = owm.weather_at_place(place)
w = observation.get_weather()
temp = w.get_temperature('celsius')['temp']
print('В городе '+ place + ' сейчас ' + w.get_detailed_status())
print('Температура сейчас в районе ' + str(temp))
place = input('Что хочешь одеть?: ')
if temp < 10:
    print('нууу не знаю!Лучше Что-то теплое!и не забудь шапку!')
if temp > 10:
    print('МММммм...знаешь что, для такой отличной погоды  Одевай платье!')