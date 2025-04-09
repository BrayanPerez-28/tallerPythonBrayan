class ListaDatos:
    def __init__(self, matricula:str, estudiante:str, asignatura:str):
        self.matricula = matricula
        self.estudiante = estudiante
        self.asignatura = asignatura


if __name__ == '__main__':
    lista = []
    lista.append(ListaDatos("123456789", "Brayan Daniel", "Matematicas"))
    lista.append(ListaDatos("1234567818", "Hannia", "POO"))
    lista.append(ListaDatos("1234567894", "Nely", "Estructurada"))
    lista.append(ListaDatos("123456783", "Cyrene", "Redes"))

    for obj in lista:
        print(f"Matricula: {obj.matricula}")
        print(f"Nombre: {obj.estudiante}")
        print(f"Asignatura: {obj.asignatura} \n")