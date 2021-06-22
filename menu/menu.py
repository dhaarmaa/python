import os
import time
option = 1
userOne = None
userTwo = None
userThree= None
passwordOne = None
passwordTwo = None
passwordThree = None
while option!= 3:
    try:
        
        print("**********************************************************")
        print("         *               MENU                *            ")
        print("**********************************************************")
        print ("\t1 - Iniciar Sesion")
        print ("\t2 - Registrar Usuario")
        print ("\t3 - Salir")

        option =int(input("ingrese opcion: "))
        os.system('cls')

        if option == 1:
            #answer = "s"
            print("==iniciar sesion==")
            #while answer == "s":
            user = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            if user == userOne  and password == passwordOne:
                print ("\t1 - Realizar llamada")
                print ("\t2 - Enviar correo electrónico")
                print ("\t3 - Cerrar")
                menu = int(input(" Ingrese una opción: "))
                if menu ==1:
                    print("Realizar llamada")
                    number = int(input("ingrese su numero con el dijito 9 al comienzo: "))
                    while number[0]!= 9 or len(number):
                        print("el telefono debe comenzar con 9 y contener 9 digitos ")
                        number(int(input("Ingrese nuevamente el numero")))
                                
                elif menu == 2:
                    found = True
                    print("Enviar correo")
                    email = input("ingrese correo: ")
                    for i in email:
                        if i == "@":
                            found = False
                            break
                    if found:
                        print("Debe ingresar un correo valido")
                    message = input("ingrese mensaje: ")
                    while len(message) ==0:
                        message = input("ingrese mensaje: ")
                    print("correo completo...")
                    user = ""
                    password =""
                    time.sleep(2)
                    print("SEsión cerrada")
                elif menu ==3:
                    print("FIN DEL PROGRAMA")
                    break

                else:
                    print("opción invalida")
            else:
                print("este usuario no existe...")
                #answer = input("DEsea volver al menu principal : s/n").lower()

        elif option == 2:
            print("Registrar a usuario")
            userOne = input("ingrese un nombre de usuario: ")
            passwordOne = input("ingrese una contraseña: ")
            answer = input("desea ingresar otro usuario? s/n").lower()
            if answer =="s":
                userTwo = input("ingrese un nombre de usuario: ")
                passwordTwo = input("ingrese una contraseña: ")
                answer = input("desea ingresar otro usuario? s/n").lower()
                if answer == "s":
                    userThree = input("ingrese un nombre de usuario: ")
                    passwordThree = input("ingrese una contraseña: ")

        elif option== 3:
            print("fin del programa")
            break
        else:
            print("opcion invalida")
        

        pause = input("Presione Enter para volver al menu principal...")
    except:
        print("Ha ocurrido un error al ingresar...")

        pause = input("Presione Enter para continuar...")