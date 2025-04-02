import json
import sys
def traerPersonas():
    try:
        archivo = open("datos123.json", "r", encoding="utf-8")
        datos = json.load(archivo)
        for persona in datos["personas"]:

            yield persona

    except FileNotFoundError:
        print("!Error! El archivo no existe")
    except json.JSONDecodeError:
        print("!Error! El archivo no contiene un JSON valido")
    except Exception as e:
        print("Pues no se que ocurrio",e)
    else:
        archivo.close()
        print(RESET, "Archivo JSON cerrado")

if __name__ == '__main__':
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    RESET = "\033[0m"
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
