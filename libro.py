class Libro:
    def __innit__(self, v, autor, fecha, genero, paginas):
        self.velocidad = v
        self.autor = autor
        self.fecha = fecha
        self.genero = genero
        self.paginas = paginas

    def situar_valores(self, paginas, velocidad):
        dias = 0
        self.paginas = paginas
        self.velocidad = velocidad
        dias == self.paginas/self.velocidad
        print(f"Se tardará {dias} días en escribir el libro")

libro = Libro()

libro.situar_valores(100, 2)
