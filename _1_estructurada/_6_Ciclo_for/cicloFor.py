import sys
if __name__ == '__main__':
    for i in range(10):
        print(f"{i}")

    for i in range(6,12):
        print(f"{i}")

   # for i in range(60, 12, -3):
       # print(f"{i}")

    for j in range(1, 20):
        print(f"{j}", end=" ")#Esto end "" se ussa para no dar salto de linea solo espacios entre estos

    sys.stdout.write("Texto sin salto de linea")