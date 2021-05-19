#Se ingresa un numero. Si este es mayor a 50 obtener el cubo, si es menor sacar el cuadraro. (elevado a 3 es el cubo y elevado a 2 es el cuadrado)
import os
os.system('cls')

num = int(input("ingrese unn numero: "))

if num>50:
    calculo =pow(num, 3)
    tipoCalculo = "cubo"
    
else:
    calculo = pow(num,2)
    tipoCalculo = "cuadrado"

print(f"el  valor de {num} al {tipoCalculo} es {calculo}")