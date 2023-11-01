from credencial_fl0 import conn
from time import sleep


def existencia_tabla():
    cursor = conn.cursor()

    cursor.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';""")
    tables = cursor.fetchall()

    if ("palabras",) in tables:
        return True
    else:
        print("La tabla 'palabras' no existe\n")
        return False

def crear_tabla():
    print("Creando tabla...")
    sleep(0.5)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE palabras(id Serial PRIMARY KEY, palabra text);""")

    # Usar codigo si se quiere ver las tablas creadas

    cursor.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';""")
    tables = cursor.fetchall()
    print(tables)
    
