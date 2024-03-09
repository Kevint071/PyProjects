import flet as ft


def configuracion_ventana(page: ft.Page):
    page.title = "Gestor de Evidencias SENA"
    page.window_width = 1020
    page.window_height = 600
    page.window_center()
    page.window_resizable = False
    page.window_maximizable = False
    page.bgcolor = "#101010"

def configuracion_menu():
    alignment=ft.alignment.top_left
    height=20
    padding = ft.padding.only(left=20)
    margin = ft.margin.only(top=10)

    return (alignment, height, padding, margin)


def main(page: ft.Page):
    configuracion_ventana(page)
    
    # titulo = ft.Row(
    #     controls=[
    #         ft.Text("Organiza y Registra con Facilidad", theme_style=ft.TextThemeStyle.HEADLINE_SMALL, text_align=ft.TextAlign.CENTER)
    #     ], alignment=ft.MainAxisAlignment.CENTER
    # )

    # page.controls.append(titulo)

    page.add(
        ft.Row(
            [
                ft.Container(
                    bgcolor="#EEF2F5",
                    alignment=ft.alignment.center,
                    width=250,
                    padding=0,
                    margin=0,
                    content=ft.Column(controls=[
                        ft.Container(
                            content=ft.Text("Utilidades", color=ft.colors.GREY_500, weight=ft.FontWeight.W_600),
                            alignment=ft.alignment.top_left ,
                            height=20,
                            padding = ft.padding.only(left=20),
                            margin = ft.margin.only(top=10),
                        ),
                        ft.Container(
                            content=ft.Text("Automatización", color=ft.colors.BLACK38, weight=ft.FontWeight.W_700),
                            alignment=ft.alignment.top_left ,
                            height=20,
                            padding = ft.padding.only(left=20),
                            margin = ft.margin.only(top=10),
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            expand=True,
                            padding=0,
                            margin=0,
                        ),
                    ]), 
                ),
                 ft.VerticalDivider(width=0),
                ft.Container(
                    bgcolor="#FFFFFF",
                    alignment=ft.alignment.center,
                    expand=True,
                    padding=0,
                    margin=0,
                ),
            ],
            spacing=0,
            expand=True,
        )
    )

    page.update()

ft.app(target=main)