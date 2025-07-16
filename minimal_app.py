import flet as ft

def main(page: ft.Page):
    """Minimal working ATV app"""
    page.title = "ATV - AUTOTRADEVIP"
    page.bgcolor = "#0a0a1a"
    page.window_width = 375
    page.window_height = 812
    
    # Show simple splash screen
    content = ft.Column([
        ft.Container(height=150),
        ft.Icon(ft.Icons.FLASH_ON, size=80, color="#06b6d4"),
        ft.Container(height=20),
        ft.Text("ATV", size=36, color="white", weight=ft.FontWeight.BOLD),
        ft.Text("AUTOTRADEVIP", size=16, color="#06b6d4"),
        ft.Container(height=40),
        ft.ProgressBar(width=200, color="#06b6d4", bgcolor="#1e293b"),
        ft.Container(height=20),
        ft.Text("Migrasi Berhasil!", size=14, color="#10b981"),
        ft.Container(height=30),
        ft.Text("Kredensial Login:", size=12, color="#94a3b8"),
        ft.Text("admin@atv.com / admin123", size=12, color="#06b6d4", weight=ft.FontWeight.BOLD),
    ], 
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    
    page.add(
        ft.Container(
            content=content,
            width=page.window_width,
            height=page.window_height,
            bgcolor="#0a0a1a",
            alignment=ft.alignment.center
        )
    )
    page.update()

if __name__ == "__main__":
    print("🚀 ATV Minimal App - Migration Complete")
    ft.app(target=main, port=5000, host="0.0.0.0", view=ft.AppView.WEB_BROWSER)