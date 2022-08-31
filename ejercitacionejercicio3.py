
from ejercitacionejercicio2 import Cuenta


class CuentaJoven(Cuenta):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.edad= 0
        self.bonificacion = 0
        self.tipocuenta = "Estandar"
    def setBonificacion(self,valor):
        try:
            if int(valor) > 0:
                self.bonificacion = int(valor)
            else:
                print("La bonificacion debe ser mayor a 0")
        except:
             print("Caracter no soportado")
    def esTitularValido(self):
        if self.getEdad() >= 18 and self.getEdad() < 25:
            return True
        else:
            return False
    def getEdad(self):
        return self.edad
    def setEdad(self,valor):
        try:
            if valor > 0 and 100 > valor:
                self.edad = valor
            else:
                print("La edad debe ser entre 0 y 100 años")
        except:
            print("Error - Solo se permite numeros")
    def setTipoCuenta(self):
        if self.esTitularValido():
            self.tipocuenta = "Cuenta Joven"
        else:
            self.tipocuenta = "Estandar"
    def getBonificacion(self):
        return self.bonificacion
    def getTipoCuenta(self):
        return self.tipocuenta
    def TipoCuenta(self):
        print(f"Tipo de Cuenta: {self.getTipoCuenta()} - Bonificacion: {self.getBonificacion()}")
    def retirar(self,valor):
        if self.esTitularValido():
            try:
                if self.getCantidad() > valor :
                    self.setCantidad(self.getCantidad()-valor)
                    print(f"Se retiraron {valor} de la cuenta")
                    print(f"Su nuevo Saldo es:{self.cantidad}")
                else:
                    print("El valor ingresado es mas grande que la cantidad de la cuenta")
            except:
                print("Debe ingresar solo numeros")
        else:
            print("El titular no es valido - debe ser menor de 25 años")



