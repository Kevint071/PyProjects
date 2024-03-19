import flet as ft
from seccion_menu import seccion_menu
from seccion_contenido import seccion_contenido


def configuracion_ventana(page: ft.Page):
    page.title = "Territorium Flow"
    page.window_width = 1020
    page.window_height = 600
    page.window_center()
    page.window_resizable = False
    page.window_maximizable = False
    page.theme_mode = ft.ThemeMode.LIGHT


def main(page: ft.Page):
    configuracion_ventana(page)
    
    # titulo = ft.Row(
    #     controls=[
    #         ft.Text("Organiza y Registra con Facilidad", theme_style=ft.TextThemeStyle.HEADLINE_SMALL, text_align=ft.TextAlign.CENTER)
    #     ], alignment=ft.MainAxisAlignment.CENTER
    # )

    # page.controls.append(titulo)


    contenedor_principal = ft.Row(
        expand=True,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )
    
    contenedor_principal.controls.append(seccion_menu())
    contenedor_principal.controls.append(ft.VerticalDivider(width=0))
    contenedor_principal.controls.append(seccion_contenido())
    page.add(contenedor_principal)
    page.update()

ft.app(target=main)