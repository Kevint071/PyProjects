from tkinter import Tk, Canvas, Label, Entry, Button, Toplevel, font, END, Listbox
from Conexion_base_de_datos import conn
from Estudiar_palabras_verbos_ingles import iniciar_test

palabras_traducidas = {}
validacion = []


def verificar_palabras(palabra, label, x, y):

    """Función que verifica palabras con errores de caracteres especiales. 
    Parametros palabra cualquier str, label de tkinter, x cualquier int, y cualquier int. 
    Returns True o False"""

    label.place(x=x, y=y)
    if palabra.count(" ") >= 1:
        if palabra.replace(" ", "").replace(",", "").isalpha():
            label["text"] = "  "
            return True
        else:
            label["text"] = "X"
            return False
    else:
        if palabra.replace(",", "").isalpha():
            label["text"] = "  "
            return True
        elif palabra.isalpha() == False or palabra.len() == 0:
            label["text"] = "X"
            return False


def limpiar_input(*entry):
    for i in entry:
        i.delete(0, END)


def obtener_palabra(query, conn, valor):

    """Función que obtiene el dato de la base de datos para mostrar en ventana_mostrar
    parametro query tipo SQL, conn coneccion con base de datos, valor cualquier str
    returns datos o None"""

    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchall()

    for i in row:
        for j in i:
            if valor in str(j):
                datos = i
                return datos


def buscar_palabras(valor, label):

    """Funcion que busca palabras en la ventana mostrar
       parametros palabra cualquier str, label"""

    valor = valor.strip().capitalize()
    
    if valor == "":
        row = None
    else:
        query = '''SELECT * FROM palabras;'''
        row = obtener_palabra(query, conn, valor)

    mostrar_busqueda(row, label)

    return label["text"]


def mostrar_busqueda(row, label):

    """Funcion que muestra el resultado de la busqueda en ventana_mostrar
    parametros row tupla de datos, label de tkinter"""

    if row == None or row == "":
        label["text"] = "Dato no encontrado"
    else:
        label["text"] = (f"{row[0]}. {row[1]} → {row[2]}")


def validar_palabras(entry_mostrar, label_mostrar, boton, accion, ventana):

    valor = entry_mostrar.get().strip().capitalize()
    resultado = buscar_palabras(entry_mostrar.get(), label_mostrar)

    limpiar_input(entry_mostrar)


    if valor == "" or resultado == "Dato no encontrado":
        boton.place_forget()
        return None
    else:
        if accion == "borrar":
            boton.place(x=390, y=89)
            boton["command"] = lambda: borrar(valor, boton)
        elif accion == "editar":

            label_palabra.place_forget()
            entry_palabra.place_forget()
            label_traduccion.place_forget()
            entry_traduccion.place_forget()
            boton_guardar.place_forget()

            boton["command"] = lambda: agregar_palabras_editar(valor, boton, ventana, label_palabra, entry_palabra, label_traduccion, entry_traduccion)
            boton.place(x=215, y=165)


def agregar_palabras_editar(valor, boton_editar, ventana_editar, label_palabra, entry_palabra, label_traduccion, entry_traduccion):

    boton_editar.place_forget()
    label_palabra.place(x=155, y=170)
    entry_palabra.place(x=255, y=170, width=90)
    label_traduccion.place(x=177, y=200)
    entry_traduccion.place(x=255, y=200, width=90)

    # Guardar

    global boton_guardar

    boton_guardar["command"] = lambda: editar(valor, label_palabra, entry_palabra, label_traduccion, entry_traduccion, boton_guardar, ventana_editar, )
    boton_guardar.place(x=215, y=235)


