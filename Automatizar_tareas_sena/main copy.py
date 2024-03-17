import flet as ft

def main(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Contenedor principal con distribución horizontal
    main_container = ft.Row(
        expand=True,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    # Sección 1 (izquierda)
    section1 = ft.Container(
        content=ft.Text("Sección 1", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        alignment=ft.alignment.center,
        width=250,
        bgcolor=ft.colors.BLACK,
    )

    # Sección 2 (derecha)
    section2 = ft.Container(
        content=ft.Column(
            [
                ft.Text("Sección 2", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                ft.Text("Contenido en la parte inferior", style=ft.TextThemeStyle.BODY_MEDIUM),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    
        alignment=ft.alignment.center,
        expand=True,
        bgcolor=ft.colors.YELLOW,
    )

    main_container.controls.append(section1)
    main_container.controls.append(ft.VerticalDivider(width=1, color="#000000"))
    main_container.controls.append(section2)

    page.add(main_container)

ft.app(target=main)