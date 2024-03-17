import flet as ft

def main(page: ft.Page):
    cl = ft.Column(
        spacing=10,
        height=200,
        width=200,
        scroll=ft.ScrollMode.ALWAYS,
    )

    # Agregar 100 elementos iniciales
    for i in range(0, 100):
        cl.controls.append(ft.Text(f"Text line {i}", key=str(i)))

    page.add(ft.Container(cl, border=ft.border.all(1)))

ft.app(main)