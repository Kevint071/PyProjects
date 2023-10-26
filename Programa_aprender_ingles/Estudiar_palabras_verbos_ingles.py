from os import name, system
from credenciales import conn
from Conexion_base_de_datos import existencia_tabla, crear_tabla

lista_palabras = {}


tabla_existe = existencia_tabla()
if tabla_existe == False:
    crear_tabla()


def limpiar_pantalla():
    if name == "posix":
        system("clear")
    elif name == "nt" or name == "dos" or name == "ce":
        system("cls")


def variacion_respuesta_derecho(lista_item):
    """Funcion que une significados con conjuncion 'o'.
       Parametros lista_item list con valores tipo strings.
       returns temporal."""

    temporal = ""
    for x in lista_item:
        if type(x) == list:
            x = "".join(x)
        temporal += x
        if x != "".join(lista_item[-1]):
            temporal += " o "

    return temporal.capitalize()


def variacion_respuesta_inversa(lista_item):
    """Funcion que une significados en sentido inverso con conjuncion 'o'.
       Parametros lista_item list con valores tipo strings.
       returns temporal"""

    temporal = ""
    for x in reversed(lista_item):
        if type(x) == list:
            x = "".join(x)
        temporal += x
        if x != "".join(lista_item[0]):
            temporal += " o "

    return temporal.capitalize()


def agregar_variaciones_respuestas(i, lista_palabras):
    """Funcion que agrega respuestas unidas con la conjuncion 'o' a listas.
       Parámetro i string ó list, lista_palabras cualquier list, id_separable int 1 ó 2, tipo_verbo string.
       returns list con variables palabra_traducida, tipo_verbo, id_separable"""

    # Separar significados para ser mostrados en caso de equivocacion

    if type(lista_palabras[i]) == list:

        lista_item = lista_palabras[i]

        temporal = variacion_respuesta_derecho(lista_item)
        temporal_2 = variacion_respuesta_inversa(lista_item)

        # Agregando una variacion de respuesta con las 2 opciones

        lista_palabras[i].append(temporal)
        lista_palabras[i].append(temporal_2)

    for x in range(0, len(lista_palabras[i])):
        if type(lista_palabras[i][x]) == list:
            lista_palabras[i][x] = str(lista_palabras[i][x]).strip("[]'")

    palabra_traducida = lista_palabras[i]

    return palabra_traducida


def mostrar_respuestas(lista_palabra_traducida):
    """Función que muestra significados de una palabra en inglés.
       Parámetros lista_palabra_traducida cualquier list
       returns None
       """

    for i in lista_palabra_traducida:
        if type(i) == list:
            for j in i:
                print(f"- {j}")
        else:
            i = str(i).replace("[", "")
            i = i.replace("]", "")
            print(f"- {i}")


def iniciar_test():
    cursor = conn.cursor()

    query = '''SELECT * FROM palabras'''
    cursor.execute(query)

    row = cursor.fetchall()

    for x in row:
        if x[2].count(",") >= 1:
            palabras = x[2].split(",")

            for i in range(len(palabras)):

                palabras[i] = palabras[i].strip().capitalize()

                if palabras[i].count(" ") >= 1:
                    palabras[i] = [palabras[i]]

            lista_palabras[x[1]] = palabras
        else:
            lista_palabras[x[1]] = x[2]
    limpiar_pantalla()

    # Mostrar palabras

    print("PALABRAS INGLES: ESPAÑOL\n")

    for i, j in lista_palabras.items():

        if type(j) == list:
            j = variacion_respuesta_derecho(j)

        print(f"{i}: {j}")

    input("\nPresiona enter para comenzar prueba... ")

    limpiar_pantalla()

    # Iniciar proceso de evaluacion uniendo los dos tipos de verbos frasales

    puntos = 0

    palabras_ingles = set(list(lista_palabras.keys()))

    for i in palabras_ingles:
        # Ciclo while True para evitar errores de valores
        while True:
            traduccion = input(f"\nTraduce {i}: ")
            traduccion = traduccion.capitalize().strip(" ")

            traduccion_temp = traduccion.replace(" ", "")

            if traduccion_temp.isalpha():
                break
            else:
                limpiar_pantalla()
                print("No utilices números ni caracteres especiales...")

        palabra_traducida = agregar_variaciones_respuestas(i, lista_palabras)

        if type(palabra_traducida) == str:
            palabra_traducida = list([palabra_traducida])

        # Mostrando resultados dependiendo de lo que haya escrito el usuario en la variable "traduccion" y "es"

        if traduccion in palabra_traducida:
            puntos += 1
            print(
                f"Bien, {puntos} puntos de {len(palabras_ingles)} puntos {int((puntos/len(palabras_ingles)) * 100)}%")
        else:
            print(
                f'\nEl significado es incorrecto...\nPuedes colocar una de estas respuestas:\n')

            mostrar_respuestas(palabra_traducida)

    if __name__ != "__main__":
        input("\nPresiona enter para salir...")


if __name__ == "__main__":
    iniciar_test()
    input("\nPresiona enter para salir: ")
