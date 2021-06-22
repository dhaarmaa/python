#●●	Ingrese un número entero y muestre su tabla de multiplicar.
import os
os.system('cls')

num = int(input("ingrese un numero entero: "))
#for=iteración
#i es la variable del for en este caso el i pseran los numeors del 1 al 12
#la funcion range muestra los numeros dependiendo del rango que le demos
for i in range(1, 13):
    print(f"{i} x {num} = {i*num}")