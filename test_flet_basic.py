import flet as ft

def main(page: ft.Page):
    page.title = "Test Flet"
    page.bgcolor = "#0a0a1a"
    page.add(
        ft.Text("Hello from Flet!", color="white", size=20)
    )

if __name__ == "__main__":
    print("Starting basic Flet test...")
    ft.app(target=main, port=5000, host="0.0.0.0", view=ft.AppView.WEB_BROWSER)