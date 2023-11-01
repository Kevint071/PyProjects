from os import chdir, path
from conexion_DB_biblia import crear_tabla, existencia_tabla
from credencial_fl0 import conn
from funciones import limpiar_pantalla, estudiar_nueva_palabra, consultar_palabras, eliminar_palabra

chdir(path.dirname(path.abspath(__file__)))

driver = None

def operacion():
    limpiar_pantalla()
    while True:
        try:
            accion = int(input("""¿Qué operación desea realizar?:
            
    1. Obtener palabra para estudiar
    2. Consultar palabras en la Base de datos
    3. Eliminar una palabra de la Base de datos
            
    Elije una opcion: """))
            if accion == 1  or accion == 2 or accion == 3:
                break
            else:
                limpiar_pantalla()
                print("Opcion no válida\n")
        except KeyboardInterrupt:
            accion = False
        except:
            limpiar_pantalla()
            print("Valor no válido\n")

    return accion


def run():
    # Verificar estado de la DB
    tabla_existe = existencia_tabla()

    if not tabla_existe:
        crear_tabla()

    while True:
        limpiar_pantalla()
        accion = operacion()
        limpiar_pantalla()

        if accion == 1:
            estudiar_nueva_palabra()
        elif accion == 2:
            consultar_palabras()
        elif accion == 3:
            eliminar_palabra()
        elif not accion:
            return
        
        repetir = int(input("\nElije el número 1 para hacer otra operacion y 2 para salir: "))
        
        if repetir == 2: break

    conn.commit()
    conn.close()


if __name__ == "__main__":
    run()
