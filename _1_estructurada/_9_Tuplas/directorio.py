if __name__ == '__main__':
    agenda = {}
    agenda["GOAT800717"] = ("Tomas Gonzales", "Correo1@gmail.com", "22240031")
    agenda["GOAT800718"] = ("MOni Gonzales", "Correo2@gmail.com", "22240032")
    agenda["GOAT800719"] = ("Kevin Gonzales", "Correo3@gmail.com", "22240033")
    agenda["GOAT800716"] = ("Edgar Gonzales", "Correo4@gmail.com", "22240034")

    nombre, correo, numero = agenda["GOAT800716"]

    print(f"Nombre : {nombre} correo: {correo} numero: {numero}")