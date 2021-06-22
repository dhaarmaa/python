import os
os.system('cls')
lista = []
ejecuta = True
while ejecuta:
    nombre = input("Ingrese nombre:")
    lista.append(nombre)
    respuesta = input("¿Ingresa otro nombre s/n?").lower()
    while respuesta!="s" and respuesta!="n":
        respuesta = input("Respuesta incorrecta...¿Ingresa otro nombre s/n?").lower()
    if respuesta=="s":
         ejecuta=True
    else:
        ejecuta=False
os.system('cls')
encontrado = False
nombre_buscar = input("Ingrese nombre a buscar:")
for indice in range(len(lista)):
    if lista[indice]==nombre_buscar:
        encontrado = True
        ubicacion = indice
        break
if encontrado:
    print(f"El nombre {nombre_buscar} se encontro en el indice: {ubicacion}")
else:
    print(f"Nombre no encontrado")