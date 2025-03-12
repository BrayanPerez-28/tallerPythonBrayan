if __name__ == '__main__':
    cantidad:int= int(input("Cuantos nombres quieres"))
    indios = [0,0,0,0,0,0,0,0,0,0]
    extras: int = 1
    for i in range (cantidad):
        nombre=str(input("Proporciona el nombre: "))
        tam=len(nombre)
        match tam:
            case 1: indios[0]+=1
            case 2: indios[1]+=1
            case 3: indios[2]+=1
            case 4: indios[3]+=1
            case 5: indios[4]+=1
            case 6: indios[5]+=1
            case 7: indios[6]+=1
            case 8: indios[7]+=1
            case 9: indios[8]+=1
            case 10:indios[9]+=1
            case _: extras+=1

    a =1
    for nom in indios:
        if nom > 0:
            print(f"Se encuantran {nom} de {a} letras")
        a+=1
    print(f"Sobrepasan {extras}")