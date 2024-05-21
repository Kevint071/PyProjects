from Herramientas_navegador import esperar_obtener_elemento, esperar_obtener_elementos
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from colorama import Fore, Style
from time import sleep
from random import randint, sample
from lxml import html
from Globals import variables_globales
from winsound import Beep
import unicodedata
from threading import Thread


def jugar_slot(coins: int):
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]", 10)
    text_box.click()
    sleep(0.4)
    text_box.send_keys(f"!slots {coins}")
    sleep(2)
    text_box.send_keys(f"{Keys.ENTER}")
    sleep(randint(1, 2))


def normalizar_texto(texto: str):
    return ''.join(letra for letra in unicodedata.normalize('NFD', texto) if unicodedata.category(letra) != 'Mn').lower()


def obtener_nombres_usuario():
    perfil_usuario = esperar_obtener_elemento(Driver, By.XPATH, "//div[2]/div/div/div/div/div[1]/section/div[2]/div[1]/div[2]", 10)
    perfil_usuario.click()

    contenedor_nombres_usuario = esperar_obtener_elemento(Driver, By.XPATH, '//div/div/div/div/div/div/div[3]/div[1]/div/div/div/div[1]/div[h2]', 10)

    nombre = esperar_obtener_elemento(contenedor_nombres_usuario, By.TAG_NAME, 'h2', 10).text
    nombre_usuario = esperar_obtener_elemento(contenedor_nombres_usuario, By.XPATH, './/div/span', 10).text
    nombre, nombre_usuario = normalizar_texto(nombre), normalizar_texto(nombre_usuario)

    print(f"Nombre: {nombre}")
    print(f"Nombre usuario: {nombre_usuario}")

    return nombre, nombre_usuario


def detector_de_llamada(texto: str, autor: str, nombre: str, nombre_usuario: str):
    texto_normalizado = normalizar_texto(texto)

    if texto_normalizado.count(nombre) or texto_normalizado.count(nombre_usuario):
         print(f"Posible llamada: {texto_normalizado} de {autor}")
         return True
    else:
        palabras = texto_normalizado.split(" ")
        secciones_texto = [palabra[i:i+3] for palabra in palabras for i in range(len(palabra)-2) if len(palabra[i:i+3]) == 3]

        for seccion_texto in secciones_texto:
            if nombre.count(seccion_texto) or nombre_usuario.count(seccion_texto):
                print(f"Posible llamada: {texto_normalizado} de {autor}")
                variables_globales["palabras_ignorar"].append(seccion_texto)
                variables_globales["contadores_palabras"][seccion_texto] = 0

                return True


def reproducir_sonido():
    while True:
        Beep(3500, 500)
        sleep(0.5)
        if variables_globales["detener_sonido"]:
            variables_globales["detener_sonido"] = False
            break


def ejecutar_alerta():
    hilo_sonido = Thread(target=lambda: reproducir_sonido())
    hilo_sonido.start()

    continuar = input("Presione Enter para continuar o ingrese 'q' para salir: ")
    
    if continuar.lower() == 'q':
        variables_globales["detener_sonido"] = True
        hilo_sonido.join()
        return False
    variables_globales["detener_sonido"] = True
    hilo_sonido.join()
    return True


def proteccion_antibot(nombre: str, nombre_usuario: str, cantidad_jugadas_activar_antibot: int, jugadas_realizadas: int):
    spans_mensajes_chat = esperar_obtener_elementos(Driver, By.XPATH, '//*[@class="markup_a7e664 messageContent_abea64"][child::*]', 10)
    spans_autor_mensaje = esperar_obtener_elementos(Driver, By.XPATH, '//*[@class="markup_a7e664 messageContent_abea64"][child::*]/preceding-sibling::*[1]/span[1]/span[1]', 10)

    spans_mensajes_chat = spans_mensajes_chat[-cantidad_jugadas_activar_antibot:][::-1]
    spans_autor_mensaje = spans_autor_mensaje[-cantidad_jugadas_activar_antibot:][::-1]

    mensajes_chat = [[span.text for span in esperar_obtener_elementos(mensaje, By.TAG_NAME, 'span', 10)] for mensaje in spans_mensajes_chat]
    autores_mensajes = [autor.text for autor in spans_autor_mensaje]

    # autores_y_mensajes = {}

    # for autor, mensajes in zip(autores_mensajes, mensajes_chat):
    #     mensajes_unicos = set(mensajes)  # Convertir la lista de mensajes en un conjunto para eliminar duplicados
        
    #     if autor in autores_y_mensajes:
    #         autores_y_mensajes[autor].extend(mensajes_unicos - set(autores_y_mensajes[autor]))
    #     else:
    #         autores_y_mensajes[autor] = list(mensajes_unicos)
    
    continuar_juego = True
    palabras_ignorar = variables_globales["palabras_ignorar"]

    for autor, mensaje in zip(autores_mensajes, mensajes_chat):
        for texto in mensaje:
            if any(palabra_ignorar in texto for palabra_ignorar in palabras_ignorar):
                continue
            print(texto)
            llamada = detector_de_llamada(texto, autor, nombre, nombre_usuario)
            continuar_juego = ejecutar_alerta() if llamada else True
    
    return continuar_juego


