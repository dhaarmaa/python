import os

option = 1
userOne = None
userTwo = None
userThree= None
passwordOne = None
passwordTwo = None
passwordThree = None
while option!= 3:
    try:
        os.system('cls')
        print("**********************************************************")
        print("         *               MENU                *            ")
        print("**********************************************************")

        print ("\t1 - Iniciar Sesion")
        print ("\t2 - Registrar Usuario")
        print ("\t3 - Salir")
        option =int(input("ingrese opcion: "))
        if option == 1:
            #answer = "s"
            print("==iniciar sesion==")
            #while answer == "s":
            user = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            if user == userOne  and password == passwordOne:
                print("holi")
            else:
                print("este usuario no existe...")
                #answer = input("DEsea volver al menu principal : s/n").lower()

        elif option == 2:
            print("Registrar a usuario")
            #agregar codigo
        elif option== 3:
            print("fin del programa")
        else:
            print("opcion invalida")
        pausa = input("Presione Enter para volver al menu principal...")
    except:
        print("Ha ocurrido un error al ingresar...")

        pausa = input("Presione Enter para continuar...")