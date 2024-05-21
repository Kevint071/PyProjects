from Configuracion_interfaces import configuracion_ventana_popup, estilos_ventana_popup
from tkinter import ttk
from threading import Thread
from tkinter import Frame, LEFT
from Logica_interfaces import obtener_ventana_emergente_abierta, modificar_ventana_emergente_abierta, cerrar_ventana, obtener_descargar_videos, deshabilitar_botones
from Globals import variables_globales


def mensaje_descarga(formato: str):
    mensaje = ttk.Label(popup, text=f"¿Estás seguro de descargar la lista de reproducción en {formato}?", style="Confirmacion.TLabel")
    mensaje.pack(pady=10)


def boton_aceptar_comando(formato):
    cerrar_ventana(popup)
    variables_globales["formato"] = formato
    
    deshabilitar_botones()
    hilo_descarga = Thread(target=obtener_descargar_videos)
    hilo_descarga.start()


def contenedor_botones(formato: str):
    frame_botones = Frame(popup, bg="#2c2c2c")
    frame_botones.pack(side="top", pady=10)  # Centrar el marco horizontalmente

    boton_aceptar = ttk.Button(frame_botones, text="Aceptar", command=lambda: boton_aceptar_comando(formato), style="Confirmacion.TButton")
    boton_cancelar = ttk.Button(frame_botones, text="Cancelar", command=lambda: cerrar_ventana(popup), style="Confirmacion.TButton")

    boton_aceptar.pack(side=LEFT, padx=10)
    boton_cancelar.pack(side=LEFT, padx=10)


def ventana_confirmacion(root, enlace_validado, formato: str):

    # Si hay una ventana emergente abierta o si el enlace no es valido no se crea la ventana
    if not enlace_validado or not enlace_validado[1]:
        return False
    elif obtener_ventana_emergente_abierta() is not None:
        return False
    
    global popup
    popup = configuracion_ventana_popup(root)
    estilos_ventana_popup()

    mensaje_descarga(formato)
    contenedor_botones(formato)
    modificar_ventana_emergente_abierta(popup)

