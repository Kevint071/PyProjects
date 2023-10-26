from credenciales import conn


def existencia_tabla():
    cursor = conn.cursor()

    cursor.execute(
        """SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';""")
    tables = cursor.fetchall()

    if ("palabras",) in tables:
        print("La tabla 'palabras' existe")
        return True
    else:
        print("La tabla 'palabras' no existe")
        return False

def crear_tabla():
    cursor = conn.cursor()
    
    cursor.execute("""
  CREATE TABLE palabras(
    id Serial PRIMARY KEY,
    palabra text,
    traduccion text
  );
""")

    # Usar codigo si se quiere ver las tablas creadas

    # cursor.execute(
    # """SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';""")
    # tables = cursor.fetchall()
    # print(tables)

    
