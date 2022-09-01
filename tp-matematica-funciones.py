#   Imports y Variables globales
import random, math
run = True
opcion=0


                # Funciones
    #   Funcion random 
def funcionrandom(b):
    listado = []
    con = 0
    while con <= 3:
        num = random.randint(-100,100)
        if num not in listado and num != b:
            listado.append(num)
            con +=1
    return listado
    #   Funcion Paralela
def paralela(a,b):
    listado = funcionrandom(b)
    print(f"""Rectas paralelas f = {a}x+{b}
                Recta N°1 = {a}x + {listado[0]}
                Recta N°2 = {a}x + {listado[1]}
                Recta N°3 = {a}x + {listado[2]}
    """)
    #   Funcion Perpendicular
def perpendicular(a,b):
    listado = funcionrandom(101)
    ainversa = 1/-a
    print(f"""Rectas perpendiculares f = {a}x+{b}
                Recta N°1 = {ainversa}x + {listado[0]}
                Recta N°2 = {ainversa}x + {listado[1]}
                Recta N°3 = {ainversa}x + {listado[2]}
    """)
    #   Funcion Analisis de una recta
def analisisrecta(a,b):
    if a < 0 :
        direccion = "Recta Decreciente"
    if a > 0:
        direccion = "Recta Creciente"
    print(f"""El corte con el eje x es : {-b/a}
              El corte con el eje y es : {b}
              La recta es {direccion}
    """)
    #   Funcion de Parabola
def parabola(a,b,c):
    #Comprobamos hacia donde va la parabola
    if a < 0 :
        direccion = "Parabola Concava Arriba"
    if a > 0:
        direccion = "Parabola Concava Abajo"
    # Calculamos el eje de simetria
    ejesimetria = -(b/(2*a))
    # Calculamos el Vertice de la parabola
    vertice = a*(ejesimetria)**2 + b*(ejesimetria) + c
    # Comprobamos si hay corte en el eje x
    corte = b**2 -4*a*c
    if corte > 0:
        print(f"Corta el eje x : {corte}")
        print("Tiene dos Raices Reales")
    if corte == 0:
        print("Toca el eje x pero no lo corta")
        print("Tiene una Raiz Doble")
    if corte < 0:
        print("No corta con el eje x")
        print("No tiene solucion")
    # Calcularmos los dos extremos por donde la parabola corta el eje x
    corte1= (-b + math.sqrt( b**2 - 4*a * c))/2*a
    corte2 = (-b - math.sqrt( b**2 - 4*a * c))/2*a
    print(f"la parabola es {direccion} su eje de simetria es {ejesimetria} y su vertice es {vertice} ")
    print(f"Los cortes en x son x1:{corte1} x2:{corte2}")

    #   Bucle Principal
while run:
    print("1- Rectas paralela y perpendicular a una dada\n2- Análisis de una recta\n3- Análisis de una parábola\n999- Salir")
    opcion = float(input("Elige una opción: "))

    if opcion == 1:
        a = float(input("Ingresa el termino coeficiente principal: "))
        b = float(input("Ingresa el termino independiente: "))
        if a == 0:
            print("El coeficiente principal no puede ser cero")
            continue
        else:
            paralela(a,b)
            perpendicular(a,b)
    if opcion == 2:
        a = float(input("Ingresa el termino coeficiente principal: "))
        b = float(input("Ingresa el termino independiente: "))
        if a == 0:
            print("El coeficiente principal no puede ser cero")
            continue
        else:
            analisisrecta(a,b)
    if opcion == 3:
        a = float(input("Ingresar Coeficiente principal: "))
        b = float(input("Ingresar Coeficiente lineal: "))
        c = float(input("Ingresar Termino Independiente: "))
        parabola(a,b,c)
    if opcion == 999:
        run = False




    