def editar(valor, label_palabra, entry_palabra, label_traduccion, entry_traduccion, boton_guardar, ventana_editar):

    palabra = entry_palabra.get().strip().capitalize()
    traduccion = entry_traduccion.get().strip().capitalize()

    label_1 = Label(ventana_editar, font=("Comic sans Ms", 11))
    label_2 = Label(ventana_editar, font=("Comic sans Ms", 11))

    verificacion_palabra = verificar_palabras(palabra, label_1, x=350, y=170)
    verificacion_traduccion = verificar_palabras(traduccion, label_2, x=350, y=200)

    if verificacion_palabra and verificacion_traduccion:
        label_palabra.place_forget()
        entry_palabra.place_forget()
        label_traduccion.place_forget()
        entry_traduccion.place_forget()
        boton_guardar.place_forget()

        limpiar_input(entry_palabra, entry_traduccion)
    
    else:
        return None

    # Conectar con base de datos

    # Editar palabra

    query = '''SELECT * FROM palabras'''
    row = obtener_palabra(query, conn, valor)

    cursor = conn.cursor()

    query = f'''UPDATE palabras SET palabra='{palabra}', traduccion='{traduccion}' WHERE id={row[0]};'''
    cursor.execute(query)

    # organizar tabla base de datos

    query = '''SELECT * FROM palabras'''
    cursor.execute(query)
    lista_palabras = cursor.fetchall()

    lista_palabras.sort()

    for i in lista_palabras:

        query = f'''UPDATE palabras SET palabra='{i[1]}', traduccion='{i[2]}' WHERE id={i[0]};'''
        cursor.execute(query)


    print("Datos editados")


def borrar(valor, boton_borrar):

    query = '''SELECT * FROM palabras'''
    row = obtener_palabra(query, conn, valor)

    query = f'''DELETE FROM palabras WHERE id={row[0]};
    UPDATE palabras SET id=1000000 + nextval('palabras_id_seq');
    ALTER SEQUENCE palabras_id_seq RESTART WITH 1;
    UPDATE palabras SET id=nextval('palabras_id_seq');'''
    cursor = conn.cursor()
    cursor.execute(query)

    print("Datos borrados")

    boton_borrar.place_forget()


def guardar_palabras(entry_ingles, entry_traducir, ventana_agregar):

    # Obteniendo palabra de las entradas y verificando que no tengan caracteres especiales

    palabra = entry_ingles.get().strip().capitalize()
    traduccion = entry_traducir.get().strip().capitalize()

    # Creando labels para agregar datos y luego se verifican para ser agregados

    label_1 = Label(ventana_agregar, font=("Comic sans Ms", 11))
    label_2 = Label(ventana_agregar, font=("Comic sans Ms", 11))
    
    verificacion_palabra = verificar_palabras(palabra, label_1, x=430, y=85)
    verificacion_traducir = verificar_palabras(traduccion, label_2, x=430, y=115)

    if verificacion_palabra and verificacion_traducir:
        limpiar_input(entry_ingles, entry_traducir)
        palabra = palabra.capitalize()
        traduccion = traduccion.capitalize()
    else:
        return None

    # Estableciendo conección con la base de datos postgresql para agregar las palabras

    cursor = conn.cursor()
    query = '''INSERT INTO palabras(palabra, traduccion) VALUES (%s, %s)'''
    cursor.execute(query, (palabra, traduccion))
    print("Datos guardados")


def abrir_ventana_agregar():
    """Funcion que abre una nueva ventana para agregar palabras en ingles
       returns None"""

    ventana_agregar = Toplevel()
    ventana_agregar.title("Agregar palabras a base de datos")
    ventana_agregar.resizable(0, 0)

    canvas = Canvas(ventana_agregar, width=500, height=380)
    canvas.pack()

    estilo_label = font.Font(family="Bahnschrift", size=12)
    estilo_botones = font.Font(family="Bahnschrift", size=10)

    # Título

    label = Label(ventana_agregar, text="Agregar palabra", font=("Comic sans Ms", 20))
    label.place(x=150, y=20)

    # Entrada 1

    label = Label(ventana_agregar, text="Añade la palabra en ingles: ", font=estilo_label)
    label.place(x=70, y=90)

    entry_ingles = Entry(ventana_agregar)
    entry_ingles.place(x=300, y=90)

    # Entrada 2

    label = Label(ventana_agregar, text="Añade la traducción de la palabra: ", font=estilo_label)
    label.place(x=20, y=120)

    entry_traducir = Entry(ventana_agregar)
    entry_traducir.place(x=300, y=120)

    boton_1 = Button(ventana_agregar, text="Guardar", width=9, font=estilo_botones, command=lambda: (guardar_palabras(entry_ingles, entry_traducir, ventana_agregar)))
    boton_1.place(x=220, y=170)

    # Salir

    boton_salir = Button(ventana_agregar, text="Salir", command=ventana_agregar.destroy, width=9, font=estilo_botones)
    boton_salir.place(x=220, y=220)


