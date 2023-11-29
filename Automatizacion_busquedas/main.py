import requests
from time import sleep
import webbrowser 
import pyautogui as pyto
from os import name, system, getenv
from dotenv import load_dotenv
from colorama import Fore, Style, init

load_dotenv()
init()


def limpiar_pantalla():
    if name == "posix":
        system("clear")
    elif name == "nt" or name == "dos" or name == "ce":
        system("cls")


def obtenerPalabra():
  url = "https://random-word-api.p.rapidapi.com/get_word"

  headers = {
    "X-RapidAPI-Key": getenv("API_KEY"),
    "X-RapidAPI-Host": "random-word-api.p.rapidapi.com"
  }

  response = requests.get(url, headers=headers)
  word = response.json()["word"]
  return word
 

def elegir_navegador():
  url_navegadores = {
    "1": ("https://www.bing.com/search?q=", "&qs=n&form=QBRE&setlang=es"),
    "2": ("https://www.google.es/search?q=", "&source=web"),
    "3": ("https://search.brave.com/search?q=", ""),
    "4": ("https://duckduckgo.com/?q=", "&t=h_&ia=web"),
    "5": ("https://search.yahoo.com/search?p=", "")
  }

  navegador = input("""Digite el navegador para hacer las búsquedas: 

  1. Bing
  2. Google
  3. Brave
  4. Duck Duck Go
  5. Yahoo

  Elija un navegador escirbiendo su número en la lista: """)

  return url_navegadores[navegador]


def cerrar_pagina():
   pyto.hotkey("ctrl", "w")


def hacer_busqueda(datos_url, buscar_apalabra = False):
  if buscar_apalabra:
    word = obtenerPalabra()
    webbrowser.open(datos_url[0] + word + datos_url[1])
    return word
  else:
    webbrowser.open(datos_url)


def run():
  limpiar_pantalla()
  print(Fore.LIGHTCYAN_EX + "ABRE PRIMERO EL NAVEGADOR WEB PREDETERMINADO ANTES DE EJECUTAR EL PROGRAMA, LUEGO REGRESA PARA CONTINUAR".center(110, "*"), end="\n\n" + Style.RESET_ALL)
  datos_url = elegir_navegador()
  cantidad_busquedas = int(input("\nDigite el número de busquedas que quiere hacer: "))
  hacer_busqueda(datos_url[0])
  limpiar_pantalla()
  print(f"Total de busquedas a realizar: {cantidad_busquedas}\n")

  # Comenzar busquedas

  [(print(f"Busqueda {i}: {hacer_busqueda(datos_url, True)}"), sleep(8.5), cerrar_pagina()) for i in range(1, cantidad_busquedas+1)]
  

if __name__ == "__main__":
  run()