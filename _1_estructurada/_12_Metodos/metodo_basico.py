import statistics as mate
# def suma(a, b):
#     print(f"La suma de {a} + {b} es: {a+b}")


# def suma(a, b=None, c= None):
#     if c is None:
#         if b is None:
#             print(f"La suma de {a} es: {a}")
#         else:
#             print(f"La suma de {a} + {b} es: {a + b}")
#     else:
#         print(f"La suma de {a} + {b} +{c} es: {a + b + c}")


def promedioArreglo(lista):
    lista.append(5)
    lista.append(45)
    lista.append(56)
    p = mate.mean(lista)
    print(f"El promedio es {p}")

if __name__ == '__main__':
    # suma(5, 90, 45)
    # suma(90, 45)
    # suma(90)
    #Pythin es paso por referencia
    lista2 = [1, 2, 3, 4 ,5]
    promedioArreglo(lista2)
    print(lista2)




