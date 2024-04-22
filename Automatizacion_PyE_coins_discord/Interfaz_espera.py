from Configuracion_interfaz import configuracion_ventana_root, estilos_ventana_root
from tkinter import ttk, Frame, LEFT


def crear_componentes():
    componentes = [
        mensaje_descarga,
        contenedor_botones
    ]

    [componente() for componente in componentes]


def mensaje_descarga():
    mensaje = ttk.Label(root, text=f"Presiona el boton 'Listo' cuando hayas entrado al canal de PyE en discord", style="Confirmacion.TLabel")
    mensaje.pack(pady=(20, 15))


def boton_aceptar_comando():
    root.destroy()


def cerrar_ventana():
    root.destroy()


def contenedor_botones():
    frame_botones = Frame(root, bg="#2c2c2c")
    frame_botones.pack(side="top", pady=10)  # Centrar el marco horizontalmente
    
    boton_cancelar = ttk.Button(frame_botones, text="Cancelar", command=lambda: cerrar_ventana(), style="Confirmacion.TButton")
    boton_aceptar = ttk.Button(frame_botones, text="Listo", command=lambda: boton_aceptar_comando(), style="Confirmacion.TButton")

    boton_cancelar.pack(side=LEFT, padx=10)
    boton_aceptar.pack(side=LEFT, padx=10)


def ventana_confirmacion():
    global root
    root = configuracion_ventana_root()

    estilos_ventana_root()
    crear_componentes()

    root.mainloop()
