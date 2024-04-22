from Configuracion_interfaz import configuracion_ventana_root, estilos_ventana_root
from tkinter import ttk, Frame, LEFT

juego = None

def crear_componentes():
    componentes = [
        mensaje_eleccion,
        contenedor_botones
    ]

    [componente() for componente in componentes]


def mensaje_eleccion():
    mensaje = ttk.Label(root, text=f"Selecciona un modo de juego", style="Confirmacion.TLabel")
    mensaje.pack(pady=(20, 15))


def jugar_slot():
    global juego
    juego = "Slot"
    root.destroy()

def jugar_ruleta():
    global juego
    juego = "Ruleta"
    root.destroy()

def cerrar_ventana():
    root.destroy()


def contenedor_botones():
    frame_botones = Frame(root, bg="#2c2c2c")
    frame_botones.pack(side="top", pady=10)  # Centrar el marco horizontalmente
    
    boton_cancelar = ttk.Button(frame_botones, text="Cancelar", command=lambda: cerrar_ventana(), style="Confirmacion.TButton")
    boton_slots = ttk.Button(frame_botones, text="Jugar Slot", command=lambda: jugar_slot(), style="Confirmacion.TButton")
    boton_ruletas = ttk.Button(frame_botones, text="Jugar Ruleta", command=lambda: jugar_ruleta(), style="Confirmacion.TButton")

    boton_cancelar.pack(side=LEFT, padx=10)
    boton_slots.pack(side=LEFT, padx=10)
    boton_ruletas.pack(side=LEFT, padx=10)


def ventana_eleccion_juego():
    global root
    root = configuracion_ventana_root()

    estilos_ventana_root()
    crear_componentes()

    root.mainloop()
    return juego
