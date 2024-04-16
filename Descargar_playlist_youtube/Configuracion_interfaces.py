import tkinter as tk
from tkinter import ttk


def configuracion_ventana_root():
    root = tk.Tk()
    root.title("Descargador de YouTube")
    root.geometry("820x350")
    root.resizable(0, 0)
    root.configure(bg="#2c2c2c")
    return root


def estilos_ventana_root():
    style_root = ttk.Style()
    style_root.theme_use("clam")
    style_root.configure("TLabel", font=("Arial", 12, "bold"), background="#2c2c2c", foreground="white")
    style_root.configure("Title.TLabel", font=("Arial", 18, "bold"), background="#2c2c2c", foreground="white")
    style_root.configure("Info.TLabel", font=("Arial", 10, "bold"), background="#2c2c2c", foreground="white")

    style_root.configure("TButton", font=("Arial", 12), background="#4c4c4c", foreground="white")
    style_root.map("TButton", background=[("active", "#6c6c6c")])

    style_root.configure("Entrada.TFrame", font=("Arial", 12, "bold"), foreground="black", background="#4c4c4c")
    style_root.map("Entrada.TFrame", foreground=[("disabled", "gray")], background=[("disabled", "#2c2c2c")])


def configuracion_ventana_popup(root):
    popup = tk.Toplevel(root)
    popup.title("Confirmar descarga")
    popup.geometry("500x110")
    popup.resizable(0, 0)
    popup.configure(bg="#2c2c2c")
    popup.protocol("WM_DELETE_WINDOW", lambda: None)
    return popup


def estilos_ventana_popup():
    style_popup = ttk.Style()
    style_popup.theme_use("clam")
    style_popup.configure("Confirmacion.TLabel", font=("Arial", 12), background="#2c2c2c", foreground="white")
    style_popup.configure("Confirmacion.TButton", font=("Arial", 10), background="#4c4c4c", foreground="white")
    style_popup.map("Confirmacion.TButton", background=[("active", "#6c6c6c")])