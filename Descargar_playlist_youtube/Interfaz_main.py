import tkinter as tk
from tkinter import ttk
from Logica_interfaces import validar_enlace, agregar_url, configurar_botones
from Configuracion_interfaces import configuracion_ventana_root, estilos_ventana_root
from Interfaz_popup import ventana_confirmacion
from time import sleep
from threading import Thread

label_info = None


def crear_ventana_y_configurar_estilos():
    root = configuracion_ventana_root()
    estilos_ventana_root()
    return root


def crear_componentes():
    componentes = [
        crear_titulo_principal,
        crear_contenedor_entry,
        crear_mensaje_info,
        crear_contenedor_botones,
        crear_boton_salir
    ]

    [componente() for componente in componentes]

def crear_titulo_principal():
    titulo = ttk.Label(root, text="Descargador de PlayLists de YouTube", anchor="center", style="Title.TLabel")
    titulo.pack(pady=30)


def crear_contenedor_entry():
    frame_entry = tk.Frame(root, bg="#2c2c2c")
    frame_entry.pack(pady=(40, 10), padx=20)

    label_entry = ttk.Label(frame_entry, text="Ingresa el enlace de la playlist:", style="TLabel")
    label_entry.pack(side=tk.LEFT, padx=10)

    global entry_playlist
    entry_playlist = ttk.Entry(frame_entry, width=80, font=("Arial", 10, "bold"))
    entry_playlist.pack(side=tk.LEFT, padx=10)


# mensajes = ["Ejemplo: https://www.youtube.com/playlist?list=PLTVcU6RR9nxvaS4KxRnBteKL2A6T5H0Ko", "Complete el campo con un enlace de playlist de youtube..."]
# indice_mensaje = 1


# def actualizar_mensaje():
#     global indice_mensaje
#     label_info.config(text=mensajes[indice_mensaje])
#     indice_mensaje = (indice_mensaje + 1) % len(mensajes)
#     root.after(5000, actualizar_mensaje)  # Actualiza el mensaje cada segundo


def crear_mensaje_info():
    global label_info
    label_info = ttk.Label(root, text="", style="Info.TLabel")
    label_info.pack(pady=(10, 0))
    # actualizar_mensaje()        


def crear_contenedor_botones():
    frame_botones = tk.Frame(root, bg="#2c2c2c")
    frame_botones.pack(pady=(20, 10))  # Centrar el marco horizontalmente

    formato_mp3 = "MP3"
    formato_mp4 = "MP4"

    boton_mp3 = ttk.Button(frame_botones, text="Descargar MP3", command=lambda: (ventana_confirmacion(root, validar_enlace(entry_playlist, label_info), formato_mp3), agregar_url(entry_playlist)))
    boton_mp3.pack(side=tk.LEFT, padx=10)

    boton_mp4 = ttk.Button(frame_botones, text="Descargar MP4", command=lambda: (ventana_confirmacion(root, validar_enlace(entry_playlist, label_info), formato_mp4), agregar_url(entry_playlist)))
    boton_mp4.pack(side=tk.LEFT, padx=10)

    configurar_botones(boton_mp3, boton_mp4)


def crear_boton_salir():
    boton_salir = ttk.Button(root, text="Salir", command=lambda: root.destroy())
    boton_salir.pack(pady=(20, 0))


def ventana_pricipal():
    try:
        global root
        root = crear_ventana_y_configurar_estilos()
        crear_componentes()
        root.mainloop()
        return True
    except KeyboardInterrupt:
        return False
    except Exception as e:
        print(e)
        print("Error")