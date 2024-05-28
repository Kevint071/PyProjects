from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, time
from Globals import variables_globales, Driver
from Comandos_juegos import obtener_dinero, guardar_todo_dinero, consultar_dinero, jugar_ruleta
from Funciones_juegos import obtener_nombres_usuario, ejecutar_funciones_aleatorias, estrategia_juegos


def obtener_jugada_ruleta(numero_ruleta):
  pass


def iniciar_automatizacion_ruleta():
    balance = 4000
    balance_temporal = 4000

    nombre, nombre_usuario = obtener_nombres_usuario()
    ejecutar_funciones_aleatorias(consultar_dinero, lambda: obtener_dinero(balance))

    coins = 500
    tiempo_inicio = time()
    ganancia_total = 0

    for numero_ruleta in range(1, 21):
        for i in range(1, 9):
            color = "red" if i <= 4 else "black"
            jugar_ruleta(coins, color)
            # estrategia_juegos("ruleta", numero_ruleta, coins, nombre, nombre_usuario, color)

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
            
            guardar_todo_dinero(dinero_a_guardar)
            balance_temporal = 4000

        print("\nRetomando jugada\n")

    tiempo_fin = time()

    print(f"\nGanancia total: {ganancia_total}")
    print(f"Duracion de ejecución: {(tiempo_fin - tiempo_inicio) / 60} minutos")