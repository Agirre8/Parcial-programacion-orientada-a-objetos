


class Pollo(Animal, Oviparo):
    def __innit__(self):
        super().__init__()
        

class Gato(Animal, Mamifero):
    def __innit__(self):
        super().__init__()

    def miau():
        print("MIAUUUUUUUU MIAUUUUUUUU")

class Oviparo(Animal):

    def __innit__(self, huevos):
        super().__init__()
        self.huevos = huevos
    def aovar(self):
        print("El animal está poniendo huevos")

class Mamifero(Animal):

    def __innit__(self, embarazo):
        super().__init__()
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
    
pollo = Animal(3, "femenino")

pollo.aovar()