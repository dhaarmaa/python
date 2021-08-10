from random import *
import os 
os.system('cls')
list =[]

def number():
    for i in range(5):
        alzNumber = randint(1, 10)
        list.append(alzNumber)
        print(f"-{i}")
    print("tenemos 5 numeros al azar entre el 1 y el 10")
       
        


def numberFound():
    ingFoundNum =  int(input("ingrese un numero: "))
    if ingFoundNum in list:
        print("El numero ingresado si esta en la lista")
    else:
        print("el numero ingresado no esta en la lista")
number()
numberFound()



