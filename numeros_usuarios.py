




while True:
    print("Pensa un numero de dos cifras que no sean iguales")
    num = int(input("Cuando lo pienses, ingresalo: "))
    num_inv =int (str(num)[1]+str(num)[0])
    print(f"El numero invertido es:{num_inv} ")
    if num_inv > num:
        print(f"El numero invertido es mas grande que el que habias ingresado.")
        n1 = num_inv - num
    else:
        print("El numero invertido es menor que el numero ingresado")
        n1 = num - num_inv
    n2 = int(str(num)[0]) + int(str(num)[1])
    termino1 = n1 / 2
    termino2 = (n2-2) /2
    termino3 = (n2+2) /2
    print(f"el numero que pensaste es el {int(termino2)}{int(termino3)}")
    break
    