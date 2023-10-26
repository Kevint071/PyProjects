from os import path, chdir, remove, makedirs
from sys import path as pth
from colorama import Fore, Style
from datetime import datetime
from Funciones_filtro_ema import ejecutar_navegador, cerrar_anuncio, obtener_senales_txt, agregar_senales_textarea, agregar_periodo, iniciar_filtrado, obtener_senales_filtradas, retroceder_a_filtrador, limpiar_pantalla

root = path.dirname(path.dirname(path.abspath(__file__)))
pth.append(root)

from Directorio import obtener_directorio


def num_senales_antes_despues(senales_confluenciadas, archivo):
    # Obtener la cantidad de señales filtradas

    num_lineas = len(senales_confluenciadas)
    archivo = archivo.split("_sen_")
    senales_antes_filtrado = archivo[1].split(".txt")[0]
    nombre_archivo = f'{archivo[0]}_sen_{str(num_lineas)}.txt'
    
    print(f"Señales validadas: {num_lineas} de {senales_antes_filtrado}\n")

    return nombre_archivo


def guardar_senales_confluenciadas(directorio_filtro_ema, tiempo, dia, nombre_archivo, senales_confluenciadas):
    chdir(directorio_filtro_ema)

    ruta_completa = path.join(directorio_filtro_ema, tiempo, dia)
    makedirs(ruta_completa, exist_ok=True)

    senales_confluenciadas = "\n".join(senales_confluenciadas)

    # Abrir archivo en ruta completa para escribir 

    ruta_archivo = path.join(ruta_completa, nombre_archivo)
    with open(ruta_archivo, "w") as f:
        f.write(senales_confluenciadas)


def confluenciar_senales(senales_emas):
    senales_confluenciadas = set(senales_emas[0]) & set(senales_emas[1])
    return senales_confluenciadas


def guardar_progreso(directorio_filtro_ema, archivo):
    chdir(directorio_filtro_ema)

    with open("progreso.txt", "a") as progreso:
        progreso.write(f"{archivo}\n")


