import flet as ft
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main(page: ft.Page):
    page.title = "ATV Test"
    page.bgcolor = "#0a0a1a"
    page.window_width = 375
    page.window_height = 812
    
    # Simple test content
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("ATV", size=32, color=ft.Colors.WHITE),
                ft.Text("Test Application", size=16, color=ft.Colors.CYAN),
                ft.ElevatedButton("Test Button", on_click=lambda e: print("Button clicked")),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            alignment=ft.alignment.center,
            bgcolor="#151528",
            padding=20,
            margin=20,
            border_radius=10,
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=main, port=8000, host="0.0.0.0", view=ft.AppView.WEB_BROWSER)