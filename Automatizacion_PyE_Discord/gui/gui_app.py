import flet as ft
from .gui_texto_title import texto_title
from .gui_botones_juegos import botones_juegos


def configuracion_ventana(page: ft.Page):
    page.title = "Elección Juego"
    page.window_width = 500
    page.window_height = 180
    page.window_center()
    page.window_resizable = False
    page.window_maximizable = False
    page.theme_mode = ft.ThemeMode.DARK


def main(page: ft.Page):
    configuracion_ventana(page)
    page.add(texto_title())
    page.add(botones_juegos(page))
    page.update()