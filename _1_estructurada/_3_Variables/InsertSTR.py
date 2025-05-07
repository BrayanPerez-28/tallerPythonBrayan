


if __name__ == '__main__':
    palabra: str = "%s"
    lista : list = ["id", "nombre-completo", "nombre_usuario", "correo_electronico", "contrasennia", "id_rol"]
    lista2 : list = []

    t = len(lista)
    print(t)

    for i in range(t):
        lista2.append(palabra)

    print(lista2)
    campos = ", ".join(lista) #Genera una sola cadena
    values = ", ".join(lista2)

    querySQL = f"INSERT INTO tabla ({campos}) Values ({values})"
    print(querySQL)

