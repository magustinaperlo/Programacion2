

class Cuenta():
    def __init__(self,nombre):
        self.titular = nombre
        self.cantidad = 0.0
    def getTitular(self):
        return self.titular
    def mostrar(self):
        return print(f"Titular:{self.getTitular()} Cantidad:{self.getCantidad()}")
    def getCantidad(self):
        return self.cantidad
    def setCantidad(self,valor):
        try:
            if valor > 0:
                self.cantidad = valor
            else:
                print("La Cantidad ingresada es incorrecta")
                self.setCantidad(int(input("Ingresar Cantidad:")))
        except:
            print("Solo se pueden ingresar numeros")
    def ingresar(self,valor):
        self.setCantidad(valor)
    def retirar(self,valor):
        try:
            if self.getCantidad() > valor :
                if valor > 0:
                    self.setCantidad(self.getCantidad()-valor)
                    print(f"Se retiraron {valor} de la cuenta")
                    print(f"Su nuevo Saldo es:{self.cantidad}")
            else:
                print("El valor ingresado es mas grande que la cantidad de la cuenta")
                self.retirar(int(input("Vuelva a ingresar el numero: ")))
        except:
            print("Debe ingresar solo numeros")
            self.retirar(int(input("Vuelva a ingresar el numero: ")))




