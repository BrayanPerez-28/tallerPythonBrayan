import statistics as mate
def suma(lista)->int:
    suma = 0
    for valor in lista:
        suma += valor
    return suma


if __name__ == '__main__':
    lista2 = [5,6,9,3,8]
    print(f"La suma es {suma(lista2)}")