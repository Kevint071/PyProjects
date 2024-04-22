from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Herramientas_pagina import esperar_obtener_elemento, esperar_obtener_elementos, obtener_driver
from time import sleep, time
from random import randint, sample
from math import ceil
from lxml import html
from colorama import init, Fore, Style

def jugar_slot(coins):
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]")
    text_box.click()
    sleep(0.3)
    text_box.send_keys(f"!slots {coins}")
    sleep(2)
    text_box.send_keys(f"{Keys.ENTER}")
    sleep(1.2)


def obtener_nombre_usuario():
    contenedor_nombre_user = esperar_obtener_elemento(Driver, By.XPATH, "//div[2]/div/div/div/div/div[1]/section/div[2]/div[1]/div[2]")
    contenedor_nombre_user.click()

    nombre_user = esperar_obtener_elemento(Driver, By.XPATH, "//div/div/div/div/div/div/div[3]/div[1]/div/div/div/div[1]/div/div/span", 4)
    print(f"Nombre usuario: {nombre_user.text}")

    return nombre_user.text


def obtener_jugada_slot(numero_slot, nombre_user):
    mensajes = esperar_obtener_elementos(Driver, By.XPATH, "//article/div/div[.//span[contains(., 'Tragamonedas')]]")
    mensajes = mensajes[::-1]

    for mensaje in mensajes:
        try:
            cuerpo_html = mensaje.get_attribute("innerHTML")
            arbol = html.fromstring(cuerpo_html)

            jugada = arbol.xpath(".//div[2][.//span[contains(., 'Tragamonedas')]]/span[contains(., 'Has')]/text()")
            jugada = jugada.pop().strip("\n ")

            dinero_jugada = arbol.xpath(".//div[2][.//span[contains(., 'Tragamonedas')]]/strong/span/text()")
            dinero_jugada = int(dinero_jugada.pop().strip())

            nombre_user_mensaje = arbol.xpath(".//div[1][.//span[contains(@class, 'embedAuthorName')]]/span/text()")
            nombre_user_mensaje = nombre_user_mensaje.pop().strip("#0")

            if nombre_user == nombre_user_mensaje:
                print(Fore.LIGHTCYAN_EX + f"{numero_slot}. " + Style.RESET_ALL + (Fore.LIGHTGREEN_EX if "ganado" in jugada else Fore.LIGHTRED_EX) + f"{jugada} {dinero_jugada} PyE coins" + Style.RESET_ALL)
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


def obtener_dinero(balance):
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]")
    text_box.click()
    sleep(0.2)
    text_box.send_keys(f"!wd {balance}")
    sleep(3)
    text_box.send_keys(f"{Keys.ENTER}")
    print(Fore.LIGHTCYAN_EX + f"{balance} PyE coins obtenidas para jugar\n" + Style.RESET_ALL)


def guardar_todo_dinero():
    print("Guardando todo el dinero...")
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]")
    text_box.click()
    sleep(0.5)
    text_box.send_keys(f"!dep all")
    sleep(1.5)
    text_box.send_keys(f"{Keys.ENTER}")
    print("Dinero guardado\n")


def estrategia_slots(numero_slot, coins, nombre_user):
    tiempo_inicio_operacion = time()
    sleep(randint(1, 3))
    jugar_slot(coins)
    sleep(1)
    jugada, dinero_jugada = obtener_jugada_slot(numero_slot, nombre_user)

    if "perdido" in jugada:
        global jugadas_perdidas
        jugadas_perdidas += 1
        dinero_jugada -= dinero_jugada * 2
    elif "ganado" in jugada:
        global jugadas_ganadas
        global jugadas_ganadas_temporales
        jugadas_ganadas += 1
        jugadas_ganadas_temporales += 1
    tiempo_fin_operacion = time()
    print(Fore.YELLOW + f"Tiempo de jugada: {round(tiempo_fin_operacion - tiempo_inicio_operacion, 2)} segundos" + Style.RESET_ALL)
    return dinero_jugada


def ejecutar_funciones_aleatorias(*funciones):
    indices = sample(range(len(funciones)), len(funciones))
    for numero_funcion in indices:
        funciones[numero_funcion]()


