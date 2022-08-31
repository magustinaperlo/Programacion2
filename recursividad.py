def palindromo(palabra):
    if palabra == palabra[::-1]:
        print("La palabra es palindromo! - "+palabra)
    else:
        print("La palabra no es palindromo - intentar nuevamente")
        palindromo(input("Ingresar nueva palabra: "))

palindromo("Nada")