from Interfaz_espera import ventana_confirmacion
from Herramientas_pagina import ejecutar_navegador
from Automatizacion_slots import iniciar_automatizacion_slot, guardar_todo_dinero
from Interfaz_eleccion_juego import ventana_eleccion_juego
from Automatizacion_ruleta import iniciar_automatizacion_ruleta
from time import sleep


def conteo_inicio():
    print("\nIniciando automatización en     ", end="", flush=True)
    for i in range(3, 0, -1):
        print("\b" * 4 + f"{i}...", end="", flush=True)
        sleep(1)
    print("\nComenzando automatización...")


def run():
    url = "https://discord.com/channels/768278151435386900/973425187301261393"
    ejecutar_navegador(url)

    ventana_confirmacion()
    juego = ventana_eleccion_juego()

    conteo_inicio()

    if juego == "Slot":
        try:
            iniciar_automatizacion_slot()
        except KeyboardInterrupt:
            guardar_todo_dinero()
    elif juego == "Ruleta":
        iniciar_automatizacion_ruleta()


if __name__ == "__main__":
    run()