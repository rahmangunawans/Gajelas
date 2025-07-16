import flet as ft
import time
import threading
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from core.styles import AppStyles
from services.database.postgres_manager import PostgresManager

class SimpleATVApp:
    def __init__(self):
        self.db_manager = PostgresManager()
        self.styles = AppStyles()
        
    def main(self, page: ft.Page):
        page.title = "ATV - AUTOTRADEVIP"
        page.window_width = 375
        page.window_height = 812
        page.bgcolor = self.styles.PRIMARY_COLOR
        page.theme_mode = ft.ThemeMode.DARK
        
        # Initialize database once
        try:
            self.db_manager.init_db()
            print("Database ready")
        except Exception as e:
            print(f"DB error: {e}")
        
        # Show splash
        self.show_splash(page)
        
    def show_splash(self, page):
        page.add(
            ft.Container(
                content=ft.Column([
                    ft.Container(height=100),
                    ft.Icon(ft.Icons.FLASH_ON, size=80, color="#06b6d4"),
                    ft.Text("ATV", size=36, color="white", weight=ft.FontWeight.BOLD),
                    ft.Text("AUTOTRADEVIP", size=16, color="#06b6d4"),
                    ft.Container(height=40),
                    ft.ProgressBar(width=200, color="#06b6d4", bgcolor="#334155"),
                    ft.Container(height=20),
                    ft.Text("Loading...", size=14, color="#94a3b8"),
                ], 
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                width=375,
                height=812,
                bgcolor=self.styles.PRIMARY_COLOR,
                alignment=ft.alignment.center
            )
        )
        page.update()
        
        # Navigate to login after delay
        def navigate_after_delay():
            time.sleep(3)
            self.show_login(page)
            
        thread = threading.Thread(target=navigate_after_delay)
        thread.daemon = True
        thread.start()
        
    def show_login(self, page):
        page.clean()
        
        email_field = ft.TextField(
            label="Email",
            hint_text="admin@atv.com",
            border_color="#475569",
            focused_border_color="#06b6d4",
        )
        
        password_field = ft.TextField(
            label="Password", 
            hint_text="admin123",
            password=True,
            border_color="#475569",
            focused_border_color="#06b6d4",
        )
        
        def handle_login(e):
            email = email_field.value
            password = password_field.value
            
            if not email or not password:
                return
                
            try:
                user = self.db_manager.authenticate_user(email, password)
                if user:
                    self.show_success(page, user)
                else:
                    print("Login failed")
            except Exception as ex:
                print(f"Login error: {ex}")
        
        page.add(
            ft.Container(
                content=ft.Column([
                    ft.Container(height=50),
                    ft.Text("Login ATV", size=28, color="white", weight=ft.FontWeight.BOLD),
                    ft.Container(height=30),
                    email_field,
                    ft.Container(height=10),
                    password_field,
                    ft.Container(height=30),
                    ft.ElevatedButton(
                        "Login",
                        on_click=handle_login,
                        bgcolor="#06b6d4",
                        color="white",
                        width=250,
                        height=45
                    ),
                ], 
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                width=375,
                height=812,
                bgcolor=self.styles.PRIMARY_COLOR,
                alignment=ft.alignment.center,
                padding=20
            )
        )
        page.update()
        
    def show_success(self, page, user):
        page.clean()
        
        page.add(
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.CHECK_CIRCLE, size=80, color="#10b981"),
                    ft.Text("Login Berhasil!", size=24, color="white"),
                    ft.Text(f"Selamat datang {user['full_name']}", size=16, color="#06b6d4"),
                    ft.Text(f"Admin: {'Ya' if user['is_admin'] else 'Tidak'}", size=14, color="#94a3b8"),
                ], 
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                width=375,
                height=812,
                bgcolor=self.styles.PRIMARY_COLOR,
                alignment=ft.alignment.center
            )
        )
        page.update()

if __name__ == "__main__":
    print("🚀 Starting Simple ATV App...")
    app = SimpleATVApp()
    ft.app(target=app.main, port=5000, host="0.0.0.0", view=ft.AppView.WEB_BROWSER)