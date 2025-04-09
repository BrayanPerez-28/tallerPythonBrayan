class Auto:
    marca="Honda"
    modelo=1000
    placa="PCH-52-16"


if __name__ == '__main__':
    taxi = Auto()
    miauto = Auto()
    print(taxi.placa)
    miauto.placa = "YHG-44-45"
    print(miauto.placa)