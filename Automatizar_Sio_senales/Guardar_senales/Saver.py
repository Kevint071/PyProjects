import os
from datetime import datetime
from Funciones_saver import ejecutar_navegador, retroceder_a_catalogador, cerrar_anuncio, elegir_idioma, seleccionar_mercado, obtener_inputs, agregar_efectividad, agregar_direccion_op, agregar_timeframe, agregar_dia, filtrar_noticias, iniciar_catalogacion, obtener_senales
from time import time, sleep
from Optimizador_descargas import configuracion_listas_senales
from colorama import Fore, Style
import locale


def guardar_senales_txt(nombre_archivo, senales):
    with open(nombre_archivo, "w") as archivo:
        archivo.write(senales)


def obtener_cantidad_senales(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        cantidad_senales = archivo.readlines()
        print(f"Cantidad de señales: {len(cantidad_senales)}")
        return cantidad_senales


def configuracion_catalogador_txt(directorio_sin_filtro, timeframe, tiempos, dia, porcentaje, cantidad_archivos_descargados, mercados):
    os.chdir(directorio_sin_filtro)

    with open("configuracion_catalogador.txt", "w") as archivo:
        if timeframe == tiempos[0]:
            archivo.write(f"{tiempos}\n")
        elif timeframe == tiempos[1]:
            archivo.write(f"{tiempos[1:]}\n")
        else:
            archivo.write(f"{tiempos[2]}\n")

        archivo.write(f"{dia}\n")
        archivo.write(f"{porcentaje}\n")
        archivo.write(f"{cantidad_archivos_descargados}\n")
        archivo.write(f"{mercados}")


def configurar_catalogacion(timeframe, porcentaje, dia, mercados):
    print(type(timeframe))
    print(timeframe)
    print("Iniciando configuración de catalogación...")
    funciones_catalogacion = [seleccionar_mercado, obtener_inputs, agregar_efectividad, agregar_direccion_op, agregar_timeframe, agregar_dia, filtrar_noticias, iniciar_catalogacion]

    params = {seleccionar_mercado: (mercados, ),
              agregar_efectividad: (porcentaje, ),
              agregar_timeframe: (timeframe, ),
              agregar_dia: (dia, ),}

    for funcion in funciones_catalogacion:
        args = params.get(funcion, ())
        funcion(*args)
        sleep(0.1)


def obtener_guardar_senales(directorio):
    """
    Esta función crea directorios y guarda señales en archivos de texto.
    Parametros: directorio (str) - Ruta del directorio donde se guardarán las señales.
    """

    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
    # Creando directorio carpeta fecha
    dia_actual, mes_actual = [datetime.now().day, datetime.now().strftime("%B")]
    carpeta_fecha = f"Senales_{mes_actual}_dia_{dia_actual}"

    os.chdir(directorio)
    
    # Creando directorio carpeta Sin_filtro

    carpeta_senales_sin_filtro = "Sin_filtro"
    lista_tiempos_catalogacion = []

    ruta_sin_filtro = os.path.join(directorio, carpeta_fecha, carpeta_senales_sin_filtro)

    configuraciones = configuracion_listas_senales(ruta_sin_filtro)
    os.makedirs(ruta_sin_filtro, exist_ok=True)
    tiempos, rango_dias, rango_porcentaje, cantidad_archivos_descargados, mercados = configuraciones
    hora_inicio = datetime.now().strftime("%H:%M:%S")
    print(f"Hora de inicio: {hora_inicio}")

    is_headless = ejecutar_navegador()
    sleep(0.5)
    cerrar_anuncio()
    sleep(0.5)
    if not is_headless:
        elegir_idioma()

    for timeframe in tiempos:
        
        os.chdir(ruta_sin_filtro)
        carpeta_tiempo = f"Tiempo_M{timeframe}"

        if not os.path.exists(carpeta_tiempo):
            os.mkdir(carpeta_tiempo)

        for dia in rango_dias:
           
            directorio_tiempo = os.path.join(ruta_sin_filtro, carpeta_tiempo)
            carpeta_dia = f"Dia_{dia}"
            os.chdir(directorio_tiempo)

            if not os.path.exists(carpeta_dia):
                os.mkdir(carpeta_dia)

            for porcentaje in rango_porcentaje:
                tiempo_inicio = time()
                print(Fore.LIGHTCYAN_EX + f"Iniciando Descarga N° {cantidad_archivos_descargados+1}" + Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX + f"Archivo Número {cantidad_archivos_descargados+1}" + Style.RESET_ALL)

                print(f"Tiempo_operación: {timeframe} minutos")
                print(f"Día: {dia}")
                print(f"Porcentaje: {porcentaje}\n")
                # Configurar catalogación para obtener las señales
                configurar_catalogacion(timeframe, porcentaje, dia, mercados)

                senales = obtener_senales()
                if senales == None:
                    print("No hay señales en esta catalogación...")
                    retroceder_a_catalogador()
                    break
                elif senales == False:
                    print("Error al obtener las señales en esta catalogación...\n")
                    cerrar_anuncio()
                    continue

                if (rango_porcentaje != range(70, 100+1, 5) or porcentaje == 100) or senales == None:
                        rango_porcentaje, rango_dias = range(70, 100 + 1, 5), range(2, 11 + 1)
                print("Señales obtenidas...")
                retroceder_a_catalogador()
                sleep(1)

                # Crear carpeta dia, guardando señales en arhcivos txt

                directorio_dia = os.path.join(directorio_tiempo, carpeta_dia)
                os.chdir(directorio_dia)

                lineas = senales.split("\n")
                num_lineas = len(lineas)
                nombre_archivo = f"Tiempo_{timeframe}_dia_{dia}_porcentaje_{porcentaje}_sen_{num_lineas}.txt"

                guardar_senales_txt(nombre_archivo, senales)
                cantidad_archivos_descargados += 1

                print(Fore.LIGHTGREEN_EX + f"Archivo N° {cantidad_archivos_descargados} descargado exitosamente..." + Style.RESET_ALL)
                
                print(f"Cantidad de señales: {num_lineas}")

                # obtener_cantidad_senales(nombre_archivo)
                configuracion_catalogador_txt(ruta_sin_filtro, timeframe, tiempos, dia, porcentaje, cantidad_archivos_descargados, mercados)

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


    ruta_archivo_configuracion = os.path.join(ruta_sin_filtro, "configuracion_catalogador.txt")

    if os.path.exists(ruta_archivo_configuracion):
        os.remove(ruta_archivo_configuracion)