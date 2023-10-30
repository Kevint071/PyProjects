from os import system, name
import requests
from bs4 import BeautifulSoup
from credencial_fl0 import conn


def limpiar_pantalla():
    if name == "posix":
        system("clear")
    elif name == "nt" or name == "dos" or name == "ce":
        system("cls")


def estudiar_nueva_palabra():
    def obtener_palabra():
        url = "https://www.wikicristiano.org/index.php?id=aleatoria"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return (soup.find("h2").text).split(" ")[-1]

    def agregar_palabra_DB(cursor, palabra):
        cursor.execute("SELECT * FROM palabras;")
        cant_datos = len(cursor.fetchall()) + 1

        query = f'''ALTER SEQUENCE palabras_id_seq RESTART WITH {cant_datos};
    INSERT INTO palabras(palabra) VALUES (%s);'''
        cursor.execute(query, (palabra, ))

    def mostrar_palabra_opcion(palabra):
        while True:
            try:
                print(f"Palabra obtenida: {palabra}\n")
                desicion = int(input("""Elija lo que quiere hacer con esta palabra:

    1. Guardarla en la Base de Datos
    2. Cambiar esa palabra por otra palabra
    3. Descartar palabra y salir
        
    Escoja una opción: """))

                if desicion == 1 or desicion == 2 or desicion == 3:
                    break
                else:
                    print("Opcion no válida")
                    limpiar_pantalla()
            except:
                print("Valor no válido")
                limpiar_pantalla()
        return desicion

    while True:
        palabra = obtener_palabra()
        desicion = mostrar_palabra_opcion(palabra)

        if desicion == 1:
            cursor = conn.cursor()
            agregar_palabra_DB(cursor, palabra)
            print("\nDatos guardados")
            conn.commit()
            break
        elif desicion == 2:
            limpiar_pantalla()
        elif desicion == 3:
            break


def consultar_palabras():
    cursor = conn.cursor()
    query = "SELECT * FROM palabras;"
    cursor.execute(query)
    rows = cursor.fetchall()

    print("Las palabras en la base de datos de estudio son:\n")
    [print(f"   {row[0]}. {row[1]}") for row in rows]


def eliminar_palabra():
    cursor = conn.cursor()
    query = "SELECT * FROM palabras;"
    cursor.execute(query)
    rows = cursor.fetchall()

    print("Las palabras en la base de datos de estudio son:\n")
    [print(f"   {row[0]}. {row[1]}") for row in rows]

    while True:
        try:
            id = int(input("\nDigite el ID de la palabra que quiere eliminar: "))
            if id > len(rows):
                print(f"Solo hay {len(rows)} elementos, no puede seleccionar un ID mayor")
            else:
                break
        except:
            print("Valor no válido")

    while True:
        confirmacion = input(f"\n¿Seguro que quiere eliminar la palabra ({rows[id-1][1]})? S/N: ")

        if confirmacion.upper() == "S":
            cursor.execute(f"""DELETE FROM palabras WHERE id = {id};""")

            cursor.execute("""ALTER SEQUENCE palabras_id_seq RESTART WITH 1;
                          WITH updated AS (SELECT id, row_number() OVER (ORDER BY id) AS new_id FROM palabras) UPDATE palabras SET id = updated.new_id FROM updated WHERE palabras.id = updated.id;""")
            break
        elif confirmacion.upper() == "N":
            break
        else:
            print("Valor no válido")

    conn.commit()