def abrir_ventana_mostrar():
    """Funcion que abre una nueva ventana para mostrar palabras en ingles
       returns None"""

    ventana_mostrar = Toplevel()
    ventana_mostrar.resizable(0, 0)

    canvas = Canvas(ventana_mostrar, width=500, height=380)
    canvas.pack()

    estilo_label = font.Font(family="Bahnschrift", size=10)
    estilo_botones = font.Font(family="Bahnschrift", size=10)

    # Conectar con base de datos

    cursor = conn.cursor()
    query = '''SELECT * FROM palabras'''
    cursor.execute(query)

    # Extraer palabras de base de datos y mostrarla en un listbox

    row = cursor.fetchall()

    listbox = Listbox(ventana_mostrar, width=40, height=5)
    listbox.place(x= 130, y = 130)

    for x in row:
        listbox.insert(END, x)
        palabras_traducidas[x[1]] = x[2]

    # Título

    label = Label(ventana_mostrar, text="Lista palabras", font=("Comic sans Ms", 20))
    label.place(x=160, y=20)

    # Buscar palabras

    label = Label(ventana_mostrar, text="Buscar palabra:", font=estilo_label)
    label.place(x=130, y=90)

    entry_buscar = Entry(ventana_mostrar)
    entry_buscar.place(x=230, y=92, width=80)

    label_busqueda = Label(ventana_mostrar, font=("Bahnschrift", 10), anchor="center", width=40)
    label_busqueda.place(x=110, y=230)

    boton_buscar = Button(ventana_mostrar, text="Buscar", command=lambda: buscar_palabras(entry_buscar.get(), label_busqueda))
    boton_buscar.place(x=320, y=89)

    # Salir

    boton_salir = Button(ventana_mostrar, text="Salir", command=ventana_mostrar.destroy, width=9, font=estilo_botones)
    boton_salir.place(x=210, y=270)


def abrir_ventana_editar():

    ventana_editar = Toplevel()
    ventana_editar.resizable(0, 0)

    canvas = Canvas(ventana_editar, width=500, height=380)
    canvas.pack()

    estilo_label = font.Font(family="Bahnschrift", size=10)

    # Título 

    label = Label(ventana_editar, text="Editar palabras", font=("Comic sans Ms", 20))
    label.place(x=145, y=20)

    # Buscar palabras

    label = Label(ventana_editar, text="Escribir id o palabra: ", font=estilo_label)
    label.place(x=95, y=90)

    entry_mostrar = Entry(ventana_editar)
    entry_mostrar.place(x=230, y=92, width=90)

    label_mostrar = Label(ventana_editar, font=("Bahnschrift", 10), anchor="center", width=40)
    label_mostrar.place(x=100, y=130)

    boton_salir = Button(ventana_editar, text="Salir", command=ventana_editar.destroy, width=9, font=estilo_botones)
    boton_salir.place(x=210, y=270)

    # Mostrar y borrar palabras

        # Agregar palabra en ingles

    global label_palabra, entry_palabra, label_traduccion, entry_traduccion, boton_guardar

    label_palabra = Label(ventana_editar, text="Nueva palabra: ", font=("Bahnschrift", 10))
    entry_palabra = Entry(ventana_editar)

        # Agregar traducción de palabra

    label_traduccion = Label(ventana_editar, text="Traducción: ", font=("Bahnschrift", 10))
    entry_traduccion = Entry(ventana_editar)

        # Guardar edicion

    boton_guardar = Button(ventana_editar, text="Guardar") 
    boton_editar = Button(ventana_editar, text="Editar", width=7)

    boton_mostrar = Button(ventana_editar, text="Mostrar", command=lambda: validar_palabras(entry_mostrar, label_mostrar, boton_editar, "editar", ventana_editar))
    boton_mostrar.place(x=335, y=89)



