from os import chdir, listdir, mkdir, path
from shutil import move
from tkinter import filedialog
from tkinter import *


def elegir_directorio():
    root = Tk()
    root.withdraw()
    return filedialog.askdirectory()


def filtrar_carpetas_archivos(directorio):
    ext_ignorar = [".ini"]
    lista_directorio = listdir(directorio)

    def filtrar_extension(nombre: str):
        if path.isfile(nombre):
            return not nombre.endswith(tuple(ext_ignorar))

    return list(filter(filtrar_extension, lista_directorio))


def run():
    directorio = elegir_directorio()

    chdir(directorio)
    lista_archivos = filtrar_carpetas_archivos(directorio)
    print(lista_archivos)

    for archivo in lista_archivos:
        nombre, extension = path.splitext(archivo)
        carpeta = f"Archivos_{extension[1:]}"
        ruta_carpeta = path.join(directorio, carpeta)

        if not path.exists(ruta_carpeta):
            try:
                print(f"Creando carpeta {extension}...")
                mkdir(ruta_carpeta)
                print(f"Carpeta {extension} creada...")
            except:
                print("\nNo se pudo crear la carpeta...")

        ruta_origen = path.join(directorio, archivo)
        ruta_destino = path.join(ruta_carpeta, archivo)
        move(ruta_origen, ruta_destino)


if __name__ == "__main__":
    run()
