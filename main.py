import flet as ft
import time
import threading
from styles import AppStyles

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
                color=self.styles.TEXT_TERTIARY,
                text_align=ft.TextAlign.CENTER,
            ),
            opacity=0,
            animate_opacity=ft.Animation(800, ft.AnimationCurve.EASE_IN_OUT)
        )
        return version_text
        
    def create_loading_text(self):
        """Create loading text with animation"""
        loading_text = ft.Container(
            content=ft.Text(
                "Loading...",
                size=14,
                color=self.styles.TEXT_SECONDARY,
                text_align=ft.TextAlign.CENTER,
            ),
            opacity=0,
            animate_opacity=ft.Animation(800, ft.AnimationCurve.EASE_IN_OUT)
        )
        return loading_text
        
    def animate_progress(self, progress_bar):
        """Animate the progress bar"""
        def update_progress():
            for i in range(101):
                progress_bar.content.value = i / 100
                self.page.update()
                time.sleep(0.03)
        
        thread = threading.Thread(target=update_progress)
        thread.daemon = True
        thread.start()
        
    def show_main_content(self):
        """Show main application content after splash"""
        self.page.clean()
        
        # Create scrollable content for better mobile experience
        description_content = ft.Container(
            content=ft.Column([
                # Logo section
                ft.Container(
                    content=ft.Image(
                        src="assets/logo.svg",
                        width=80,
                        height=80,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(top=20, bottom=20),
                ),
                
                # Title
                ft.Text(
                    "ATV - AUTOTRADEVIP",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=self.styles.TEXT_PRIMARY,
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=10),
                
                # Description card
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "ROBOT TRADING & SIGNAL TRADING",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color=self.styles.TEXT_SECONDARY,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        
                        ft.Container(height=15),
                        
                        ft.Text(
                            "AUTO TRADE VIP adalah platform robot trading yang kuat dan aman yang dapat dijalankan di broker binomo, olymptrade, stockity, iqoption, dan quotex.",
                            size=16,
                            color=self.styles.TEXT_PRIMARY,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Berdasarkan sinyal trading dari indikator platform MetaTrader atau dari penyedia sinyal trading terbaik Anda.",
                            size=16,
                            color=self.styles.TEXT_PRIMARY,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        
                        ft.Container(height=20),
                        
                        # Supported brokers
                        ft.Text(
                            "Broker yang Didukung:",
                            size=14,
                            weight=ft.FontWeight.BOLD,
                            color=self.styles.TEXT_SECONDARY,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        
                        ft.Container(height=10),
                        
                        ft.Row([
                            ft.Container(
                                content=ft.Text("Binomo", size=12, color=self.styles.TEXT_PRIMARY),
                                bgcolor=self.styles.ACCENT_COLOR,
                                padding=ft.padding.symmetric(horizontal=12, vertical=6),
                                border_radius=15,
                            ),
                            ft.Container(
                                content=ft.Text("OlympTrade", size=12, color=self.styles.TEXT_PRIMARY),
                                bgcolor=self.styles.ACCENT_COLOR,
                                padding=ft.padding.symmetric(horizontal=12, vertical=6),
                                border_radius=15,
                            ),
                            ft.Container(
                                content=ft.Text("Stockity", size=12, color=self.styles.TEXT_PRIMARY),
                                bgcolor=self.styles.ACCENT_COLOR,
                                padding=ft.padding.symmetric(horizontal=12, vertical=6),
                                border_radius=15,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=8,
                        wrap=True,
                        ),
                        
                        ft.Container(height=5),
                        
                        ft.Row([
                            ft.Container(
                                content=ft.Text("IQ Option", size=12, color=self.styles.TEXT_PRIMARY),
                                bgcolor=self.styles.ACCENT_COLOR,
                                padding=ft.padding.symmetric(horizontal=12, vertical=6),
                                border_radius=15,
                            ),
                            ft.Container(
                                content=ft.Text("Quotex", size=12, color=self.styles.TEXT_PRIMARY),
                                bgcolor=self.styles.ACCENT_COLOR,
                                padding=ft.padding.symmetric(horizontal=12, vertical=6),
                                border_radius=15,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=8,
                        wrap=True,
                        ),
                        
                    ],
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=self.styles.SECONDARY_COLOR,
                    padding=25,
                    margin=ft.margin.symmetric(horizontal=20),
                    border_radius=15,
                    border=ft.border.all(1, self.styles.ACCENT_COLOR),
                ),
                
                ft.Container(height=30),
                
                # Get Started Button
                ft.ElevatedButton(
                    "GET STARTED",
                    on_click=lambda _: self.show_getting_started(),
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        bgcolor=self.styles.TEXT_SECONDARY,
                        padding=ft.padding.symmetric(horizontal=50, vertical=18),
                        shape=ft.RoundedRectangleBorder(radius=12),
                        text_style=ft.TextStyle(
                            size=16,
                            weight=ft.FontWeight.BOLD,
                        ),
                    ),
                    width=250,
                    height=55,
                ),
                
                ft.Container(height=30),
                
            ],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            ),
            expand=True,
            bgcolor=self.styles.PRIMARY_COLOR,
            padding=ft.padding.symmetric(horizontal=10, vertical=20),
            opacity=0,
            animate_opacity=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
        )
        
        self.page.add(description_content)
        description_content.opacity = 1
        self.page.update()
        
    def show_getting_started(self):
        """Show getting started confirmation"""
        self.page.clean()
        
        getting_started_content = ft.Container(
            content=ft.Column([
                ft.Container(height=50),
                
                ft.Icon(
                    ft.Icons.CHECK_CIRCLE,
                    size=80,
                    color=ft.Colors.GREEN,
                ),
                
                ft.Container(height=20),
                
                ft.Text(
                    "Selamat Datang!",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=self.styles.TEXT_PRIMARY,
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=10),
                
                ft.Text(
                    "Anda siap memulai trading otomatis dengan ATV - AUTOTRADEVIP",
                    size=16,
                    color=self.styles.TEXT_SECONDARY,
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=30),
                
                ft.ElevatedButton(
                    "MULAI TRADING",
                    on_click=lambda _: print("Start trading functionality"),
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        bgcolor=self.styles.TEXT_SECONDARY,
                        padding=ft.padding.symmetric(horizontal=40, vertical=15),
                        shape=ft.RoundedRectangleBorder(radius=12),
                    ),
                    width=200,
                    height=50,
                ),
                
            ],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            alignment=ft.alignment.center,
            bgcolor=self.styles.PRIMARY_COLOR,
            opacity=0,
            animate_opacity=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
        )
        
        self.page.add(getting_started_content)
        getting_started_content.opacity = 1
        self.page.update()
        
    def start_splash_sequence(self):
        """Start the splash screen animation sequence"""
        def animation_sequence():
            # Phase 1: Show logo
            time.sleep(0.5)
            self.logo.opacity = 1
            self.page.update()
            
            # Phase 2: Show brand text
            time.sleep(0.8)
            self.brand_text.opacity = 1
            self.page.update()
            
            # Phase 3: Show progress bar and loading text
            time.sleep(0.6)
            self.progress_bar.opacity = 1
            self.loading_text.opacity = 1
            self.page.update()
            
            # Phase 4: Animate progress
            time.sleep(0.4)
            self.animate_progress(self.progress_bar)
            
            # Phase 5: Show version
            time.sleep(1.0)
            self.version_text.opacity = 1
            self.page.update()
            
            # Phase 6: Wait for progress to complete
            time.sleep(2.0)
            
            # Phase 7: Fade out splash and show main content
            self.fade_out_splash()
            time.sleep(1.0)
            self.show_main_content()
        
        thread = threading.Thread(target=animation_sequence)
        thread.daemon = True
        thread.start()
        
    def fade_out_splash(self):
        """Fade out the splash screen"""
        self.logo.opacity = 0
        self.brand_text.opacity = 0
        self.progress_bar.opacity = 0
        self.loading_text.opacity = 0
        self.version_text.opacity = 0
        self.page.update()
        
    def build(self):
        """Build and display the splash screen"""
        # Create all components
        self.logo = self.create_logo()
        self.brand_text = self.create_brand_text()
        self.progress_bar = self.create_progress_bar()
        self.loading_text = self.create_loading_text()
        self.version_text = self.create_version_text()
        
        # Create main container
        splash_container = ft.Container(
            content=ft.Column([
                ft.Container(height=50),  # Top spacing
                self.logo,
                ft.Container(height=30),
                self.brand_text,
                ft.Container(height=60),
                self.progress_bar,
                ft.Container(height=20),
                self.loading_text,
                ft.Container(height=40),
                self.version_text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            ),
            expand=True,
            alignment=ft.alignment.center,
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        # Add to page
        self.page.add(splash_container)
        self.page.update()
        
        # Start animation sequence
        self.start_splash_sequence()

def main(page: ft.Page):
    """Main application entry point"""
    splash = SplashScreen(page)
    splash.build()

if __name__ == "__main__":
    ft.app(target=main, port=5000, host="0.0.0.0", view=ft.AppView.WEB_BROWSER)
