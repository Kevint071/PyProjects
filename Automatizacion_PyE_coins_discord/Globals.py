from typing import Optional
from selenium import webdriver


variables_globales = {
    "Driver": Optional[webdriver.Chrome],
    "jugadas_ganadas": int(),
    "jugadas_perdidas": int(),
    "jugadas_ganadas_temporales": int(),
}
