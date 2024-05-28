from Herramientas_navegador import esperar_obtener_elemento
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from colorama import Fore, Style
from time import sleep
from random import randint
from Globals import Driver


def jugar_slot(coins: int):
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]", 10)
    text_box.click()
    sleep(0.4)
    text_box.send_keys(f"!slots {coins}")
    sleep(2)
    text_box.send_keys(f"{Keys.ENTER}")
    sleep(randint(1, 2))


def jugar_ruleta(coins: int, color: str):
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]", 10)
    text_box.click()
    sleep(0.4)
    text_box.send_keys(f"!ruleta {coins} {color}")
    sleep(0.5)
    text_box.send_keys(f"{Keys.ENTER}")
    sleep(2.5)


def consultar_dinero():
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]", 10)
    text_box.click()
    sleep(0.5)
    text_box.send_keys("!bal")
    sleep(1)
    text_box.send_keys(f"{Keys.ENTER}")
    sleep(randint(1, 4))
    print(Fore.LIGHTGREEN_EX + "Consulta de dinero exitosa...\n" + Style.RESET_ALL)


def guardar_todo_dinero():
    print("Guardando todo el dinero...")
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]", 10)
    text_box.click()
    sleep(0.5)
    text_box.send_keys(f"!dep all")
    sleep(1.5)
    text_box.send_keys(f"{Keys.ENTER}")
    print("Dinero guardado\n")


def obtener_dinero(balance: int):
    text_box = esperar_obtener_elemento(Driver, By.XPATH, "//form/div/div/div/div[3]/div/div[2]", 10)
    text_box.click()
    sleep(0.2)
    text_box.send_keys(f"!wd {balance}")
    sleep(3)
    text_box.send_keys(f"{Keys.ENTER}")
    print(Fore.LIGHTCYAN_EX + f"{balance} PyE coins obtenidas para jugar\n" + Style.RESET_ALL)