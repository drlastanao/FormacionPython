import requests


json = requests.get('http://api.open-notify.org/astros.json').json()

print("Estas son las personas que están en el espacio actualmente:")
for persona in json['people']:
    print(persona['name'], "en la nave", persona['craft'])
