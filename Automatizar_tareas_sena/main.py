import flet as ft


def configuracion_ventana(page: ft.Page):
    page.title = "Territorium Flow"
    page.window_width = 1020
    page.window_height = 600
    page.window_center()
    page.window_resizable = False
    page.window_maximizable = False
    page.bgcolor = "#101010"


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
                            content=ft.Text("Opciones Automatizadas", color=ft.colors.GREY_600, weight=ft.FontWeight.W_600, size=15),
                            alignment=ft.alignment.top_left ,
                            height=20,
                            padding = ft.padding.only(top=0, right=10, bottom=0, left=20),
                            margin = ft.margin.only(top=10, bottom=-10),
                           
                        ),
                        ft.Container(
                            content=ft.Text("Gestión de Evidencias", color=ft.colors.BLACK87, weight=ft.FontWeight.W_700, size=20),
                            alignment=ft.alignment.top_left,
                            height=25,
                            padding = ft.padding.only(left=20, top=0),
                            margin = ft.margin.only(top=10),
                        ),
                        ft.Container(
                            content=ft.Row([ft.Icon(name=ft.icons.ADD_TASK),ft.Text("Publicar Evidencias", color=ft.colors.BLACK87, weight=ft.FontWeight.W_500, size=15)]),
                            alignment=ft.alignment.top_left,
                            height=25,
                            padding = ft.padding.only(left=20, top=0),
                            margin = ft.margin.only(top=10),
                            on_click=lambda _: print("Publicado!")
                        ),
                        ft.Container(
                            content=ft.Row([ft.Icon(name=ft.icons.QUESTION_MARK),ft.Text("Consultar Evidencias", color=ft.colors.BLACK87, weight=ft.FontWeight.W_500, size=15)]),
                            alignment=ft.alignment.top_left,
                            height=25,
                            padding = ft.padding.only(left=20, top=0),
                            margin = ft.margin.only(top=5),
                            on_click=lambda _: print("Consultado!"),
                        ),
                        ft.Container(
                            content=ft.Text("Mensajes", color=ft.colors.BLACK87, weight=ft.FontWeight.W_700, size=20),
                            alignment=ft.alignment.top_left,
                            height=25,
                            padding = ft.padding.only(left=20, top=0),
                            margin = ft.margin.only(top=20),
                        ),
                        ft.Container(
                            content=ft.Row([ft.Icon(name=ft.icons.SEND),ft.Text("Enviar Mensaje", color=ft.colors.BLACK87, weight=ft.FontWeight.W_500, size=15)]),
                            alignment=ft.alignment.top_left,
                            height=25,
                            padding = ft.padding.only(left=20, top=0),
                            margin = ft.margin.only(top=10),
                            on_click=lambda _: print("Mensaje Enviado!"),
                        ),
                        ft.Container(
                            content=ft.Row([ft.Icon(name=ft.icons.CHAT),ft.Text("Ver Conversaciones", color=ft.colors.BLACK87, weight=ft.FontWeight.W_500, size=15)]),
                            alignment=ft.alignment.top_left,
                            height=25,
                            padding = ft.padding.only(left=20, top=0),
                            margin = ft.margin.only(top=10),
                            on_click=lambda _: print("Conversación Mostrada"),
                        ),
                        ft.Container(
                            content=ft.Text("Contenido", color=ft.colors.BLACK87, weight=ft.FontWeight.W_700, size=20),
                            alignment=ft.alignment.top_left,
                            height=25,
                            padding = ft.padding.only(left=20, top=0),
                            margin = ft.margin.only(top=20),
                        ),
                        ft.Container(
                            content=ft.Row([ft.Icon(name=ft.icons.BOOKMARK_BORDER_ROUNDED),ft.Text("Guías de Aprendizaje", color=ft.colors.BLACK87, weight=ft.FontWeight.W_500, size=15)]),
                            alignment=ft.alignment.top_left,
                            height=25,
                            padding = ft.padding.only(left=20, top=0),
                            margin = ft.margin.only(top=10),
                            on_click=lambda _: print("Mensaje Enviado!"),
                        ),
                        ft.Container(
                            content=ft.Row([ft.Icon(name=ft.icons.LIBRARY_BOOKS),ft.Text("Material de Formación", color=ft.colors.BLACK87, weight=ft.FontWeight.W_500, size=15)]),
                            alignment=ft.alignment.top_left,
                            height=25,
                            padding = ft.padding.only(left=20, top=0),
                            margin = ft.margin.only(top=10),
                            on_click=lambda _: print("Mensaje Enviado!"),
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
                    content=ft.Column(controls=[
                        ft.Container(
                            content=ft.Text("Territorium Flow", theme_style=ft.TextThemeStyle.HEADLINE_LARGE, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK87, weight=ft.FontWeight.W_700),
                            alignment=ft.alignment.center,
                            height=60,
                            margin = ft.margin.only(top=30),
                        ),
                        ft.Container(
                            content=ft.Text("Guías de Aprendizaje", color=ft.colors.BLACK87, weight=ft.FontWeight.W_500, size=15),
                            alignment=ft.alignment.top_left,
                            height=25,
                            padding = ft.padding.only(left=20, top=0),
                            margin = ft.margin.only(top=10),
                            on_click=lambda _: print("Mensaje Enviado!"),
                        ),
                    ])
                ),
            ],
            spacing=0,
            expand=True,
        )
    )

    page.update()

ft.app(target=main)