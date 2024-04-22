import tkinter as tk
from tkinter import ttk


def configuracion_ventana_root():
    root = tk.Tk()
    root.title("Descargador de YouTube")
    root.geometry("660x130")
    root.resizable(0, 0)
    root.configure(bg="#2c2c2c")
    return root


def estilos_ventana_root():
    style_root = ttk.Style()
    style_root.theme_use("clam")
    style_root.configure("TLabel", font=("Arial", 12, "bold"), background="#2c2c2c", foreground="white")
    style_root.configure("TButton", font=("Arial", 12), background="#4c4c4c", foreground="white")
    style_root.map("TButton", background=[("active", "#6c6c6c")])