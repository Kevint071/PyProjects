import datetime
from os import chdir, getcwd, listdir, path
import cv2


def hallar_tiempo (numero_contador, directorio_video, nombre):
    # Funcion que halla el tiempo de el video por medio de un directorio
    datos = cv2.VideoCapture(directorio_video)

    frames = int(datos.get(cv2.CAP_PROP_FRAME_COUNT)) # Fotogramas
    fps = datos.get(cv2.CAP_PROP_FPS)

    seconds = int(frames / fps)
    video_time = str(datetime.timedelta(seconds=seconds))

    if len(str(numero_contador)) == 1 :
        print(f"{numero_contador}. Duracion del video: {video_time}      Nombre: {nombre}")
    elif len(str(numero_contador)) == 2:
        print(f"{numero_contador}. Duracion del video: {video_time}     Nombre: {nombre}")
    elif len(str(numero_contador)) == 3:
        print(f"{numero_contador}. Duracion del video: {video_time}    Nombre: {nombre}")
    else:
        print(f"{numero_contador}. Duracion del video: {video_time}   Nombre: {nombre}")


def run():
    # Obtener directorio de la carpeta de videos
    directorio = input("Digite el directorio raiz de los videos (carpeta donde se encuentran los videos): ")

    chdir(directorio)
    directorio_principal = getcwd()

    # Obtener la lista de videos y eliminar archivos de la lista que no sean videos

    lista_videos = listdir(directorio_principal)

    # for i in lista_videos:
    #     if i.count(".ini") >= 1:
    #         print(i)
    #         lista_videos.remove(i)

    # for i in range(len(lista_videos)-1, -1, -1):
    #     if lista_videos[i].count(".mp4") == 0:
    #         print(f"Archivo eliminado de la lista: {lista_videos[i]}")
    #         lista_videos.remove(lista_videos[i])

    # Usando la lista al revés con reversed para evitar problemas con archivos de carpetas .ini y/o parecidos

    for i in reversed(lista_videos):
        if i.count(".mp4") == 0:
            print(f"Archivo eliminado de la lista: {i}")
            lista_videos.remove(i)

    print("\nLista de los videos...\n")
    lista_videos.sort()

    j = 0

    # Ciclo para hallar la duracion de cada video de la lista de videos

    acum = 0
    num_inicio = 0

    for i in lista_videos:
        num_inicio += 1
        # num = lista_videos[j][0:3]
        # num = int(num.strip(" ._"))
        nombre = i.split(".mp4")[0]

        # Hallar directorio de cada video y ver su peso

        directorio_video = f"{directorio_principal}/{i}"
        peso = path.getsize(directorio_video) / (1024 ** 2)
        acum += peso

        # Hallar el tiempo de cada video
        hallar_tiempo(num_inicio, directorio_video, nombre)
        j += 1

    print(f"\nPeso total: {round(acum, 2)} MB")

if __name__ == "__main__":
    run()