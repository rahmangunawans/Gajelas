import flet as ft
import time
import threading
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from core.styles import AppStyles

class SplashScreen:
    def __init__(self, page: ft.Page, on_complete_callback):
        self.page = page
        self.styles = AppStyles()
        self.on_complete_callback = on_complete_callback
        
    def create_logo(self):
        """Create the ATV logo with enhanced effects"""
        logo_container = ft.Container(
            content=ft.Stack([
                # Animated glow effect
                ft.Container(
                    width=140,
                    height=140,
                    border_radius=70,
                    gradient=ft.RadialGradient(
                        colors=[
                            ft.Colors.with_opacity(0.3, self.styles.TEXT_SECONDARY),
                            ft.Colors.with_opacity(0.1, self.styles.TEXT_SECONDARY),
                            ft.Colors.TRANSPARENT,
                        ],
                        center=ft.alignment.center,
                        radius=1.0,
                    ),
                    animate_opacity=ft.Animation(2000, ft.AnimationCurve.EASE_IN_OUT),
                ),
                # Floating particles around logo
                ft.Container(
                    content=ft.Stack([
                        # Particle 1
                        ft.Container(
                            width=4,
                            height=4,
                            bgcolor=self.styles.TEXT_SECONDARY,
                            border_radius=2,
                            opacity=0.6,
                            left=20,
                            top=30,
                            animate_offset=ft.Animation(3000, ft.AnimationCurve.EASE_IN_OUT),
                        ),
                        # Particle 2
                        ft.Container(
                            width=3,
                            height=3,
                            bgcolor="#e94560",
                            border_radius=1.5,
                            opacity=0.8,
                            right=25,
                            top=40,
                            animate_offset=ft.Animation(4000, ft.AnimationCurve.EASE_IN_OUT),
                        ),
                        # Particle 3
                        ft.Container(
                            width=5,
                            height=5,
                            bgcolor=self.styles.TEXT_SECONDARY,
                            border_radius=2.5,
                            opacity=0.4,
                            left=30,
                            bottom=35,
                            animate_offset=ft.Animation(3500, ft.AnimationCurve.EASE_IN_OUT),
                        ),
                        # Particle 4
                        ft.Container(
                            width=3,
                            height=3,
                            bgcolor="#e94560",
                            border_radius=1.5,
                            opacity=0.7,
                            right=20,
                            bottom=30,
                            animate_offset=ft.Animation(4500, ft.AnimationCurve.EASE_IN_OUT),
                        ),
                    ]),
                    width=140,
                    height=140,
                ),
                # Logo container with SVG fallback
                ft.Container(
                    content=ft.Stack([
                        # Background circle
                        ft.Container(
                            width=120,
                            height=120,
                            border_radius=60,
                            bgcolor="#0f3460",
                            border=ft.border.all(4, "#e94560"),
                        ),
                        # ATV Text Logo
                        ft.Container(
                            content=ft.Column([
                                ft.Text(
                                    "ATV",
                                    size=32,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE,
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                ft.Text(
                                    "AUTOTRADEVIP",
                                    size=8,
                                    weight=ft.FontWeight.W_600,
                                    color="#e94560",
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ],
                            spacing=0,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            width=120,
                            height=120,
                            alignment=ft.alignment.center,
                        ),
                        # Decorative corners
                        ft.Container(
                            content=ft.Stack([
                                ft.Container(
                                    width=6,
                                    height=6,
                                    border_radius=3,
                                    bgcolor="#e94560",
                                    opacity=0.7,
                                    left=25,
                                    top=25,
                                ),
                                ft.Container(
                                    width=6,
                                    height=6,
                                    border_radius=3,
                                    bgcolor="#e94560",
                                    opacity=0.7,
                                    right=25,
                                    top=25,
                                ),
                                ft.Container(
                                    width=6,
                                    height=6,
                                    border_radius=3,
                                    bgcolor="#e94560",
                                    opacity=0.7,
                                    left=25,
                                    bottom=25,
                                ),
                                ft.Container(
                                    width=6,
                                    height=6,
                                    border_radius=3,
                                    bgcolor="#e94560",
                                    opacity=0.7,
                                    right=25,
                                    bottom=25,
                                ),
                            ]),
                            width=120,
                            height=120,
                        ),
                    ]),
                    padding=ft.padding.all(10),
                    border_radius=60,
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=30,
                        color=ft.Colors.with_opacity(0.5, self.styles.TEXT_SECONDARY),
                        offset=ft.Offset(0, 0),
                    ),
                ),
            ]),
            opacity=0,
            animate_opacity=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT),
            animate_scale=ft.Animation(1000, ft.AnimationCurve.BOUNCE_OUT),
        )
        return logo_container
        
    def create_brand_text(self):
        """Create enhanced brand text with gradient effects"""
        brand_container = ft.Container(
            content=ft.Column([
                # Main title with glow effect
                ft.Container(
                    content=ft.Text(
                        "ATV",
                        size=36,
                        weight=ft.FontWeight.BOLD,
                        color=self.styles.TEXT_PRIMARY,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=20,
                        color=ft.Colors.with_opacity(0.6, self.styles.TEXT_SECONDARY),
                        offset=ft.Offset(0, 0),
                    ),
                ),
                # Subtitle with typing effect
                ft.Container(
                    content=ft.Text(
                        "AUTOTRADEVIP",
                        size=16,
                        weight=ft.FontWeight.W_600,
                        color=self.styles.TEXT_SECONDARY,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    padding=ft.padding.only(top=5),
                ),
                # Tagline
                ft.Container(
                    content=ft.Text(
                        "Professional Trading Platform",
                        size=12,
                        weight=ft.FontWeight.W_400,
                        color=self.styles.TEXT_TERTIARY,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    padding=ft.padding.only(top=8),
                ),
            ],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            opacity=0,
            animate_opacity=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT),
            animate_offset=ft.Animation(1000, ft.AnimationCurve.EASE_OUT),
        )
        return brand_container
        
    def create_progress_bar(self):
        """Create modern animated progress bar with floating dots"""
        progress_container = ft.Container(
            content=ft.Column([
                # Progress bar with gradient
                ft.Container(
                    content=ft.ProgressBar(
                        width=220,
                        height=6,
                        color=self.styles.TEXT_SECONDARY,
                        bgcolor=self.styles.PROGRESS_BG,
                        value=0,
                    ),
                    border_radius=3,
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=10,
                        color=ft.Colors.with_opacity(0.3, self.styles.TEXT_SECONDARY),
                        offset=ft.Offset(0, 2),
                    ),
                ),
                # Animated loading dots
                ft.Container(
                    content=ft.Row([
                        ft.Container(
                            width=8,
                            height=8,
                            bgcolor=self.styles.TEXT_SECONDARY,
                            border_radius=4,
                            opacity=0.3,
                            animate_opacity=ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT),
                        ),
                        ft.Container(
                            width=8,
                            height=8,
                            bgcolor=self.styles.TEXT_SECONDARY,
                            border_radius=4,
                            opacity=0.3,
                            animate_opacity=ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT),
                        ),
                        ft.Container(
                            width=8,
                            height=8,
                            bgcolor=self.styles.TEXT_SECONDARY,
                            border_radius=4,
                            opacity=0.3,
                            animate_opacity=ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT),
                        ),
                    ],
                    spacing=12,
                    alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    padding=ft.padding.only(top=20),
                ),
                # Progress percentage
                ft.Container(
                    content=ft.Text(
                        "0%",
                        size=10,
                        color=self.styles.TEXT_TERTIARY,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    padding=ft.padding.only(top=10),
                ),
            ],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            opacity=0,
            animate_opacity=ft.Animation(800, ft.AnimationCurve.EASE_IN_OUT)
        )
        return progress_container
        
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
        """Animate the progress bar with percentage updates and dancing dots"""
        def update_progress():
            for i in range(101):
                # Update progress bar
                progress_bar.content.controls[0].content.value = i / 100
                progress_bar.content.controls[2].content.value = f"{i}%"
                
                # Animate dots with wave effect
                dots = progress_bar.content.controls[1].content.controls
                for j, dot in enumerate(dots):
                    # Create wave effect - each dot animates with delay
                    cycle_position = (i + j * 20) % 60
                    if cycle_position < 20:
                        dot.opacity = 0.3 + (cycle_position / 20) * 0.7
                    elif cycle_position < 40:
                        dot.opacity = 1.0 - ((cycle_position - 20) / 20) * 0.7
                    else:
                        dot.opacity = 0.3
                
                self.page.update()
                time.sleep(0.05)
        
        thread = threading.Thread(target=update_progress)
        thread.daemon = True
        thread.start()
        
    def animate_floating_particles(self):
        """Animate floating particles around the logo"""
        def animate_particles():
            import math
            cycle = 0
            while cycle < 100:  # Run for about 5 seconds
                # Get particle containers
                particles = self.logo.content.controls[1].content.controls
                
                for i, particle in enumerate(particles):
                    # Create circular floating motion
                    angle = (cycle * 0.1) + (i * 1.5)  # Different phase for each particle
                    radius = 15 + (i * 5)  # Different radius for each particle
                    
                    # Calculate new position
                    x_offset = math.cos(angle) * radius
                    y_offset = math.sin(angle) * radius
                    
                    # Apply smooth movement
                    if i % 2 == 0:  # Even particles move clockwise
                        particle.left = 70 + x_offset
                        particle.top = 70 + y_offset
                    else:  # Odd particles move counter-clockwise
                        particle.right = 70 - x_offset
                        particle.bottom = 70 - y_offset
                
                # Pulse logo glow effect
                glow = self.logo.content.controls[0]
                glow.opacity = 0.3 + (math.sin(cycle * 0.2) * 0.2)
                
                self.page.update()
                time.sleep(0.05)
                cycle += 1
        
        thread = threading.Thread(target=animate_particles)
        thread.daemon = True
        thread.start()

    def simple_progress_animation(self):
        """Simple progress animation"""
        def progress_update():
            try:
                # Get progress bar from the page
                progress_bar = self.page.controls[0].content.controls[5]
                
                # Animate progress
                for i in range(0, 101, 5):
                    progress_bar.value = i / 100
                    self.page.update()
                    time.sleep(0.1)
                
                # Wait a moment then navigate to auth
                time.sleep(1)
                self.on_complete_callback()
                
            except Exception as e:
                print(f"Progress animation error: {e}")
                # Fallback - just wait and continue
                time.sleep(3)
                self.on_complete_callback()
        
        thread = threading.Thread(target=progress_update)
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
        
    def show_main_content(self):
        """Show product description after splash"""
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
                    on_click=lambda _: self.on_complete_callback(),
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
        
    def build(self):
        """Build and display the splash screen"""
        try:
            self.page.controls.clear()
            
            # Simple splash screen
            splash_content = ft.Column([
                ft.Container(height=100),
                # Simple logo icon
                ft.Icon(
                    ft.Icons.FLASH_ON,
                    size=80,
                    color=ft.Colors.BLUE_400
                ),
                ft.Container(height=20),
                # Brand text
                ft.Text(
                    "ATV",
                    size=36,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),
                ft.Text(
                    "AUTOTRADEVIP",
                    size=16,
                    color=ft.Colors.BLUE_400
                ),
                ft.Container(height=40),
                # Progress bar
                ft.ProgressBar(
                    width=200,
                    color=ft.Colors.BLUE_400,
                    bgcolor=ft.Colors.WHITE12,
                    value=0
                ),
                ft.Container(height=15),
                ft.Text(
                    "Loading...",
                    size=14,
                    color=ft.Colors.WHITE70
                ),
                ft.Container(height=20),
                ft.Text(
                    "Version 1.0.0",
                    size=12,
                    color=ft.Colors.WHITE54
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
            
            # Main container
            splash_container = ft.Container(
                content=splash_content,
                width=self.page.window_width or 375,
                height=self.page.window_height or 812,
                bgcolor=AppStyles.PRIMARY_COLOR,
                alignment=ft.alignment.center
            )
            
            self.page.add(splash_container)
            self.page.update()
            
            # Simple progress animation
            self.simple_progress_animation()
            
        except Exception as e:
            print(f"Error in splash build: {e}")
            # Ultra simple fallback
            self.page.add(ft.Text("ATV - Loading...", color=ft.Colors.WHITE))
            self.page.update()
            # Continue to auth after short delay
            time.sleep(2)
            self.on_complete_callback()