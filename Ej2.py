

class Oviparo(Animal):
    super().__innit__()

    def __innit__(self, huevos):
        self.huevos = huevos
    def aovar(self):
        print("El animal está poniendo huevos")

class Mamifero(Animal):

    super().__innit__()
    def __innit__(self, embarazo):
        self.embarazo = embarazo
    
    def parto(self):
        print("El animal esta de aprto")

class Animal:
    def __innit__(self, edad, sexo):
        self.edad = edad
        self.sexo = sexo
    
    def comer(self):
        print("El animal esta comiendo")

    def dormir(self):
        print("El animal esta durmiendo")
    