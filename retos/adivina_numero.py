import random
if __name__ == '__main__':
    i: int = 0
    nuRandom = random.randint(1,100)
    bol = False
    while bol == False:
        y = int(input("Ingresa un numero entero entre 1 y 100: "))
        if y < nuRandom:
            print(f"Es menor tu numero que el numero a adivinar")
            i = +1
        else:
            if y>nuRandom:
                print(f"Es mayor tu numero que el numero a adivinar")
                i = +1
            else:
                if y==nuRandom:
                    print("Felicidades has acertado el numero")
                    print(f"Lo has intentado : {i} veces")
                    bol = True

