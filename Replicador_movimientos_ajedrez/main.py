from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from time import sleep
from os import chdir, path
import sys
from colorama import init, Style, Fore


init()


def ejecutar_navegador():
    """Encuentra la ruta del webdriver, abre una ventana y navega a una URL específica."""

    chdir(path.dirname(path.dirname(path.abspath(__file__))))
    options = Options()
    options.headless = True
    options.add_argument("--log-level=3")
    
    global driver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Definir la ruta a abrir y abrirla
    url = "https://chess.com/es"
    driver.get(url)


def esperar_elemento(locator, by_arg, valor_arg, time=3):
    """
    Espera hasta que un elemento esté presente en la página.
    Paráms: locator (WebDriver): La instancia del navegador. by_arg (By): El método de búsqueda del elemento. valor_arg (str): El valor a buscar. time (int): El tiempo máximo de espera en segundos.
    Returns: WebElement: El elemento encontrado.
    """
    WebDriverWait(locator, time).until(EC.presence_of_element_located((by_arg, valor_arg)))
    element = driver.find_element(by=by_arg, value=valor_arg)
    return element


def esperar_elementos(locator, by_arg, valor_arg, time=3):
    """
    Espera hasta que un elemento esté presente en la página.
    Paráms: locator (WebDriver): La instancia del navegador. by_arg (By): El método de búsqueda del elemento. valor_arg (str): El valor a buscar. time (int): El tiempo máximo de espera en segundos.
    Returns: WebElement: El elemento encontrado.
    """
    WebDriverWait(locator, time).until(EC.presence_of_all_elements_located((by_arg, valor_arg)))
    elements = driver.find_elements(by=by_arg, value=valor_arg)
    return elements


def enlace_jugar():
    enlace_jugar = esperar_elemento(driver, By.XPATH, '//div[2]/div[2]/a')
    enlace_jugar.click()
    boton_comenzar = esperar_elemento(driver, By.XPATH, '//div/div[2]/div/div[2]/div/button')
    boton_comenzar.click()


def animacion_puntos(mensaje: list):
    for frame in mensaje:
        sys.stdout.write('\r' + frame)  # Escribe en la misma línea
        sys.stdout.flush()  # Fuerza la actualización de la salida
        sleep(0.5)


def verificacion_jugadas_blancas(cantidad_movimientos, contenedor_movimientos):
    while True:
        try:
            jugadas = esperar_elementos(contenedor_movimientos, By.CLASS_NAME, 'move')
            if len(jugadas) != cantidad_movimientos:
                print(Fore.LIGHTBLUE_EX + "\nJugada de las blancas hecha\n" + Style.RESET_ALL)
                return True
            else: 
                mensaje_blancas = [Fore.LIGHTYELLOW_EX + 'Las blancas no han jugado.  ', 'Las blancas no han jugado.. ', 'Las blancas no han jugado...' + Style.RESET_ALL]
                animacion_puntos(mensaje_blancas)
            
        except TimeoutException:
            print("Aún no hay jugadas")
        sleep(0.7)


def verificacion_jugadas_negras(contenedor_movimientos):
    while True:
        jugadas = esperar_elementos(contenedor_movimientos, By.CLASS_NAME, 'move')
        movimientos = jugadas[-1].text.strip().split('\n')[1:]
        if len(movimientos) < 2:        
            mensaje_negras = [Fore.LIGHTYELLOW_EX + 'Las negras no han jugado.  ', 'Las negras no han jugado.. ', 'Las negras no han jugado...' + Style.RESET_ALL]
            animacion_puntos(mensaje_negras)
        else:
            print(Fore.LIGHTCYAN_EX + "\nJugada de las negras hecha\n" + Style.RESET_ALL)
            return True


def verificacion_jugadas(contenedor_movimientos, cantidad_movimientos: int):
    jugadas = esperar_elementos(contenedor_movimientos, By.CLASS_NAME, 'move')

    if verificacion_jugadas_blancas(cantidad_movimientos, contenedor_movimientos) and verificacion_jugadas_negras(contenedor_movimientos):
        return True


def iniciar_sesion_chess():
    user = "Kevin_071"
    password = "Torrecilla.123"
    
    sleep(100)


def detectar_movimientos(cantidad_movimientos, veces_contenedor_encontrado):
    while True:
        try:
            contenedor_movimientos = esperar_elemento(driver, By.XPATH, '//*[@id="scroll-container"]/wc-vertical-move-list')
            if veces_contenedor_encontrado < 1: 
                print(Fore.LIGHTGREEN_EX + "Ya se encontró el contenedor de movimientos" + Style.RESET_ALL)
            break
        except TimeoutException:
            print(Fore.LIGHTRED_EX + "No se encuentra el contenedor de movimientos" + Style.RESET_ALL)
        
    return verificacion_jugadas(contenedor_movimientos, cantidad_movimientos)


def obtener_movimientos():
    contenedor_movimientos = esperar_elemento(driver, By.XPATH, '//*[@id="scroll-container"]/wc-vertical-move-list')
    jugada = esperar_elementos(contenedor_movimientos, By.CLASS_NAME, 'move')[-1]

    movimientos = jugada.text.strip().split("\n")[1:]
    movimiento_blancas = movimientos[0]
    movimiento_negras = movimientos[1]
            
    return (1, movimiento_blancas, movimiento_negras)


def run():
    ejecutar_navegador()
    enlace_jugar()

    cantidad_movimientos = 0
    veces_contenedor_encontrado = 0

    while True:
        if detectar_movimientos(cantidad_movimientos, veces_contenedor_encontrado):
            veces_contenedor_encontrado += 1
            movimientos, movimiento_blancas, movimiento_negras = obtener_movimientos()
            cantidad_movimientos += movimientos
            print(Fore.LIGHTGREEN_EX + f"Movimiento Blancas: {movimiento_blancas}" + Style.RESET_ALL)
            print(Fore.LIGHTGREEN_EX + f"Movimiento Negras: {movimiento_negras}\n" + Style.RESET_ALL)
    
    driver.quit()


if __name__ == "__main__":
    run()