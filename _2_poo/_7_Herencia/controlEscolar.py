class ListaDatos:
    def __init__(self, matricula:str, estudiante:str, asignatura:str):
        self.matricula = matricula
        self.estudiante = estudiante
        self.asignatura = asignatura

class ControlEscolar(ListaDatos):
    def __init__(self):
        self.lista=[]

    def addEstudiante(self, matricula, estudiante, asignatura):
        self.lista.append(ListaDatos(matricula, estudiante, asignatura))

    def show(self):
        for estudiantes in self.lista:
            print(f"Matricula: {estudiantes.matricula}  Nombre: {estudiantes.estudiante} Asignatura:{estudiantes.asignatura} \n")


if __name__ == '__main__':
    escolar = ControlEscolar()
    escolar.addEstudiante("4564683", "Brayan Daniel", "Sistemas Operativos")
    escolar.addEstudiante("4564682", "Oswaldo", "Bases de datos")
    escolar.addEstudiante("4564681", "Emiliano", "Estructurada")
    escolar.addEstudiante("4564680", "Nancy", "Ingenieria de Software")

    escolar.show()