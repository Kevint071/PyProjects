from colorama import init, Fore, Style


colores = {
    "ROJO_CLARO": Fore.LIGHTRED_EX,
    "VERDE_CLARO": Fore.LIGHTGREEN_EX
}


def colorear_texto(texto, color):
    if not color in colores:
        print("\nEl color no se encuentra en la lista de colores...\n")
        return texto
    
    color = colores[color]
    return f"{color}{texto}{Style.RESET_ALL}"