if __name__ == '__main__':
    lista = [1,2,"Lunes",3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    lista.append(200)
    lista.append("Viernes")
    lista.append(False)
    lista.append(2.69)

    for elemento in lista:
        print(elemento)

    lista2=[1222,1500,1255]
    lista2.append(lista)
    print(lista2)

    nombre : str = "Luis"
    nombre +="Gutierrez"
    #nombre.join("Gutierrez")
    print(nombre)


    lista3 = ["Federico", "Pablo", "Karla"]
    cadena:str = " - ".join(lista3)
    print(cadena)

    separado=cadena.split()
    for dato in separado:
        print(dato)
