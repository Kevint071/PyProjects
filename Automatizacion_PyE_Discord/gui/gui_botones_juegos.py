import flet as ft
from globals import variables_globales

def obtener_nombre_juego(juego: str):
    variables_globales["juego"] = juego


def botones_juegos(page: ft.Page):
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.ElevatedButton(
                    content=ft.Container(
                        content=ft.Row(
                            [ft.Text("Slots", size=16, weight=ft.FontWeight.BOLD)],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=ft.padding.all(8),
                    ),
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.GREY_900,
                        color=ft.colors.GREY_200,
                        shape=ft.RoundedRectangleBorder(radius=8),
                        side=ft.BorderSide(2, ft.colors.GREY_400),
                        elevation=4,
                        shadow_color=ft.colors.BLACK54,
                    ),
                    on_click=lambda _: (obtener_nombre_juego("Slots"), page.window_close()),
                ),
                ft.ElevatedButton(
                    content=ft.Container(
                        content=ft.Row(
                            [ft.Text("Ruleta", size=16, weight=ft.FontWeight.BOLD)],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=ft.padding.all(8),
                    ),
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.GREY_900,
                        color=ft.colors.GREY_200,
                        shape=ft.RoundedRectangleBorder(radius=8),
                        side=ft.BorderSide(2, ft.colors.GREY_400),
                        elevation=4,
                        shadow_color=ft.colors.BLACK54,
                    ),
                    on_click=lambda _: (obtener_nombre_juego("Ruleta"), page.window_close()),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        ),
        alignment=ft.alignment.center,
        margin=ft.margin.only(top=20),
    )