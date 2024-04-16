from os import chdir, path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def ejecutar_navegador(url):
    """Encuentra la ruta del webdriver, abre una ventana y navega a una URL específica."""

    chdir(path.dirname(path.dirname(path.abspath(__file__))))
    
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--headless")
    
    global Driver
    Driver = webdriver.Chrome(options=options)
    Driver.maximize_window()

    # Definir la ruta a abrir y abrirla
    
    Driver.get(url)
    return Driver


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


def obtener_enlaces_videos():
  contenedor_videos = esperar_obtener_elemento(Driver, By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-video-list-renderer/div[3]')

  info_videos = []
  videos = esperar_obtener_elementos(contenedor_videos, By.XPATH, '//*[@id="video-title"]', 6)
  print(f"Cantidad de videos: {len(videos)}")

  for video in videos:
     nombre = video.text
     enlace = video.get_attribute('href')
     info_videos.append((nombre, enlace))

  return tuple(info_videos)


def verificar_cantidad_videos():
  contenedor_videos = esperar_obtener_elemento(Driver, By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]')
  body = esperar_obtener_elemento(Driver, By.TAG_NAME, 'body')
  total_height = Driver.execute_script("return arguments[0].scrollHeight", contenedor_videos)

  while True:
    body.send_keys(Keys.END)
    total_height_nuevo = Driver.execute_script("return arguments[0].scrollHeight", contenedor_videos)

    # Verifica si has llegado al final de la página
    if total_height_nuevo <= total_height:
        body.send_keys(Keys.END)
        break
    else:
       total_height = total_height_nuevo