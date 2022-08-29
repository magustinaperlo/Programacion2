

class Persona():
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.dni = ""
    def mostrar(self):
        return print(f"Nombre: {self.getNombre()} Edad: {self.getEdad()} DNI: {self.getDni()}")
    def esMayorDeEdad(self):
            if self.edad >= 18:
                print("La persona es mayor de edad")
                return True
            else:
                print("la persona es menor de edad")
                return False
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def getDni(self):
        return self.dni
    def setNombre(self,valor):
        if valor != " " and len(valor) > 2 :
            self.nombre = valor
        else:
            print("El nombre debe contener mas de 2 caracteres")
    def setEdad(self,valor):
        try:
            if int(valor) > 0:
                self.edad = int(valor)
            else:
                print("La edad debe estar entr 0 y 100 años")
        except:
            print("La edad ingresada es incorrecta")
    def setDni(self,valor):
        try:
            if len(str(valor))>= 6 and len(str(valor))<= 8:
                self.dni = int(valor)
            else:
                print("la cantidad de caracteres del dni es incorrecta")
        except:
             print("El dni ingresado es incorrecto. solo numeros")

# persona = Persona()
# persona.setNombre("Dan")
# persona.setDni(12345678)
# persona.setEdad(18)
# persona.mostrar()
# persona.esMayorDeEdad()