def iniciar_automatizacion_slot():
    global Driver
    global jugadas_ganadas
    global jugadas_perdidas
    global jugadas_ganadas_temporales

    Driver = obtener_driver()
    jugadas_ganadas = 0
    jugadas_perdidas = 0
    jugadas_ganadas_temporales = 0
    porcentaje_jugadas_ganadas = 0.7

    balance, balance_temporal = 3000, 3000
    ejecutar_funciones_aleatorias(consultar_dinero, lambda: obtener_dinero(balance))
    nombre_user = obtener_nombre_usuario()

    coins = 300
    revision_balance = randint(5, 14)
    revision_balance_perdidas = randint(5, 8)
    jugadas_ganadas_requeridas_guardar = int(ceil(revision_balance * 0.7))
    
    print(f"\nJugadas para la consulta del balance: {revision_balance}\n")
    tiempo_inicio = time()

    ganancia_total = []

    cantidad_jugadas = sample(range(81, 112, 10), 1)
    cantidad_jugadas = cantidad_jugadas.pop()

    for numero_slot in range(1, cantidad_jugadas):
        
        dinero_jugada = estrategia_slots(numero_slot, coins, nombre_user)
        balance_temporal += dinero_jugada

        print(f"\nBalance actual: " + (Fore.LIGHTGREEN_EX if balance_temporal > 3000 else (Fore.LIGHTRED_EX if balance_temporal < 3000 else Fore.LIGHTYELLOW_EX)) + f"{balance_temporal}" + Style.RESET_ALL)
        print(f"Dinero a guardar: " + (Fore.LIGHTGREEN_EX if dinero_jugada > 0 else Fore.LIGHTRED_EX) + f"{dinero_jugada}" + Style.RESET_ALL)

        if balance_temporal < coins:
            guardar_todo_dinero()
            obtener_dinero(balance)
            balance_temporal = 3000
            porcentaje_jugadas_ganadas = 0.7
            continue

        ganancia_total.append(dinero_jugada)
        ganancia_total_neta = sum(ganancia_total)
        tiempo_parcial = time()


        print(f"Ganacia total: " + (Fore.LIGHTGREEN_EX if ganancia_total_neta > 0 else (Fore.LIGHTRED_EX if ganancia_total_neta < 0 else Fore.LIGHTYELLOW_EX)) + f"{ganancia_total_neta}" + Style.RESET_ALL)
        print(f"Tiempo transcurrido: {round((tiempo_parcial - tiempo_inicio) / 60, 3)} minutos")
        print(f"Jugadas ganadas: " + Fore.LIGHTGREEN_EX + f"{jugadas_ganadas}" + Style.RESET_ALL)
        print(f"Jugadas perdidas: " + Fore.LIGHTRED_EX + f"{jugadas_perdidas}\n" + Style.RESET_ALL)
        

        if (jugadas_ganadas + jugadas_perdidas) == revision_balance:
                consultar_dinero()

                if jugadas_ganadas_temporales >= jugadas_ganadas_requeridas_guardar:
                    guardar_todo_dinero()
                    obtener_dinero(balance)
                    balance_temporal = 3000
                    porcentaje_jugadas_ganadas = 0.7
                else:
                    porcentaje_jugadas_ganadas -= 0.2

                añadir_jugadas_revision_balance = randint(5, 14)
                revision_balance += añadir_jugadas_revision_balance
                jugadas_ganadas_requeridas_guardar = int(ceil(añadir_jugadas_revision_balance * porcentaje_jugadas_ganadas))
                jugadas_ganadas_temporales = 0
                print(f"Jugadas necesarias para la consulta del balance: {añadir_jugadas_revision_balance}\n")

        elif jugadas_perdidas >= revision_balance_perdidas:
            consultar_dinero()
            revision_balance_perdidas += randint(3, 8)
            
        print("-" * 40)
        print(f"Próxima consulta en {revision_balance - (jugadas_ganadas + jugadas_perdidas)} jugadas")
        print(f"Próxima consulta en {revision_balance_perdidas - jugadas_perdidas} jugadas perdidas")
        print((f"Próxima guardada en {jugadas_ganadas_requeridas_guardar - jugadas_ganadas_temporales} jugadas ganadas") if jugadas_ganadas_requeridas_guardar - jugadas_ganadas_temporales > 0 else f"Próxima guardada en {revision_balance - (jugadas_ganadas + jugadas_perdidas)} jugadas")
        
        print("-" * 40 + "\n")
        # elif balance_temporal >= 10000:
        #     consultar_dinero()
        #     guardar_todo_dinero()
        #     obtener_dinero(balance)
        #     balance_temporal = 3000
    
    if revision_balance_perdidas - jugadas_perdidas != 0:
        consultar_dinero()
    guardar_todo_dinero()

    tiempo_fin = time()

    print(f"\nGanancia total: {sum(ganancia_total)}")
    print(f"Ganancia promedio: {sum(ganancia_total)/len(ganancia_total)}")
    print(f"Duracion de ejecución: {int((tiempo_fin - tiempo_inicio) // 60)}:{round((tiempo_fin - tiempo_inicio) % 60)}")