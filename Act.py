"""En est ejercicio deberás crear un programa que lea los datos de un fichero de texto, que transforme cada fila en un
diccionario y lo añada a una lista llamada personas. Luego recorre las personas de la lista y para cada una muestra
de forma amigable todos sus campos. Por ejemplo así:
(id=1) Carlos Pérez => 05/01/1989
El fichero de texto se denominará personas.txt y tendrá el siguiente contenido en texto plano (créalo previamente):

1;Carlos;Pérez;05/01/1989
2;Manuel;Heredia;26/12/1973
3;Rosa;Campos;12/06/1961
4;David;García;25/07/2006
Los campos del diccionario serán por orden: id, nombre, apellido y nacimiento.
"""

archivo=open("personas.txt")
lineas=archivo.readlines()
archivo.close()
personas=[]
for linea in lineas:
    campo = linea.replace("\n","").split(";")
    persona={"id":campo[0],"nombre":campo[1],"apellido":campo[2],"nacimiento":campo[3]}
    personas.append(persona)
for persona in personas:
    print(f"id={persona['id']} {persona['nombre']} {persona['apellido']} {persona['nacimiento']}")

print("hola")