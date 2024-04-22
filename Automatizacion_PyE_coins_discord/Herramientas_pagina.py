from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Driver = None

def ejecutar_navegador(url):
    options = Options()
    options.add_argument("--log-level=3")
    # path_chrome = r"C:\Users\andre\Downloads\chrome-win64\chrome-win64\chrome.exe"
    # options.binary_location = path_chrome
    # options.add_experimental_option("detach", True)

    global Driver
    Driver = webdriver.Chrome(options=options)
    Driver.maximize_window()

    Driver.get(url)
    return Driver 


# def ejecutar_navegador_headless(url):
#     chdir(path.dirname(path.abspath(__file__)))
#     options = Options()
#     options.add_argument("--log-level=3")
#     # options.add_argument("--headless")
#     # options.add_argument("--disable-gpu")

#     Driver_new = webdriver.Chrome(options=options)
#     Driver_new.get("https://discord.com")

#     cookies = load(open("cookies.pkl", "rb"))
#     for cookie in cookies:
#         Driver_new.add_cookie(cookie)
        
#     Driver_new.get(url)
#     print("Ejecucion lista")
#     sleep(100)
#     return Driver_new


def esperar_obtener_elemento(locator, by_arg, valor_arg, time=3):
    """
    Espera hasta que un elemento esté presente en la página.
    Paráms: locator (WebDriver): La instancia del navegador. by_arg (By): El método de búsqueda del elemento. valor_arg (str): El valor a buscar. time (int): El tiempo máximo de espera en segundos.
    Returns: WebElement: El elemento encontrado.
    """
    WebDriverWait(locator, time).until(EC.presence_of_element_located((by_arg, valor_arg)))
    element = Driver.find_element(by=by_arg, value=valor_arg)
    return element


def esperar_obtener_elementos(locator, by_arg, valor_arg, time=3):
    """
    Espera hasta que un elemento esté presente en la página.
    Paráms: locator (WebDriver): La instancia del navegador. by_arg (By): El método de búsqueda del elemento. valor_arg (str): El valor a buscar. time (int): El tiempo máximo de espera en segundos.
    Returns: WebElement: El elemento encontrado.
    """
    WebDriverWait(locator, time).until(EC.presence_of_all_elements_located((by_arg, valor_arg)))
    elements = Driver.find_elements(by=by_arg, value=valor_arg)
    return elements


def obtener_driver():
    return Driver


# def obtener_cookies():
#     chdir(path.dirname(path.abspath(__file__)))
#     print("Probando a obtener cookies")
#     cookies = Driver.get_cookies()
#     dump(cookies, open("cookies.pkl", "wb"))
#     print("Cookies obtenidas")
