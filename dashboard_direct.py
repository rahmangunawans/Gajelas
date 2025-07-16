import flet as ft
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from services.database.postgres_manager import PostgresManager
from core.styles import AppStyles
from config.app_config import AppConfig

def main(page: ft.Page):
    """Main application entry point - direct to dashboard"""
    page.title = "ATV - AUTOTRADEVIP"
    page.window_width = 375
    page.window_height = 812
    page.padding = 0
    page.bgcolor = "#0a0a1a"
    page.theme_mode = ft.ThemeMode.DARK
    
    # Create broker cards with logos
    brokers = [
        {"name": "Binomo", "logo": "assets/broker_logos/binomo.svg", "active": True, "progress": 0.75},
        {"name": "IQ Option", "logo": "assets/broker_logos/iq_option.svg", "active": False, "progress": 0.30},
        {"name": "Stockity", "logo": "assets/broker_logos/stockity.svg", "active": True, "progress": 0.90},
        {"name": "Quotex", "logo": "assets/broker_logos/quotex.svg", "active": False, "progress": 0.15},
        {"name": "Olymptrade", "logo": "assets/broker_logos/olymptrade.svg", "active": True, "progress": 0.60},
    ]
    
    # Create broker cards
    broker_cards = []
    for broker in brokers:
        # Create broker card with logo
        card = ft.Container(
            content=ft.Column([
                ft.Row([
                    # Logo container
                    ft.Container(
                        content=ft.Image(
                            src=broker["logo"],
                            width=35,
                            height=35,
                            fit=ft.ImageFit.CONTAIN,
                        ),
                        width=50,
                        height=50,
                        bgcolor=ft.Colors.with_opacity(0.1, "#06b6d4"),
                        border_radius=25,
                        alignment=ft.alignment.center,
                        padding=ft.padding.all(7),
                    ),
                    # Broker info
                    ft.Column([
                        ft.Text(
                            broker["name"],
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color="#ffffff",
                        ),
                        ft.Text(
                            "Aktif" if broker["active"] else "Tidak Aktif",
                            size=12,
                            color="#10b981" if broker["active"] else "#64748b",
                        ),
                    ], spacing=2, expand=True),
                    # Switch
                    ft.Switch(
                        value=broker["active"],
                        active_color="#10b981",
                    ),
                ], spacing=15),
                
                ft.Container(height=10),
                
                # Progress bar
                ft.Column([
                    ft.Row([
                        ft.Text(
                            "Progress Trading",
                            size=12,
                            color="#94a3b8",
                        ),
                        ft.Text(
                            f"{int(broker['progress'] * 100)}%",
                            size=12,
                            color="#06b6d4",
                        ),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.ProgressBar(
                        value=broker["progress"],
                        bgcolor="#1e293b",
                        color="#06b6d4",
                        height=6,
                    ),
                ], spacing=5),
                
            ], spacing=0),
            bgcolor="#151528",
            padding=20,
            margin=ft.margin.symmetric(horizontal=15, vertical=5),
            border_radius=15,
            border=ft.border.all(1, "#334155"),
        )
        broker_cards.append(card)
    
    # Create main content
    content = ft.Column([
        # Header
        ft.Container(
            content=ft.Row([
                ft.Text(
                    "ATV - AUTOTRADEVIP",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#ffffff",
                ),
                ft.Container(expand=True),
                ft.Icon(
                    ft.Icons.STAR,
                    color="#fbbf24",
                    size=24,
                ),
            ]),
            padding=20,
        ),
        
        # Trading Bot Section
        ft.Container(
            content=ft.Row([
                ft.Icon(
                    ft.Icons.SMART_TOY,
                    color="#06b6d4",
                    size=24,
                ),
                ft.Text(
                    "Trading Bot",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#ffffff",
                ),
            ], spacing=10),
            padding=ft.padding.symmetric(horizontal=20, vertical=10),
        ),
        
        # Broker Cards
        ft.Column(broker_cards, spacing=0),
        
    ], spacing=0, scroll=ft.ScrollMode.AUTO)
    
    # Add main content to page
    page.add(content)
    page.update()

if __name__ == "__main__":
    print("🚀 Starting ATV Dashboard with Broker Logos...")
    print("📱 Mobile-first design optimized for 375x812")
    print("🌐 Access: http://localhost:5000")
    ft.app(target=main, port=5000, host="0.0.0.0", view=ft.AppView.WEB_BROWSER)