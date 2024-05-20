from typing import Optional
from selenium import webdriver


variables_globales = {
    "Driver": Optional[webdriver.Chrome],
    "jugadas_ganadas": int(),
    "jugadas_perdidas": int(),
    "jugadas_ganadas_temporales": int(),
    "detener_sonido": False,
    "palabras_ignorar": ["!slots", "!bal", "!wd", "!dep"],
    "contadores_palabras": {},
}
