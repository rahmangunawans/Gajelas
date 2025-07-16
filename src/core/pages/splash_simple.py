import flet as ft
import time
import threading
from core.styles import AppStyles

class SplashScreen:
    def __init__(self, page: ft.Page, on_complete_callback):
        self.page = page
        self.on_complete_callback = on_complete_callback
        self.styles = AppStyles()
        
    def build(self):
        """Build and display the splash screen"""
        # Create simple splash screen
        splash_container = ft.Container(
            content=ft.Column([
                ft.Container(height=150),
                # Simple logo
                ft.Image(
                    src="assets/logo.svg",
                    width=100,
                    height=100,
                    fit=ft.ImageFit.CONTAIN,
                ),
                ft.Container(height=30),
                # Brand text
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
                # Simple progress bar
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
                ft.Container(height=30),
                ft.Text(
                    "Version 1.0.0",
                    size=12,
                    color=self.styles.TEXT_MUTED,
                    text_align=ft.TextAlign.CENTER,
                ),
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0),
            width=self.styles.MOBILE_WIDTH,
            height=self.styles.MOBILE_HEIGHT,
            bgcolor=self.styles.PRIMARY_COLOR,
            alignment=ft.alignment.center,
        )
        
        # Add to page
        self.page.add(splash_container)
        
        # Start simple animation
        def simple_animation():
            time.sleep(2)  # Simple delay
            self.page.clean()
            self.show_main_content()
        
        thread = threading.Thread(target=simple_animation)
        thread.daemon = True
        thread.start()
        
    def show_main_content(self):
        """Show main content after splash"""
        # Create GET STARTED button
        button = ft.ElevatedButton(
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
        )
        
        # Create description page
        description_page = ft.Container(
            content=ft.Column([
                ft.Container(height=100),
                ft.Text(
                    "ATV - AUTOTRADEVIP",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=self.styles.TEXT_PRIMARY,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=30),
                ft.Text(
                    "Platform robot trading yang mendukung broker:\nBinomo, OlympTrade, Stockity, IQ Option, dan Quotex",
                    size=16,
                    color=self.styles.TEXT_PRIMARY,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=50),
                button,
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0),
            width=self.styles.MOBILE_WIDTH,
            height=self.styles.MOBILE_HEIGHT,
            bgcolor=self.styles.PRIMARY_COLOR,
            alignment=ft.alignment.center,
        )
        
        self.page.add(description_page)
        self.page.update()