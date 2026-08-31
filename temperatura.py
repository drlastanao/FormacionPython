import requests
import os


api_key = os.getenv('API_WEATHER')
ciudad= input("Introduzca el nombre de la ciudad para obtener la temperatura actual: ")
json = requests.get(f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={ciudad}&aqi=no').json()


print("La temperatura actual en ", ciudad, " es de", json['current']['temp_c'], "grados Celsius.")
print("El tiempo actual es", json['current']['condition']['text'], "y la humedad es del", json['current']['humidity'], "%.")