def comienzo_filtracion(directorio, directorio_filtro_ema, emas):
    directorio_filtro_riesgo = path.join(directorio, "Filtro_riesgo")
    makedirs(directorio_filtro_ema, exist_ok=True)
    chdir(directorio_filtro_ema)

    limpiar_pantalla()

    # Pedir continuar (si quedo incompleta la filtracion)

    if path.exists("progreso.txt"):
        while True:
            continuar = int(input("""¿Quiere continuar por donde quedó?:

    1. Sí
    2. No
                                
    Elija una opción (1 o 2): """))
            if continuar in [1, 2]:
                limpiar_pantalla()
                break
            else:
                limpiar_pantalla()
                print("Ese valor no es valido, escriba 1 o 2...\n")
    else:
        continuar = None
        
    # Ejecutando navegador
    chdir(directorio_filtro_riesgo)
    ejecutar_navegador()
    cerrar_anuncio()

    # Obtener señales.txt de la carpeta de señales Sin_filtro

    diccionario_archivos, archivos_todos = obtener_senales_txt(directorio_filtro_riesgo)
    archivos_todos = set(i.strip() for i in archivos_todos)

    # Obtener solo los archivos que un no se han filtrado

    if continuar == 1:
        chdir(directorio_filtro_ema)
        with open("progreso.txt", "r") as progreso:
            # cantidad_archivos_filtrados = len(progreso.readlines())
            archivos_filtrados = set(line.strip() for line in progreso)
            cantidad_archivos_filtrados = len(archivos_filtrados)
            print(f"Archivos filtrados: {cantidad_archivos_filtrados}")
        
        archivos_sin_filtrar = archivos_todos - archivos_filtrados
        print(f"Todos los archivos: {len(archivos_todos)}")
        print(f"Archivos para filtrar: {len(archivos_sin_filtrar)}\n")
    else:
        archivos_sin_filtrar = archivos_todos
        cantidad_archivos_filtrados = 0
        print(f"Archivos para filtrar: {len(archivos_todos)}")

    for tiempo, dias in diccionario_archivos.items():
        for dia, archivos in dias.items():
            for archivo in archivos:
                if archivo in archivos_sin_filtrar:
                    ruta_archivo = path.join(tiempo, dia, archivo)
                    ruta = path.join(directorio_filtro_riesgo, ruta_archivo)

                    with open(ruta, "r") as f:
                        contenido = f.read()
                        
                    with open(ruta, "r") as f:
                        lineas_contenido = f.readlines()
                    
                    print(Fore.LIGHTCYAN_EX + f"Archivo N° {cantidad_archivos_filtrados+1}\n" + Style.RESET_ALL)
                    print(f"Timeframe: {tiempo.split('_')[1]}")
                    print(f"Dia {dia.split('_')[1]}")
                    print(f"Archivo: {archivo}\n")

                    senales_emas = []

                    for ema in emas:
                        if len(lineas_contenido) > 500:
                            senales_divididas = [lineas_contenido[:len(lineas_contenido)//2], lineas_contenido[len(lineas_contenido)//2:]]

                            acum_senales_filtradas = []
                            
                            for parte_senal in senales_divididas:
                                string_parte_senal = "".join(parte_senal)
                                print(Fore.LIGHTBLUE_EX + f"EMA: {ema}" + Style.RESET_ALL)
                                agregar_senales_textarea(string_parte_senal)
                                agregar_periodo(ema)
                                iniciar_filtrado()
                                senales_filtradas = obtener_senales_filtradas()
                                if senales_filtradas != False:
                                    senales_filtradas = senales_filtradas.split("\n")
                                    acum_senales_filtradas += senales_filtradas
                                else:
                                    print(Fore.LIGHTRED_EX + "Error al obtener una parte de las señales..." + Style.RESET_ALL)
                                if parte_senal == senales_divididas[0]:
                                    retroceder_a_filtrador()
                            senales_filtradas = acum_senales_filtradas

                        else:
                            print(Fore.LIGHTBLUE_EX + f"EMA: {ema}" + Style.RESET_ALL)
                            agregar_senales_textarea(contenido)
                            agregar_periodo(ema)
                            iniciar_filtrado()
                            senales_filtradas = obtener_senales_filtradas()

                        if senales_filtradas != False:
                            retroceder_a_filtrador()
                        if senales_filtradas != None and senales_filtradas != False:
                            if type(senales_filtradas) != list:
                                senales_filtradas = senales_filtradas.split("\n")
                            cantidad_senales_ema = len(senales_filtradas)
                            print(f"Cantidad de señales: {cantidad_senales_ema}\n")
                            senales_emas.append(senales_filtradas)
                        
                    if senales_emas:
                        if len(senales_emas) == 2:
                            senales_confluenciadas = confluenciar_senales(senales_emas)
                            senales_confluenciadas = sorted(senales_confluenciadas, key=lambda x: datetime.strptime(x.split(';')[2], "%H:%M"))
                        if len(senales_emas) == 1:
                            senales_confluenciadas = senales_emas[0]
                        nombre_archivo = num_senales_antes_despues(senales_confluenciadas, archivo)
                    else:
                        guardar_progreso(directorio_filtro_ema, archivo)
                        cantidad_archivos_filtrados += 1
                        continue
                    guardar_senales_confluenciadas(directorio_filtro_ema, tiempo, dia, nombre_archivo, senales_confluenciadas)
                    guardar_progreso(directorio_filtro_ema, archivo)
                    cantidad_archivos_filtrados += 1

    chdir(directorio_filtro_ema)

    # Pedir continuar (si quedo incompleta la filtracion)

    if path.exists("progreso.txt"):
        remove("progreso.txt")


def obtener_emas():
    while True:
        emas = input("¿Va a usar las emas por defecto que son 10 y 21 ? (Y/N): ").upper()
        if emas == "Y":
            emas = (10, 21)
            break
        if emas == "N":
            emas = []
            for i in range(1, 3):
                while True:
                    value = input(f"Ingrese el periodo N° {i}: ")
                    if value.isnumeric():emas.append(int(value));break
                    else:print("Ingrese solo números!")
            emas = tuple(emas)
            break
        print("Elige Y o N...")
    return emas


def comprobar_emas():
    if path.exists("emas.txt"):
        with open("emas.txt", "r") as archivo:
            emas_actuales = eval(str(archivo.readline().strip("\n ")))
        return emas_actuales
    else:
        emas = obtener_emas()
        with open("emas.txt", "w") as archivo:
            archivo.write(str(emas))
        return emas


def run():
    directorio = obtener_directorio()
    if directorio == None:
        return None
    
    directorio_filtro_ema = path.join(directorio, "Filtro_ema")
    makedirs(directorio_filtro_ema, exist_ok=True)
    chdir(directorio_filtro_ema)

    emas = comprobar_emas()

    comienzo_filtracion(directorio, directorio_filtro_ema, emas)
    print(Fore.LIGHTYELLOW_EX + "Señales filtradas exitosamente..." + Style.RESET_ALL)
    chdir(directorio_filtro_ema)
    
    if path.exists("emas.txt"):
        remove("emas.txt")


if __name__ == "__main__":
    run()