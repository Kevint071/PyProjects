from playwright.sync_api import Page, expect
from utils import ComandosJuegos, BuscadorElementos
from games import JuegoSlots
from random import shuffle

class CasinoPage:
    def __init__ (self, page: Page):
        self.page = page
        self.buscador = BuscadorElementos()
    
    def goto(self):
        expect(self.page).to_have_url("https://discord.com/channels/@me", timeout=20000)
        self.page.goto("https://discord.com/channels/768278151435386900/973425187301261393")
    
    def consulta_y_gestion_dinero(self, coins: int):
        self.comandos_juegos = ComandosJuegos(self.page)
        operaciones = [self.comandos_juegos.consultar_dinero, lambda: self.comandos_juegos.obtener_dinero(coins)]
        shuffle(operaciones)
        
        for operacion in operaciones:
            operacion()
    
    def iniciar_juego_slots(self):
        modo_juego_slots = JuegoSlots(self.page)
        self.consulta_y_gestion_dinero(3000)
        modo_juego_slots.estrategia_juego_slots()
        
    
    def iniciar_juego_ruleta(self):
        pass

