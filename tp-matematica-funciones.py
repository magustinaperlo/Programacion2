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
    print(f"Corte en el eje y: {c}")
    # Calculamos el eje de simetria
    ejesimetria = -(b/(2*a))
    # Calculamos el Vertice de la parabola
    vertice = a*(ejesimetria)**2 + b*(ejesimetria) + c
    #Comprobamos hacia donde va la parabola
    if a < 0 :
        direccion = "Parabola Concava Hacia Abajo"
        print(f'la parabola crece hasta {ejesimetria} y luego decrece')
    if a > 0:
        direccion = "Parabola Concava Hacia Arriba"
        print(f'la parabola decrece hasta {ejesimetria} y luego crece')
    # Comprobamos si hay corte en el eje x
    determinante = b**2 -4*a*c
    print(f"la parabola es {direccion} su eje de simetria es {ejesimetria} y su vertice es {vertice} ")
    if determinante > 0:
        print(f"Determinante: {determinante}")
        print("Tiene dos Raices Reales")
        # Calcularmos los dos extremos por donde la parabola corta el eje x
        corte1= (-b + math.sqrt(determinante))/(2*a)
        corte2 = (-b - math.sqrt(determinante))/(2*a)
        print(f"Los cortes en x son x1: {corte1} x2: {corte2}")
    elif determinante == 0:
        print("Toca el eje x pero no lo corta")
        corte= (-b + math.sqrt(determinante))/(2*a)
        print(f"Tiene una Raiz Doble x1: {corte} x2: {corte}")
    elif determinante < 0:
        print("No corta con el eje x")
        print("No tiene raíces dentro de los números reales")
    

    #   Bucle Principal
while run:
    try:
        print("1- Rectas paralela y perpendicular a una dada\n2- Análisis de una recta\n3- Análisis de una parábola\n999- Salir")
        opcion = float(input("Elige una opción: "))

        if opcion == 1:
            try:
                a = float(input("Ingresa el termino coeficiente principal: "))
                b = float(input("Ingresa el termino independiente: "))
                if a == 0:
                    print("El coeficiente principal no puede ser cero")
                    continue
                else:
                    paralela(a,b)
                    perpendicular(a,b)
            except:
                print("Solo numeros")
        if opcion == 2:
            try:
                a = float(input("Ingresa el termino coeficiente principal: "))
                b = float(input("Ingresa el termino independiente: "))
                if a == 0:
                    print("El coeficiente principal no puede ser cero")
                    continue
                else:
                    analisisrecta(a,b)
            except:
                print("Solo numeros")
        if opcion == 3:
            try:
                a = float(input("Ingresar Coeficiente principal: "))
                b = float(input("Ingresar Coeficiente lineal: "))
                c = float(input("Ingresar Termino Independiente: "))
                parabola(a,b,c)
            except:
                print("Solo se ingresan numeros")
        if opcion == 999:
            run = False
        else:
            print("Ingrese una opcion valida")
    except:
        print("Solo Acepta numeros")




    
