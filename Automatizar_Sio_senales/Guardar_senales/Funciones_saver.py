from os import path, chdir
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import UnexpectedAlertPresentException
from time import sleep

# Agregar a ejecutar_navegador() si no se quiere mostrar el navegador
# options = Options()
# options.headless = True
# options.add_argument("--log-level=3")
# driver = webdriver.Chrome(options=options)

# Si se quiere ver la pantalla del navegador simplemente en la variable driver pege el codigo:
# driver = webdriver.Chrome()

def ejecutar_navegador():
    """Encuentra la ruta del webdriver, abre una ventana y navega a una URL específica."""

    # Encontrar ruta de el webdriver y abrir una ventana
    chdir(path.dirname(path.dirname(path.abspath(__file__))))
    options = Options()
    options.headless = True
    options.add_argument("--log-level=3")
    
    global driver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Definir la ruta a abrir y abrirla
    url = "https://siofiltrosinais.com/cataloger"
    driver.get(url)
    sleep(1)

    is_headless = options.headless
    return is_headless


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


def retroceder_a_catalogador(): 
    """Retrocede al catalogador en la página."""
    try:
        retroceder = esperar_elemento(driver, By.XPATH, '//*[@id="screenshot"]/div/a', 3)
        print("Volviendo al catalogador...\n")
        retroceder.click()
    except:
        print("No se pudo retroceder...\n")


def cerrar_anuncio():
    """Cierra el anuncio principal en la página."""
    # Cerrar anuncio principal
    try:
        div = esperar_elemento(driver, By.XPATH, "//div[@onclick='closeModal()']", 3)
        print("Cerrando anuncio...\n")
        div.click()
    except:
        print("No se encontró el anuncio\n")


def elegir_idioma():
    """Permite al usuario elegir el idioma de la página."""
    idiomas = ["English", "Español", "Português"]

    for indice, idioma in enumerate(idiomas, start=1):
        print(f"{indice}. {idioma}")

    while True:
        try:
            eleccion = int(input("\nElige el idioma para la página: "))
            idioma = idiomas[eleccion - 1]
            if eleccion > 0 and eleccion <= 3:
                break
        except:
            print("Opción inválida.")

    # Cambiando idioma

    try:
        select_languaje = esperar_elemento(driver, By.XPATH, f"//option[text()='{idioma}']", 3)
        print("\nCambiando idioma...\n")
        select_languaje.click()
    except:
        print("Error al cambiar el idioma... El idioma no fue encontrado no hay problemas de conexión...\n")


def seleccionar_mercado(mercados):
    """Permite al usuario seleccionar el mercado en la página."""
    # Seleccionando dropdown de mercados

    try:
        select_dropdown = esperar_elemento(driver, By.XPATH, '//div[contains(@class, "css-19bb58m") and input/@id="react-select-2-input"]', 3)
        select_dropdown.click()
    except:
        print("Error seleccionar los pares...")
    sleep(0.1)

    for mercado in mercados:
        try:
            opcion_mercado = esperar_elemento(driver, By.XPATH, f"//*[text()='{mercado}']", 3)
            opcion_mercado.click()
        except:
            print(f"Error al seleccionar la opción {mercado}...")
    select_dropdown.click()


def obtener_inputs():
    """Obtiene los elementos de entrada en la página."""
    # Obteniendo elementos input
    try:
        global elementos_input
        elementos_input = esperar_elementos(driver, By.XPATH, "//input[contains(@class,'bg-[#222f3e]')]", 3)
    except:
        print("Error al obtener inputs\n")


def agregar_efectividad(num):
    """
    Agrega un porcentaje de efectividad en la página.
    Paráms: num (int): El porcentaje de efectividad a agregar.
    """
    # Clickeando el input de porcentaje de efectividad

    try:
        input_efectividad = elementos_input[0]
        input_efectividad.click()
    except:
        print("Error al clickear el input de efectividad...\n")


def agregar_direccion_op():
    """Agrega una dirección en la página."""
    # Desplegando el Dropdown de las direcciones
    try:
        dropdown_direccion = esperar_elemento(driver, By.XPATH, "//div[4]/div/select", 3)
        dropdown_direccion.click()
    except:
        print("Error al desplegar el dropdown\n")

    # Agregando direccion call y put
    
    try:
        option_call_put = esperar_elemento(driver, By.XPATH, "//div[4]/div/select/option[3]", 3)
        option_call_put.click()
    except:
        print("Error al agregar la dirección\n")


def agregar_timeframe(timeframe):
    """
    Agrega un marco de tiempo en la página.
    Paráms: timeframe (str): El marco de tiempo a agregar.
    """
    # Desplegando el Dropdown de los timeframe
    try:
        dropdown_timeframe = esperar_elemento(driver, By.XPATH, "//div[5]/div/select", 3)
        dropdown_timeframe.click()
    except:
        print("Error al desplegar el dropdown\n")

    # Agregando timeframe
    
    try:
        option_timeframe = esperar_elemento(driver, By.XPATH, f"//div[4]/div[5]/div/select/option[@value='{timeframe}']", 3)
        option_timeframe.click()
    except:
        print("Error al agregar el timeframe\n")


def agregar_dia(dia):
    """
    Agrega un día en el input de la página.
    Paráms: dia (int): El día a agregar.
    """
    # Agregando los dias de efectividad
    try:
        input_dia = elementos_input[1]
        input_dia.click()
        sleep(0.1)
        input_dia.clear()
        sleep(0.1)
    except:
        print('No se pudo agregar el dia...\n')


def filtrar_noticias():
    """Filtra las noticias en la página."""
    # Presionando el input de filtrar noticias
    try:
        input_filtrar = esperar_elemento(driver, By.ID, "filter", 3)
        input_filtrar.click()
    except:
        print("No se pudo seleccional el input de filtrar noticias...\n")


def iniciar_catalogacion():
    """Inicia la catalogación en la página."""
    # Se preciona el boton iniciar
    try:
        boton_iniciar = esperar_elemento(driver, By.XPATH, "//div[9]/button", 3)
        print("Iniciando catalogación...")
        boton_iniciar.click()
    except Exception as e:
        print(f"Hubo un error de {e}\n")


def obtener_senales():
    """
    Obtiene las señales de la página.
    Returns: str: Las señales obtenidas. None: Si el textarea está vacío. False: Si ocurre un error.
    """
    # Obtener las señales que estan en el textarea
    try:
        textarea = esperar_elemento(driver, By.TAG_NAME, "textarea", 180)
        print("Obteniendo señales...")
        senales = textarea.get_attribute("value")
        if senales == "":
            print("No hay señales en esta catalogación...")
            return None
        return senales
    except UnexpectedAlertPresentException:
        print("Error, alert ha aparecido...")
        driver.refresh()
        return False
