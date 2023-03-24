class Animal:
    def __innit__(self,):
        self.edad = 3
        self.sexo = "hembra"
    
    def comer(self):
        print("El animal esta comiendo")

    def dormir(self):
        print("El animal esta durmiendo")


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
      
class Pollo(Oviparo):
    def __innit__(self):
        super().__init__()
        

class Gato(Mamifero):
    def __innit__(self):
        super().__init__()

    def miau():
        print("MIAUUUUUUUU MIAUUUUUUUU")

    
    def parto(self):
        print("El animal esta de aprto")

class Ornitorrinco(Mamifero, Oviparo):
        def __innit__(self):
            super().__init__()

pollo = Pollo()
pollo.aovar()