from os import path, chdir, remove, makedirs
from datetime import datetime
from time import sleep, time
from sys import path as pth
from colorama import Fore, Style
from Funciones_filtro_backtest import ejecutar_navegador, cerrar_anuncio, obtener_senales_txt, agregar_senales_textarea, agregar_dia, ajustar_martingala, iniciar_filtrado, obtener_senales_filtradas, retroceder_a_filtrador, limpiar_pantalla

root = path.dirname(path.dirname(path.abspath(__file__)))
pth.append(root)

from Directorio import obtener_directorio

def guardar_senales_filtradas(directorio_filtro_backtest, tiempo, dia, archivo, senales_filtradas):
    chdir(directorio_filtro_backtest)

    ruta_completa = path.join(directorio_filtro_backtest, tiempo, dia)
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


def comienzo_filtracion(directorio, directorio_filtro_backtest):
    directorio_filtro_ema = path.join(directorio, "Filtro_ema")
    chdir(directorio_filtro_backtest)

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
    chdir(directorio_filtro_ema)
    ejecutar_navegador()
    cerrar_anuncio()

    # Obtener señales.txt de la carpeta de señales Sin_filtro

    diccionario_archivos, archivos_todos = obtener_senales_txt(directorio_filtro_ema)

    # Obtener solo los archivos que un no se han filtrado

    if continuar == 1:
        chdir(directorio_filtro_backtest)
        with open("progreso.txt", "r") as progreso:
            archivos_filtrados = set(line.strip() for line in progreso)
            cantidad_archivos_filtrados = len(archivos_filtrados)
            print(f"Archivos filtrados: {cantidad_archivos_filtrados}")
        
        archivos_todos = set(i.strip() for i in archivos_todos)
        archivos_sin_filtrar = archivos_todos - archivos_filtrados

        print(f"Todos los archivos: {len(archivos_todos)}")
        print(f"Archivos sin filtrar: {len(archivos_sin_filtrar)}\n")
    else:
        archivos_sin_filtrar = archivos_todos
        cantidad_archivos_filtrados = 0
        print(f"Archivos para filtrar: {len(archivos_todos)}")
    
    lista_tiempos_catalogacion = []

    for tiempo, dias in diccionario_archivos.items():
        for dia, archivos in dias.items():
            for archivo in archivos:
                if archivo in archivos_sin_filtrar:
                    tiempo_inicio = time()
                    ruta_archivo = path.join(tiempo, dia, archivo)
                    ruta = path.join(directorio_filtro_ema, ruta_archivo)

                    with open(ruta, "r") as f:
                        contenido = f.read()
                    with open(ruta, "r") as f:
                        lineas_contenido = f.readlines()

                    print(Fore.LIGHTCYAN_EX + f"Archivo N° {cantidad_archivos_filtrados+1}\n" + Style.RESET_ALL)

                    print(f"Timeframe: {tiempo.split('_')[1]}")
                    print(f"Dia {dia.split('_')[1]}")
                    print(f"Archivo: {archivo}\n")

                    if len(lineas_contenido) > 250:
                        senales_divididas = [lineas_contenido[:len(lineas_contenido)//2], lineas_contenido[len(lineas_contenido)//2:]]

                        acum_senales_filtradas = []

                        for indice_parte, parte_senal in enumerate(senales_divididas, start=1):
                            string_parte_senal = "".join(parte_senal)
                            print(Fore.CYAN + f"Parte {indice_parte}\n" + Style.RESET_ALL)
                            agregar_senales_textarea(string_parte_senal)
                            agregar_dia(5)
                            ajustar_martingala()
                            iniciar_filtrado()
                            senales_filtradas = obtener_senales_filtradas()

                            if senales_filtradas != False:
                                senales_filtradas = senales_filtradas.split("\n")
                                acum_senales_filtradas += senales_filtradas
                                print(f"Cantidad de señales: {len(senales_filtradas)}")
                            else:
                                print(Fore.LIGHTRED_EX + "Error al obtener una parte de las señales..." + Style.RESET_ALL)

                            if parte_senal == senales_divididas[0]:
                                retroceder_a_filtrador()

                        senales_filtradas = "\n".join(acum_senales_filtradas)
                    else:
                        agregar_senales_textarea(contenido)
                        agregar_dia(5)
                        ajustar_martingala()
                        iniciar_filtrado()
                        senales_filtradas = obtener_senales_filtradas()

                    if senales_filtradas == None or senales_filtradas != False:
                        retroceder_a_filtrador()
                    if senales_filtradas != None and senales_filtradas != False:
                        guardar_senales_filtradas(directorio_filtro_backtest, tiempo, dia, archivo, senales_filtradas)
                    else:
                        print("No hay señales en este filtrado...\n")
                    guardar_progreso(directorio_filtro_backtest, archivo)
                    cantidad_archivos_filtrados += 1

                    tiempo_fin = time()
                    tiempo_catalogacion = round(tiempo_fin - tiempo_inicio, 2)
                    lista_tiempos_catalogacion.append(tiempo_catalogacion)
                    hora_actual = datetime.now().strftime("%H:%M:%S")

                    print(f"Hora de la descarga: {hora_actual}")
                    print(f"Tiempo de guardado: {tiempo_catalogacion} s")
                    print(
                        f"Tiempo total: {round(sum(lista_tiempos_catalogacion) // 3600):02d}:{round((sum(lista_tiempos_catalogacion) % 3600) // 60):02d}:{round((sum(lista_tiempos_catalogacion)) % 3600 % 60):02d}")
                    print(
                        f"Promedio tiempo: {round(sum(lista_tiempos_catalogacion)/len(lista_tiempos_catalogacion), 2)} s\n")

    chdir(directorio_filtro_backtest)

    # Pedir continuar (si quedo incompleta la filtracion)

    if path.exists("progreso.txt"):
        remove("progreso.txt")


def run():
    directorio = obtener_directorio()
    if directorio == None:
        return None

    directorio_filtro_backtest = path.join(directorio, "Filtro_backtest")
    makedirs(directorio_filtro_backtest, exist_ok=True)
    chdir(directorio_filtro_backtest)

    comienzo_filtracion(directorio, directorio_filtro_backtest)
    print(Fore.LIGHTYELLOW_EX + "Señales filtradas exitosamente..." + Style.RESET_ALL)


if __name__ == "__main__":
    run()
