class bibliotecaDigital:
    def __init__(self):
        self.__ISBM:str=""
        self.__titulo:str=""
        self.__autor:str=""

    @property
    def getISBM(self)->str:
        return self.__ISBM

    @property
    def getTitulo(self)->str:
        return self.__titulo

    @property
    def getAutor(self)->str:
        return self.__autor


class modLibro(bibliotecaDigital):
    def __init__(self, __ISBM, __titulo, __autor):
        self.lista=[]

    def add(self, __ISBM, __titulo, __autor):
        self.lista.append(bibliotecaDigital(__ISBM, __titulo, __autor))

    def delete(self, n):
        self.lista.remove(bibliotecaDigital(n))

    def show(self):
        lib = bibliotecaDigital
        for libro in self.lista:
            print(f"ISBM: {lib.getISBM}  Titulo: {lib.getTitulo} Autor: {lib.getAutor} \n")


if __name__ == '__main__':
    libros = modLibro
    libros.add("Don Quijote", "El mar","nuevoAutor")
    libros.add("Don Quijote", "El mar","nuevoAutor")
    libros.add("Don Quijote", "El mar","nuevoAutor")
    libros.add("Don Quijote", "El mar","nuevoAutor")

    libros.show()