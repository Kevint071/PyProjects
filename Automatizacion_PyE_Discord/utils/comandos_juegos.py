from playwright.sync_api import Page
from .buscador_elementos import BuscadorElementos

class ComandosJuegos:
    def __init__(self, page: Page):
        self.page = page
        self.buscador = BuscadorElementos()
        self.input_text = self.buscador.obtener_elemento(self.page, '//div[contains(@class, "textArea") and contains(@class, "slateContainer")]//div[@role="textbox"]', 30000)

    def obtener_dinero(self, coins: int):
        print("Obteniendo dinero...")
        self.input_text.fill(f"!wd {coins}")
        self.page.wait_for_timeout(2000)
        self.input_text.press("Enter")
        self.page.wait_for_timeout(2000)
        print(f"El dinero obtenido es de {coins}...\n")
    
    def consultar_dinero(self):
        print("Consultando balance...")
        self.input_text.fill(f"!bal")
        self.page.wait_for_timeout(1000)
        self.input_text.press("Enter")
        self.page.wait_for_timeout(1000)
        print("Balance consultado...\n")
    
    def jugar_slot(self, coins: int):
        self.input_text.fill(f"!slots {coins}")
        self.page.wait_for_timeout(1000)
        self.input_text.press("Enter")
        self.page.wait_for_timeout(2000)
