from os import path, chdir, remove, makedirs
from sys import path as pth
from colorama import Fore, Style
from Funciones_filtro_riesgo import ejecutar_navegador, cerrar_anuncio, obtener_senales_txt, agregar_senales_textarea, iniciar_filtrado, obtener_senales_filtradas, retroceder_a_filtrador, limpiar_pantalla

root = path.dirname(path.dirname(path.abspath(__file__)))
pth.append(root)

from Directorio import obtener_directorio

def guardar_senales_filtradas(directorio_filtro_riesgo, tiempo, dia, archivo, senales_filtradas):
    chdir(directorio_filtro_riesgo)

    ruta_completa = path.join(directorio_filtro_riesgo, tiempo, dia)
    makedirs(ruta_completa, exist_ok=True)

    # Obtener la cantidad de señales filtradas

    lineas = senales_filtradas.split("\n")
    num_lineas = len(lineas)

    archivo = archivo.split("_sen_")
    senales_antes_filtrado = archivo[1].split(".txt")[0]
    archivo = f'{archivo[0]}_sen_{str(num_lineas)}.txt'
    print(f"Señales validadas: {num_lineas} de {senales_antes_filtrado}\n")

    # Abrir archivo en ruta completa para escribir 

    ruta_archivo = path.join(ruta_completa, archivo)

    with open(ruta_archivo, "w") as f:
        f.write(senales_filtradas)


def guardar_progreso(directorio_filtro_riesgo, archivo):
    chdir(directorio_filtro_riesgo)

    with open("progreso.txt", "a") as progreso:
        progreso.write(f"{archivo}\n")


def comienzo_filtracion(directorio, directorio_filtro_riesgo):
    directorio_sin_filtro = path.join(directorio, "Sin_filtro")
    chdir(directorio_filtro_riesgo)

    limpiar_pantalla()

    # Pedir continuar (si quedo incompleta la filtracion)

    if path.exists("progreso.txt"):
        continuar = int(input("""¿Quiere continuar por donde quedó?:
    1. Sí
    2. No
                              
    Elija una opción (1 o 2): """))
    else:
        continuar = None
        
    # Ejecutando navegador
    chdir(directorio_sin_filtro)
    ejecutar_navegador()
    cerrar_anuncio()

    # Obtener señales.txt de la carpeta de señales Sin_filtro

    diccionario_archivos, archivos_todos = obtener_senales_txt(directorio_sin_filtro)

    # Obtener solo los archivos que un no se han filtrado

    if continuar == 1:
        chdir(directorio_filtro_riesgo)
        with open("progreso.txt", "r") as progreso:
            archivos_filtrados = set(line.strip() for line in progreso)
            print(f"Archivos filtrados: {len(archivos_filtrados)}")
        
        archivos_todos = set(i.strip() for i in archivos_todos)
        archivos_sin_filtrar = archivos_todos - archivos_filtrados
        print(f"Todos los archivos: {len(archivos_todos)}")
        print(f"Archivos sin filtrar: {len(archivos_sin_filtrar)}\n")
    else:
        archivos_sin_filtrar = archivos_todos

    for tiempo, dias in diccionario_archivos.items():
        for dia, archivos in dias.items():
            for archivo in archivos:
                if archivo in archivos_sin_filtrar:
                    ruta_archivo = path.join(tiempo, dia, archivo)
                    ruta = path.join(directorio_sin_filtro, ruta_archivo)

                    with open(ruta, "r") as f:
                        contenido = f.read()
                        lineas_contenido = f.readlines()
                    
                    print(f"{tiempo}")
                    print(f"{dia}")
                    print(f"Archivo: {archivo}")
                    agregar_senales_textarea(contenido)
                    iniciar_filtrado()
                    senales_filtradas = obtener_senales_filtradas()

                    if senales_filtradas == None or senales_filtradas != False:
                        retroceder_a_filtrador()
                    
                    if senales_filtradas != None and senales_filtradas != False:
                        guardar_senales_filtradas(directorio_filtro_riesgo, tiempo, dia, archivo, senales_filtradas)
                    else:
                        print("No hay señales en este filtrado...\n")
                    guardar_progreso(directorio_filtro_riesgo, archivo)

    chdir(directorio_filtro_riesgo)

    # Pedir continuar (si quedo incompleta la filtracion)

    if path.exists("progreso.txt"):
        remove("progreso.txt")


def run():
    directorio = obtener_directorio()
    if directorio == None:
        return None
    
    directorio_filtro_riesgo = path.join(directorio, "Filtro_riesgo")
    makedirs(directorio_filtro_riesgo, exist_ok=True)
    chdir(directorio_filtro_riesgo)
    
   
    comienzo_filtracion(directorio, directorio_filtro_riesgo)
    print(Fore.LIGHTYELLOW_EX + "Señales filtradas exitosamente..." + Style.RESET_ALL)


if __name__ == "__main__":
    run()
