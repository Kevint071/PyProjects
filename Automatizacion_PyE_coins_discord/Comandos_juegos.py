from Herramientas_pagina import esperar_obtener_elemento, esperar_obtener_elementos
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from colorama import Fore, Style
from time import sleep, time
from random import randint, sample
from lxml import html
from Globals import variables_globales
from winsound import Beep
import unicodedata


def jugar_slot(coins):
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]")
    text_box.click()
    sleep(0.5)
    text_box.send_keys(f"!slots {coins}")
    sleep(2)
    text_box.send_keys(f"{Keys.ENTER}")
    sleep(randint(3, 5))


def normalizar_texto(texto):
    return ''.join(letra for letra in unicodedata.normalize('NFD', texto) if unicodedata.category(letra) != 'Mn').lower()


def obtener_nombres_usuario():
    perfil_usuario = esperar_obtener_elemento(Driver, By.XPATH, "//div[2]/div/div/div/div/div[1]/section/div[2]/div[1]/div[2]")
    perfil_usuario.click()

    contenedor_nombres_usuario = esperar_obtener_elemento(Driver, By.XPATH, '//div/div/div/div/div/div/div[3]/div[1]/div/div/div/div[1]/div[h2]', 5)

    nombre = esperar_obtener_elemento(contenedor_nombres_usuario, By.TAG_NAME, 'h2').text
    nombre_usuario = esperar_obtener_elemento(contenedor_nombres_usuario, By.XPATH, './/div/span').text
    nombre, nombre_usuario = normalizar_texto(nombre), normalizar_texto(nombre_usuario)

    print(f"Nombre: {nombre}")
    print(f"Nombre usuario: {nombre_usuario}")

    return nombre, nombre_usuario


def detector_de_llamada(texto: str, nombre: str, nombre_usuario: str):
    texto_normalizado = normalizar_texto(texto)

    if texto_normalizado.count(nombre) or texto_normalizado.count(nombre_usuario):
         print(f"Posible llamada: {texto_normalizado}")
         return True
    else:
        palabras = texto_normalizado.split(" ")
        secciones_texto = [palabra[i:i+3] for palabra in palabras for i in range(len(palabra)-2) if len(palabra[i:i+3]) == 3]
        
        for seccion_texto in secciones_texto:
            if nombre.count(seccion_texto) or nombre_usuario.count(seccion_texto):
                print(f"Posible llamada: {seccion_texto}")
                return True


def sonar_alerta():
    while True:
        Beep(3500, 500)
        sleep(0.5)


def proteccion_antibot(nombre: str, nombre_usuario: str, cantidad_jugadas_activar_antibot: int):
    mensajes_chat = esperar_obtener_elementos(Driver, By.XPATH, '//*[@class="markup_a7e664 messageContent_abea64"][child::*]')
    mensajes_chat = mensajes_chat[-cantidad_jugadas_activar_antibot:][::-1]

    for mensaje in mensajes_chat:
        spans = esperar_obtener_elementos(mensaje, By.TAG_NAME, 'span')
        spans = [span.text for span in spans]

        for span in spans:
            llamada = detector_de_llamada(span, nombre, nombre_usuario)
            sonar_alerta() if llamada else None 


def obtener_jugada_slot(jugadas_realizadas, nombre_usuario):
    mensajes_tragamonedas = esperar_obtener_elementos(Driver, By.XPATH, "//article/div/div[.//span[contains(., 'Tragamonedas')]]")
    mensajes_tragamonedas = mensajes_tragamonedas[::-1]

    for mensaje in mensajes_tragamonedas:
        try:
            cuerpo_html = mensaje.get_attribute("innerHTML")
            arbol = html.fromstring(cuerpo_html)

            jugada = arbol.xpath(".//div[2][.//span[contains(., 'Tragamonedas')]]/span[contains(., 'Has')]/text()")
            jugada = jugada.pop().strip("\n ")

            dinero_jugada = arbol.xpath(".//div[2][.//span[contains(., 'Tragamonedas')]]/strong/span/text()")
            dinero_jugada = int(dinero_jugada.pop().strip())

            nombre_user_mensaje = arbol.xpath(".//div[1][.//span[contains(@class, 'embedAuthorName')]]/span/text()")
            nombre_user_mensaje = nombre_user_mensaje.pop().strip("#0")

            if nombre_usuario == nombre_user_mensaje:
                print(Fore.LIGHTCYAN_EX + f"{jugadas_realizadas}. " + Style.RESET_ALL + (Fore.LIGHTGREEN_EX if "ganado" in jugada else Fore.LIGHTRED_EX) + f"{jugada} {dinero_jugada} PyE coins" + Style.RESET_ALL)
                break
        except Exception as e:
            print(f"Error por {e}")
            
    return jugada, int(dinero_jugada)


def consultar_dinero():
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]")
    text_box.click()
    sleep(0.5)
    text_box.send_keys("!bal")
    sleep(1)
    text_box.send_keys(f"{Keys.ENTER}")
    sleep(randint(1, 4))
    print(Fore.LIGHTGREEN_EX + "Consulta de dinero exitosa...\n" + Style.RESET_ALL)


def guardar_todo_dinero():
    print("Guardando todo el dinero...")
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]")
    text_box.click()
    sleep(0.5)
    text_box.send_keys(f"!dep all")
    sleep(1.5)
    text_box.send_keys(f"{Keys.ENTER}")
    print("Dinero guardado\n")


def estrategia_slots(jugadas_realizadas, coins, nombre, nombre_usuario):
    tiempo_inicio_operacion = time()
    cantidad_jugadas_activar_antibot = 5

    if jugadas_realizadas >= cantidad_jugadas_activar_antibot:
        proteccion_antibot(nombre, nombre_usuario, cantidad_jugadas_activar_antibot)

    jugar_slot(coins)
    jugada, dinero_jugada = obtener_jugada_slot(jugadas_realizadas, nombre_usuario)

    if "perdido" in jugada:
        variables_globales["jugadas_perdidas"] += 1
        dinero_jugada -= dinero_jugada * 2
    elif "ganado" in jugada:
        variables_globales["jugadas_ganadas"] += 1
        variables_globales["jugadas_ganadas_temporales"] += 1

    tiempo_fin_operacion = time()

    print(Fore.YELLOW + f"Tiempo de jugada: {round(tiempo_fin_operacion - tiempo_inicio_operacion, 2)} segundos" + Style.RESET_ALL)
    return dinero_jugada


def ejecutar_funciones_aleatorias(*funciones):
    indices = sample(range(len(funciones)), len(funciones))
    for numero_funcion in indices:
        funciones[numero_funcion]()


def obtener_dinero(balance):
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]")
    text_box.click()
    sleep(0.2)
    text_box.send_keys(f"!wd {balance}")
    sleep(3)
    text_box.send_keys(f"{Keys.ENTER}")
    print(Fore.LIGHTCYAN_EX + f"{balance} PyE coins obtenidas para jugar\n" + Style.RESET_ALL)


def agregar_driver():
    global Driver
    Driver = variables_globales["Driver"]