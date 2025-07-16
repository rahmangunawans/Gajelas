import flet as ft

def main(page: ft.Page):
    page.title = "Test App"
    page.add(ft.Text("Hello ATV!", size=30, color=ft.Colors.WHITE))
    page.bgcolor = "#0a0a1a"
    page.update()

if __name__ == "__main__":
    print("Testing simple Flet app...")
    ft.app(target=main, port=5001, host="0.0.0.0", view=ft.AppView.WEB_BROWSER)