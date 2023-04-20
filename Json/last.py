"""
5) En el siguiente código, accedemos a un JSON de forma remota, a partir de la respuesta, realizar lo siguiente:

Mostrar el tipo de dato que se ha recibido
Mostrar los datos recibidos
Mostrar el número de personas que se encuentran actualmente en el espacio
Realizar un bucle que recorra a todas esas personas y muestre nombre y nave en la que se encuentra.
"""
import requests

# API que nos comunica cuantas personas se encuentran actualmente en el espacio
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
# Mostrar el tipo de dato que se ha recibido
print(type(data))

# Mostrar los datos recibidos
print(data)

# Mostrar el número de personas que se encuentran actualmente en el espacio
print(f"Hay {data['number']} personas en el espacio.")

# Recorrer a todas las personas y mostrar nombre y nave en la que se encuentra
for person in data['people']:
    print(f"{person['name']} se encuentra en la nave {person['craft']}.")
