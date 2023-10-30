import requests
from time import sleep
import webbrowser 
import pyautogui as pyto
from os import name, system
from Api_key import api_key


def limpiar_pantalla():
    if name == "posix":
        system("clear")
    elif name == "nt" or name == "dos" or name == "ce":
        system("cls")


def obtenerPalabra():
  url = "https://random-word-api.p.rapidapi.com/get_word"

  headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "random-word-api.p.rapidapi.com"
  }

  response = requests.get(url, headers=headers)
  word = response.json()["word"]
  return word


def elegir_navegador():
  url_navegadores = {
    "1": "https://www.bing.com",
    "2": "https://www.google.es/",
    "3": "https://search.brave.com/",
    "4": "https://duckduckgo.com/",
    "5": "https://search.yahoo.com/"
  }

  navegador = input("""Digite el navegador para hacer las búsquedas: 

  1. Bing
  2. Google
  3. Brave
  4. Duck Duck Go
  5. Yahoo

  Elija un navegador escirbiendo su número en la lista: """)

  return url_navegadores[navegador]


def abrir_navegador(url):
  webbrowser.open(url)
  sleep(3)


def hacer_busqueda():
  word = obtenerPalabra()
  pyto.write(word)
  sleep(0.5)
  pyto.press("enter")
  sleep(4)
  pyto.hotkey("ctrl", "w")
  sleep(1)
  return word


def run():
  limpiar_pantalla()
  url = elegir_navegador()
  cantidad_busquedas = int(input("\nDigite el número de busquedas que quiere hacer: "))
  abrir_navegador(url)
  limpiar_pantalla()
  print(f"Total de busquedas a realizar: {cantidad_busquedas}\n")

  # Comenzar busquedas

  [(abrir_navegador(url), print(f"Busqueda {i+1}: {hacer_busqueda()}")) for i in range(cantidad_busquedas)]
  

if __name__ == "__main__":
  run()