import os

import mysql.connector
from mysql.connector import Error


def mostrar_productos():
    """Consulta y muestra todos los productos de la base de datos."""
    conexion = None
    cursor = None

    try:
        # Lee la configuracion desde las variables de entorno.
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port=3306,
            database="tienda",
        )

        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        registros = cursor.fetchall()

        if not registros:
            print("La tabla productos esta vacia.")
            return

        # Obtiene los nombres de las columnas y calcula su ancho.
        columnas = [columna[0] for columna in cursor.description]
        filas = [[str(valor) if valor is not None else "NULL" for valor in fila]
                 for fila in registros]
        anchos = [
            max(len(columnas[i]), max(len(fila[i]) for fila in filas))
            for i in range(len(columnas))
        ]

        separador = "+-" + "-+-".join("-" * ancho for ancho in anchos) + "-+"
        encabezado = "| " + " | ".join(
            columnas[i].ljust(anchos[i]) for i in range(len(columnas))
        ) + " |"

        print(separador)
        print(encabezado)
        print(separador)
        for fila in filas:
            print("| " + " | ".join(
                fila[i].ljust(anchos[i]) for i in range(len(fila))
            ) + " |")
        print(separador)

    except (Error, ValueError) as error:
        print(f"Error al conectar o consultar MySQL/MariaDB: {error}")
    finally:
        # Cierra el cursor y la conexion aunque ocurra un error.
        if cursor is not None:
            cursor.close()
        if conexion is not None and conexion.is_connected():
            conexion.close()


if __name__ == "__main__":
    mostrar_productos()
