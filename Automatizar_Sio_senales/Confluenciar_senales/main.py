from os import path, walk, makedirs
from datetime import datetime
from sys import path as pth
root = path.dirname(path.dirname(path.abspath(__file__)))
pth.append(root)

from Directorio import obtener_directorio


def obtener_senales_de_archivos(archivo, raiz, lineas):
    if archivo.endswith('.txt'):
        ruta_archivo = path.join(raiz, archivo)
        print(ruta_archivo)
        with open(ruta_archivo, 'r') as f:
            lineas_archivo = f.readlines()
            if len(lineas_archivo) > 1:
                lineas_archivo = list(map(lambda x: x.replace("\n", ""), lineas_archivo))
                lineas.extend(lineas_archivo)


def contar_y_clasificar_lineas(cant_veces, lista_unica_cant_veces, linea, lineas_M5, lineas_M15, lineas_unicas_filtradas, lista_cant_veces):
    if cant_veces not in lista_unica_cant_veces:
            lista_unica_cant_veces.append(cant_veces)
    if cant_veces > 1:
        if linea.split(";")[0] == "M5":
            lineas_M5.append(linea)
        elif linea.split(";")[0] == "M15":
            lineas_M15.append(linea)
        print(f"La linea {linea} se repite {cant_veces} {'veces' if cant_veces > 1 else 'vez'}")
        lineas_unicas_filtradas.append(linea)
    lista_cant_veces.append(cant_veces)
    sorted(lista_unica_cant_veces)


def obtener_cantidad_repeticiones(lineas):
    lista_cant_veces = []
    lista_unica_cant_veces = []
    lineas_unicas = tuple(set(lineas))
    lineas_unicas_filtradas = []
    lineas_M5 = []
    lineas_M15 = []
    lineas_unicas = sorted(lineas_unicas, key=lambda x: datetime.strptime(x.split(';')[2], "%H:%M"))

    for linea in lineas_unicas:
        cant_veces = lineas.count(linea)
        contar_y_clasificar_lineas(cant_veces, lista_unica_cant_veces, lineas, lineas_M5, lineas_M15, lineas_unicas_filtradas, lista_cant_veces)

    for i in lista_unica_cant_veces:
        print(f"Las señales de {i} veces repetidas son: {lista_cant_veces.count(i)}")

    return lineas_M5, lineas_M15, lineas_unicas_filtradas


def run():
    directorio = obtener_directorio()
    if directorio == None:
        return None
    
    directorio_filtro_backtest = path.join(directorio, "Filtro_backtest")
    lineas = []

    for raiz, dirs, archivos in walk(directorio_filtro_backtest):
        for archivo in archivos:
            obtener_senales_de_archivos(archivo, raiz, lineas)
            
    lineas_M5, lineas_M15, lineas_todas = obtener_cantidad_repeticiones(lineas)
    directorio_confluencia = path.join(directorio, "Confluencia_senales")
    makedirs(directorio_confluencia, exist_ok=True)

    rutas_archivos = (path.join(directorio_confluencia, "Senales_M5.txt"), path.join(directorio_confluencia, "Senales_M15.txt"), path.join(directorio_confluencia, "Senales.txt"))
    lineas_senales = "\n".join(lineas_M5), "\n".join(lineas_M15), "\n".join(lineas_todas)

    for ruta_archivo, linea_senal in zip(rutas_archivos, lineas_senales):
        with open(ruta_archivo, "w") as f:
            f.write(linea_senal)


if __name__ == "__main__":
    run()