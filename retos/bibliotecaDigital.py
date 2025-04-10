class bibliotecaDigital:
    def __init__(self, ISBM:int, titulo:str, autor:str):
        self.__ISBM = ISBM
        self.__titulo = titulo
        self.__autor = autor

    @property
    def getISBM(self)->int:
        return self.__ISBM

    @property
    def getTitulo(self)->str:
        return self.__titulo

    @property
    def getAutor(self)->str:
        return self.__autor


class ModLibro(bibliotecaDigital):
    def __init__(self):
        self.lista=[]

    def add(self, ISBM:int, titulo:str, autor:str):
        self.lista.append(bibliotecaDigital(ISBM, titulo, autor))


    def show(self):
        lib = bibliotecaDigital
        for lib in self.lista:
            print(f"ISBM: {lib.getISBM}  Titulo: {lib.getTitulo} Autor: {lib.getAutor} \n")


    def delete(self, ISMB:int):
        lib = bibliotecaDigital
        for lib in self.lista:
            if lib.getISBM == ISMB:
                self.lista.remove(lib)
                break

if __name__ == '__main__':
    libros = ModLibro()
    libros.add(4, "El mar","nuevoAutor")
    libros.add(3, "El mar","nuevoAutor")
    libros.add(2, "El mar","nuevoAutor")
    libros.add(1, "El mar","nuevoAutor")
    libros.show()

    print("Se elimina un libro ")
    libros.delete(1)

    libros.show()


