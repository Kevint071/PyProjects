from os import walk, path, listdir
import asyncio
from time import time


async def buscar_carpetas(directorio, palabra):
    indice = 1
    cantidad_carpetas = 0
    for nombre_directorio, directorios, ficheros in walk(directorio):
        cantidad_carpetas += len(directorios)
        for directorio in directorios:
            if directorio.lower().count(palabra):
                print(f"{indice}. {path.join(nombre_directorio, directorio)}")
                indice += 1
            await asyncio.sleep(0)
    return cantidad_carpetas


async def buscar_archivos(directorios, palabra):
    cantidad_archivos = 0
    global indice
    for directorio in directorios:
        for nombre_directorio, dirs, ficheros in walk(directorio):
            cantidad_archivos += len(ficheros)
            for nombre_fichero in ficheros:
                if nombre_fichero.lower().count(palabra):
                    print(f"Coindicencia {indice}")
                    print(f"Directorio: {nombre_directorio}")
                    print(f"Archivo: {nombre_fichero}\n")
                    indice += 1
                await asyncio.sleep(0)
    return cantidad_archivos


async def elegir_tipo():
    eleccion = int(
        input(
            """\n¿Que quiere buscar?:

    1. Archivo
    2. Carpeta
            
    Elige un número: """
        )
    )
    print()
    return eleccion


async def main():
    directorio = input("Digite el directorio: ")
    global indice
    indice = 1
    carpetas = [
        path.join(directorio, archivo)
        for archivo in listdir(directorio)
        if path.isdir(path.join(directorio, archivo))
    ]
    palabra = input("Digite la palabra que desea buscar en los directorios: ").lower()
    eleccion = await elegir_tipo()

    tasks = []

    inicio = time()

    if eleccion == 1:
        for i in range(4):
            sublist = carpetas[i * len(carpetas) // 4 : (i + 1) * len(carpetas) // 4]
            task = asyncio.create_task(buscar_archivos(sublist, palabra))
            tasks.append(task)
        # print(f"Cantidad de archivos totales: {cantidad_archivos}")
    elif eleccion == 2:
        cantidad_carpetas = await buscar_carpetas(directorio, palabra)
        print(f"Cantidad de carpetas totales: {cantidad_carpetas}")

    await asyncio.gather(*tasks)
    fin = time()
    print(fin - inicio)


if __name__ == "__main__":
    asyncio.run(main())
