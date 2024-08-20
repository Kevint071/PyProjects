from playwright.sync_api import sync_playwright, Playwright, Page
from pages import LoginPage, CasinoPage
from gui.gui_main import ejecutar_gui
from globals import variables_globales
import config


def iniciar_sesion(page: Page):
    print("Iniciando sesión...")
    login_page_instance = LoginPage(page)
    login_page_instance.goto()
    login_page_instance.agregar_email(config.EMAIL)
    login_page_instance.agregar_contraseña(config.PASSWORD)
    login_page_instance.enviar_formulario()


def ejecutar_juego(page: Page):
    nombre_juego = variables_globales["juego"]
    casino_page_instance = CasinoPage(page)
    print("Entrando a la pagina del casino...")
    casino_page_instance.goto()

    if nombre_juego == "Slots":
        print("Iniciando Juego Slots...\n")
        casino_page_instance.iniciar_juego_slots()
    elif nombre_juego == "Ruleta":
        casino_page_instance.iniciar_juego_ruleta()


def run(playwright: Playwright):
    browser = playwright.chromium.launch(**config.BROWSER_OPTIONS)
    page = browser.new_page(no_viewport=True)
    
    iniciar_sesion(page)
    ejecutar_juego(page)
    
    browser.close()


if __name__ == "__main__":
    ejecutar_gui()

    with sync_playwright() as playwright:
        run(playwright)