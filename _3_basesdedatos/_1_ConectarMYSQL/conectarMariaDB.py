import mariadb
import platform
def conectar_y_consultar():
    try:
        conexion = mariadb.connect(
            host = "localhost",
            database = "almacen",
            user = "root",
            password = "",
            port = 3306
        )

        print(type(conexion))
        print("Conexion a la base de datos maria db")

        cursor = conexion.cursor()
        cursor2 = conexion.cursor()
        consulta = "select * from usuarios"
        consulta2 = "select * from roles"
        cursor.execute(consulta)
        cursor2.execute(consulta2)

        #Recuperar y mostrar resultados
        resultados = cursor.fetchall()
        print("Resultado ", type(resultados))
        print("Datos en la tabla")
        for fila in resultados:
            print(f" ID: {fila[0]}\n Nombre completo: {fila[1]}\n Nombre de usuario: {fila[2]}\n Coreo electronico: {fila[3]}\n Contraseña: {fila[4]}\n ID_Rol: {fila[5]}\n")

        resultados2 = cursor2.fetchall()
        print("Resultado ", type(resultados2))
        print("Datos en la tabla")
        for fila in resultados2:
            print(
                f" ID: {fila[0]}\n Nombre_Rol: {fila[1]}\n ")


    except mariadb.Error as e:
        print(f"Error al conectar la base de datos: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
            print("Conexion cerrada")


if __name__ == '__main__':
    conectar_y_consultar()
