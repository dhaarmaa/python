import os

respuesta =  's'
while respuesta == 's':
    os.system('cls')
    numero = int(input("ingrese numero de la tabla : "))
    contador =0
    while contador <=10:
        resultado = contador * numero 
        print(f"{numero} * {contador} = {resultado}")
        contador +=1
    respuesta = input ("desea volver a repetir el profgrama s/n: ").lower()
print("fin del programa")