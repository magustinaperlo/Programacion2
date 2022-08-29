from ejercitacionejercicio1 import Persona
from ejercitacionejercicio2 import Cuenta


class CuentaJoven(Cuenta):
    def __init__(self,nombre):
        super().__init__(nombre)
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
        if persona.getEdad() >= 18 and persona.getEdad() < 25:
            return True
        else:
            return False
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
            print("El titular no es valido")

persona = Persona()
persona.setNombre("Dan")
persona.setDni(323233)
persona.setEdad(26)
cuenta = CuentaJoven(persona.getNombre())
cuenta.setTipoCuenta()
cuenta.TipoCuenta()
cuenta.mostrar()
cuenta.ingresar(500)
cuenta.mostrar()
cuenta.retirar(150.50)

