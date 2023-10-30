from os import name, system


lista_separables = {"Set back": "Retrasar", "Fix up": "Arreglar", "Figure out": "Analizar hasta entender", "Win over": [["Estar de acuerdo con alguien"], ["Estar de acuerdo conmigo"]], "Call off": "Cancelar", "Take on": ["Contratar", ["Aceptar responsabilidad"]], "Tell of": "Criticar por algo malo", "Point out": ["Señalar", "Resaltar"], "Let down": "Desilusionar", "Mess up": "Arruinar"}

lista_inseparables = {"Get into": "Profundizar", "Cut back": ["Reducir", "Acortar"], "Blow up": "Enojar", "Die down": "Decaer", "Whatch out": ["Cuidadoso", "Cuidado"], "Step down": "Renunciar a un trabajo", "Hear of": [["Aprender algo de alguien"], ["Aprender algo de algo"]], "Settle on": ["Decidir", "Elegir"], "Touch on": "Mencionar a alguien superficialmente", "Draws on": "Plasmar"}


def limpiar_pantalla():
    if name == "posix":
        system("clear")
    elif name == "nt" or name == "dos" or name == "ce":
        system("cls")


def variacion_respuesta_derecho(lista_item):

    """Funcion que une dos significados con conjuncion 'o'.
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

    """Funcion que une dos significados en sentido inverso con conjuncion 'o'.
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


def agregar_variaciones_respuestas(i, lista_palabras, id_separable, tipo_verbo):

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

    return [palabra_traducida, tipo_verbo, id_separable]


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


def run():
    limpiar_pantalla()

    # Mostrar los verbos frasales separables

    print("VERBOS FRASABLES SEPARABLES\n")

    for i, j in lista_separables.items():

        if type(j) == list:
            j = variacion_respuesta_derecho(j)

        print(f"{i}: {j}")

    input("\nPresiona enter para ver los verbos frasales inseparables... ")

    limpiar_pantalla()

    # Mostrar verbos frasales inseparables

    print("VERBOS FRASABLES INSEPARABLES\n")

    for i, j in lista_inseparables.items():

        if type(j) == list:
            j = variacion_respuesta_derecho(j)

        print(f"{i}: {j}")

    input("\nPresiona enter para comenzar prueba... ")

    limpiar_pantalla()

    # Iniciar proceso de evaluacion uniendo los dos tipos de verbos frasales

    puntos = 0

    palabras_ingles = set(list(lista_separables.keys()) + list(lista_inseparables.keys()))

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

        if i in lista_separables:
            palabra_traducida, tipo_verbo, id_separable = agregar_variaciones_respuestas(i, lista_separables, 1, "separable")

        else:
            palabra_traducida, tipo_verbo, id_separable = agregar_variaciones_respuestas(i, lista_inseparables, 2, "inseparable")

        while True:
            try:
                es = int(input("¿Es separable? 1(si) 2(no): "))

                if es != 1 and es != 2:
                    limpiar_pantalla()
                    print("Valor no válido, digite el 1 o el 2...\n")
                else:
                    break
            except ValueError:
                limpiar_pantalla()
                print("Valor no válido, digite el 1 o el 2...\n")

        if type(palabra_traducida) == str:
            palabra_traducida = list([palabra_traducida])

        # Mostrando resultados dependiendo de lo que haya escrito el usuario en la variable "traduccion" y "es"

        if id_separable == es and traduccion in palabra_traducida:
            puntos += 1
            print(f"Bien, {puntos} puntos de 20 puntos {int((puntos/20) * 100)}%")
        elif id_separable == es and traduccion not in palabra_traducida:

            print(f'\nEl significado es incorrecto, pero el tipo de verbo frasal es correcto...\nPuedes colocar una de estas respuestas:\n')

            mostrar_respuestas(palabra_traducida)

        elif id_separable != es and traduccion in palabra_traducida:

            print(f"La traduccion es correcta pero el verbo frasal está mal ya que es {tipo_verbo}")
        else:
            print(f'\nEl significado y el tipo de verbo frasal son incorrectos ya que es {tipo_verbo}...\nPuedes colocar una de estas respuestas:\n')

            mostrar_respuestas(palabra_traducida)

if __name__ == "__main__":
    run()
    input("Presiona enter para salir: ")
