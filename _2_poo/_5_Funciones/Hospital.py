class Hospital:
    def __init__(self):
        self.__NombrePaciente:str="Federico"
        self.__nss:int=1258
        self.__enfermedad:str="Gripe"

    def getNombrePaciente(self)->str:
        return self.__NombrePaciente

    def getNss(self)->int:
        return self.__nss

    @property
    def getEnfermedad(self)->str:
        return self.__enfermedad


    def setNombrePaciente(self, nombrePaciente:str):
        self.NombrePaciente = nombrePaciente

    def setNss(self, nss:int):
        self.nss = nss


    def setEnfermedad(self, enfermedad:str):
        self.enfermedad = enfermedad

if __name__ == '__main__':
    hospital = Hospital()

    hospital.__NombrePaciente = "Juan"
    print(f"Nombre: {hospital.getNombrePaciente()}")
    print(f"Nombre: {hospital.getEnfermedad}")