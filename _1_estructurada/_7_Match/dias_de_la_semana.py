import sys
if __name__ == '__main__':
   sys.stdout.write("Proporciona un nuemro del dia de la semena  ")
   num=int(input())
   semana = ""
   match num:
       case 1:semana="Lunes"
       case 2:semana="Martes"
       case 3:semana="Miercoles"
       case 4:semana="Jueves"
       case 5:semana="Viernes"
       case 6:semana="Sabado"
       case 7:semana="Domingo"
   if num>=1 and num<=7:
       sys.stdout.write(f"El dia de la semana indicado es {semana}")
   else:
       sys.stdout.write(f"{semana}")