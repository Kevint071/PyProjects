from .buscador_elementos import BuscadorElementos
from playwright.sync_api import Page
from globals import variables_globales
from .helpers import colorear_texto
from time import time
import re

class PageInteractions:
    def __init__(self, page: Page):
        self.page = page
        self.buscador = BuscadorElementos()
    
    def imprimir_avance_juego(self, numero_jugada, jugada, dinero_jugada):
        print(colorear_texto(f"{numero_jugada}. {jugada} {dinero_jugada}", "VERDE_CLARO")) if jugada == "Has ganado" else print(colorear_texto(f"{numero_jugada}. {jugada} {dinero_jugada}", "ROJO_CLARO"))
        print(f"Jugadas ganadas: {variables_globales['jugadas_ganadas']}")
        print(f"Jugadas perdidas: {variables_globales['jugadas_perdidas']}")
        print(f"Balance: {variables_globales['dinero_ganado'] - variables_globales['dinero_perdido']}\n")

    def actualizar_partidas(self, jugada, dinero_jugada):
        if jugada == "Has ganado":
            variables_globales["jugadas_ganadas"] += 1
            variables_globales["dinero_ganado"] += dinero_jugada
        elif jugada == "Has perdido":
            variables_globales["jugadas_perdidas"] += 1
            variables_globales["dinero_perdido"] += dinero_jugada
        
    def obtener_jugada_slot(self, RESULTADOS_POSIBLES, numero_jugada):
        tiempo_inicio = time()
        mensajes_tragamonedas = self.buscador.obtener_elementos(self.page, "//article/div/div[.//span[contains(., 'Tragamonedas')]]")
        contenido_ultima_tragamoneda = mensajes_tragamonedas[-1].inner_html()

        patron = "|".join(RESULTADOS_POSIBLES)
        resultado_juego = re.findall(patron, contenido_ultima_tragamoneda)

        jugada, dinero_jugada = (resultado_juego[0], int(resultado_juego[1])) if resultado_juego else (None, None)
        self.actualizar_partidas(jugada, dinero_jugada)
        self.imprimir_avance_juego(numero_jugada, jugada, dinero_jugada)

        tiempo_fin = time()
        print(f"Tiempo obtencion jugada interna: {(tiempo_fin - tiempo_inicio):.2f}")