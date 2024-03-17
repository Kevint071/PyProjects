import flet as ft

def seccion_contenido():
  return ft.Container(
      bgcolor="#FFFFFF",
      alignment=ft.alignment.top_center,
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
      ],
      spacing=10,
      alignment=ft.MainAxisAlignment.START,
      ),
  )