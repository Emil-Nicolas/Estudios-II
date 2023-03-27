"""Tenemos 9 columnas, las 8 primeras contienen datos numéricos con los cuales podemos trabajar, crea una lista para
cada una de estas columnas (mpg, cylinders, etc.). No es necesario crear lista para name
Recorre los datos del csv.csv adecuadamente y almacena los datos de cada columna en cada una de las listas que has creado
anteriormente. Comprobar que se haya guardado en las listas la información correspondiente (con prints)"""

import csv

with open('csv.csv', 'r', newline='') as my_csv:
    reader = csv.reader(my_csv, delimiter=',')
    lista = []
    for linea in reader:
        for columna in range(len(linea)):
            if columna >= len(lista):
                lista.append([])
            lista[columna].append(linea[columna])

    for col in lista:
        print(col)
