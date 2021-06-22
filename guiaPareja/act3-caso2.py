#Crear una salida por pantalla con la siguiente información:
#i. ¿Cuál de los siguientes animales vive en el agua?
#1. Perro
#2. Cocodrilo
#3. Conejo
#4. Tiburón
#ii. Si la respuesta es Cocodrilo, asignar +0.5 a puntaje, si la respuesta es Tiburón asignar +1.0 a puntaje, del cualquier otro caso, no asignar valor, finalmente crear una salida por pantalla para mostrar el puntaje obtenido.

import os 
os.system('cls')

print("¿Cuál de los siguientes animales vive en el agua?")
print(" 1)Perro \n 2)Cocodrilo \n 3)Conejo \n 4)Tiburon")
answer = input("ingrese el numero correcto: ")

if  answer == "2":
    score = 0.5
elif answer == "4":
    score = 0.1
else:
    score = 0

print(f"su puntaje obtenido es {score}")

