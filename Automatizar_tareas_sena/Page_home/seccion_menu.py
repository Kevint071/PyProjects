import flet as ft


def seccion_menu():
  return ft.Container(
        content=ft.Column(
            [
                # ft.Container(
                #     content=ft.Text("Opciones Automatizadas", color=ft.colors.GREY_600, weight=ft.FontWeight.W_600, size=15),
                #     alignment=ft.alignment.top_left ,
                #     height=20,
                #     padding = ft.padding.only(top=0, right=10, bottom=0, left=20),
                #     margin = ft.margin.only(top=10, bottom=-10),
                    
                # ),
                ft.Container(
                    content=ft.Text("Evidencias", color=ft.colors.BLACK87, weight=ft.FontWeight.W_700, size=20),
                    alignment=ft.alignment.top_left,
                    height=25,
                    padding = ft.padding.only(left=20, top=0),
                    margin = ft.margin.only(top=30),
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
                    on_click=lambda _: print("Guías de Aprendizaje Mostradas!"),
                ),
                ft.Container(
                    content=ft.Row([ft.Icon(name=ft.icons.LIBRARY_BOOKS),ft.Text("Material de Formación", color=ft.colors.BLACK87, weight=ft.FontWeight.W_500, size=15)]),
                    alignment=ft.alignment.top_left,
                    height=25,
                    padding = ft.padding.only(left=20, top=0),
                    margin = ft.margin.only(top=10),
                    on_click=lambda _: print("Material de Formación Mostrado!"),
                ),
                ft.Container(
                    content=ft.Text("Foros", color=ft.colors.BLACK87, weight=ft.FontWeight.W_700, size=20),
                    alignment=ft.alignment.top_left,
                    height=25,
                    padding = ft.padding.only(left=20, top=0),
                    margin = ft.margin.only(top=20),
                ),
                ft.Container(
                    content=ft.Row([ft.Icon(name=ft.icons.BOOKMARK_BORDER_ROUNDED),ft.Text("Foros sin Contestar", color=ft.colors.BLACK87, weight=ft.FontWeight.W_500, size=15)]),
                    alignment=ft.alignment.top_left,
                    height=25,
                    padding = ft.padding.only(left=20, top=0),
                    margin = ft.margin.only(top=10),
                    on_click=lambda _: print("Foros sin Contestar Mostrados!"),
                ),
                ft.Container(
                    content=ft.Row([ft.Icon(name=ft.icons.LIBRARY_BOOKS),ft.Text("Foros Contestados", color=ft.colors.BLACK87, weight=ft.FontWeight.W_500, size=15)]),
                    alignment=ft.alignment.top_left,
                    height=25,
                    padding = ft.padding.only(left=20, top=0),
                    margin = ft.margin.only(top=10, bottom=20),
                    on_click=lambda _: print("Foros Contestados Mostrados!"),
                ),
            ],
            spacing=20,
            scroll=ft.ScrollMode.ALWAYS,
            width=250,
        ),
        alignment=ft.alignment.top_center,
        bgcolor="#EEF2F5",
        width=250,
    ) 