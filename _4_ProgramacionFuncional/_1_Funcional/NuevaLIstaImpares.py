if __name__ == '__main__':
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 14, 15, 16, 17, 18, 19, 20]
    listaImpares = list(filter(lambda x:x%2==0 , numeros)) #filter es un for con un if
    listaPares = list(filter(lambda x:x%2==1 , numeros))

    print(f"Lista de nuemros pares : {listaPares}")
    print(f"Lista de nuemros impares : {listaImpares}")
    paresconPotencia = list(map(lambda z:z**2, filter(lambda t:t%2==0, numeros)))
    print(f"Pares con potencia: {paresconPotencia}")
