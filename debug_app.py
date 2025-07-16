import flet as ft

def main(page: ft.Page):
    print("Debug page initialized")
    
    page.title = "ATV Debug"
    page.bgcolor = "#0a0a1a"
    
    # Test splash screen yang sederhana
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Icon(ft.Icons.FLASH_ON, size=60, color="#06b6d4"),
                ft.Text("ATV", size=32, color="white", weight=ft.FontWeight.BOLD),
                ft.Text("AUTOTRADEVIP", size=16, color="#06b6d4"),
                ft.ProgressBar(width=200, color="#06b6d4"),
                ft.Text("Testing Migration...", size=14, color="white"),
            ], 
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            bgcolor="#0a0a1a",
            width=page.window_width,
            height=page.window_height,
            alignment=ft.alignment.center
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=main, port=5000, host="0.0.0.0")