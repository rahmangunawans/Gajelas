import flet as ft

def main(page: ft.Page):
    page.title = "Test App"
    page.window_width = 375
    page.window_height = 812
    page.bgcolor = "#0a0a1a"
    
    page.add(
        ft.Text(
            "Test Application Running",
            size=20,
            color=ft.Colors.WHITE,
            text_align=ft.TextAlign.CENTER,
        )
    )

if __name__ == "__main__":
    ft.app(target=main, port=5000, host="0.0.0.0", view=ft.AppView.WEB_BROWSER)