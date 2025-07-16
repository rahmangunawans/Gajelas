import flet as ft

def main(page: ft.Page):
    page.title = "Test ATV App"
    page.add(ft.Text("Hello World - ATV Application Test"))
    
if __name__ == "__main__":
    ft.app(target=main, port=5001, host="0.0.0.0", view=ft.AppView.WEB_BROWSER)