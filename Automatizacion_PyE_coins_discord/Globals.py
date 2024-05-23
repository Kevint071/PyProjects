from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def creacion_driver():
    options = Options()
    options.add_argument("--log-level=3")

    Driver = webdriver.Chrome(options=options)
    Driver.maximize_window()
    return Driver


Driver = creacion_driver()

variables_globales = {
    "jugadas_ganadas": int(),
    "jugadas_perdidas": int(),
    "jugadas_ganadas_temporales": int(),
    "detener_sonido": False,
    "palabras_ignorar": ["!slots", "!bal", "!wd", "!dep"],
    "contadores_palabras": {},
}
