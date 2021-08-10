import os
os.system('cls ')
listaPasillos  = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, "||", 25, 27, 29, 31, 33, 35, 37, 39]
listaVentana = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, "||", 26, 28, 30, 32, 34, 36, 38, 40]
asientoComprado=[]

def asientosDisponibles():
    for x in listaPasillos: 
        Verificacion = True
        for compra in asientoComprado:
            if x == compra[0]:
                print("X", end=" ")
                Verificacion = False
        if Verificacion:
            print(x, end=" ")
    print()
    for i in listaVentana:
        Verificacion = True
        for compra in asientoComprado:
            if i == compra[0]:
                print("X", end=" ")
                Verificacion = False
        if Verificacion:
            print(i, end=" ")
    print()

def CompraDeAsientos():
    compra = []
    cliente = []

    verificacionDEAsientos =  False
    while not verificacionDEAsientos:
        asientos = int(input("ingrese el asiento que desee: "))
        error = False
        
        for x in asientoComprado:
            if asientos == x[0] or asientos <1 or asientos >40:
                print(f"EL asiento {asientos} no esta disponible o no existe ")
                verificacionDEAsientos =  False
                error = True
        if not error:
            verificacionDEAsientos = True
    if asientos <= 24 :
        print("Este asiento tiene un valor de $14.900")
    else:
        print("Este asiento tiene un valor de $24.000")

    Confirmacion = input("Desea confirmar la compra: s/n").lower()
    if Confirmacion =="s":
        rut= input("ingrese su rut sin puntos ni guion: ") 
        while len(rut)<8 or len(rut)>9:
            print("rut invalido")  
            rut= input("ingrese su rut sin puntos ni guion: ")
        cliente.append(rut) 
        nombre= input("Ingrese su nombre: ")
        cliente.append(nombre)
        caja = input("¿Tiene caja de compensación? en caso de que tenga se le aplicara un descuento de 15%. s/n ").lower()
        if asientos <= 24:
            total = 14900
        else:
            total = 24000
        if caja == "s":
            if asientos <= 24:
                total = 14900*0.85
            else:
                total = 24000*0.85
        print(f"El precio de su pasaje es {total}")       
        cliente.append(caja)
        compra.append(asientos)
        compra.append(cliente)
        asientoComprado.append(compra)

def  AnulacionDePasaje():
    verificacion =  True
    while True:
        numAsiento =  int(input("ingrese el numero del asiento: "))
        for i in asientoComprado:
            if numAsiento == i[0]:
                asientoComprado.remove(i)
                print("su pasaje ha sido eliminado con exito!")
                verificacion = False
                break
        if not verificacion:
            break
        print("No se encontro el asiento")
    
def modificacionDeDatos():
    
    Verificacion = True
    while Verificacion:
        VerificacionRut =  input("Ingrese su rut sin puntos ni guion: ")
        numAsiento =  int(input("ingrese el numero del asiento: "))
        for i in asientoComprado:
            if numAsiento == i[0] and VerificacionRut in i[1]:
                Verificacion =  False
                respuesta =  "s"
                while respuesta != "n":
                    print("\t 1.- Modificación de nombre")
                    print("\t 2.- Modificacion de caja")
                    opcion = int(input("ingrese su opcion: "))
                    if opcion ==1:
                        nombre = input("ingrese el nuevo nombre: ")
                        i[1][1]= nombre
                    elif opcion ==2:
                        caja = input("¿Posee caja de compensación? s/n: ")
                        i[1][2] = caja
                        if caja == "s":
                            if numAsiento <= 24:
                                total = 14900*0.85
                                print(f"El precio de su pasaje es {total}")
                            else:
                                total = 24000*0.85
                                print(f"El precio de su pasaje es {total}")
                        else:
                            if numAsiento <= 24:
                                total = 14900
                                print(f"El precio de su pasaje es {total}")
                            else:
                                total = 24000
                                print(f"El precio de su pasaje es {total}")
                    else:
                        print("numero invalido")
                    respuesta = input("Desea modificar otro dato: s/n")
        if Verificacion:
            print("datos incorrectos")
           
def menu():

    ejecutar = True
    while ejecutar:
        try:
            
            print("**********************************************************")
            print("         *               MENU                *            ")
            print("**********************************************************")
            print ("\t1 - Ver asientos disponibles")
            print ("\t2 - Comprar asiento")
            print ("\t3 - Anular viaje")
            print("\t4 - Modificar datos por rut")
            print ("\t5 - Salir")
            option =int(input("Ingrese opcion: "))
            os.system('cls')
            if option ==1:
                print ("\t1 - Ver asientos disponibles")
               
                print("cliente tenga en cuenta que los asientos desde el 25 al 40 son VIP")
                print("valor de pasaje normal: $14.900")
                print("valor de pasaje VIP: $24.000")
                asientosDisponibles()
            elif option==2:
                print ("\t2 - Comprar asiento")
                asientosDisponibles()
                CompraDeAsientos()
            elif option==3:
                print ("\t3 - Anular viaje")
                AnulacionDePasaje()
            elif option==4:
                print("\t4 - Modificar datos por rut")
                modificacionDeDatos()
            elif option==5:
                ejecutar = False
                print("\tfin del programa")
            else:
                print("opcion invalida")
            if ejecutar:
                pause = input("Presione Enter para volver al menu principal...")
        except:
            print("Ha ocurrido un error al ingresar...")

            pause = input("Presione Enter para continuar...")

menu()