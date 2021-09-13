import time
import requests
import json
class ValueToCor(Exception):
    """Вызывается, когда координаты не находятся"""
    pass
class ValueYesorNo(ValueToCor):
    """Вызывается, когда не введени да или нет"""
    pass
lat=56.13
lon=47.25
try:
 print('Введите широту города: (широта чеб- 56.13)')
 #lat=str(input())
 if int(lat) < -90 or int(lat)>90:
            raise ValueToCor
            
 print('Введите долготу города: (долгота чеб- 47.25)')
 #lon=str(input())
 if int(lon) < -90 or int(lon)>90 :
            raise ValueToCor
except ValueToCor:
  print('Введите корректные координаты')

api_url = "http://api.openweathermap.org/data/2.5/onecall"
params = {
    'lat' : lat,
    'lon': lon,
    'lang' : 'ru',
    'appid' : '11c0d3dc6093f7442898ee49d2430d20',
    'units' : 'metric',
    'exclude':'alerts'
 }

res = requests.get(api_url, params = params)
data = res.json()

print('Сохранить данные в текстовый документ? (да/нет)')

try:
  a=str(input())
  if a !='да' and a!='нет':
     raise ValueYesorNo
except ValueYesorNo:
     print("Введите да или нет!")
if a == 'да':
    f = open('city.txt', 'w')
    f.write('Зона: ' + data['timezone']+'\n'+ 
         'Дата, время: '+time.ctime(data['minutely'][-1]['dt'])+'\n'+
         'Координаты: '+' широта: '+str(data['lat'])+','+' долгота: '+str(data['lon'])+'\n'+
         'Температура: '+str(data['current']['temp'])+'\n'+
         'Скорость ветра: '+ str(data['current']['wind_speed'])+'м/с'+'\n'+
         'Описание погоды: '+data['current']['weather'][0]['description'])
    print('данные успешно сохранены, желаете продолжить? (да/нет)')
    a1=str(input())
    try:
     if a1!='да' and a1!='нет':
       raise ValueYesorNo
    except ValueYesorNo:
       print("Введите да или нет!")
    if a1 == 'нет':
      exit(0)

if a == 'нет':
    print('данные не сохранены, желаете продолжить?(да/нет)')
    a1=str(input())
    try:
     if a1!='да' and a1!='нет':
       raise ValueYesorNo
    except ValueYesorNo:
       print("Введите да или нет!")
    if a1 == 'нет':
      exit(0)


  

#print(data['timezone'])
#a=time.ctime(data['minutely'][-1]['dt'])
#print(data['lat'], data['lon'])
#print(data['current']['temp'])
#print(data['current']['wind_speed'])
#print(data['current']['weather'][0]['description'])
#for i in data['current']:
 #print(i ,' : ',data['current'][i])
#for i in data:
 #print(i ,' : ',data[i])
