import flet as ft
import sys
import os
import time
import threading

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from core.pages.auth_handler import AuthHandler
from services.database.postgres_manager import PostgresManager
from core.styles import AppStyles
from config.app_config import AppConfig
from utils.logger import logger

# Global initialization flag
_initialized = False

class ATVApp:
    def __init__(self):
        self.db_manager = PostgresManager()
        self.styles = AppStyles()
        self.current_page = None
        self.page = None
        
    def setup_page(self, page: ft.Page):
        """Configure the main page settings"""
        global _initialized
        
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
        
        # Initialize database only once
        if not _initialized:
            try:
                self.db_manager.init_db()
                logger.info("Database initialized successfully")
                _initialized = True
            except Exception as e:
                logger.error(f"Database initialization error: {e}")
        
        # Show original sophisticated splash screen
        from core.pages.splash_screen import SplashScreen
        splash_screen = SplashScreen(self.page, self.navigate_to_auth)
        splash_screen.build()
        splash_screen.start_splash_sequence()
        

        
    def navigate_to_auth(self):
        """Navigate to authentication pages"""
        logger.debug("Navigating to authentication")
        self.current_page = AuthHandler(self.page, self.navigate_to_dashboard)
        self.current_page.show_login()
        
    def navigate_to_dashboard(self, user_data):
        """Navigate to main dashboard after successful login"""
        logger.info(f"User {user_data.get('email')} logged in successfully")
        from core.pages.dashboard import Dashboard
        dashboard = Dashboard(self.page, user_data)
        dashboard.build()

def main(page: ft.Page):
    """Main application entry point"""
    try:
        logger.info("Starting ATV Mobile Application with sophisticated design")
        app = ATVApp()
        app.setup_page(page)
    except Exception as e:
        logger.error(f"Error in main application: {e}")
        page.add(ft.Text(f"Error: {e}", color=ft.Colors.RED))
        page.update()

if __name__ == "__main__":
    logger.info("🚀 Starting ATV Mobile - Sophisticated Design")
    logger.info("📱 Mobile-first design optimized for 375x812 (iPhone X/11)")
    logger.info("🌐 Access: http://localhost:5000")
    logger.info("👤 Admin login: admin@atv.com / admin123")
    
    try:
        ft.app(
            target=main, 
            port=5000, 
            host="0.0.0.0",
            view=ft.AppView.WEB_BROWSER
        )
    except Exception as e:
        logger.critical(f"Critical error starting application: {e}")
        import traceback
        logger.error(traceback.format_exc())