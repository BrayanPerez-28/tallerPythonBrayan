def extra(agenda:tuple):
    i:int=0
    while(i<len(agenda)):
        i+=1
        yield agenda[i-1]

if __name__ == '__main__':
    agenda=[]
    agenda.append(("Juan", "correo1@gmail.com", "22240030"))
    agenda.append(("Jose", "correo2@gmail.com", "22240031"))
    agenda.append(("Joel", "correo3@gmail.com", "22240032"))
    agenda.append(("Luis", "correo4@gmail.com", "22240033"))
    agenda.append(("Kevin", "correo5@gmail.com", "22240034"))
    agenda.append(("Moni", "correo6@gmail.com", "22240035"))
    agenda.append(("Paola", "correo7@gmail.com", "22240036"))
    agenda.append(("Ulices", "correo8@gmail.com", "22240037"))
    agenda.append(("Samantha", "correo9@gmail.com", "22240038"))
    agenda.append(("Gabo", "correo0@gmail.com", "22240039"))

    for valor in extra(agenda):
        nombre, correo, numero = valor
        print(f"{nombre}{correo}{numero}")