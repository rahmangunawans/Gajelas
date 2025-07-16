import flet as ft
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from core.pages.splash_screen import SplashScreen
from core.pages.auth_handler import AuthHandler
from services.database.postgres_manager import PostgresManager
from core.styles import AppStyles
from config.app_config import AppConfig
from utils.logger import logger

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
        
        # Initialize database safely (only once)
        if not hasattr(self, 'db_initialized'):
            try:
                self.db_manager.init_db()
                logger.info("Database initialized successfully")
                self.db_initialized = True
            except Exception as e:
                logger.error(f"Database initialization error: {e}")
                self.db_initialized = False
        
        # Start with splash screen
        self.show_splash_screen()
        
    def show_splash_screen(self):
        """Show splash screen"""
        try:
            splash_screen = SplashScreen(self.page, self.navigate_to_auth)
            splash_screen.build()
            splash_screen.start_splash_sequence()
        except Exception as e:
            logger.error(f"Error showing splash screen: {e}")
            # Simple fallback
            self.page.add(
                ft.Container(
                    content=ft.Column([
                        ft.Text("ATV", size=48, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                        ft.Text("AUTOTRADEVIP", size=16, color="#06b6d4"),
                        ft.Container(height=20),
                        ft.Text("Loading...", size=14, color=ft.Colors.WHITE),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                    ),
                    expand=True,
                    alignment=ft.alignment.center,
                    bgcolor="#0a0a1a",
                )
            )
            self.page.update()
            # Navigate to auth after 3 seconds
            import threading
            import time
            def delayed_auth():
                time.sleep(3)
                self.navigate_to_auth()
            threading.Thread(target=delayed_auth, daemon=True).start()
        
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
    try:
        logger.info("Starting ATV Mobile Application")
        # Simple test first
        page.title = "ATV - AUTOTRADEVIP"
        page.window_width = 375
        page.window_height = 812
        page.bgcolor = "#0a0a1a"
        page.padding = 20
        
        # Add simple content first
        page.add(
            ft.Container(
                content=ft.Column([
                    ft.Text("ATV", size=48, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                    ft.Text("AUTOTRADEVIP", size=16, color="#06b6d4"),
                    ft.Container(height=20),
                    ft.Text("Mobile Trading Application", size=14, color=ft.Colors.WHITE70),
                    ft.Container(height=30),
                    ft.ElevatedButton(
                        "Continue to App",
                        on_click=lambda e: load_full_app(page),
                        bgcolor="#06b6d4",
                        color=ft.Colors.WHITE,
                        width=200,
                        height=50,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                ),
                expand=True,
                alignment=ft.alignment.center,
            )
        )
        page.update()
        
    except Exception as e:
        logger.error(f"Error in main application: {e}")
        page.add(ft.Text(f"Error: {e}", color=ft.Colors.RED))
        page.update()

def load_full_app(page):
    """Load the full ATV application"""
    try:
        page.controls.clear()
        app = ATVApp()
        app.setup_page(page)
    except Exception as e:
        logger.error(f"Error loading full app: {e}")
        page.add(ft.Text(f"Error loading app: {e}", color=ft.Colors.RED))
        page.update()

if __name__ == "__main__":
    logger.info("🚀 Starting ATV Mobile Application...")
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