from Tools.scripts.verify_ensurepip_wheels import print_notice

if __name__ == '__main__':
    try:
        numero = int(input("Introduce un numero:"))
        resultado = 10/numero
    except ValueError:
        #Manejo de la excepcion si se introduce un valor no entero
        print("Error debes introducir un numero entero")
    except ZeroDivisionError:
        #Manejo d ela excepcion si  intenta dividir por cero
        print("Error! No se puede dividir entre cero")
    else:
        #se ejecuta si no hubo excepciones
        print("El resultado es:", resultado)
    finally:
        print("Fin del programa")