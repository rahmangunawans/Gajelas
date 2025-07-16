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
        
        # Show sophisticated splash screen
        self.show_sophisticated_splash()
        
    def show_sophisticated_splash(self):
        """Show sophisticated splash screen with all original design"""
        try:
            # Clear page
            self.page.clean()
            
            # Create ATV logo with SVG-like styling
            logo = ft.Container(
                content=ft.Stack([
                    # Glow effect background
                    ft.Container(
                        width=120,
                        height=120,
                        border_radius=60,
                        bgcolor="#1e3a8a",
                        opacity=0.3,
                        blur=ft.Blur(sigma_x=10, sigma_y=10)
                    ),
                    # Main logo circle
                    ft.Container(
                        content=ft.Text(
                            "ATV",
                            size=32,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE,
                            text_align=ft.TextAlign.CENTER
                        ),
                        width=100,
                        height=100,
                        border_radius=50,
                        bgcolor=ft.LinearGradient(
                            colors=["#1e3a8a", "#3b82f6", "#06b6d4"],
                            begin=ft.alignment.top_left,
                            end=ft.alignment.bottom_right
                        ),
                        alignment=ft.alignment.center,
                        border=ft.border.all(2, "#06b6d4"),
                        shadow=ft.BoxShadow(
                            spread_radius=5,
                            blur_radius=15,
                            color="#06b6d4",
                            opacity=0.5
                        )
                    ),
                    # Floating particles
                    *[ft.Container(
                        width=6,
                        height=6,
                        border_radius=3,
                        bgcolor="#06b6d4",
                        opacity=0.7,
                        left=60 + (i * 20),
                        top=60 + (i * 15),
                        animate=ft.animation.Animation(
                            duration=2000 + (i * 200),
                            curve=ft.AnimationCurve.EASE_IN_OUT
                        )
                    ) for i in range(4)]
                ]),
                width=140,
                height=140,
                alignment=ft.alignment.center,
                opacity=0,
                animate_opacity=ft.animation.Animation(1000)
            )
            
            # Brand text with gradient effect
            brand_text = ft.Container(
                content=ft.Column([
                    ft.Text(
                        "AUTOTRADEVIP",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color="#06b6d4",
                        text_align=ft.TextAlign.CENTER,
                        style=ft.TextStyle(
                            shadow=ft.BoxShadow(
                                blur_radius=10,
                                color="#06b6d4",
                                opacity=0.5
                            )
                        )
                    ),
                    ft.Text(
                        "ROBOT TRADING & SIGNAL TRADING",
                        size=12,
                        color=ft.Colors.WHITE70,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.W300
                    )
                ], spacing=5),
                opacity=0,
                animate_opacity=ft.animation.Animation(1000)
            )
            
            # Progress bar with dancing dots
            progress_bar = ft.Container(
                content=ft.Column([
                    ft.ProgressBar(
                        width=280,
                        height=4,
                        bgcolor="#1e293b",
                        color="#06b6d4",
                        value=0,
                        border_radius=2
                    ),
                    ft.Container(height=10),
                    ft.Row([
                        *[ft.Container(
                            width=8,
                            height=8,
                            border_radius=4,
                            bgcolor="#06b6d4",
                            opacity=0.3,
                            animate_opacity=ft.animation.Animation(
                                duration=600,
                                curve=ft.AnimationCurve.EASE_IN_OUT
                            )
                        ) for _ in range(5)]
                    ], alignment=ft.MainAxisAlignment.CENTER, spacing=8),
                    ft.Container(height=10),
                    ft.Text("0%", size=14, color="#06b6d4", text_align=ft.TextAlign.CENTER)
                ]),
                opacity=0,
                animate_opacity=ft.animation.Animation(1000)
            )
            
            # Loading text
            loading_text = ft.Text(
                "Loading...",
                size=16,
                color=ft.Colors.WHITE70,
                text_align=ft.TextAlign.CENTER,
                opacity=0,
                animate_opacity=ft.animation.Animation(1000)
            )
            
            # Version text
            version_text = ft.Text(
                f"Version {AppConfig.APP_VERSION}",
                size=12,
                color=ft.Colors.WHITE38,
                text_align=ft.TextAlign.CENTER,
                opacity=0,
                animate_opacity=ft.animation.Animation(1000)
            )
            
            # Main splash container
            splash_container = ft.Container(
                content=ft.Column([
                    ft.Container(height=80),
                    logo,
                    ft.Container(height=40),
                    brand_text,
                    ft.Container(height=60),
                    progress_bar,
                    ft.Container(height=20),
                    loading_text,
                    ft.Container(height=40),
                    version_text,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                ),
                expand=True,
                alignment=ft.alignment.center,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[
                        self.styles.PRIMARY_COLOR,
                        self.styles.SECONDARY_COLOR,
                        self.styles.PRIMARY_COLOR
                    ]
                ),
            )
            
            # Add to page
            self.page.add(splash_container)
            self.page.update()
            
            # Start sophisticated animation sequence
            self.animate_sophisticated_splash(logo, brand_text, progress_bar, loading_text, version_text)
            
        except Exception as e:
            logger.error(f"Error in sophisticated splash: {e}")
            # Fallback
            self.show_simple_fallback()
    
    def animate_sophisticated_splash(self, logo, brand_text, progress_bar, loading_text, version_text):
        """Animate sophisticated splash screen"""
        def animation_sequence():
            try:
                # Phase 1: Show logo with glow
                time.sleep(0.5)
                logo.opacity = 1
                self.page.update()
                
                # Phase 2: Show brand text
                time.sleep(0.8)
                brand_text.opacity = 1
                self.page.update()
                
                # Phase 3: Show progress and loading
                time.sleep(0.6)
                progress_bar.opacity = 1
                loading_text.opacity = 1
                self.page.update()
                
                # Phase 4: Animate progress bar and dancing dots
                progress_control = progress_bar.content.controls[0]
                dots = progress_bar.content.controls[2].controls
                percentage_text = progress_bar.content.controls[4]
                
                for i in range(101):
                    # Update progress
                    progress_control.value = i / 100
                    percentage_text.value = f"{i}%"
                    
                    # Animate dancing dots
                    for j, dot in enumerate(dots):
                        cycle = (i + j * 20) % 60
                        if cycle < 20:
                            dot.opacity = 0.3 + (cycle / 20) * 0.7
                        elif cycle < 40:
                            dot.opacity = 1.0 - ((cycle - 20) / 20) * 0.7
                        else:
                            dot.opacity = 0.3
                    
                    self.page.update()
                    time.sleep(0.03)
                
                # Phase 5: Show version
                time.sleep(0.5)
                version_text.opacity = 1
                self.page.update()
                
                # Phase 6: Wait then fade out
                time.sleep(1.5)
                
                # Fade out all elements
                logo.opacity = 0
                brand_text.opacity = 0
                progress_bar.opacity = 0
                loading_text.opacity = 0
                version_text.opacity = 0
                self.page.update()
                
                time.sleep(1.0)
                
                # Navigate to login
                self.navigate_to_auth()
                
            except Exception as e:
                logger.error(f"Animation error: {e}")
                time.sleep(3)
                self.navigate_to_auth()
        
        thread = threading.Thread(target=animation_sequence)
        thread.daemon = True
        thread.start()
    
    def show_simple_fallback(self):
        """Simple fallback splash"""
        self.page.clean()
        self.page.add(
            ft.Container(
                content=ft.Column([
                    ft.Text("ATV", size=48, color="white", weight=ft.FontWeight.BOLD),
                    ft.Text("AUTOTRADEVIP", size=24, color="#06b6d4"),
                    ft.ProgressBar(width=200, color="#1e3a8a"),
                    ft.Text("Loading...", size=16, color="white")
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20),
                expand=True,
                alignment=ft.alignment.center,
                bgcolor=self.styles.PRIMARY_COLOR
            )
        )
        self.page.update()
        
        def delayed_auth():
            time.sleep(3)
            self.navigate_to_auth()
        
        thread = threading.Thread(target=delayed_auth)
        thread.daemon = True
        thread.start()
        
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