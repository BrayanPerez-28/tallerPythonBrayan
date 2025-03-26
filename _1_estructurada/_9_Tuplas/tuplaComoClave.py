if __name__ == '__main__':
    #No existen posiciones en los diccionarios
    # diccionario = {
    #     ('id', 'int') : '2',
    #     'nombre' : 'Juan',
    #     'apellido' : 'Gutierrez'
    # }

    diciconario= {}
    diccionario[("Ana", 25)] = "Estudiante"
    diccionario[("Luis", 30)] = "Ingenieria"
    diccionario[("Carlos", 40)] = "Abogado"


    ocupacion_ana = diccionario[("Ana", 25)]
    ocupacion_luis = diccionario[("Luis", 30)]
    print(f"Ana es: {ocupacion_ana}")
    print(f"Luis es: {ocupacion_luis}")
