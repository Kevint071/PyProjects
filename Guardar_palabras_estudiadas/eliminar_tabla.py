from credenciales import conn
from conexion_DB_biblia import existencia_tabla


tabla_existe = existencia_tabla()

if tabla_existe == True:
  print("La tabla existe...")
  cursor = conn.cursor()
  query = "DROP TABLE palabras;"
  cursor.execute(query)
  print("Pero ahora no...")

conn.commit()
conn.close()