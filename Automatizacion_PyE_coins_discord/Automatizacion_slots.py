from Comandos_juegos import agregar_driver, consultar_dinero, obtener_nombres_usuario, ejecutar_funciones_aleatorias, obtener_dinero, guardar_todo_dinero, estrategia_slots
from time import time, sleep
from random import randint, sample
from math import ceil
from colorama import init, Fore, Style
from Globals import variables_globales


init()


def iniciar_automatizacion_slot():
    agregar_driver()
    porcentaje_jugadas_ganadas = 0.7

    balance, balance_temporal = 3000, 3000
    nombre, nombre_usuario = obtener_nombres_usuario()
    ejecutar_funciones_aleatorias(consultar_dinero, lambda: obtener_dinero(balance))

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
        dinero_jugada = estrategia_slots(numero_slot, coins, nombre, nombre_usuario)
        balance_temporal += dinero_jugada

        jugadas_ganadas = variables_globales["jugadas_ganadas"]
        jugadas_perdidas = variables_globales["jugadas_perdidas"]
        jugadas_ganadas_temporales = variables_globales["jugadas_ganadas_temporales"]

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
                variables_globales["jugadas_ganadas_temporales"] = 0
                print(f"Jugadas necesarias para la consulta del balance: {añadir_jugadas_revision_balance}\n")

        elif jugadas_perdidas >= revision_balance_perdidas:
            consultar_dinero()
            revision_balance_perdidas += randint(3, 8)
            
        print("-" * 40)
        print(f"Próxima consulta en {revision_balance - (jugadas_ganadas + jugadas_perdidas)} jugadas")
        print(f"Próxima consulta en {revision_balance_perdidas - jugadas_perdidas} jugadas perdidas")
        print((f"Próxima guardada en {jugadas_ganadas_requeridas_guardar - jugadas_ganadas_temporales} jugadas ganadas") if jugadas_ganadas_requeridas_guardar - jugadas_ganadas_temporales > 0 else f"Próxima guardada en {revision_balance - (jugadas_ganadas + jugadas_perdidas)} jugadas")
        
        print("-" * 40 + "\n")
    
    if revision_balance_perdidas - jugadas_perdidas != 0:
        consultar_dinero()
    guardar_todo_dinero()

    tiempo_fin = time()

    print(f"\nGanancia total: {sum(ganancia_total)}")
    print(f"Ganancia promedio: {sum(ganancia_total)/len(ganancia_total)}")
    print(f"Duracion de ejecución: {int((tiempo_fin - tiempo_inicio) // 60)}:{round((tiempo_fin - tiempo_inicio) % 60)}")