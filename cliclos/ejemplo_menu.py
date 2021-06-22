import os

opcion =1

while opcion!=3:

    try:

        os.system('cls')

        print("== Menú de Opciones==")

        print("1.Obtener suma\n2.Obtener Resta\n3.Salir")

        opcion=int(input("Ingrese opción:"))

        if opcion==1:

            valor1 = int(input("Ingrese primer valor:"))

            valor2 = int(input("Ingrese segundo valor:"))

            suma = valor1 + valor2

            print(f"La suma es:{suma}")

        elif opcion==2:

            valor1 = int(input("Ingrese primer valor:"))

            valor2 = int(input("Ingrese segundo valor:"))

            resta = valor1 - valor2

            print(f"La resta es:{resta}")

        elif opcion==3:

            print("Fin del programa...")

        pausa = input("Presione Enter para continuar...")

    except:

        print("Ha ocurrido un error al ingresar...")

        pausa = input("Presione Enter para continuar...")