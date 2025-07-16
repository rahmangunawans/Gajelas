import flet as ft
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from core.pages.splash_simple import SplashScreen
from core.pages.auth_handler import AuthHandler
from services.database.postgres_manager import PostgresManager
from core.styles import AppStyles
from config.app_config import AppConfig

class ATVApp:
    def __init__(self):
        self.db_manager = PostgresManager()
        self.styles = AppStyles()
        self.current_page = None
        self.page = None
        
    def setup_page(self, page: ft.Page):
        """Configure the main page settings"""
        self.page = page
        page.title = AppConfig.APP_NAME
        page.window_width = AppConfig.MOBILE_WIDTH
        page.window_height = AppConfig.MOBILE_HEIGHT
        page.padding = 0
        page.spacing = 0
        page.bgcolor = self.styles.PRIMARY_COLOR
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.DARK
        
        # Initialize database
        self.db_manager.init_db()
        
        # Start with splash screen
        self.show_splash_screen()
        
    def show_splash_screen(self):
        """Show splash screen"""
        # Create simple splash with direct UI
        self.page.add(
            ft.Container(
                content=ft.Column([
                    ft.Container(height=200),
                    ft.Text(
                        "ATV",
                        size=36,
                        weight=ft.FontWeight.BOLD,
                        color=self.styles.TEXT_PRIMARY,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        "AUTOTRADEVIP",
                        size=16,
                        weight=ft.FontWeight.W_600,
                        color=self.styles.TEXT_SECONDARY,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(height=50),
                    ft.ProgressBar(
                        width=200,
                        height=4,
                        color=self.styles.TEXT_SECONDARY,
                        bgcolor=self.styles.PROGRESS_BG,
                    ),
                    ft.Container(height=20),
                    ft.Text(
                        "Loading...",
                        size=14,
                        color=self.styles.TEXT_SECONDARY,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(height=50),
                    ft.ElevatedButton(
                        "GET STARTED",
                        on_click=lambda _: self.navigate_to_auth(),
                        bgcolor=self.styles.TEXT_SECONDARY,
                        color=ft.Colors.WHITE,
                        width=200,
                    ),
                ], 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0),
                width=self.styles.MOBILE_WIDTH,
                height=self.styles.MOBILE_HEIGHT,
                bgcolor=self.styles.PRIMARY_COLOR,
                alignment=ft.alignment.center,
            )
        )
        self.page.update()
        
    def navigate_to_auth(self):
        """Navigate to authentication pages"""
        self.current_page = AuthHandler(self.page, self.navigate_to_dashboard)
        self.current_page.show_login()
        
    def navigate_to_dashboard(self, user_data):
        """Navigate to main dashboard after successful login"""
        from core.pages.dashboard import Dashboard
        
        # Create and show dashboard
        dashboard = Dashboard(self.page, user_data)
        dashboard.build()

def main(page: ft.Page):
    """Main application entry point"""
    page.title = "ATV - AUTOTRADEVIP"
    page.window_width = 375
    page.window_height = 812
    page.padding = 20
    page.bgcolor = "#0a0a1a"
    page.theme_mode = ft.ThemeMode.DARK
    
    # Add simple content first
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text(
                    "ATV",
                    size=36,
                    weight=ft.FontWeight.BOLD,
                    color="#ffffff",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "AUTOTRADEVIP",
                    size=16,
                    weight=ft.FontWeight.W_600,
                    color="#06b6d4",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=30),
                ft.ElevatedButton(
                    "GET STARTED",
                    bgcolor="#06b6d4",
                    color=ft.Colors.WHITE,
                    width=200,
                    on_click=lambda _: start_app(page),
                ),
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            alignment=ft.alignment.center,
            expand=True,
        )
    )
    
def start_app(page):
    """Start the full application"""
    try:
        app = ATVApp()
        app.setup_page(page)
    except Exception as e:
        page.add(ft.Text(f"Error: {str(e)}", color="red"))
        page.update()

if __name__ == "__main__":
    print("🚀 Starting ATV Mobile Application...")
    print("📱 Mobile-first design optimized for 375x812 (iPhone X/11)")
    print("🌐 Access: http://localhost:5000")
    print("👤 Admin login: admin@atv.com / admin123")
    ft.app(target=main, port=5000, host="0.0.0.0", view=ft.AppView.WEB_BROWSER)