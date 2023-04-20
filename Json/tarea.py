"""
1) A continuación se muestra un JSON String
{"jefe_proyecto": {"Nombre": "Juan","Edad": 28,"Experiencia": ["Gestion","Finanzas","Bases de datos"],"Residencia":
"Madrid","HorasProyecto": 3500},"empleados":
[{"Nombre": "Elena","Edad": 26,"Experiencia":
["JavaScript","Python"],"Residencia": "Madrid","HorasProyecto": 500},
{"Nombre": "Luis","Edad": 31,"Experiencia":
["Django","Flask","Pyramid"],"Residencia": "Barcelona","HorasProyecto": 1100}]}

Si es necesario utiliza un visualizador de JSON para entenderlo.
El objetivo es crear un diccionario con todos los datos y estructuras internas necesarias para que sea igual que el JSON
String Vete creando estructuras más pequeñas hasta que llegues a formar el mismo JSON string que ves arriba
Una vez que lo tengas creado, vamos a operar con él
Almacena esta estructura (el diccionario) en una variable
Comprueba su tipo y muéstrala por pantalla
Crea dos variables: horas_empleados y horas_jefe
Extrae las horas del jefe e introducelas en su variable
Crea un bucle que recorra el número de empleados que se tienen en la estructura, y para cada empleado vete sumando sus
horas en su correspondiente variable
Suma todas las horas y muéstralas por pantalla"""

import json
data = {
    "jefe_proyecto": {
        "Nombre": "Juan",
        "Edad": 28,
        "Experiencia": ["Gestion", "Finanzas", "Bases de datos"],
        "Residencia": "Madrid",
        "HorasProyecto": 3500
    },
    "empleados": [
        {
            "Nombre": "Elena",
            "Edad": 26,
            "Experiencia": ["JavaScript", "Python"],
            "Residencia": "Madrid",
            "HorasProyecto": 500
        },
        {
            "Nombre": "Luis",
            "Edad": 31,
            "Experiencia": ["Django", "Flask", "Pyramid"],
            "Residencia": "Barcelona",
            "HorasProyecto": 1100
        }
    ]
}

print(type(data))  # <class 'dict'>

horas_jefe = data["jefe_proyecto"]["HorasProyecto"]
horas_empleados = 0

for empleado in data["empleados"]:
    horas_empleados += empleado["HorasProyecto"]

print("Horas totales:", horas_jefe + horas_empleados)  # Horas totales: 5100

"""
En el ejercicio anterior has trabajado con un diccionario que tu mismo/a creaste, conviértelo a un formato JSON String, 
muestra su tipo y los datos por pantalla
"""
json_data = json.dumps(data)
print(type(json_data))  # <class 'str'>
print(json_data)