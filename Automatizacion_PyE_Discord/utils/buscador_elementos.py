from playwright.sync_api import Page, expect

class BuscadorElementos:
    def obtener_elemento(self, locator_elemento: Page, elemento_buscar: str, timeout: float = 10000):
        locator_elemento.wait_for_selector(elemento_buscar, timeout=timeout)
        elemento = locator_elemento.locator(elemento_buscar)        
        expect(elemento).to_be_enabled(timeout=timeout)
        expect(elemento).to_be_visible(timeout=timeout)
        return elemento

    def obtener_elementos(self, locator_elemento: Page, elemento_buscar: str, timeout: float = 10000):
        locator_elemento.wait_for_selector(elemento_buscar, timeout=timeout)
        elementos = locator_elemento.locator(elemento_buscar).all()
        return elementos
