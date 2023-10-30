from os import chdir, path, listdir, name, system
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys
from time import sleep
from colorama import Fore, Style, init

init()
# from selenium.webdriver.chrome.options import Options

# Agregar a ejecutar_navegador() si no se quiere mostrar el navegador
# options = Options()
# options.headless = True
# options.add_argument("--log-level=3")
# driver = webdriver.Chrome(options=options)

def limpiar_pantalla():
    if name == "posix":
        system("clear")
    elif name == "nt" or name == "dos" or name == "ce":
        system("cls")


def ejecutar_navegador():

    options = Options()
    options.headless = True
    options.add_argument("--log-level=3")

    # Encontrar ruta de el webdriver y abrir una ventana
    chdir(path.dirname(path.dirname(path.abspath(__file__))))
    global driver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Definir la ruta a abrir y abrirla
    url = "https://siofiltrosinais.com/trend"
    driver.get(url)
    sleep(1)
    
    
def esperar_elemento(locator, by_arg, valor_arg, time=3):
    """
    Espera hasta que un elemento esté presente en la página.
    Paráms: locator (WebDriver): La instancia del navegador. by_arg (By): El método de búsqueda del elemento. valor_arg (str): El valor a buscar. time (int): El tiempo máximo de espera en segundos.
    Returns: WebElement: El elemento encontrado.
    """
    WebDriverWait(locator, time).until(EC.presence_of_element_located((by_arg, valor_arg)))
    element = driver.find_element(by=by_arg, value=valor_arg)
    return element


def obtener_timeframes(directorio_filtro_riesgo):
    chdir(directorio_filtro_riesgo)

    temporalidades = listdir(directorio_filtro_riesgo)
    timeframes = []

    for i in temporalidades:
        num = i.split("M")[1]
        timeframes.append(int(num))
    return timeframes


def obtener_senales_txt(directorio_filtro_riesgo):
   
    chdir(directorio_filtro_riesgo)
    temporalidades = listdir(directorio_filtro_riesgo)
    archivos_filtrar = {}
    archivos_unicos_lista = []

    print("Obteniendo señales...")

    for tiempo in temporalidades:
        directorio_temporalidades = path.join(directorio_filtro_riesgo, tiempo)
        archivos_por_dias = {}
        for dia in listdir(directorio_temporalidades):
            directorio_dias = path.join(directorio_temporalidades, dia)
            archivos = listdir(directorio_dias)
            archivos_unicos_for_dict = []
            num_senales_unicos = []
            for archivo in archivos:
                num_senales_archivo = archivo.split(".txt")[0].split("sen_")[1]
                if num_senales_archivo not in num_senales_unicos:
                    num_senales_unicos.append(num_senales_archivo)
                    archivos_unicos_for_dict.append(archivo)
                    archivos_unicos_lista.append(archivo)
            archivos_por_dias[dia] = archivos_unicos_for_dict
        archivos_filtrar[tiempo] = archivos_por_dias
    print("Señales obtenidas...\n")
    return archivos_filtrar, archivos_unicos_lista


def cerrar_anuncio():
    # Cerrar anuncio principal
    try:
        div = esperar_elemento(driver, By.XPATH, "//div[@onclick='closeModal()']", 3)
        print("Cerrando anuncio...\n")
        div.click()
    except:
        print(Fore.YELLOW + "No se encontró el anuncio\n" + Style.RESET_ALL)


def agregar_senales_textarea(senales):
    try:
        textarea = esperar_elemento(driver, By.TAG_NAME, "textarea", 3)
        textarea.click()
        print("Agregando señales...")
        sleep(0.1)
        driver.execute_script("arguments[0].value = arguments[1];", textarea, senales)
        sleep(0.1)
        textarea.click()
        textarea.send_keys(" ")
        textarea.send_keys(Keys.BACKSPACE)
        sleep(0.1)
    except:
        print("No se agregaron las señales...\n")


def agregar_periodo(ema):
  # Obteniendo elemento input
  try:
      input_periodo = esperar_elemento(driver, By.XPATH, "//input[contains(@class,'bg-[#222f3e]')]", 3)
      sleep(0.1)
      input_periodo.clear()
      sleep(0.1)
      input_periodo.send_keys(f"{ema}")
  except:
      print("Error al agregar el periodo\n")


def iniciar_filtrado():
    try:
        print("Calibrando configuraciones...")
        boton_iniciar = esperar_elemento(driver, By.XPATH, "//div[4]/button", 3)
        boton_iniciar.click()
        esperar_elemento(driver, By.XPATH, '//*[@id="root"]/div/div/span', 15)
       
        print("Iniciando proceso de filtracion con EMA...")
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"No se pudo iniciar el filtrado... debido a {e}\n" + Style.RESET_ALL)


def retroceder_a_filtrador():
    try:
        retroceder = esperar_elemento(driver, By.XPATH, '//div/a', 3)
        print("Volviendo al filtrador...")
        retroceder.click()
    except Exception as e:
        print(Fore.LIGHTRED_EX +  f"No se pudo retroceder por {e}...\n" + Style.RESET_ALL)


def obtener_senales_filtradas():
    try:
        sleep(4)
        textarea = esperar_elemento(driver, By.TAG_NAME, "textarea", 180)
        textarea.click()
        senales_filtradas = textarea.get_attribute("value")
        if senales_filtradas == "":
            print(Fore.LIGHTRED_EX + "No hay señales en esta catalogación..." + Style.RESET_ALL)
            return None
        else:
            print(Fore.LIGHTGREEN_EX + "Señales filtradas y obtenidas correctamente..." + Style.RESET_ALL)
            sleep(0.5)
            return senales_filtradas
        
    except UnexpectedAlertPresentException:
        print("Error, alert ha aparecido...")
        driver.refresh()
        return False