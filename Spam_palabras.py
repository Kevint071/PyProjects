import pyautogui as pyto
from time import sleep
import keyboard
import requests
from time import time

url = "https://random-word-api.herokuapp.com/word?lang=es"

def obtener_palabra():
    inicio = time()
    response = requests.get(url)
    fin = time()
    print(fin - inicio)
    return response.json()[0]


def palabras():
    for _ in range(0, 300):
        pyto.write(f"{obtener_palabra()}")
        pyto.press("Enter")
        sleep(0.5)
    
        if keyboard.is_pressed('esc'):
            return True
            

def run():
    palabras()
    print("Programa terminado")


if __name__ == "__main__":
    sleep(5)
    run()