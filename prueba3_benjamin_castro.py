libreria = []
ventas = []
generos = ("ficción","no ficción","ciencia")

#OPCION 1
#Se agrega la variable stock para más adelante poder realizar la opción de registrar ventas.
def RegistrarLibro():
    titulo = validacionTexto("Ingrese el título del libro:\n")
    autor = validacionTexto("Ingrese el autor del libro:\n")
    genero = validacionTexto("Ingrese el género del libro:\n").lower()
    global generos
    if genero not in generos:
        generos += (genero,)
    precio = validacionEntero("Ingrese el precio del libro:\n ")
    stock = validacionEntero("Ingrese el stock del libro:\n")
    libreria.append({"titulo":titulo,"autor":autor,"genero":genero,"precio":precio,"stock":stock})

#valida que el input no sea vacío
def validacionTexto(pregunta):
    while True:
        respuesta = input(pregunta)
        if respuesta != "":
            return respuesta.lower()
        
#valida que el input sea entero no negativo
def validacionEntero(pregunta):
    while True:
        try:
            respuesta = int(input(pregunta))
            if respuesta < 0:
                print("El valor ingresado debe ser mayor o igual a cero")
            else:
                return respuesta
        except:
            print("El valor ingresado debe ser un número entero mayor a 0")
# -----------------------

#OPCION 2
def listarLibros():
    for l in libreria:
        print(f"Título: {l['titulo']}, autor: {l['autor']}, género: {l['genero']}, precio: {l['precio']}, stock: {l['stock']}")
#------------------------

#OPCION 3
def registrarVenta():
    titulo_buscado = validacionTexto("Ingrese el título del libro que busca:\n").lower()
    for l in libreria:
        #Se realizará la venta considerando el primer libro que coincida con el título.(no se está cubriendo el caso de libros con igual nombre)
        if titulo_buscado == l['titulo']:
            print("Libro encontrado!. Información del libro:")
            print(f"Título: {l['titulo']}, autor: {l['autor']}, género: {l['genero']}, precio: {l['precio']}, stock: {l['stock']}")
            #Verificación de stock
            cantidad_vendida = validacionEntero("Ingrese la cantidad vendida:\n")
            if cantidad_vendida > l['stock']:
                print("La cantidad vendida  no puede ser superior al stock del producto. Vuelva a intentarlo desde el menú inicial.")
                return ""
            else:
                #Generación de boleta por pantalla, la venta es un diccionario y se agrega a la lista ventas
                l['stock'] -= cantidad_vendida
                venta = {'libro':l,'cantidad vendida':cantidad_vendida,'valor total':cantidad_vendida*l['precio']}
                print("fLibro\t\tCantidad\tValor unitario\tValor total")
                print(f"{venta['libro']['titulo']}\t\t{venta['cantidad vendida']}\t\t${venta['libro']['precio']}\t\t${venta['valor total']}")
                ventas.append(venta)
                print("venta realizada con éxito")
                return ""
    print("El título que buscas no ha sido encontrado en la librería.")
#------------------------------
            
#OPCION 4
def imprimirReporteVentas():
    while True:
        opcionReporte=input("--IMPRESIÓN DE REPORTES DE VENTAS---\nSeleccione la opción que prefiera:\
                            \n(1)Imprimir todos los reportes\n(2)Imprimir por género en específico\n")
        #Impresión de todos los reportes
        if opcionReporte == "1":
            print("Seleccionaste la opción 'Imprimir todos los reportes'")
            for v in ventas:
                print(f"Título: {v['libro']['titulo']}, Cantidad vendida: {v['cantidad vendida']}, Valor unitario: {v['libro']['precio']},\
Valor total: {v['valor total']}")
            print("impresión realizada con éxito")
            return ""
        #Impresión de reportes por género
        elif opcionReporte == "2":
            print("Seleccionaste la opción 'Imprimir por género en específico'")
            for i in range(len(generos)):
                print(f"({i}){generos[i]}")
            opcionGenero = validacionEntero("Ingresa una opción de género\n")
            if opcionGenero >= len(generos) or opcionGenero < 0:
                print("Opción inválida intenta nuevamente desde el menú inicial.")
            else:
                genero_buscado = generos[opcionGenero]
                for v in ventas:
                    if v['libro']['genero'] == genero_buscado:
                        print(f"Título: {v['libro']['titulo']}, Género: {v['libro']['genero']}, Cantidad vendida: {v['cantidad vendida']},\
Valor unitario: {v['libro']['precio']},Valor total: {v['valor total']}")
                print("impresión realizada con éxito")
            return ""
        else:
            print("La opción de impresión es inválida, inténtelo denuevo")
#------------------------------
        
#OPCION 5
def generarTxt():
    with open('registroVentas.txt','w') as archivo:
        for v in ventas:
            archivo.write(f"Titulo: {v['libro']['titulo']}, Cantidad vendida: {v['cantidad vendida']}, Valor unitario: {v['libro']['precio']},\
Valor total: {v['valor total']}\n")
        print("archivo creado con éxito.")
#------------------------------
        
#se agrega opción 7 para cargar datos de ejemplo y facilitar la evaluación del código.
#OPCION 7
def cargarDatosEjemplo():
    libreria.append({"titulo":"programacion en Python","autor":"benjamín castro","genero":"ciencia","precio":2999,"stock":4})
    libreria.append({"titulo":"programacion en Java","autor":"benjamín castro","genero":"ciencia","precio":1000,"stock":15})
    libreria.append({"titulo":"cuentos de un programador","autor":"alin alcaya","genero":"ficción","precio":5000,"stock":22})
    ventas.append({'libro':libreria[0],'cantidad vendida':2,'valor total': 5998})
    ventas.append({'libro':libreria[0],'cantidad vendida':3,'valor total': 8997})
    ventas.append({'libro':libreria[1],'cantidad vendida':2,'valor total': 10000})
    ventas.append({'libro':libreria[2],'cantidad vendida':11,'valor total': 55000})
    print("se han cargado los siguientes datos de ejemplo:")
    print("libros:")
    print(libreria[0])
    print(libreria[1])
    print(libreria[2])
    print("ventas:")
    print(ventas[0])
    print(ventas[1])
    print(ventas[2])
#--------------------------

#MAIN
while True:
    opcion = input("---Menú---\n(1)Registrar libro\n(2)Listar todos los libros\n(3)Registrar venta\
                   \n(4)Imprimir reporte de ventas\n(5)Generar Txt\n(6)Salir del programa\n(7)Cargar datos de ejemplo(llame a esta opción al comienzo y solo una vez)\n")
    if opcion == "1":
        print("Seleccionaste la opción 'Registrar libro'")
        RegistrarLibro()
    elif opcion == "2":
        print("Seleccionaste la opción 'Listar todos los libros'")
        listarLibros()
    elif opcion == "3":
        print("Seleccionaste la opción 'Registrar venta'")
        registrarVenta()
    elif opcion == "4":
        print("Seleccionaste la opción 'Imprimir reportes de venta'")
        imprimirReporteVentas()
    elif opcion == "5":
        print("Seleccionaste la opción 'Generar Txt'")
        generarTxt()
    elif opcion == "6":
        print("Seleccionaste la opción 'Salir del programa'")
        break
    elif opcion == "7":
        print("Seleccionaste la opción 'Cargar datos de ejemplo'")
        cargarDatosEjemplo()
    else:
        print("La opción ingresada es inválida, inténtelo otra vez.")