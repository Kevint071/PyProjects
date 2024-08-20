import flet as ft


def texto_title():
    return ft.Container(
              content=ft.Text("¿Qué juego quieres jugar?", color=ft.colors.WHITE, weight=ft.FontWeight.W_500, size=17),
              alignment=ft.alignment.center,
              height=25,
              padding = ft.padding.only(left=0, top=0),
              margin = ft.margin.only(top=15)
          )