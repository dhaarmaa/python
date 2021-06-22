import os
os.system('cls')
try:
     # seleccion de hamburguesa
    print("== Tipo Hamburguesa ==")
    print("1.Hamburguesa queso $2000\n 2.Hamburguesa con Tocino $2500\n 3.Hamburguesa doble especial $3000")
    suma = 0
    opcion = int(input("Ingrese opcion:"))
    if opcion==1:
        precio = 2000
        hamburguesa= "Hamburguesa queso $2000"
    elif opcion==2:
        precio = 2500
        hamburguesa = "Hamburguesa con Tocino $2500"
    elif opcion==3:
        precio = 3000
        hamburguesa = "Hamburguesa doble especial $3500"
    else:
        print("Opcion inconrrecta...")
    suma+= precio #es lo mismo:suma = suma + precio 
    # seleccion de bebida 
    print("n== Bebida ==")    
    print("1.Bebida normal $500\n 2.Bebida grande $2500\n 3.Jugo nectar $1000 \ n 4.ninguna ")
    opcion = int(input("Ingrese Opcion:"))
    if opcion==1:
       precioBebida = 500
       Bebida = "normal $500"
    elif opcion==2:
         precioBebida = 600
         Bebida = "grande $2500"

    elif opcion==3:
         precioBebida= 1000
         Bebida="jugo nectar $1000" 
    elif opcion==4: 
         precioBbeida= 0 
         Bebida= "ninguna"     
    else: 
        print("Opcion incorrecta ")   
    suma += precioBebida 
    # seleccion de agregados  
    print("\n== Agregados ==")   
    print("1.Papas fritas $600\n 2.Porcion 2 empanadas de queso $500\n 3.Porcion de 4 empanadas $900\n 4.ninguna")  
    opcion = int(input("Ingrese opcion:"))
    if opcion==1:
         agregado = "papas fritas $600"
         precioAgregados = 600
    elif opcion==2:
         agregado = " 2 empanadas queso $500"
         precioAgregados = 500
    elif opcion==3: 
        agregado = " 4 empanadas queso $900"
        precioAgregados= 900
    elif opcion==4:
        agregado = "ninguna"
        precioAgregados = 0
    else:
        print("Opcion inorrecta")
    suma += precioAgregados
    # Postres 
    print("\n== Postres ==")   
    print("1.Vaso helado $300\n2.fruta a eleccion $200\n4.ninguna")
    opcion = int(input("Ingrese opcion"))
    if opcion==1:
       Postre = "vasodehelado $300"
       precioPostre = 300
    elif opcion==2:
        Postre = "eleccion fruta $200"
        precioPostre = 200
    elif opcion==3:
        Postre = "ninguna "
        precioPostre = 0
    else: 
        print("Opcion incorrecta")
    suma += precioPostre 
    print("\n== Tipo de cliente ==")
    print("1.Estudiante Becado\n 2.Profesor\n 3.Administrativo\n 4. otro")
    cliente=int(input("Ingrese una opcion:"))
    if cliente==1: 
       TipoDeCliente = " Estudiante becado " 
       calculo = (suma*60)/100
       descuento = suma-calculo
    if cliente==2:
        TipoDeCliente = " Profesor"
        calculo = ( suma*40)/100
        descuento = suma-calculo
    if cliente==3:
        TipoDeCliente = " Administrativo"
    if cliente==4:
        TipoDeCliente = "Otro"
        descuento = suma 
    print(f"El total a pagar es de {suma} ")
    IngresoDeDinero=int(input(" Ingrese el monto de dinero a pagar"))
    if IngresoDeDinero>=0: 
       Vuelto=IngresoDeDinero-descuento 
    else: 
        print("Dinero insuficiente")  
    print("Resumen de compra")
    print(f"Tipo de hamburguesa: {hamburguesa} ")
    print(f"Tipo de bebida:  {Bebida} ")
    print(f"Tipo de agregado: {agregado} ")
    print(f"Postre: {Postre} ")
    print(f"Tipo de cliente: {TipoDeCliente} ")
    print(f"El total  es de:  $ {suma}")
    print(f" El descuento que se le aplica es: $ {calculo} ")
    print(f"Dinero con el descuento aplicado es de: $ {descuento} ")
    print(f"Monto con el que paga es de:  $ {IngresoDeDinero} ")
    print(f"Su vuelto es de: $ {Vuelto } ")

    
except: 
    print("respuesta invalida") 