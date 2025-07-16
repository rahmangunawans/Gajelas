import flet as ft

def main(page: ft.Page):
    page.title = "ATV Test"
    page.bgcolor = "#0a0a1a"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 375
    page.window_height = 812
    
    # Test simple splash screen
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("🚀 ATV", size=48, color="white", weight=ft.FontWeight.BOLD),
                ft.Text("AUTOTRADEVIP", size=24, color="#06b6d4"),
                ft.ProgressBar(width=200, color="#1e3a8a"),
                ft.Text("Loading...", size=16, color="white")
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20),
            expand=True,
            alignment=ft.alignment.center,
            bgcolor="#0a0a1a"
        )
    )

if __name__ == "__main__":
    ft.app(target=main, port=5000, host="0.0.0.0", view=ft.AppView.WEB_BROWSER)