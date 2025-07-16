import flet as ft
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from services.database.postgres_manager import PostgresManager
from core.styles import AppStyles
from config.app_config import AppConfig

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
        page.padding = 20
        page.spacing = 0
        page.bgcolor = self.styles.PRIMARY_COLOR
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.DARK
        
        # Initialize database
        self.db_manager.init_db()
        
        # Show simple login
        self.show_login()
        
    def show_login(self):
        """Show simple login page"""
        self.page.clean()
        
        # Login form
        email_field = ft.TextField(
            label="Email",
            value="admin@atv.com",
            width=300,
            bgcolor=self.styles.SECONDARY_COLOR,
            border_color=self.styles.INPUT_BORDER,
            color=self.styles.TEXT_PRIMARY,
        )
        
        password_field = ft.TextField(
            label="Password",
            password=True,
            can_reveal_password=True,
            value="admin123",
            width=300,
            bgcolor=self.styles.SECONDARY_COLOR,
            border_color=self.styles.INPUT_BORDER,
            color=self.styles.TEXT_PRIMARY,
        )
        
        def handle_login(e):
            email = email_field.value
            password = password_field.value
            
            if not email or not password:
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Please fill in all fields"),
                    bgcolor=self.styles.ERROR_COLOR,
                )
                self.page.snack_bar.open = True
                self.page.update()
                return
                
            # Authenticate user
            user = self.db_manager.authenticate_user(email, password)
            if user:
                self.show_dashboard(user)
            else:
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Invalid credentials"),
                    bgcolor=self.styles.ERROR_COLOR,
                )
                self.page.snack_bar.open = True
                self.page.update()
        
        login_button = ft.ElevatedButton(
            text="Login",
            on_click=handle_login,
            width=300,
            bgcolor=self.styles.TEXT_SECONDARY,
            color=ft.Colors.WHITE,
        )
        
        # Add to page
        self.page.add(
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "ATV - AUTOTRADEVIP",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=self.styles.TEXT_PRIMARY,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(height=20),
                    email_field,
                    ft.Container(height=10),
                    password_field,
                    ft.Container(height=20),
                    login_button,
                ], 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0),
                padding=20,
                bgcolor=self.styles.SECONDARY_COLOR,
                border_radius=15,
                border=ft.border.all(1, self.styles.CARD_BORDER),
            )
        )
        
    def show_dashboard(self, user_data):
        """Show simple dashboard with broker logos"""
        self.page.clean()
        
        # Create broker cards with logos
        brokers = [
            {"name": "Binomo", "logo": "assets/broker_logos/binomo.svg", "active": True},
            {"name": "IQ Option", "logo": "assets/broker_logos/iq_option.svg", "active": False},
            {"name": "Stockity", "logo": "assets/broker_logos/stockity.svg", "active": True},
            {"name": "Quotex", "logo": "assets/broker_logos/quotex.svg", "active": False},
            {"name": "Olymptrade", "logo": "assets/broker_logos/olymptrade.svg", "active": True},
        ]
        
        broker_cards = []
        for broker in brokers:
            card = ft.Container(
                content=ft.Row([
                    ft.Image(
                        src=broker["logo"],
                        width=40,
                        height=40,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Column([
                        ft.Text(
                            broker["name"],
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=self.styles.TEXT_PRIMARY,
                        ),
                        ft.Text(
                            "Active" if broker["active"] else "Inactive",
                            size=12,
                            color=self.styles.SUCCESS_COLOR if broker["active"] else self.styles.TEXT_MUTED,
                        ),
                    ], expand=True, spacing=2),
                    ft.Switch(
                        value=broker["active"],
                        active_color=self.styles.SUCCESS_COLOR,
                    ),
                ], spacing=15),
                padding=20,
                bgcolor=self.styles.SECONDARY_COLOR,
                border_radius=10,
                border=ft.border.all(1, self.styles.CARD_BORDER),
                margin=ft.margin.only(bottom=10),
            )
            broker_cards.append(card)
        
        # Add to page
        self.page.add(
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        f"Welcome, {user_data.get('full_name', 'User')}!",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=self.styles.TEXT_PRIMARY,
                    ),
                    ft.Container(height=20),
                    ft.Text(
                        "Trading Bots",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=self.styles.TEXT_SECONDARY,
                    ),
                    ft.Container(height=10),
                    ft.Column(broker_cards, spacing=0),
                ], spacing=0),
                padding=20,
                expand=True,
            )
        )

def main(page: ft.Page):
    """Main application entry point"""
    app = SimpleATVApp()
    app.setup_page(page)

if __name__ == "__main__":
    print("🚀 Starting ATV Mobile Application...")
    print("📱 Mobile-first design optimized for 375x812 (iPhone X/11)")
    print("🌐 Access: http://localhost:5000")
    print("👤 Admin login: admin@atv.com / admin123")
    ft.app(target=main, port=5000, host="0.0.0.0", view=ft.AppView.WEB_BROWSER)