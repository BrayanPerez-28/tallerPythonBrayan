from math import pow

def suma (x: []) -> int:
    suma = 0
    for elemento in x:
        suma += elemento
    return suma

# def potencia(x:int) -> int:
#     return int(pow(x,2))

if __name__ == '__main__':
    numeros = [1,2,3,4,5,6,7,8,9,10,11,12,16,14,15,16,17,18,19,20]
    print(f"Numeros originales: {numeros}")
    print(f"La suma total con una funcion: {suma(numeros)}")


    # numerosCuadrado = list(map(potencia, numeros))
    # print(f"Numeros Cuadrados con una funcion: {numerosCuadrado}")

    numerosCuadrado1 = list(map(lambda x:x*x , numeros)) #recorre la lista
    print(f"Numeros Cuadrados con un lambda: {numerosCuadrado1}")