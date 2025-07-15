import flet as ft
from pages.splash_screen import SplashScreen
from pages.auth_handler import AuthHandler
from database.postgres_manager import PostgresManager
from styles import AppStyles
import os

class ATVApp:
    def __init__(self):
        self.db_manager = PostgresManager()
        self.styles = AppStyles()
        self.current_page = None
        self.page = None
        
    def setup_page(self, page: ft.Page):
        """Configure the main page settings"""
        self.page = page
        page.title = "ATV - AUTOTRADEVIP"
        page.window_width = 375
        page.window_height = 812
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
        splash_screen = SplashScreen(self.page, self.navigate_to_auth)
        splash_screen.build()
        splash_screen.start_splash_sequence()
        
    def navigate_to_auth(self):
        """Navigate to authentication pages"""
        self.current_page = AuthHandler(self.page, self.navigate_to_dashboard)
        self.current_page.show_login()
        
    def navigate_to_dashboard(self, user_data):
        """Navigate to main dashboard after successful login"""
        from pages.dashboard import Dashboard
        
        # Create and show dashboard
        dashboard = Dashboard(self.page, user_data)
        dashboard.build()

def main(page: ft.Page):
    """Main application entry point"""
    app = ATVApp()
    app.setup_page(page)

if __name__ == "__main__":
    print("🚀 Starting ATV Mobile Application...")
    print("📱 Mobile-first design optimized for 375x812 (iPhone X/11)")
    print("🌐 Access: http://localhost:5000")
    print("👤 Admin login: admin@atv.com / admin123")
    ft.app(target=main, port=5000, host="0.0.0.0", view=ft.AppView.WEB_BROWSER)