"""3) A veces os encontraréis con JSON que tendréis que modificar. Para ello tenéis que decodificarlos, realizar las
modificaciones pertinentes y volver a codificarlo para dejarlo como JSON de nuevo. En el siguiente ejemplo os habéis
dado cuenta de que hay algunos errores:

A Superman le falta como poder "Volar"
En Batman, la edad es 35, no 350
En Batman, le sobra el poder de "Rayos en los ojos"
En Wonder Woman le falta el poder "Lazo de la verdad"
Después de corregir todo esto, transforma estos datos en un JSONString
"""
import json

superheroes = {
    "nombreEquipo": "Super Hero Squad",
    "ciudad": "Metro City",
    "formado": 2016,
    "baseSecreta": "Super Tower",
    "activo": "Si",
    "miembros": [
        {
            "nombre": "SuperMan",
            "edad": 29,
            "identidadSecreta": "Clart Kent",
            "poderes": [
                "Super fuerza",
                "Super velocidad",
                "Rayos en los ojos"
            ]
        },
        {
            "nombre": "Batman",
            "edad": 35,
            "identidadSecreta": "Bruce Wayne",
            "poderes": [
                "Detective",
                "Dinero"
            ]
        },
        {
            "nombre": "Wonder Woman",
            "edad": 900,
            "identidadSecreta": "Diana de Temiscira",
            "poderes": [
                "Super fuerza",
                "Super velocidad",
                "Lazo de la verdad"
            ]
        }
    ]
}

# Convertimos el diccionario a JSON String
json_string = json.dumps(superheroes)

# Mostramos el tipo y el contenido del JSON String resultante
print(type(json_string))
print(json_string)

"""4) En base al ejercicio anterior, modifica la estructura de super para lograr que miembros tenga dos ramas: 
"miembrosActivos" y "miembrosInactivos", 
donde cada una de estas ramas, almacenen los héroes que están en activo y los que no. En este caso, introduce a 
SuperMan y Wonder Woman en la lista de activos y a Batman en la de Inactivos.
"""
import json

superheroes = {
    "nombreEquipo": "Super Hero Squad",
    "ciudad": "Metro City",
    "formado": 2016,
    "baseSecreta": "Super Tower",
    "activo": "Si",
    "miembros": [
        {
            "nombre": "SuperMan",
            "edad": 29,
            "identidadSecreta": "Clart Kent",
            "poderes": [
                "Super fuerza",
                "Super velocidad",
                "Volar"
            ],
            "activo": "Si"
        },
        {
            "nombre": "Batman",
            "edad": 35,
            "identidadSecreta": "Bruce Wayne",
            "poderes": [
                "Detective",
                "Dinero"
            ],
            "activo": "No"
        },
        {
            "nombre": "Wonder Woman",
            "edad": 900,
            "identidadSecreta": "Diana de Temiscira",
            "poderes": [
                "Super fuerza",
                "Super velocidad",
                "Lazo de la verdad"
            ],
            "activo": "Si"
        }
    ]
}

miembrosActivos = []
miembrosInactivos = []

for miembro in superheroes['miembros']:
    if miembro['activo'] == 'Si':
        miembrosActivos.append(miembro)
    else:
        miembrosInactivos.append(miembro)

superheroes_modificado = {
    "nombreEquipo": superheroes["nombreEquipo"],
    "ciudad": superheroes["ciudad"],
    "formado": superheroes["formado"],
    "baseSecreta": superheroes["baseSecreta"],
    "activo": superheroes["activo"],
    "miembrosActivos": miembrosActivos,
    "miembrosInactivos": miembrosInactivos
}

json_string = json.dumps(superheroes_modificado, indent=4)

print(json_string)
