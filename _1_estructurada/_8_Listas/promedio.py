import statistics as mate

if __name__ == '__main__':
    numeros = [10, 20, 50, 80, 90, 30, 90]

    # Opción Tardada
    conteo = 0
    suma = 0
    promedio: float
    for valor in numeros:
        suma += valor
        conteo += 1

    promedio = suma / conteo
    print(promedio)

    # Opción Medio Lenta
    suma = 0
    for valor in numeros:
        suma += valor
    promedio = suma / len(numeros)
    print(promedio)

    # Opción Rapida
    promedio = mate.mean(numeros)
    print(promedio)