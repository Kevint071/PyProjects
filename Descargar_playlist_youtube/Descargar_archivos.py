from pytube import YouTube, Stream
from os import chdir, remove
from re import sub
from time import sleep
from pytube.exceptions import AgeRestrictedError, RegexMatchError


def obtener_video(video: Stream, indice, nombre, label_info):
    try:
        video.download()
        label_info["text"] = f"{indice}. {nombre} Descargado correctamente"
        return True
    except:
        return False


def mensajes_excepcion(intento, tipo_archivo):
    print(f"No se pudo descargar el {tipo_archivo}. ", end="")
    if intento == 0:
        print(f"Intentando descargar el {tipo_archivo} de nuevo\n")
    elif intento == 1:
        return False
    

def obtener_stream_archivo(link, tipo_archivo):
    stream = YouTube(link)

    if tipo_archivo == "mp4":
        video = stream.streams.get_highest_resolution()
        return video
    elif tipo_archivo == "mp3":
        audio = stream.streams.filter(only_audio=True).order_by("abr").desc().first()
        return audio


def descargar_video(indice, nombre, link, directorio, label_info):
    try:
        chdir(directorio)
        video = obtener_stream_archivo(link, "mp4")

        for intento in range(2):
            try:
                obtencion_video = obtener_video(video, indice, nombre, label_info)
                return obtencion_video
            except:
                mensaje = mensajes_excepcion(intento, "video")
                print("Mensaje: video", mensaje)
                return mensaje
    except:
        print("Terminar descarga del video...")
        return False


def limpiar_nombre(nombre):
    return sub(r'[\\/*?:"<>|]', "", nombre)


def obtener_audio(audio: Stream, indice, nombre_limpio, directorio, label_info):
    try:
        audio.download(output_path=directorio, filename=f"{nombre_limpio}.mp3")
        remove(audio.download())
        label_info["text"] = f"{indice}. {nombre_limpio} Descargado correctamente"
        return True
    except:
        return False


def descargar_audio(indice, nombre, link, directorio: str, label_info):
    try:
        chdir(directorio)
        audio = obtener_stream_archivo(link, "mp3")
        nombre_limpio = limpiar_nombre(nombre)

        for intento in range(2):
            try:
                obtencion_audio = obtener_audio(audio, indice, nombre_limpio, directorio, label_info)
                return obtencion_audio
            except:
                mensaje = mensajes_excepcion(intento, "mp3")
                print("Mensaje audio", mensaje)
                return mensaje
    
    except KeyboardInterrupt:
        print("Ejecucion finalizada por interrupcion manual")
        return False


def descarga_de_archivos(info_videos, directorio, formato, label_info):
    archivos_omitidos = 0

    for indice, info_video in enumerate(info_videos, start=1):
        try:
            verificacion_descarga = descargar_video(indice, info_video[0], info_video[1], directorio, label_info) if formato == "MP4" else descargar_audio(indice, info_video[0], info_video[1], directorio, label_info)
            if verificacion_descarga == None or verificacion_descarga == False:
                print("Terminando Ejecución")
                break
        except AgeRestrictedError:
            label_info["text"] = f"{indice}. No se pudo descargar por restricciones de edad"
            archivos_omitidos += 1
            sleep(2)
        except RegexMatchError:
            label_info["text"] = f"{indice}. No se pudo obtener el codigo fuente del video"
            archivos_omitidos += 1
            sleep(2)
        except Exception as e:
            print(f"Error: {e}")
            label_info["text"] = f"{indice}. Error desconocido"
            archivos_omitidos += 1
            print(type(e))