def abrir_ventana_borrar():

    ventana_borrar = Toplevel()
    ventana_borrar.resizable(0, 0)

    canvas = Canvas(ventana_borrar, width=500, height=380)
    canvas.pack()

    estilo_label = font.Font(family="Bahnschrift", size=10)

    # Título 

    label = Label(ventana_borrar, text="Borrar palabras", font=("Comic sans Ms", 20))
    label.place(x=145, y=20)

    # Buscar palabras

    label = Label(ventana_borrar, text="Escribir id o palabra: ", font=estilo_label)
    label.place(x=100, y=90)

    entry_mostrar = Entry(ventana_borrar)
    entry_mostrar.place(x=230, y=92, width=90)

    label_mostrar = Label(ventana_borrar, font=("Bahnschrift", 10), anchor="center", width=40)
    label_mostrar.place(x=100, y=130)

    # Mostrar y borrar palabras

    boton_borrar = Button(ventana_borrar, text="Borrar", width=7)

    boton_mostrar = Button(ventana_borrar, text="Mostrar", command=lambda: validar_palabras(entry_mostrar, label_mostrar, boton_borrar, "borrar", ventana_borrar))
    boton_mostrar.place(x=330, y=89)

    # Salir

    boton_salir = Button(ventana_borrar, text="Salir", width=9, command=lambda: ventana_borrar.destroy())
    boton_salir.place(x=207, y=170)


def run():


    root = Tk()
    root.title("Palabras de ingles")
    root.resizable(0, 0)

    # Canvas principal

    canvas = Canvas(root, height=380, width=490)
    canvas.pack()

    # Título principal

    estilo_label = font.Font(family="Bahnschrift", size=12)
    global estilo_botones
    estilo_botones = font.Font(family="Bahnschrift", size=10)

    label = Label(text="Inicio", font=("Comic sans Ms", 20))
    label.place(x=220, y=20)

    # Entrada 1

    label = Label(root, text="Mostrar palabras agregadas: ", font=estilo_label)
    label.place(x=66, y=80)

    boton_mostrar = Button(root, text="Mostrar", width= 9, font=estilo_botones, command=lambda: abrir_ventana_mostrar())
    boton_mostrar.place(x=296, y= 78)

    # Entrada 2

    label = Label(root, text="Anadir nueva palabra: ", font=estilo_label)
    label.place(x=117, y=120)

    boton_agregar = Button(root, text="Agregar", command=abrir_ventana_agregar, font=estilo_botones, width=9)
    boton_agregar.place(x=295, y= 118)

    # Entrada 3

    label = Label(root, text="Editar palabras agregadas: ", font=estilo_label)
    label.place(x=77, y=160)

    boton_editar = Button(root, text="Editar", width= 9, font=estilo_botones, command=lambda: abrir_ventana_editar())
    boton_editar.place(x=296, y= 158)

    # Entrada 4

    label = Label(root, text="Borrar palabras agregadas: ", font=estilo_label)
    label.place(x=72, y=200)

    boton_borrar = Button(root, text="Borrar", width= 9, command=abrir_ventana_borrar, font=estilo_botones)
    boton_borrar.place(x=296, y= 198)

    # Entrada 5

    label = Label(root, text="Iniciar test: ", font=estilo_label)
    label.place(x=195, y=240)

    boton_test = Button(root, text="Iniciar", width= 9, font=estilo_botones, command=lambda: (root.destroy(), iniciar_test()))
    boton_test.place(x=296, y= 238)

    # Salida

    boton_salir = Button(root, text="Salir", command=root.destroy, width=6, font=estilo_botones)
    boton_salir.place(x=220, y=300)

    root.mainloop()

if __name__ == "__main__":
    run()
    conn.commit()
    conn.close()