import flet as ft
import time
import threading
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from core.styles import AppStyles

class SplashScreen:
    def __init__(self, page: ft.Page):
        self.page = page
        self.styles = AppStyles()
        self.setup_page()
        
    def setup_page(self):
        """Configure the main page settings for mobile"""
        self.page.title = "ATV - AUTOTRADEVIP"
        self.page.window_width = 375
        self.page.window_height = 812
        self.page.padding = 0
        self.page.spacing = 0
        self.page.bgcolor = self.styles.PRIMARY_COLOR
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        
    def create_logo(self):
        """Create the ATV logo using SVG"""
        logo_svg = ft.Container(
            content=ft.Image(
                src="assets/logo.svg",
                width=120,
                height=120,
                fit=ft.ImageFit.CONTAIN,
            ),
            opacity=0,
            animate_opacity=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
        )
        return logo_svg
        
    def create_brand_text(self):
        """Create the brand text with styling"""
        brand_container = ft.Container(
            content=ft.Column([
                ft.Text(
                    "ATV",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=self.styles.TEXT_PRIMARY,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "AUTOTRADEVIP",
                    size=18,
                    weight=ft.FontWeight.W_400,
                    color=self.styles.TEXT_SECONDARY,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            spacing=5,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            opacity=0,
            animate_opacity=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
        )
        return brand_container
        
    def create_progress_bar(self):
        """Create animated progress bar"""
        progress_bar = ft.Container(
            content=ft.ProgressBar(
                width=200,
                height=4,
                color=self.styles.ACCENT_COLOR,
                bgcolor=self.styles.PROGRESS_BG,
                value=0,
            ),
            opacity=0,
            animate_opacity=ft.Animation(800, ft.AnimationCurve.EASE_IN_OUT)
        )
        return progress_bar
        
    def create_version_text(self):
        """Create version information text"""
        version_text = ft.Container(
            content=ft.Text(
                "Version 1.0.0",
                size=12,
                color=self.styles.TEXT_MUTED,
                text_align=ft.TextAlign.CENTER,
            ),
            opacity=0,
            animate_opacity=ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT)
        )
        return version_text
        
    def create_loading_text(self):
        """Create loading text with animation"""
        loading_text = ft.Container(
            content=ft.Text(
                "Loading...",
                size=14,
                color=self.styles.TEXT_TERTIARY,
                text_align=ft.TextAlign.CENTER,
            ),
            opacity=0,
            animate_opacity=ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT)
        )
        return loading_text
        
    def animate_progress(self, progress_bar):
        """Animate the progress bar"""
        def update_progress():
            for i in range(101):
                progress_bar.content.value = i / 100
                self.page.update()
                time.sleep(0.03)
                
        # Run animation in separate thread
        thread = threading.Thread(target=update_progress)
        thread.daemon = True
        thread.start()
        
    def show_main_content(self):
        """Show main application content after splash"""
        self.page.clean()
        
        # Main content
        main_content = ft.Column([
            ft.Container(height=100),
            ft.Text(
                "ATV - AUTOTRADEVIP",
                size=24,
                weight=ft.FontWeight.BOLD,
                color=self.styles.TEXT_PRIMARY,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Container(height=20),
            ft.Text(
                "Platform Trading Otomatis untuk Trader Profesional",
                size=16,
                color=self.styles.TEXT_SECONDARY,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Container(height=40),
            ft.Container(
                content=ft.Column([
                    ft.Text("• Trading bot otomatis untuk berbagai broker", size=14, color=self.styles.TEXT_TERTIARY),
                    ft.Text("• Keamanan tingkat bank dengan enkripsi", size=14, color=self.styles.TEXT_TERTIARY),
                    ft.Text("• Analisis real-time dan metrik performa", size=14, color=self.styles.TEXT_TERTIARY),
                    ft.Text("• Dukungan untuk Binomo, Quotex, Olymptrade, IQ Option", size=14, color=self.styles.TEXT_TERTIARY),
                ], spacing=10),
                padding=20,
            ),
            ft.Container(height=60),
            ft.ElevatedButton(
                text="Mulai Sekarang",
                on_click=lambda e: self.show_getting_started(),
                style=ft.ButtonStyle(
                    color=self.styles.TEXT_PRIMARY,
                    bgcolor=self.styles.ACCENT_COLOR,
                    padding=ft.padding.symmetric(horizontal=40, vertical=15),
                )
            )
        ], 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0
        )
        
        self.page.add(main_content)
        self.page.update()
        
    def show_getting_started(self):
        """Show getting started confirmation"""
        self.page.clean()
        
        # Getting started content
        getting_started_content = ft.Column([
            ft.Container(height=150),
            ft.Icon(
                ft.icons.ROCKET_LAUNCH,
                size=80,
                color=self.styles.ACCENT_COLOR,
            ),
            ft.Container(height=30),
            ft.Text(
                "Siap untuk Memulai?",
                size=24,
                weight=ft.FontWeight.BOLD,
                color=self.styles.TEXT_PRIMARY,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Container(height=20),
            ft.Text(
                "Aplikasi ATV akan membantu Anda mengoptimalkan trading dengan bot otomatis yang canggih.",
                size=16,
                color=self.styles.TEXT_SECONDARY,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Container(height=80),
            ft.ElevatedButton(
                text="Ya, Saya Siap!",
                on_click=lambda e: self.page.window_close(),
                style=ft.ButtonStyle(
                    color=self.styles.TEXT_PRIMARY,
                    bgcolor=self.styles.SUCCESS_COLOR,
                    padding=ft.padding.symmetric(horizontal=40, vertical=15),
                )
            )
        ], 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0
        )
        
        self.page.add(getting_started_content)
        self.page.update()
        
    def start_splash_sequence(self):
        """Start the splash screen animation sequence"""
        def animation_sequence():
            # Wait for initial setup
            time.sleep(0.5)
            
            # Show logo
            self.logo.opacity = 1
            self.page.update()
            
            # Wait and show brand text
            time.sleep(1)
            self.brand_text.opacity = 1
            self.page.update()
            
            # Wait and show progress bar
            time.sleep(1)
            self.progress_bar.opacity = 1
            self.page.update()
            
            # Wait and show version text
            time.sleep(0.5)
            self.version_text.opacity = 1
            self.page.update()
            
            # Wait and show loading text
            time.sleep(0.5)
            self.loading_text.opacity = 1
            self.page.update()
            
            # Start progress animation
            self.animate_progress(self.progress_bar)
            
            # Wait for progress to complete
            time.sleep(3.5)
            
            # Fade out splash screen
            self.fade_out_splash()
            
        # Run animation sequence in separate thread
        thread = threading.Thread(target=animation_sequence)
        thread.daemon = True
        thread.start()
        
    def fade_out_splash(self):
        """Fade out the splash screen"""
        def fade_out():
            # Fade out all elements
            self.logo.opacity = 0
            self.brand_text.opacity = 0
            self.progress_bar.opacity = 0
            self.version_text.opacity = 0
            self.loading_text.opacity = 0
            self.page.update()
            
            # Wait for fade out to complete
            time.sleep(1)
            
            # Show main content
            self.show_main_content()
            
        # Run fade out in separate thread
        thread = threading.Thread(target=fade_out)
        thread.daemon = True
        thread.start()
        
    def build(self):
        """Build and display the splash screen"""
        self.page.clean()
        
        # Create all elements
        self.logo = self.create_logo()
        self.brand_text = self.create_brand_text()
        self.progress_bar = self.create_progress_bar()
        self.version_text = self.create_version_text()
        self.loading_text = self.create_loading_text()
        
        # Main splash container
        splash_container = ft.Container(
            content=ft.Column([
                ft.Container(height=150),
                self.logo,
                ft.Container(height=30),
                self.brand_text,
                ft.Container(height=60),
                self.progress_bar,
                ft.Container(height=30),
                self.version_text,
                ft.Container(height=10),
                self.loading_text,
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
            ),
            expand=True,
            bgcolor=self.styles.PRIMARY_COLOR,
            padding=ft.padding.symmetric(horizontal=20),
        )
        
        self.page.add(splash_container)
        self.page.update()

def main(page: ft.Page):
    """Main application entry point"""
    splash = SplashScreen(page)
    splash.build()
    splash.start_splash_sequence()

if __name__ == "__main__":
    ft.app(target=main, port=5000, host="0.0.0.0", view=ft.AppView.WEB_BROWSER)