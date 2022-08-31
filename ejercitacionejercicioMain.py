from ejercitacionejercicio1 import Persona
from ejercitacionejercicio2 import Cuenta
from ejercitacionejercicio3 import CuentaJoven


while True:
    try:
        print("="*30)
        print("1- Para registrar persona\n2- Para registrar cuenta\n3- Para registrar cuenta joven\n99- para salir")
        op = int(input("Ingresar Opcion:"))
        if op == 1:
            persona = Persona()
            persona.setNombre(input("Ingrese El nombre: "))
            persona.setDni(int(input("Ingrese DNI:")))
            persona.setEdad(int(input("Ingresar Edad: ")))
            persona.mostrar()
            persona.esMayorDeEdad()
        if op == 2:
            persona = Persona()
            if persona.setNombre(input("Ingrese El nombre: ")):
                if persona.setDni(int(input("Ingrese DNI:"))):
                    if persona.setEdad(int(input("Ingresar Edad: "))):
                        cuenta = Cuenta(persona.nombre)
                        while True:
                            try:
                                print("="*30)
                                print("Sistema de fondos\n1- Para ingresar dinero\n2- Para retirar dinero\n3- Para ver datos de la cuenta\n9- Para Volver al menu anterior")
                                opf = int(input("Ingresar Opcion: "))
                                if opf == 1:
                                    cuenta.ingresar(float(input("Ingresar Dinero: ")))
                                if opf == 2:
                                    cuenta.retirar(float(input("Retiro de Dinero: ")))
                                if opf == 3:
                                    cuenta.mostrar()
                                if opf == 9:
                                    break
                            except:
                                print("Opcion ingresada incorrecta. solo numeros")
                    else: print("La edad deben ser solo numeros")
                else: print("El DNI son solo numeros. debe contener entre 6 y 8 caracteres")
            else: print("Debe ingresar bien el nombre, no puede tener menos de 3 caracteres")
        elif op == 3:
            persona = Persona()
            if persona.setNombre(input("Ingrese El nombre: ")):
                if persona.setDni(int(input("Ingrese DNI:"))):
                    if persona.setEdad(int(input("Ingresar Edad: "))):
                        cuenta = CuentaJoven(persona.nombre)
                        cuenta.setEdad(persona.getEdad())
                        cuenta.setTipoCuenta()
                        while True:
                            try:
                                print("="*30)
                                print("Sistema de fondos\n1- Para ingresar dinero\n2- Para retirar dinero\n3- Para mostrar informacion de la cuenta\n4- Para setear Bonificacion\n9- Para Salir")
                                opj = int(input("Ingresar opcion: "))
                                if opj == 1:
                                    cuenta.ingresar(float(input("Ingresar Dinero: ")))
                                if opj == 2:
                                    cuenta.retirar(float(input("Monto a Retirar: ")))
                                if opj == 3:
                                    cuenta.mostrar()
                                    cuenta.TipoCuenta()
                                if opj == 4:
                                    if cuenta.esTitularValido():
                                        cuenta.setBonificacion(float(input("Ingresar Bonificacion: ")))
                                    else:
                                        print("Su cuenta no es Cuenta joven. No se puede aplicar Bonificacion")
                                if opj == 9:
                                    break
                            except:
                                print("Caracter invalido, solo numeros")
                    else: print("La edad deben ser solo numeros")
                else: print("El DNI son solo numeros. debe contener entre 6 y 8 caracteres")
            else: print("Debe ingresar bien el nombre, no puede tener menos de 3 caracteres")
        elif op == 99:
            print("Proceso terminado")
            break
        else:
            print("Opcion ingresada incorrecta. intente de nuevo")
    
    except:
        print("El valor ingresado es incorrecto, solo numeros.")