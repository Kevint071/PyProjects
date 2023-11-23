import requests
from requests.exceptions import RequestException
from colorama import Fore, Style, init
import sys

# Para que una clave sea correcta debe estar la letra la cantidad indicada en el rango
#Ejemplo de la respuesta de la peticion:

# 8-10 r: ozrcdfnug
#
# Aqui debe haber entre 8 y 10 letras 'r' pero solo hay 1 así que es falso

def ejecutar_peticion(url: str):
  try:
    response = requests.get(url)
    response.raise_for_status()
  except RequestException as err:
    print(f"Ocurrio un error al realizar la petición...")
    print(Fore.LIGHTRED_EX + f"Error: {err}" + Style.RESET_ALL)
    sys.exit(1)
  
  return response.text


def validar_codigo(codigo: list[str]):
  min, max = map(int, codigo[0].split("-"))
  letra = codigo[1].strip(":")
  texto = codigo[2]

  return max >= texto.count(letra) >= min

url = "https://codember.dev/data/encryption_policies.txt"
response_text = ejecutar_peticion(url)

codigos = response_text.split("\n")
codigos = [codigo.split(" ") for codigo in codigos]

validacion_codigos = [f"{indice + 1}. {codigo}" + Fore.LIGHTGREEN_EX + " Correcto" + Style.RESET_ALL if validar_codigo(codigo) else f"{indice + 1}. {codigo}" + Fore.LIGHTRED_EX + " Incorrecto" + Style.RESET_ALL for indice, codigo in enumerate(codigos)]

for codigo in validacion_codigos:
  print(codigo)


# Más ejemplos de la peticion

# 9-10 q: hvsazxrigf
# 1-9 j: bbqonxjt
# 6-8 e: pzqcywelwiogwt
# 4-7 t: vvxirpoid
# 2-3 n: fkrmnniuxeboq