import flet as ft
import sys
import os
import time
import threading

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from core.pages.splash_screen import SplashScreen
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
        self.is_initialized = False
        
    def setup_page(self, page: ft.Page):
        """Configure the main page settings"""
        if self.is_initialized:
            return
            
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
        
        # Initialize database once
        try:
            self.db_manager.init_db()
            print("Database initialized successfully")
        except Exception as e:
            print(f"Database initialization error: {e}")
        
        # Mark as initialized to prevent loops
        self.is_initialized = True
        
        # Start with splash screen
        self.show_splash_screen()
        
    def show_splash_screen(self):
        """Show splash screen with all original animations"""
        try:
            splash_screen = SplashScreen(self.page, self.navigate_to_auth)
            splash_screen.build()
        except Exception as e:
            print(f"Splash error: {e}")
            # Fallback navigation
            time.sleep(2)
            self.navigate_to_auth()
        
    def navigate_to_auth(self):
        """Navigate to authentication pages"""
        try:
            self.current_page = AuthHandler(self.page, self.navigate_to_dashboard)
            self.current_page.show_login()
        except Exception as e:
            print(f"Auth navigation error: {e}")
        
    def navigate_to_dashboard(self, user_data):
        """Navigate to main dashboard after successful login"""
        try:
            from core.pages.dashboard import Dashboard
            dashboard = Dashboard(self.page, user_data)
            dashboard.build()
        except Exception as e:
            print(f"Dashboard error: {e}")

def main(page: ft.Page):
    """Main application entry point"""
    try:
        app = ATVApp()
        app.setup_page(page)
    except Exception as e:
        print(f"Error in main: {e}")
        page.add(ft.Text(f"Error: {e}", color=ft.Colors.RED))
        page.update()

if __name__ == "__main__":
    print("🚀 Starting ATV Mobile Application...")
    print("📱 Mobile-first design optimized for 375x812 (iPhone X/11)")
    print("🌐 Access: http://localhost:5000")
    print("👤 Admin login: admin@atv.com / admin123")
    
    try:
        ft.app(
            target=main, 
            port=5000, 
            host="0.0.0.0",
            view=ft.AppView.WEB_BROWSER
        )
    except Exception as e:
        print(f"Error starting app: {e}")
        import traceback
        traceback.print_exc()