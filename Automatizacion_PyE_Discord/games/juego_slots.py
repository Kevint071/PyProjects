from playwright.sync_api import Page
from utils import ComandosJuegos, PageInteractions, colorear_texto
from random import randrange, randint
from time import time


class JuegoSlots:

    APUESTA_1 = 300
    APUESTA_2 = 299

    GANANCIA_1 = 810
    PERDIDA_1 = 300

    GANANCIA_2 = 806
    PERDIDA_2 = 299

    MIN_JUGADAS = 80
    MAX_JUGADAS = 111

    RESULTADOS_POSIBLES = ["Has perdido", "Has ganado", str(GANANCIA_1), str(PERDIDA_1), str(GANANCIA_2), str(PERDIDA_2)]

    def __init__(self, page: Page):
        self.page = page
        self.comandos_juegos = ComandosJuegos(self.page)
        self.page_interactions = PageInteractions(self.page)

    def _obtener_apuesta(self, numero_jugada):
        return self.APUESTA_1 if numero_jugada % 2 else self.APUESTA_2

    def _obtener_proximas_jugadas_consulta(self):
        return randint(3, 7)

    def _realizar_jugada(self, numero_jugada, apuesta):
        inicio_juego = time()

        self.comandos_juegos.jugar_slot(apuesta)
        self.page_interactions.obtener_jugada_slot(self.RESULTADOS_POSIBLES, numero_jugada)
        
        self.page.wait_for_timeout(3000)

        fin_juego = time()
        
        print(f"Jugada del slot: {(fin_juego - inicio_juego):.2f}\n")

    def _consultar_dinero(self, numero_jugada, jugadas_proxima_consulta):
        if numero_jugada == jugadas_proxima_consulta:
            self.comandos_juegos.consultar_dinero()
            jugadas_proxima_consulta += self._obtener_proximas_jugadas_consulta()

        jugadas_restantes = jugadas_proxima_consulta - numero_jugada
        print(f"Faltan {jugadas_restantes} jugadas para la próxima consulta")

        return jugadas_proxima_consulta

    def estrategia_juego_slots(self):
        jugadas_proxima_consulta = self._obtener_proximas_jugadas_consulta()
        print(f"Se necesitan {jugadas_proxima_consulta} jugadas para la primera consulta del balance...\n")

        for numero_jugada in range(1, randrange(self.MIN_JUGADAS, self.MAX_JUGADAS)):
            apuesta = self._obtener_apuesta(numero_jugada)
            self._realizar_jugada(numero_jugada, apuesta)
            jugadas_proxima_consulta = self._consultar_dinero(numero_jugada, jugadas_proxima_consulta)