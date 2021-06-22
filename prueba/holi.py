import os
os.system ('cls')
try:
    #Seleccion de la hamburguesa
    suma = 0
    print("***Tipo de hamburguesa***")
    print("1.Hamburguesa queso $2000\n2. Hamburguesa con tocino $2500\n3. Hamburguesa doble especial $3000\n4 ninguna.")
    opcion = int(input("Ingrese opcion"))
    if opcion==1:
        precio=2000
        hamburguesa = "Hamburguesa queso $2000"
    elif opcion==2:
        precio=2500
        hamburguesa = "Hamburguesa con tocino $2500"
    elif opcion==3:
        precio=3000
        hamburguesa= "Hamburguesa doble especial $3000"
    elif opcion==4:
        precio=0
        hamburguesa= "Ninguna"
    else:
        print("Opcion incorrecta...")
    suma = suma+precio
    #Seleccion de bebida
    print("Seleccione bebida")
    print("1.Bebida Normal $500\n2. Bebida grande $1000\n3. Jugo Nectar $1000\n4. Ninguno")
    opcion = int(input("Ingrese opcion"))
    if opcion==1:
        precio=500
        bebida = "bebida normal $500"
    elif opcion==2:
        precio=1000
        bebida = "bebida grande $1000"
    elif opcion==3:
        precio=1000
        bebida = "jugo nectar $1000"
    elif opcion==4:
        precio=0
        bebida = "Ninguna"
    else:
        print("Opcion incorrecta...")
    suma = suma+precio
    #Seleccion de agregados
    print("Agregados")
    print("1.Papas fritas $600\n2. porcion 2 empanadas queso $500\n3.porcion 4 empanadas de queso $900\n4.ninguna")
    opcion = int(input("Ingrese opcion"))
    if opcion==1:
        precio=600
        agregado= "Papas fritas $600"
    elif opcion==2:
        precio=500
        agregado = "Porcion 2 empanadas de queso $500"
    elif opcion==3:
        precio=900
        agregado = "Porcion 4 empanadas de queso $900"
    elif opcion==4:
        precio=0
        agregado= "Ninguno"
    else:
        print("Opcion incorrecta...")
    suma = suma+precio
    #Seleccion de postres
    print("Postres")
    print("1.Vaso helado $300\n2.Fruta a eleccion $200\n3. ninguno")
    opcion = int(input("Ingrese opcion"))
    if opcion==1:
        precio=300
        postre= "Vaso de helado $300"
    elif opcion==2:
        precio=200
        postre= "Fruta a eleccion $200"
    elif opcion==3:
        precio=0
        postre= "Ninguno"
    else:
        print("Opcion incorrecta...")
    suma = suma+precio
    print("Descuento")
    print("1.Becado\n2.Profesor\n3.Administrativo\n4.cliente")
    opcion1 = int(input("Ingrese opcion"))
    if opcion==1:
        descuento=suma*0.6
        Descuento= "Descuento 60%"
    elif opcion==2:
        descuento=suma*0.4
        descuento= "Descuento 40%"
    elif opcion==3:
        descuento=suma-suma
        descuento= "Descuento 100%"
    elif opcion==4:
        descuento=0
    else:
        print("Ingrese opcion valida...")
    total_dscto=suma-descuento
    print(f"\nTotal es:${suma}")
    dinero = int(input("Ingrese Dinero"))
    if dinero>=suma:
        vuelto = dinero - total_dscto
        print("========================")
        print(f"Detalle de venta:\n{hamburguesa}\n{bebida}\n{agregado}\n{postre}")
        print(f"Tipo hamburguesa seleccionada : {hamburguesa}")
        print(f"Tipo de bebida seleccionada : {bebida}")
        print(f"Tipo de agregado seleccionado : {agregado}")
        print(f"Tipo de postre seleccionado : {postre}")
        print(f"Total venta:${suma}")
        print(f"Paga con:{dinero}")
        print(f"Vuelto:{vuelto}")
        print(f"Total con descuento aplicado: {total_dscto}")
        print("==============================")
    else:
        print("Falta dinero para pagar...")
except:
    print("Error al ingresar...")