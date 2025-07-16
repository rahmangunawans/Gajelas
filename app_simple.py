import flet as ft
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from core.pages.auth_handler import AuthHandler
from services.database.postgres_manager import PostgresManager
from core.styles import AppStyles
from config.app_config import AppConfig
from utils.logger import logger

class SimpleATVApp:
    def __init__(self):
        self.db_manager = PostgresManager()
        self.styles = AppStyles()
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
        page.theme_mode = ft.ThemeMode.DARK
        
        # Initialize database
        try:
            self.db_manager.init_db()
            logger.info("Database initialized successfully")
        except Exception as e:
            logger.error(f"Database initialization error: {e}")
        
        # Go directly to auth (skip splash screen)
        self.show_auth()
        
    def show_auth(self):
        """Show authentication directly"""
        auth_handler = AuthHandler(self.page, self.navigate_to_dashboard)
        auth_handler.show_login()
        
    def navigate_to_dashboard(self, user_data):
        """Navigate to main dashboard after successful login"""
        from core.pages.dashboard import Dashboard
        dashboard = Dashboard(self.page, user_data)
        dashboard.build()

def main(page: ft.Page):
    """Main application entry point"""
    try:
        logger.info("Starting Simplified ATV Mobile Application")
        app = SimpleATVApp()
        app.setup_page(page)
    except Exception as e:
        logger.error(f"Error in main application: {e}")
        page.add(ft.Text(f"Error: {e}", color=ft.Colors.RED))
        page.update()

if __name__ == "__main__":
    logger.info("🚀 Starting Simplified ATV Mobile Application...")
    logger.info("📱 Mobile-first design optimized for 375x812 (iPhone X/11)")
    logger.info("🌐 Access: http://localhost:6000")
    logger.info("👤 Admin login: admin@atv.com / admin123")
    
    try:
        ft.app(
            target=main, 
            port=6000, 
            host="0.0.0.0",
            view=ft.AppView.WEB_BROWSER
        )
    except Exception as e:
        logger.critical(f"Critical error starting application: {e}")
        import traceback
        logger.error(traceback.format_exc())