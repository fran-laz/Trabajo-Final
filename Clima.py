import requests # type: ignore
API_KEY = 'a06749bb0149695ba0b8e0787d029580'
ciudad = 'Cochabamba,BO'
url = f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es'
respuesta = requests.get(url)
datos = respuesta.json()

if respuesta.status_code == 200:
    temperatura = datos['main']['temp']
    descripcion = datos['weather'][0]['description']
    humedad = datos['main']['humidity']
    
    print(f"Clima en {ciudad}:")
    print(f"Temperatura: {temperatura}°C")
    print(f"Descripción: {descripcion}")
    print(f"Humedad: {humedad}%")
else:
    print("Error al obtener el clima")
