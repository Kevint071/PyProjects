from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Globals import variables_globales


def ejecutar_navegador(url):
    options = Options()
    options.add_argument("--log-level=3")

    global Driver
    Driver = webdriver.Chrome(options=options)
    Driver.maximize_window()
    Driver.get(url)
    
    variables_globales["Driver"] = Driver


def esperar_obtener_elemento(locator: webdriver.Chrome, by_arg, valor_arg, time=3):
    """
    Espera hasta que un elemento esté presente en la página.
    Paráms: locator (WebDriver): La instancia del navegador. by_arg (By): El método de búsqueda del elemento. valor_arg (str): El valor a buscar. time (int): El tiempo máximo de espera en segundos.
    Returns: WebElement: El elemento encontrado.
    """
    WebDriverWait(locator, time).until(EC.presence_of_element_located((by_arg, valor_arg)))
    element = locator.find_element(by=by_arg, value=valor_arg)
    return element


def esperar_obtener_elementos(locator: webdriver.Chrome, by_arg, valor_arg, time=3):
    """
    Espera hasta que un elemento esté presente en la página.
    Paráms: locator (WebDriver): La instancia del navegador. by_arg (By): El método de búsqueda del elemento. valor_arg (str): El valor a buscar. time (int): El tiempo máximo de espera en segundos.
    Returns: WebElement: El elemento encontrado.
    """
    WebDriverWait(locator, time).until(EC.presence_of_all_elements_located((by_arg, valor_arg)))
    elements = locator.find_elements(by=by_arg, value=valor_arg)
    return elements
