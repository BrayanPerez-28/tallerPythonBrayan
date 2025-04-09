class Datos:
    def __init__(self, nombre, correo, whatssap):
        self.nombre = nombre
        self.correo = correo
        self.whatssap = whatssap


    def setNombre(self, nombre):
        self.nombre = nombre

if __name__ == '__main__':
    datos = Datos("Brayan", "brayan@gmail.com", 2412003527)

    print(datos.nombre)
    datos.setNombre("Juan")
    print(datos.nombre)
    datos.nombre="Gabriela"
    print(datos.nombre)