def obtener_elementos_jugada_slot(arbol):
    jugada = arbol.xpath(".//div[2][.//span[contains(., 'Tragamonedas')]]/span[contains(., 'Has')]/text()")
    jugada = jugada.pop().strip("\n ")

    dinero_jugada = arbol.xpath(".//div[2][.//span[contains(., 'Tragamonedas')]]/strong/span/text()")
    dinero_jugada = int(dinero_jugada.pop().strip())

    nombre_user_mensaje = arbol.xpath(".//div[1][.//span[contains(@class, 'embedAuthorName')]]/span/text()")
    nombre_user_mensaje = nombre_user_mensaje.pop().strip("#0")

    return jugada, dinero_jugada, nombre_user_mensaje


def obtener_jugada_slot(jugadas_realizadas: int, nombre_usuario: str):
    mensajes_tragamonedas = esperar_obtener_elementos(Driver, By.XPATH, "//article/div/div[.//span[contains(., 'Tragamonedas')]]", 10)
    mensajes_tragamonedas = mensajes_tragamonedas[::-1]

    for mensaje in mensajes_tragamonedas:
        try:
            cuerpo_html = mensaje.get_attribute("innerHTML")
            arbol = html.fromstring(cuerpo_html)

            jugada, dinero_jugada, nombre_user_mensaje = obtener_elementos_jugada_slot(arbol)

            if nombre_usuario == nombre_user_mensaje:
                print(Fore.LIGHTCYAN_EX + f"{jugadas_realizadas}. " + Style.RESET_ALL + (Fore.LIGHTGREEN_EX if "ganado" in jugada else Fore.LIGHTRED_EX) + f"{jugada} {dinero_jugada} PyE coins" + Style.RESET_ALL)
                break
        except Exception as e:
            print(f"Error por {e}")
            
    return jugada, int(dinero_jugada)


def consultar_dinero():
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]", 10)
    text_box.click()
    sleep(0.5)
    text_box.send_keys("!bal")
    sleep(1)
    text_box.send_keys(f"{Keys.ENTER}")
    sleep(randint(1, 4))
    print(Fore.LIGHTGREEN_EX + "Consulta de dinero exitosa...\n" + Style.RESET_ALL)


def guardar_todo_dinero():
    print("Guardando todo el dinero...")
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]", 10)
    text_box.click()
    sleep(0.5)
    text_box.send_keys(f"!dep all")
    sleep(1.5)
    text_box.send_keys(f"{Keys.ENTER}")
    print("Dinero guardado\n")


def procesar_resultado_jugada(jugada, dinero_jugada):
    if "perdido" in jugada:
        variables_globales["jugadas_perdidas"] += 1
        dinero_jugada = -abs(dinero_jugada)
    elif "ganado" in jugada:
        variables_globales["jugadas_ganadas"] += 1
        variables_globales["jugadas_ganadas_temporales"] += 1
    return dinero_jugada


def eliminacion_palabras_ignoradas():
    limite_jugadas_ignorar_palabras = 7
    
    if variables_globales["contadores_palabras"]:
        palabras_a_eliminar = []
        for palabra, contador in variables_globales["contadores_palabras"].items():
            variables_globales["contadores_palabras"][palabra] += 1
            if variables_globales["contadores_palabras"][palabra] >= limite_jugadas_ignorar_palabras:
                palabras_a_eliminar.append(palabra)

        if palabras_a_eliminar:
            for palabra in palabras_a_eliminar:
                variables_globales["palabras_ignorar"].remove(palabra)
                del variables_globales["contadores_palabras"][palabra]


def estrategia_slots(jugadas_realizadas: int, coins: int, nombre: str, nombre_usuario: str):
    cantidad_jugadas_activar_antibot = 5

    if jugadas_realizadas >= cantidad_jugadas_activar_antibot:
        if not proteccion_antibot(nombre, nombre_usuario, cantidad_jugadas_activar_antibot, jugadas_realizadas):
            return False

    jugar_slot(coins)
    jugada, dinero_jugada = obtener_jugada_slot(jugadas_realizadas, nombre_usuario)
    dinero_jugada = procesar_resultado_jugada(jugada, dinero_jugada)

    eliminacion_palabras_ignoradas()
    
    return dinero_jugada


def ejecutar_funciones_aleatorias(*funciones):
    indices = sample(range(len(funciones)), len(funciones))
    for numero_funcion in indices:
        funciones[numero_funcion]()


def obtener_dinero(balance: int):
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]", 10)
    text_box.click()
    sleep(0.2)
    text_box.send_keys(f"!wd {balance}")
    sleep(3)
    text_box.send_keys(f"{Keys.ENTER}")
    print(Fore.LIGHTCYAN_EX + f"{balance} PyE coins obtenidas para jugar\n" + Style.RESET_ALL)


def agregar_driver():
    global Driver
    Driver = variables_globales["Driver"]