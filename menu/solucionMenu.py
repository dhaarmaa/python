import os

import time

usuario1=None

clave1=None

usuario2=None

clave2=None

usuario3=None

clave3=None

usuario=None

clave=None

logeado=False

opcion=1

while opcion!=3:

    os.system('cls')

    print("== Menú Principal ==")

    print("1.Iniciar Sesión\n2.Registrar Usuario\n3.Salir")

    opcion=int(input("Ingrese opción:"))

    if opcion==1:

        print("-- Iniciar Sesión --")

        # código para login

        usuario=input("Ingrese Usuario:")

        clave=input("Ingrese clave:")

        if usuario==usuario1 and clave==clave1:

            accede= True

        elif usuario==usuario2 and clave==clave2:

            accede= True

        elif usuario==usuario3 and clave==clave3:

            accede= True

        else:

            accede= False

        #si accede es verdadero haga

        if accede:

            print(f"Bienvenid@ {usuario}...")    

            opcion2=1

            while opcion2!=3:

                print("= Submenu =")

                print("1.Realizar llamada\n2.Enviar Correo\n3.Cerrar sesión")

                opcion2=int(input("Ingrese opción:"))

                if opcion2==1:

                    print("- Realizar llamada -")

                    telefono=input("Ingrese teléfono:")

                    while telefono[0]!="9" or len(telefono)!=9:

                        print("teléfono debe comenzar con 9 y tener 9 caracteres...")

                        telefono=input("Ingrese nuevamente teléfono:")

                elif opcion2==2:                    

                    encontro = True

                    while encontro:

                        print("- Enviar un correo -")

                        correo = input("Ingrese correo:")

                        for caracter in correo:

                            if caracter=="@":

                                encontro=False

                                break  #break abandona el ciclo for

                        if encontro:

                            print("*Debe ingresar un correo correcto...")

                    mensaje=input("Ingrese mensaje")

                    while len(mensaje)==0:

                        mensaje=input("Debe Ingresar un mensaje:")

                    print("Mensaje correctamente ingresado...")

                    print("Correo completo...")

                elif opcion2==3:

                    #cerrar sesión es limpiar las variables usuario y clave luego volver al menú principal

                    print("Cerrando sesión...")

                    usuario1=None

                    clave1=None

                    usuario2=None

                    clave2=None

                    usuario3=None

                    clave3=None

                    logeado=True #si cerro sesión cambió a True

                    time.sleep(2) #pausa automática de 2 segundos  

                    print("Sesión cerrada...")                  

                elif opcion<1 or opcion>3:

                    print("Opción incorrecta...")

                pausa= input("Presione Enter para continuar.