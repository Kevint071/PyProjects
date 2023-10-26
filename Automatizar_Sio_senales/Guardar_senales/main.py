from os import makedirs, path
from Saver import obtener_guardar_senales
import sys
from colorama import Fore, Style, init

init()

root = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(root)

from Directorio import obtener_directorio


def main():
    directorio = obtener_directorio()
    if directorio == None:
        return None

    print("Ruta de la carpeta seleccionada:", directorio)
    makedirs(directorio, exist_ok=True)

    obtener_guardar_senales(directorio)
    print(Fore.LIGHTYELLOW_EX + "\nDescarga de señales finalizada exitosamente..." + Style.RESET_ALL)


if __name__ == "__main__":
    main()
