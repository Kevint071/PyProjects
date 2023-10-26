from os import path, walk, makedirs
from datetime import datetime
from sys import path as pth
from operator import itemgetter
root = path.dirname(path.dirname(path.abspath(__file__)))
pth.append(root)

from Directorio import obtener_directorio


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
    for i in lista_unica_cant_veces:
        print(f"Las señales de {i} veces repetidas son: {lista_cant_veces.count(i)}")
        
    
    # repeticiones_ordenadas = sorted(repeticiones.items(), key=itemgetter(1))
    # print(repeticiones_ordenadas)
    # print(type(repeticiones_ordenadas))

    # for linea, cantidad in repeticiones_ordenadas:
    #     print(f"{cantidad}. {linea}")

    return lineas_M5, lineas_M15, lineas_unicas_filtradas


def run():
    directorio = obtener_directorio()
    if directorio == None:
        return None
    
    directorio_filtro_backtest = path.join(directorio, "Filtro_backtest")
    lineas = []

    for raiz, dirs, archivos in walk(directorio_filtro_backtest):
        for archivo in archivos:
            if archivo.endswith('.txt'):
                ruta_archivo = path.join(raiz, archivo)
                print(ruta_archivo)
                with open(ruta_archivo, 'r') as f:
                    lineas_archivo = f.readlines()
                    if len(lineas_archivo) > 1:
                        lineas_archivo = list(map(lambda x: x.replace("\n", ""), lineas_archivo))
                        lineas.extend(lineas_archivo)
    lineas_M5, lineas_M15, lineas_todas = obtener_cantidad_repeticiones(lineas)

    directorio_confluencia = path.join(directorio, "Confluencia_senales")
    makedirs(directorio_confluencia, exist_ok=True)
    ruta_archivo_M5, ruta_archivo_M15, ruta_archivo_todas = path.join(directorio_confluencia, "Senales_M5.txt"), path.join(directorio_confluencia, "Senales_M15.txt"), path.join(directorio_confluencia, "Senales.txt")

    lineas_M5, lineas_M15, lineas_todas = "\n".join(lineas_M5), "\n".join(lineas_M15), "\n".join(lineas_todas)

    with open(ruta_archivo_M5, "w") as f:
        f.write(lineas_M5)
    with open(ruta_archivo_M15, "w") as f:
        f.write(lineas_M15)
    with open(ruta_archivo_todas, "w") as f:
        f.write(lineas_todas)


if __name__ == "__main__":
    run()