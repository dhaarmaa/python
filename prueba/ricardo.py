import os
os.system('cls')
try:
    # seleccionar tipo de hamburguesa
    print("== Tipo de Hamburguesa ==")
    print("1.Hamburguesa Queso $2000\n2.Hamburguesa con Tocino $2500\n3.Hamburguesa doble Especial $3500\n4.Ninguna")
    opcion = int(input("Ingrese opción:"))
    if opcion==1:
        precio = 2000
        hamburguesa = "Hamburguesa Queso $2000"
    elif opcion==2:
        precio = 2500
        hamburguesa = "Hamburguesa con Tocino $2500"
    elif opcion==3:
        precio = 3500
        hamburguesa = "Hamburguesa doble Especial $3500"
    elif opcion==4:
        precio = 0  
        hamburguesa = "Ninguna"
    else:
        print("Opción incorrecta")    
    suma = 0
    suma += precio  #es lo mismo: suma = suma + precio
    # selección tamañp de bebida 
    print("\n== Tamaño bebida ==")
    print("1.Normal $500\n2.Grande $1000\n3.Nectar $1000\n4.Ninguna")
    opcion = int(input("Ingrese opción:"))
    if opcion==1:
        precio = 500
        tamaño = "Normal $500"
    elif opcion==2:
        precio = 1000
        tamaño = "Grande $1000"
    elif opcion==3:
        precio = 1000
        tamaño = "Nectar $1000"
    elif opcion==4:
        precio = 0 
        tamaño= "Ninguna"         
    else:
        print("Opción incorrecta")
    suma += precio
    # selección de agregados 
    print("\n== Agregados ==")
    print("1.Papas fritas $600\n2.Porcion 2 Empanadas de Queso $500\n3.Porcion 4 Empanadas de Queso $900\n4.Ninguna")
    opcion = int(input("Ingrese opción:"))
    if opcion==1:
        agregado = "Papas fritas $600"
        precio = 600
    elif opcion==2:
        agregado = "Porcion 2 Empanadas de Queso $500"
        precio = 500
    elif opcion==3:
        agregado = "Porcion 4 Empanadas de Queso $900"
        precio = 900
    elif opcion==4:
        agregado = "Ninguna"
        precio = 0
    else:
        print("Opción incorrecta")
    suma += precio
    #seleccion de postre
    print("\n== Postres ==")
    print("1.Vaso Helado $300\n2.Fruta a eleccion $200\n3.Ninguno")
    opcion = int(input("Ingrese opción:"))
    if opcion==1:
        postre = "Vaso Helado $300"
        precio = 300
    elif opcion==2:
        postre = "Fruta a Eleccion $200"
        precio = 200
    elif opcion==3:
        postre = "Ninguno"
        precio = 0  
    else:
        print("Opción incorrecta")
    suma += precio       
    #seleccion de descuento
    print("\n== Descuento ==")
    print("1.Becado\n2.Profesor\n3.Administrativo\n4.Cliente")
    opcion = int(input("Ingrese opción:"))
    if opcion==1:
        descuento = suma*0.6
    elif opcion==2: 
        descuento = suma*0.4
    elif opcion==3:
        descuento = suma-suma
    elif opcion==4:
        descuento = 0 
    else:
        print("Opción incorrecta")
    total_dcto=suma-descuento

    print(f"\nTotal es:${suma}")
    dinero = int(input("Ingrese Dinero:"))
    if dinero>=suma:
        vuelto = dinero - suma
        print("=================================")
        print(f"Boleta de venta:\n{hamburguesa}\n{tamaño}\n{agregado}\n{postre}")
        print(f"Total venta:${suma}")
        print(f"Paga con: {dinero}")
        print(f"Total a pagar con descuento aplicado: {total_dcto}")
        print(f"Vuelto:{vuelto}")
        print("===================================")
    else:
        print("Falta dinero para pagar...")
except:
    print("Error al ingresar...\n vuelva a ejecutar el programa.")
