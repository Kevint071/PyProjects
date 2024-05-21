from tkinter import ttk, DISABLED, NORMAL
from Administracion_pagina import ejecutar_navegador, verificar_cantidad_videos, obtener_enlaces_videos
from Interfaz_directorio import obtener_directorio
from Descargar_archivos import descargar_archivos
import threading
from Globals import variables_globales


ventana_emergente_abierta = None
tipo_archivo = str()
hilo_descarga = threading.Thread
boton_mp3 = ttk.Button
boton_mp4 = ttk.Button


def validar_enlace(entry_playlist: ttk.Entry, label_info_: ttk.Label):
    global label_info

    label_info = label_info_
    enlace = entry_playlist.get().strip()
    base_enlace = 'https://www.youtube.com/playlist?list='

    if not enlace:
        label_info["text"] = "El campo está vacio..."
        return None
    elif "/watch?" in enlace and "&list" in enlace:
        enlace = enlace.split("&")
        variables_globales["url"] = enlace[0].replace("/watch", "/playlist").split("v=")[0] + enlace[1]
        return enlace, True
    elif base_enlace not in enlace:
        label_info["text"] = "El enlace no es válido..."
        return False
    elif base_enlace in enlace:
        label_info['text'] = ""
        return enlace, True


def agregar_tipo_formato(formato: str):
    global tipo_archivo
    tipo_archivo = formato
    label_info["text"] = "Obteniendo enlaces de los videos..."


def obtener_formato():
    return tipo_archivo


def cerrar_ventana(popup: ttk.Button):
    popup.destroy()
    global ventana_emergente_abierta
    ventana_emergente_abierta = None


def obtener_ventana_emergente_abierta():
    return ventana_emergente_abierta


def modificar_ventana_emergente_abierta(valor):
    global ventana_emergente_abierta
    ventana_emergente_abierta = valor


def descarga_actual(info_videos, directorio, formato, label_info):
    label_info["text"] = f"Descargando lista de reproducción en {formato}..."
    descargar_archivos(info_videos, directorio, formato, label_info)
    label_info["text"] = "Descarga completada exitosamente"
    habilitar_botones()
 

def obtener_descargar_videos():
    directorio = obtener_directorio()

    if directorio == None:
        return None

    label_info["text"] = "Obteniendo enlaces de los videos..."
    enlace = variables_globales["url"]
    Driver = ejecutar_navegador(enlace)

    verificar_cantidad_videos()

    info_videos = obtener_enlaces_videos()
    Driver.quit()
    formato = variables_globales["formato"]

    global hilo_descarga
    hilo_descarga = threading.Thread(target=descarga_actual, args=(info_videos, directorio, formato, label_info))
    hilo_descarga.start()

    
def deshabilitar_botones():
    global boton_mp3, boton_mp4
    boton_mp3.config(state=DISABLED)
    boton_mp4.config(state=DISABLED)


def habilitar_botones():
    global boton_mp3, boton_mp4
    boton_mp3.config(state=NORMAL)
    boton_mp4.config(state=NORMAL)


def configurar_botones(boton_mp3_, boton_mp4_):
    global boton_mp3, boton_mp4
    boton_mp3 = boton_mp3_
    boton_mp4 = boton_mp4_
