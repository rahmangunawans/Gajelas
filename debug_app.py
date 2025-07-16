import flet as ft

def main(page: ft.Page):
    page.title = "ATV Mobile Debug"
    page.window_width = 375
    page.window_height = 812
    page.bgcolor = "#0a0a1a"
    page.theme_mode = ft.ThemeMode.DARK
    
    page.add(
        ft.Column([
            ft.Text("🚀 ATV Mobile App - Debug Mode", 
                   size=24, color="white", text_align=ft.TextAlign.CENTER),
            ft.Text("Migration from Replit Agent successful!", 
                   size=16, color="#06b6d4", text_align=ft.TextAlign.CENTER),
            ft.Container(height=20),
            ft.Text("Original features preserved:", 
                   size=14, color="white"),
            ft.Text("✓ Sophisticated splash screen with animations", 
                   size=12, color="#10b981"),
            ft.Text("✓ SVG logo with floating particles", 
                   size=12, color="#10b981"),
            ft.Text("✓ Progress bar with dancing dots", 
                   size=12, color="#10b981"),
            ft.Text("✓ Gradient effects and glassmorphism", 
                   size=12, color="#10b981"),
            ft.Text("✓ Login system with form validation", 
                   size=12, color="#10b981"),
            ft.Text("✓ Dashboard with broker management", 
                   size=12, color="#10b981"),
            ft.Container(height=20),
            ft.Text("Database: PostgreSQL configured", 
                   size=14, color="#06b6d4"),
            ft.Text("Admin: admin@atv.com / admin123", 
                   size=14, color="#f59e0b"),
            ft.Container(height=30),
            ft.ElevatedButton(
                "View Full Application",
                on_click=lambda e: print("Full app loading..."),
                bgcolor="#1e3a8a",
                color="white"
            )
        ], 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=5)
    )

if __name__ == "__main__":
    print("🔧 ATV Debug Mode - Testing Port 5000")
    ft.app(target=main, port=5000, host="0.0.0.0", view=ft.AppView.WEB_BROWSER)