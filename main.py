"""
Aplicación en Flet: ventana con un botón.
Al presionar el botón, se actualiza un texto en pantalla.

Ejecutar en modo escritorio (ventana activa):
    flet run main.py

Construir el ejecutable para Windows:
    flet build windows
"""

import flet as ft


def main(page: ft.Page):
    # --- Configuración de la ventana ---
    page.title = "Mi Primera App con Flet"
    page.window.width = 400
    page.window.height = 300
    page.window.resizable = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.BLUE_GREY_50

    # --- Texto que se actualizará al presionar el botón ---
    mensaje = ft.Text(
        value="Presiona el botón para comenzar",
        size=18,
        weight=ft.FontWeight.W_500,
        color=ft.Colors.BLUE_GREY_800,
        text_align=ft.TextAlign.CENTER,
    )

    contador = ft.Text(value="Clics: 0", size=14, color=ft.Colors.BLUE_GREY_500)
    clics = {"total": 0}

    # --- Lógica del botón ---
    def al_hacer_clic(e):
        clics["total"] += 1
        mensaje.value = "¡Botón presionado! 🎉"
        contador.value = f"Clics: {clics['total']}"
        page.update()

    boton = ft.Button(
        content="Haz clic aquí",
        icon=ft.Icons.TOUCH_APP,
        on_click=al_hacer_clic,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_600,
            color=ft.Colors.WHITE,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=8),
        ),
    )

    # --- Estructura de la ventana ---
    page.add(
        ft.Column(
            controls=[
                ft.Icon(ft.Icons.ROCKET_LAUNCH, size=48, color=ft.Colors.BLUE_600),
                mensaje,
                boton,
                contador,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )


if __name__ == "__main__":
    ft.run(main)
