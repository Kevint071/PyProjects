import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de Sesión"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Campos de entrada de texto
    usuario_input = ft.TextField(label="Usuario")
    contrasena_input = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)

    # Función para validar el inicio de sesión
    def iniciar_sesion(e):
        usuario = usuario_input.value
        contrasena = contrasena_input.value
        # Aquí deberías implementar la lógica para validar las credenciales
        # contra tu base de datos o sistema de autenticación
        if usuario == "admin" and contrasena == "contraseña":
            page.window_center()
            page.add(ft.Text("Inicio de sesión exitoso"))
        else:
            page.add(ft.Text("Credenciales incorrectas", color="red"))

    # Botón de inicio de sesión
    boton_iniciar_sesion = ft.ElevatedButton("Iniciar Sesión", on_click=iniciar_sesion)

    # Agregamos los campos y el botón al formulario
    page.add(usuario_input, contrasena_input, boton_iniciar_sesion)

ft.app(target=main)