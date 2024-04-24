from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Herramientas_pagina import esperar_obtener_elemento, esperar_obtener_elementos
from time import sleep, time
from Globals import variables_globales


def obtener_dinero(balance):
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]")
    text_box.click()
    sleep(0.5)
    text_box.send_keys(f"!wd {balance}")
    text_box.send_keys(f"{Keys.ENTER}")
    sleep(3)


def jugar_ruleta(coins, color):
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]")
    text_box.click()
    sleep(0.2)
    text_box.send_keys(f"!ruleta {coins} {color}")
    sleep(0.3)
    text_box.send_keys(f"{Keys.ENTER}")
    sleep(2.5)


def obtener_jugada_slot(numero_slot):
    jugada = esperar_obtener_elementos(Driver, By.XPATH, "//article/div/div/div[2][.//span[contains(., 'Tragamonedas')]]/span[contains(., 'Has')]")[-1].text
    dinero_jugada = esperar_obtener_elementos(Driver, By.XPATH, "//article/div/div/div[2][.//span[contains(., 'Tragamonedas')]]/strong/span")[-1].text

    print(f"{numero_slot}. {jugada} {dinero_jugada} PyE coins")
    return jugada, int(dinero_jugada)


def guardar_dinero(dinero_a_guardar):
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]")
    text_box.click()
    sleep(0.5)
    text_box.send_keys(f"!dep {dinero_a_guardar}")
    text_box.send_keys(f"{Keys.ENTER}")
    sleep(1)


def iniciar_automatizacion_ruleta():
    global Driver
    Driver = variables_globales["Driver"]

    balance = 4000
    balance_temporal = 4000
    obtener_dinero(balance)

    coins = 500
    tiempo_inicio = time()
    ganancia_total = 0

    for numero_ruleta in range(1, 21):
        for i in range(1, 9):
            color = "red" if i <= 4 else "black"
            jugar_ruleta(coins, color)

        balance_temporal += int((coins * 8 * 1.35) - (coins * 8))
        ganancia_total += int((coins * 8 * 1.35) - (coins * 8))
        print(f"Jugadas realizadas: {numero_ruleta}")
        print(f"Balance actual {balance_temporal}\n")
        print(f"Ganancia total: {ganancia_total}")

        sleep(5.8)

        if numero_ruleta == 10 and balance_temporal <= 7500:
            dinero_a_guardar = balance_temporal - 4000
            ganancia_total += dinero_a_guardar

        if balance_temporal >= 7500:
            print(f"\nBalance temporal: {balance_temporal}\n")
            dinero_a_guardar = balance_temporal - 4000
            print("Dinero a guardar:", dinero_a_guardar)
            
            guardar_dinero(dinero_a_guardar)
            balance_temporal = 4000

        print("\nRetomando jugada\n")

    tiempo_fin = time()

    print(f"\nGanancia total: {ganancia_total}")
    print(f"Duracion de ejecución: {(tiempo_fin - tiempo_inicio) / 60} minutos")