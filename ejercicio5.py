import os
os.system('cls')

#se ingresa el numero de día de la semana, luego mostrar en palabra. Ejemplo se ingresa 5 mostrara el viernes. De ingresar un numero distinto entre el 1 y 7 arrojar un mensaje de error 

day = int(input("ingrese un numero del 1 al 7: "))

if day ==1:
    print("lunes")
elif day ==2:
    print("martes")
elif day==3:
    print("miércoles")
elif day==4:
    print("jueves")
elif day==5:
    print("viernes")
elif day==6:
    print("sabado")
elif day == 7:
    print("domingo")
else:
    print("por favor ingrese un numero entre el 1 y el 7")