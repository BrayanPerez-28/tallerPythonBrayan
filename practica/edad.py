import json
import sys
def traerPersonas():
    with open("datos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        for persona in datos["personas"]:
            yield persona

if __name__ == '__main__':

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    persons = list(traerPersonas())

    for i, personaBase in enumerate(persons, 1):
        match i:
            case 1:
                sys.stdout.write(RED)
                if personaBase['edad'] >= 18:
                    print(f"Es mayor de edad", end='  ')
                else:
                    print(f"Es menor edad", end='  ')
                print(f"{i}. {personaBase['id']} - {personaBase['nombre']} {personaBase['edad']} {personaBase['rfc']}")
            case 2:
                print(GREEN)
                if personaBase['edad'] >= 18:
                    print(f"Es mayor de edad", end='  ')
                else:
                    print(f"Es menor edad", end='  ')
                print(f"{i}. {personaBase['id']} - {personaBase['nombre']} {personaBase['edad']} {personaBase['rfc']}")
            case 3:
                print(BLUE)
                if personaBase['edad'] >= 18:
                    print(f"Es mayor de edad", end='  ')
                else:
                    print(f"Es menor edad", end='  ')
                print(f"{i}. {personaBase['id']} - {personaBase['nombre']} {personaBase['edad']} {personaBase['rfc']}")
            case 4:
                print(MAGENTA)
                if personaBase['edad'] >= 18:
                    print(f"Es mayor de edad", end='  ')
                else:
                    print(f"Es menor edad", end='  ')
                print(f"{i}. {personaBase['id']} - {personaBase['nombre']} {personaBase['edad']} {personaBase['rfc']}")
            case 5:
                print(CYAN)
                if personaBase['edad'] >= 18:
                    print(f"Es mayor de edad", end='  ')
                else:
                    print(f"Es menor edad", end='  ')
                print(f"{i}. {personaBase['id']} - {personaBase['nombre']} {personaBase['edad']} {personaBase['rfc']}")
            case _:
                pass

