from playwright.sync_api import Page
from utils import BuscadorElementos
from time import sleep

class LoginPage:
    def __init__ (self, page: Page):
        self.page = page
        self.buscador = BuscadorElementos()
    
    def goto(self):
        self.page.goto("https://discord.com/login")

    def agregar_email(self, email: str):
        email_input = self.buscador.obtener_elemento(self.page, "#uid_7")
        email_input.fill(email)
    
    def agregar_contraseña(self, contraseña: str):
        password_input = self.buscador.obtener_elemento(self.page, "#uid_9")
        password_input.fill(contraseña)
    
    def enviar_formulario(self):
        boton_submit = self.buscador.obtener_elemento(self.page, "//form/div[2]/div/div[1]/div[2]/button[2]")
        boton_submit.click()

    