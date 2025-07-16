import flet as ft
import threading
import time
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from core.styles import AppStyles

class Dashboard:
    def __init__(self, page: ft.Page, user_data):
        self.page = page
        self.user_data = user_data
        self.styles = AppStyles()
        self.current_tab = "beranda"
        self.current_broker = "Beranda"
        
    def create_app_header(self):
        """Create the top app header with logo, search, VIP button, and notifications"""
        return ft.Container(
            content=ft.Row([
                # ATV Logo
                ft.Container(
                    content=ft.Row([
                        ft.Icon(
                            ft.Icons.TRENDING_UP,
                            color=self.styles.TEXT_SECONDARY,
                            size=24,
                        ),
                        ft.Text(
                            "ATV",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=self.styles.TEXT_PRIMARY,
                        ),
                    ], spacing=5),
                    padding=ft.padding.only(left=10),
                ),
                
                # Search Bar
                ft.Container(
                    content=ft.TextField(
                        hint_text="Cari broker atau bot...",
                        hint_style=ft.TextStyle(
                            color=self.styles.TEXT_MUTED,
                            size=14,
                        ),
                        text_style=ft.TextStyle(
                            color=self.styles.TEXT_PRIMARY,
                            size=14,
                        ),
                        border_color=self.styles.INPUT_BORDER,
                        focused_border_color=self.styles.INPUT_FOCUS,
                        bgcolor=self.styles.SECONDARY_COLOR,
                        border_radius=20,
                        height=35,
                        content_padding=ft.padding.symmetric(horizontal=15, vertical=5),
                        prefix_icon=ft.Icons.SEARCH,
                    ),
                    expand=True,
                    padding=ft.padding.symmetric(horizontal=10),
                ),
                
                # VIP Button
                ft.Container(
                    content=ft.ElevatedButton(
                        content=ft.Row([
                            ft.Icon(ft.Icons.STAR, size=16, color=ft.Colors.YELLOW),
                            ft.Text("VIP", size=12, weight=ft.FontWeight.BOLD),
                        ], spacing=3),
                        on_click=self.show_vip_options,
                        bgcolor=self.styles.ACCENT_COLOR,
                        color=ft.Colors.WHITE,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=15),
                            padding=ft.padding.symmetric(horizontal=10, vertical=5),
                        ),
                        height=35,
                    ),
                    padding=ft.padding.only(right=5),
                ),
                
                # Notification Icon
                ft.Container(
                    content=ft.IconButton(
                        icon=ft.Icons.NOTIFICATIONS_OUTLINED,
                        icon_color=self.styles.TEXT_SECONDARY,
                        on_click=self.show_notifications,
                        icon_size=24,
                    ),
                    padding=ft.padding.only(right=10),
                ),
            ]),
            bgcolor=self.styles.SECONDARY_COLOR,
            padding=ft.padding.symmetric(vertical=10),
            border=ft.border.only(bottom=ft.BorderSide(1, self.styles.CARD_BORDER)),
        )
    
    def create_admin_panel(self):
        """Create admin panel section"""
        return ft.Container(
            content=ft.Column([
                # Admin Panel Header
                ft.Container(
                    content=ft.Row([
                        ft.Icon(
                            ft.Icons.ADMIN_PANEL_SETTINGS,
                            color=self.styles.ERROR_COLOR,
                            size=24,
                        ),
                        ft.Text(
                            "Admin Panel",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color=self.styles.ERROR_COLOR,
                        ),
                        ft.Container(expand=True),
                        ft.IconButton(
                            icon=ft.Icons.SETTINGS,
                            icon_color=self.styles.ERROR_COLOR,
                            on_click=lambda e: self.show_admin_settings(),
                        ),
                    ]),
                    padding=ft.padding.symmetric(horizontal=20, vertical=10),
                ),
                
                # Admin Quick Actions
                ft.Container(
                    content=ft.Row([
                        # User Management
                        ft.Container(
                            content=ft.Column([
                                ft.Icon(ft.Icons.PEOPLE, color=self.styles.TEXT_PRIMARY, size=20),
                                ft.Text("Users", size=12, color=self.styles.TEXT_PRIMARY),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            bgcolor=self.styles.SECONDARY_COLOR,
                            padding=ft.padding.all(10),
                            border_radius=8,
                            on_click=lambda e: self.show_user_management(),
                            expand=True,
                        ),
                        
                        ft.Container(width=10),
                        
                        # Bot Management
                        ft.Container(
                            content=ft.Column([
                                ft.Icon(ft.Icons.SMART_TOY, color=self.styles.TEXT_PRIMARY, size=20),
                                ft.Text("Bots", size=12, color=self.styles.TEXT_PRIMARY),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            bgcolor=self.styles.SECONDARY_COLOR,
                            padding=ft.padding.all(10),
                            border_radius=8,
                            on_click=lambda e: self.show_bot_management(),
                            expand=True,
                        ),
                        
                        ft.Container(width=10),
                        
                        # System Stats
                        ft.Container(
                            content=ft.Column([
                                ft.Icon(ft.Icons.ANALYTICS, color=self.styles.TEXT_PRIMARY, size=20),
                                ft.Text("Stats", size=12, color=self.styles.TEXT_PRIMARY),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            bgcolor=self.styles.SECONDARY_COLOR,
                            padding=ft.padding.all(10),
                            border_radius=8,
                            on_click=lambda e: self.show_system_stats(),
                            expand=True,
                        ),
                        
                        ft.Container(width=10),
                        
                        # Audit Logs
                        ft.Container(
                            content=ft.Column([
                                ft.Icon(ft.Icons.HISTORY, color=self.styles.TEXT_PRIMARY, size=20),
                                ft.Text("Logs", size=12, color=self.styles.TEXT_PRIMARY),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            bgcolor=self.styles.SECONDARY_COLOR,
                            padding=ft.padding.all(10),
                            border_radius=8,
                            on_click=lambda e: self.show_audit_logs(),
                            expand=True,
                        ),
                    ]),
                    padding=ft.padding.symmetric(horizontal=20, vertical=5),
                ),
            ]),
            bgcolor=ft.Colors.with_opacity(0.05, self.styles.ERROR_COLOR),
            border=ft.border.all(1, ft.Colors.with_opacity(0.3, self.styles.ERROR_COLOR)),
            border_radius=10,
            margin=ft.margin.symmetric(horizontal=10, vertical=5),
        )
    
    def create_horizontal_navigation(self):
        """Create horizontal navigation bar for brokers"""
        brokers = ["Beranda", "Binomo", "Quotex", "Olymptrade", "IQ Option", "Stockity"]
        
        nav_items = []
        for broker in brokers:
            is_active = broker == self.current_broker
            
            nav_items.append(
                ft.Container(
                    content=ft.TextButton(
                        text=broker,
                        on_click=lambda e, b=broker: self.switch_broker(b),
                        style=ft.ButtonStyle(
                            color=self.styles.TEXT_SECONDARY if is_active else self.styles.TEXT_TERTIARY,
                            bgcolor=ft.Colors.with_opacity(0.2, self.styles.TEXT_SECONDARY) if is_active else ft.Colors.TRANSPARENT,
                            shape=ft.RoundedRectangleBorder(radius=15),
                            padding=ft.padding.symmetric(horizontal=15, vertical=8),
                        ),
                    ),
                    margin=ft.margin.only(right=5),
                )
            )
        
        return ft.Container(
            content=ft.Row(
                nav_items,
                scroll=ft.ScrollMode.AUTO,
                spacing=0,
            ),
            bgcolor=self.styles.PRIMARY_COLOR,
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
            border=ft.border.only(bottom=ft.BorderSide(1, self.styles.CARD_BORDER)),
        )
    
    def create_vip_status_card(self):
        """Create VIP status card"""
        is_vip = self.user_data.get('vip_status', 'basic') == 'premium'
        
        return ft.Container(
            content=ft.Row([
                ft.Icon(
                    ft.Icons.STAR if is_vip else ft.Icons.STAR_BORDER,
                    color=ft.Colors.YELLOW if is_vip else self.styles.TEXT_MUTED,
                    size=24,
                ),
                ft.Column([
                    ft.Text(
                        "Status VIP" if is_vip else "Status Regular",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=self.styles.TEXT_PRIMARY,
                    ),
                    ft.Text(
                        "Akses penuh ke semua bot trading" if is_vip else "Akses terbatas, upgrade ke VIP",
                        size=12,
                        color=self.styles.TEXT_TERTIARY,
                    ),
                ], spacing=2, expand=True),
                ft.Container(
                    content=ft.ElevatedButton(
                        text="Kelola VIP" if is_vip else "Upgrade VIP",
                        on_click=self.show_vip_options,
                        bgcolor=self.styles.SUCCESS_COLOR if is_vip else self.styles.WARNING_COLOR,
                        color=ft.Colors.WHITE,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                        ),
                    ),
                    padding=ft.padding.only(left=10),
                ),
            ]),
            bgcolor=self.styles.SECONDARY_COLOR,
            padding=20,
            margin=ft.margin.symmetric(horizontal=15, vertical=10),
            border_radius=15,
            border=ft.border.all(1, self.styles.CARD_BORDER),
        )
    
    def create_broker_card(self, broker_name, is_active=False, progress=0.0):
        """Create individual broker card with progress"""
        broker_icons = {
            "Binomo": ft.Icons.TRENDING_UP,
            "Stockity": ft.Icons.SHOW_CHART,
            "IQ Option": ft.Icons.INSIGHTS,
            "Olymptrade": ft.Icons.SPORTS_MOTORSPORTS,
            "Quotex": ft.Icons.QUERY_STATS,
        }
        
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Container(
                        content=ft.Icon(
                            broker_icons.get(broker_name, ft.Icons.CANDLESTICK_CHART),
                            color=self.styles.TEXT_SECONDARY,
                            size=32,
                        ),
                        width=50,
                        height=50,
                        bgcolor=ft.Colors.with_opacity(0.1, self.styles.TEXT_SECONDARY),
                        border_radius=25,
                        alignment=ft.alignment.center,
                    ),
                    ft.Column([
                        ft.Text(
                            broker_name,
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=self.styles.TEXT_PRIMARY,
                        ),
                        ft.Text(
                            "Aktif" if is_active else "Tidak Aktif",
                            size=12,
                            color=self.styles.SUCCESS_COLOR if is_active else self.styles.TEXT_MUTED,
                        ),
                    ], spacing=2, expand=True),
                    ft.Container(
                        content=ft.Switch(
                            value=is_active,
                            on_change=lambda e: self.toggle_broker(broker_name, e.control.value),
                            active_color=self.styles.SUCCESS_COLOR,
                        ),
                        padding=ft.padding.only(right=10),
                    ),
                ]),
                
                ft.Container(height=10),
                
                # Progress Bar
                ft.Column([
                    ft.Row([
                        ft.Text(
                            "Progress Trading",
                            size=12,
                            color=self.styles.TEXT_TERTIARY,
                        ),
                        ft.Text(
                            f"{int(progress * 100)}%",
                            size=12,
                            color=self.styles.TEXT_SECONDARY,
                        ),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.ProgressBar(
                        value=progress,
                        bgcolor=self.styles.PROGRESS_BG,
                        color=self.styles.TEXT_SECONDARY,
                        height=6,
                    ),
                ], spacing=5),
                
            ], spacing=0),
            bgcolor=self.styles.SECONDARY_COLOR,
            padding=20,
            margin=ft.margin.symmetric(horizontal=15, vertical=5),
            border_radius=15,
            border=ft.border.all(1, self.styles.CARD_BORDER),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=10,
                color=ft.Colors.BLACK12,
                offset=ft.Offset(0, 2),
            ),
        )
    
    def create_trading_bot_section(self):
        """Create the trading bot section"""
        brokers_data = [
            {"name": "Binomo", "active": True, "progress": 0.75},
            {"name": "Stockity", "active": False, "progress": 0.30},
            {"name": "IQ Option", "active": True, "progress": 0.90},
            {"name": "Olymptrade", "active": False, "progress": 0.15},
            {"name": "Quotex", "active": True, "progress": 0.60},
        ]
        
        return ft.Column([
            # Section Header
            ft.Container(
                content=ft.Row([
                    ft.Icon(
                        ft.Icons.SMART_TOY,
                        color=self.styles.TEXT_SECONDARY,
                        size=24,
                    ),
                    ft.Text(
                        "Trading Bot",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=self.styles.TEXT_PRIMARY,
                    ),
                ], spacing=10),
                padding=ft.padding.symmetric(horizontal=20, vertical=10),
            ),
            
            # VIP Status Card
            self.create_vip_status_card(),
            
            # Broker Cards
            ft.Column([
                self.create_broker_card(
                    broker["name"],
                    broker["active"],
                    broker["progress"]
                )
                for broker in brokers_data
            ], spacing=0),
            
        ], spacing=0)
    
    def create_bottom_navigation(self):
        """Create modern bottom navigation bar with clean design"""
        nav_items = [
            {"icon": ft.Icons.HOME, "label": "Beranda", "key": "beranda"},
            {"icon": ft.Icons.SMART_TOY, "label": "Active Bots", "key": "bots"},
            {"icon": ft.Icons.HISTORY, "label": "History", "key": "history"},
            {"icon": ft.Icons.PERSON, "label": "Saya", "key": "profile"},
        ]
        
        # Create navigation buttons
        nav_buttons = []
        
        for item in nav_items:
            is_active = item["key"] == self.current_tab.lower()
            
            # Create navigation button with modern styling
            nav_button = ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=ft.Icon(
                            item["icon"],
                            color=ft.Colors.WHITE if is_active else "#64748b",
                            size=24,
                        ),
                        width=48,
                        height=32,
                        bgcolor="#10b981" if is_active else ft.Colors.TRANSPARENT,
                        border_radius=16,
                        alignment=ft.alignment.center,
                        animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
                    ),
                    ft.Container(height=4),
                    ft.Text(
                        item["label"],
                        size=10,
                        color="#10b981" if is_active else "#64748b",
                        weight=ft.FontWeight.W_500 if is_active else ft.FontWeight.W_400,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
                padding=ft.padding.symmetric(vertical=8),
                on_click=lambda e, key=item["key"]: self.switch_tab(key),
                expand=True,
                animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
            )
            nav_buttons.append(nav_button)
        
        # Create the main navigation bar
        nav_bar = ft.Container(
            content=ft.Row(
                nav_buttons,
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                spacing=0,
            ),
            height=70,
            bgcolor=ft.Colors.WHITE,
            border_radius=ft.border_radius.only(
                top_left=20,
                top_right=20,
            ),
            padding=ft.padding.symmetric(horizontal=10, vertical=5),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=10,
                color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                offset=ft.Offset(0, -2),
            ),
            border=ft.border.only(
                top=ft.BorderSide(1, ft.Colors.with_opacity(0.1, ft.Colors.BLACK))
            ),
        )
        
        return nav_bar
    
    def show_vip_options(self, e):
        """Show VIP subscription options"""
        def close_dialog(e):
            dialog.open = False
            self.page.update()
        
        def select_plan(e, plan):
            print(f"Selected VIP plan: {plan}")
            close_dialog(e)
        
        dialog = ft.AlertDialog(
            title=ft.Text("Pilih Paket VIP", color=self.styles.TEXT_PRIMARY),
            content=ft.Container(
                content=ft.Column([
                    ft.Text(
                        "Dapatkan akses penuh ke semua bot trading",
                        size=14,
                        color=self.styles.TEXT_TERTIARY,
                    ),
                    ft.Container(height=20),
                    
                    # 1 Month Plan
                    ft.Container(
                        content=ft.Row([
                            ft.Column([
                                ft.Text("1 Bulan", size=16, weight=ft.FontWeight.BOLD, color=self.styles.TEXT_PRIMARY),
                                ft.Text("Rp 150.000", size=14, color=self.styles.TEXT_SECONDARY),
                            ], expand=True),
                            ft.ElevatedButton(
                                text="Pilih",
                                on_click=lambda e: select_plan(e, "1_month"),
                                bgcolor=self.styles.ACCENT_COLOR,
                                color=ft.Colors.WHITE,
                            ),
                        ]),
                        bgcolor=self.styles.SECONDARY_COLOR,
                        padding=15,
                        border_radius=10,
                        border=ft.border.all(1, self.styles.CARD_BORDER),
                    ),
                    
                    ft.Container(height=10),
                    
                    # 3 Month Plan
                    ft.Container(
                        content=ft.Row([
                            ft.Column([
                                ft.Text("3 Bulan", size=16, weight=ft.FontWeight.BOLD, color=self.styles.TEXT_PRIMARY),
                                ft.Text("Rp 400.000", size=14, color=self.styles.TEXT_SECONDARY),
                                ft.Text("Hemat 11%", size=12, color=self.styles.SUCCESS_COLOR),
                            ], expand=True),
                            ft.ElevatedButton(
                                text="Pilih",
                                on_click=lambda e: select_plan(e, "3_month"),
                                bgcolor=self.styles.SUCCESS_COLOR,
                                color=ft.Colors.WHITE,
                            ),
                        ]),
                        bgcolor=self.styles.SECONDARY_COLOR,
                        padding=15,
                        border_radius=10,
                        border=ft.border.all(1, self.styles.SUCCESS_COLOR),
                    ),
                    
                ], spacing=0),
                width=300,
                height=200,
            ),
            actions=[
                ft.TextButton("Tutup", on_click=close_dialog),
            ],
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()
    
    def show_notifications(self, e):
        """Show notifications"""
        print("Showing notifications")
    
    def switch_broker(self, broker):
        """Switch active broker"""
        self.current_broker = broker
        self.page.update()
    
    def toggle_broker(self, broker_name, is_active):
        """Toggle broker active status"""
        print(f"Toggling {broker_name}: {is_active}")
        self.page.update()
    
    def switch_tab(self, tab_key):
        """Switch bottom navigation tab"""
        self.current_tab = tab_key
        
        # Handle different tab actions
        if tab_key == "beranda":
            self.show_home_content()
        elif tab_key == "bots":
            self.show_active_bots()
        elif tab_key == "history":
            self.show_history()
        elif tab_key == "profile":
            self.show_profile()
        
        self.page.update()
    
    def show_home_content(self):
        """Show home/beranda content"""
        self.build()
    
    def show_active_bots(self):
        """Show active bots page"""
        # Clear current content and show active bots
        self.page.clean()
        
        # Create active bots page
        active_bots_content = ft.Container(
            content=ft.Column([
                # Header
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: self.build(),
                            icon_color=self.styles.TEXT_PRIMARY,
                        ),
                        ft.Text(
                            "Active Bots",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=self.styles.TEXT_PRIMARY,
                        ),
                    ]),
                    bgcolor=self.styles.SECONDARY_COLOR,
                    padding=ft.padding.symmetric(vertical=15, horizontal=10),
                ),
                
                # Active bots list
                ft.Container(
                    content=ft.Column([
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(ft.Icons.SMART_TOY, color=self.styles.SUCCESS_COLOR),
                                ft.Column([
                                    ft.Text("Binomo Bot", size=16, weight=ft.FontWeight.BOLD, color=self.styles.TEXT_PRIMARY),
                                    ft.Text("Status: Active", size=12, color=self.styles.SUCCESS_COLOR),
                                    ft.Text("Profit: +$1,250", size=12, color=self.styles.SUCCESS_COLOR),
                                ], expand=True),
                                ft.Switch(value=True, active_color=self.styles.SUCCESS_COLOR),
                            ]),
                            bgcolor=self.styles.SECONDARY_COLOR,
                            padding=15,
                            border_radius=10,
                            margin=ft.margin.only(bottom=10),
                        ),
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(ft.Icons.SMART_TOY, color=self.styles.SUCCESS_COLOR),
                                ft.Column([
                                    ft.Text("Quotex Bot", size=16, weight=ft.FontWeight.BOLD, color=self.styles.TEXT_PRIMARY),
                                    ft.Text("Status: Active", size=12, color=self.styles.SUCCESS_COLOR),
                                    ft.Text("Profit: +$850", size=12, color=self.styles.SUCCESS_COLOR),
                                ], expand=True),
                                ft.Switch(value=True, active_color=self.styles.SUCCESS_COLOR),
                            ]),
                            bgcolor=self.styles.SECONDARY_COLOR,
                            padding=15,
                            border_radius=10,
                            margin=ft.margin.only(bottom=10),
                        ),
                    ]),
                    expand=True,
                    padding=20,
                ),
                
                # Bottom navigation
                self.create_bottom_navigation(),
            ], spacing=0),
            expand=True,
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.add(active_bots_content)
        
    def show_history(self):
        """Show trading history page"""
        # Clear current content and show history
        self.page.clean()
        
        # Create history page
        history_content = ft.Container(
            content=ft.Column([
                # Header
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: self.build(),
                            icon_color=self.styles.TEXT_PRIMARY,
                        ),
                        ft.Text(
                            "Trading History",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=self.styles.TEXT_PRIMARY,
                        ),
                    ]),
                    bgcolor=self.styles.SECONDARY_COLOR,
                    padding=ft.padding.symmetric(vertical=15, horizontal=10),
                ),
                
                # History list
                ft.Container(
                    content=ft.Column([
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(ft.Icons.TRENDING_UP, color=self.styles.SUCCESS_COLOR),
                                ft.Column([
                                    ft.Text("EUR/USD", size=16, weight=ft.FontWeight.BOLD, color=self.styles.TEXT_PRIMARY),
                                    ft.Text("2024-01-15 14:30", size=12, color=self.styles.TEXT_TERTIARY),
                                    ft.Text("Binomo", size=12, color=self.styles.TEXT_SECONDARY),
                                ], expand=True),
                                ft.Text("+$125", size=16, color=self.styles.SUCCESS_COLOR, weight=ft.FontWeight.BOLD),
                            ]),
                            bgcolor=self.styles.SECONDARY_COLOR,
                            padding=15,
                            border_radius=10,
                            margin=ft.margin.only(bottom=10),
                        ),
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(ft.Icons.TRENDING_DOWN, color=self.styles.ERROR_COLOR),
                                ft.Column([
                                    ft.Text("GBP/USD", size=16, weight=ft.FontWeight.BOLD, color=self.styles.TEXT_PRIMARY),
                                    ft.Text("2024-01-15 13:45", size=12, color=self.styles.TEXT_TERTIARY),
                                    ft.Text("Quotex", size=12, color=self.styles.TEXT_SECONDARY),
                                ], expand=True),
                                ft.Text("-$50", size=16, color=self.styles.ERROR_COLOR, weight=ft.FontWeight.BOLD),
                            ]),
                            bgcolor=self.styles.SECONDARY_COLOR,
                            padding=15,
                            border_radius=10,
                            margin=ft.margin.only(bottom=10),
                        ),
                    ]),
                    expand=True,
                    padding=20,
                ),
                
                # Bottom navigation
                self.create_bottom_navigation(),
            ], spacing=0),
            expand=True,
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.add(history_content)
        
    def show_profile(self):
        """Show profile page"""
        # Clear current content and show profile
        self.page.clean()
        
        # Create profile page
        profile_content = ft.Container(
            content=ft.Column([
                # Header
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: self.build(),
                            icon_color=self.styles.TEXT_PRIMARY,
                        ),
                        ft.Text(
                            "Profile",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=self.styles.TEXT_PRIMARY,
                        ),
                    ]),
                    bgcolor=self.styles.SECONDARY_COLOR,
                    padding=ft.padding.symmetric(vertical=15, horizontal=10),
                ),
                
                # Profile info
                ft.Container(
                    content=ft.Column([
                        # User info card
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Icon(ft.Icons.PERSON, size=60, color=self.styles.TEXT_SECONDARY),
                                    ft.Column([
                                        ft.Text(
                                            f"{self.user_data.get('first_name', 'User')} {self.user_data.get('last_name', '')}",
                                            size=18,
                                            weight=ft.FontWeight.BOLD,
                                            color=self.styles.TEXT_PRIMARY,
                                        ),
                                        ft.Text(
                                            self.user_data.get('email', 'user@example.com'),
                                            size=14,
                                            color=self.styles.TEXT_TERTIARY,
                                        ),
                                        ft.Row([
                                            ft.Icon(
                                                ft.Icons.STAR if self.user_data.get('vip_status') == 'premium' else ft.Icons.STAR_BORDER,
                                                color=ft.Colors.YELLOW if self.user_data.get('vip_status') == 'premium' else self.styles.TEXT_MUTED,
                                                size=16,
                                            ),
                                            ft.Text(
                                                "VIP Premium" if self.user_data.get('vip_status') == 'premium' else "Regular",
                                                size=12,
                                                color=self.styles.TEXT_SECONDARY,
                                            ),
                                        ]),
                                    ], expand=True),
                                ]),
                            ]),
                            bgcolor=self.styles.SECONDARY_COLOR,
                            padding=20,
                            border_radius=10,
                            margin=ft.margin.only(bottom=20),
                        ),
                        
                        # Profile options
                        ft.Container(
                            content=ft.Column([
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.SETTINGS, color=self.styles.TEXT_SECONDARY),
                                    title=ft.Text("Settings", color=self.styles.TEXT_PRIMARY),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS, color=self.styles.TEXT_TERTIARY),
                                    on_click=lambda e: self.show_settings(),
                                ),
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.HELP, color=self.styles.TEXT_SECONDARY),
                                    title=ft.Text("Help & Support", color=self.styles.TEXT_PRIMARY),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS, color=self.styles.TEXT_TERTIARY),
                                ),
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.LOGOUT, color=self.styles.ERROR_COLOR),
                                    title=ft.Text("Logout", color=self.styles.ERROR_COLOR),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS, color=self.styles.TEXT_TERTIARY),
                                    on_click=lambda e: self.logout(),
                                ),
                            ]),
                            bgcolor=self.styles.SECONDARY_COLOR,
                            padding=10,
                            border_radius=10,
                        ),
                    ]),
                    expand=True,
                    padding=20,
                ),
                
                # Bottom navigation
                self.create_bottom_navigation(),
            ], spacing=0),
            expand=True,
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.add(profile_content)
        
    def show_settings(self):
        """Show settings page"""
        # Clear current content and show settings
        self.page.clean()
        
        # Create settings page
        settings_content = ft.Container(
            content=ft.Column([
                # Header
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: self.show_profile(),
                            icon_color=self.styles.TEXT_PRIMARY,
                        ),
                        ft.Text(
                            "Settings",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=self.styles.TEXT_PRIMARY,
                        ),
                    ]),
                    bgcolor=self.styles.SECONDARY_COLOR,
                    padding=ft.padding.symmetric(vertical=15, horizontal=10),
                ),
                
                # Settings content
                ft.Container(
                    content=ft.Column([
                        # Account Settings
                        ft.Container(
                            content=ft.Column([
                                ft.Text(
                                    "Account Settings",
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color=self.styles.TEXT_PRIMARY,
                                ),
                                ft.Container(height=10),
                                
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.PERSON, color=self.styles.TEXT_SECONDARY),
                                    title=ft.Text("Edit Profile", color=self.styles.TEXT_PRIMARY),
                                    subtitle=ft.Text("Update your personal information", color=self.styles.TEXT_TERTIARY),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS, color=self.styles.TEXT_TERTIARY),
                                    on_click=lambda e: self.show_edit_profile(),
                                ),
                                
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.LOCK, color=self.styles.TEXT_SECONDARY),
                                    title=ft.Text("Change Password", color=self.styles.TEXT_PRIMARY),
                                    subtitle=ft.Text("Update your account password", color=self.styles.TEXT_TERTIARY),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS, color=self.styles.TEXT_TERTIARY),
                                    on_click=lambda e: self.show_change_password(),
                                ),
                                
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.STAR, color=ft.Colors.YELLOW),
                                    title=ft.Text("VIP Status", color=self.styles.TEXT_PRIMARY),
                                    subtitle=ft.Text("Manage your VIP subscription", color=self.styles.TEXT_TERTIARY),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS, color=self.styles.TEXT_TERTIARY),
                                    on_click=lambda e: self.show_vip_management(),
                                ),
                            ]),
                            bgcolor=self.styles.SECONDARY_COLOR,
                            padding=15,
                            border_radius=10,
                            margin=ft.margin.only(bottom=20),
                        ),
                        
                        # Trading Settings
                        ft.Container(
                            content=ft.Column([
                                ft.Text(
                                    "Trading Settings",
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color=self.styles.TEXT_PRIMARY,
                                ),
                                ft.Container(height=10),
                                
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.SMART_TOY, color=self.styles.TEXT_SECONDARY),
                                    title=ft.Text("Bot Configuration", color=self.styles.TEXT_PRIMARY),
                                    subtitle=ft.Text("Configure trading bot settings", color=self.styles.TEXT_TERTIARY),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS, color=self.styles.TEXT_TERTIARY),
                                    on_click=lambda e: self.show_bot_config(),
                                ),
                                
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.ACCOUNT_BALANCE, color=self.styles.TEXT_SECONDARY),
                                    title=ft.Text("Trading Accounts", color=self.styles.TEXT_PRIMARY),
                                    subtitle=ft.Text("Manage broker accounts", color=self.styles.TEXT_TERTIARY),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS, color=self.styles.TEXT_TERTIARY),
                                    on_click=lambda e: self.show_trading_accounts(),
                                ),
                                
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.NOTIFICATIONS, color=self.styles.TEXT_SECONDARY),
                                    title=ft.Text("Notifications", color=self.styles.TEXT_PRIMARY),
                                    subtitle=ft.Text("Configure notification settings", color=self.styles.TEXT_TERTIARY),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS, color=self.styles.TEXT_TERTIARY),
                                    on_click=lambda e: self.show_notification_settings(),
                                ),
                            ]),
                            bgcolor=self.styles.SECONDARY_COLOR,
                            padding=15,
                            border_radius=10,
                            margin=ft.margin.only(bottom=20),
                        ),
                        
                        # App Settings
                        ft.Container(
                            content=ft.Column([
                                ft.Text(
                                    "App Settings",
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color=self.styles.TEXT_PRIMARY,
                                ),
                                ft.Container(height=10),
                                
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.DARK_MODE, color=self.styles.TEXT_SECONDARY),
                                    title=ft.Text("Dark Mode", color=self.styles.TEXT_PRIMARY),
                                    subtitle=ft.Text("Always enabled for better trading", color=self.styles.TEXT_TERTIARY),
                                    trailing=ft.Switch(value=True, disabled=True),
                                ),
                                
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.LANGUAGE, color=self.styles.TEXT_SECONDARY),
                                    title=ft.Text("Language", color=self.styles.TEXT_PRIMARY),
                                    subtitle=ft.Text("Bahasa Indonesia", color=self.styles.TEXT_TERTIARY),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS, color=self.styles.TEXT_TERTIARY),
                                    on_click=lambda e: self.show_language_settings(),
                                ),
                                
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.INFO, color=self.styles.TEXT_SECONDARY),
                                    title=ft.Text("About ATV", color=self.styles.TEXT_PRIMARY),
                                    subtitle=ft.Text("Version 1.0.0", color=self.styles.TEXT_TERTIARY),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS, color=self.styles.TEXT_TERTIARY),
                                    on_click=lambda e: self.show_about(),
                                ),
                            ]),
                            bgcolor=self.styles.SECONDARY_COLOR,
                            padding=15,
                            border_radius=10,
                            margin=ft.margin.only(bottom=20),
                        ),
                    ]),
                    expand=True,
                    padding=20,
                ),
                
                # Bottom navigation
                self.create_bottom_navigation(),
            ], spacing=0),
            expand=True,
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.add(settings_content)
        
    def show_edit_profile(self):
        """Show edit profile page"""
        # Clear current content and show edit profile
        self.page.clean()
        
        # Create form fields
        first_name_field = ft.TextField(
            label="First Name",
            value=self.user_data.get('first_name', ''),
            bgcolor=self.styles.SECONDARY_COLOR,
            border_color=self.styles.INPUT_BORDER,
            focused_border_color=self.styles.INPUT_FOCUS,
            color=self.styles.TEXT_PRIMARY,
            label_style=ft.TextStyle(color=self.styles.TEXT_TERTIARY),
        )
        
        last_name_field = ft.TextField(
            label="Last Name",
            value=self.user_data.get('last_name', ''),
            bgcolor=self.styles.SECONDARY_COLOR,
            border_color=self.styles.INPUT_BORDER,
            focused_border_color=self.styles.INPUT_FOCUS,
            color=self.styles.TEXT_PRIMARY,
            label_style=ft.TextStyle(color=self.styles.TEXT_TERTIARY),
        )
        
        email_field = ft.TextField(
            label="Email",
            value=self.user_data.get('email', ''),
            bgcolor=self.styles.SECONDARY_COLOR,
            border_color=self.styles.INPUT_BORDER,
            focused_border_color=self.styles.INPUT_FOCUS,
            color=self.styles.TEXT_PRIMARY,
            label_style=ft.TextStyle(color=self.styles.TEXT_TERTIARY),
            disabled=True,  # Email cannot be changed
        )
        
        def save_profile(e):
            # TODO: Implement profile update in database
            success_dialog = ft.AlertDialog(
                title=ft.Text("Success", color=self.styles.TEXT_PRIMARY),
                content=ft.Text("Profile updated successfully!", color=self.styles.TEXT_TERTIARY),
                actions=[ft.TextButton("OK", on_click=lambda e: close_success_dialog(e))],
                bgcolor=self.styles.PRIMARY_COLOR,
            )
            
            def close_success_dialog(e):
                success_dialog.open = False
                self.page.update()
                
            self.page.overlay.append(success_dialog)
            success_dialog.open = True
            self.page.update()
        
        # Create edit profile page
        edit_profile_content = ft.Container(
            content=ft.Column([
                # Header
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: self.show_settings(),
                            icon_color=self.styles.TEXT_PRIMARY,
                        ),
                        ft.Text(
                            "Edit Profile",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=self.styles.TEXT_PRIMARY,
                        ),
                    ]),
                    bgcolor=self.styles.SECONDARY_COLOR,
                    padding=ft.padding.symmetric(vertical=15, horizontal=10),
                ),
                
                # Form content
                ft.Container(
                    content=ft.Column([
                        # Profile picture section
                        ft.Container(
                            content=ft.Column([
                                ft.Icon(ft.Icons.PERSON, size=80, color=self.styles.TEXT_SECONDARY),
                                ft.TextButton(
                                    "Change Picture",
                                    on_click=lambda e: print("Change picture clicked"),
                                    style=ft.ButtonStyle(color=self.styles.TEXT_SECONDARY),
                                ),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            margin=ft.margin.only(bottom=30),
                        ),
                        
                        # Form fields
                        first_name_field,
                        ft.Container(height=20),
                        last_name_field,
                        ft.Container(height=20),
                        email_field,
                        ft.Container(height=30),
                        
                        # Save button
                        ft.ElevatedButton(
                            content=ft.Text("Save Changes", size=16, weight=ft.FontWeight.BOLD),
                            on_click=save_profile,
                            bgcolor=self.styles.SUCCESS_COLOR,
                            color=ft.Colors.WHITE,
                            width=200,
                            height=45,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                            ),
                        ),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    expand=True,
                    padding=20,
                ),
                
                # Bottom navigation
                self.create_bottom_navigation(),
            ], spacing=0),
            expand=True,
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.add(edit_profile_content)
        
    def show_change_password(self):
        """Show change password page"""
        # Clear current content and show change password
        self.page.clean()
        
        # Create form fields
        current_password_field = ft.TextField(
            label="Current Password",
            password=True,
            can_reveal_password=True,
            bgcolor=self.styles.SECONDARY_COLOR,
            border_color=self.styles.INPUT_BORDER,
            focused_border_color=self.styles.INPUT_FOCUS,
            color=self.styles.TEXT_PRIMARY,
            label_style=ft.TextStyle(color=self.styles.TEXT_TERTIARY),
        )
        
        new_password_field = ft.TextField(
            label="New Password",
            password=True,
            can_reveal_password=True,
            bgcolor=self.styles.SECONDARY_COLOR,
            border_color=self.styles.INPUT_BORDER,
            focused_border_color=self.styles.INPUT_FOCUS,
            color=self.styles.TEXT_PRIMARY,
            label_style=ft.TextStyle(color=self.styles.TEXT_TERTIARY),
        )
        
        confirm_password_field = ft.TextField(
            label="Confirm New Password",
            password=True,
            can_reveal_password=True,
            bgcolor=self.styles.SECONDARY_COLOR,
            border_color=self.styles.INPUT_BORDER,
            focused_border_color=self.styles.INPUT_FOCUS,
            color=self.styles.TEXT_PRIMARY,
            label_style=ft.TextStyle(color=self.styles.TEXT_TERTIARY),
        )
        
        def change_password(e):
            # TODO: Implement password change in database
            if new_password_field.value != confirm_password_field.value:
                error_dialog = ft.AlertDialog(
                    title=ft.Text("Error", color=self.styles.ERROR_COLOR),
                    content=ft.Text("New passwords do not match!", color=self.styles.TEXT_TERTIARY),
                    actions=[ft.TextButton("OK", on_click=lambda e: close_error_dialog(e))],
                    bgcolor=self.styles.PRIMARY_COLOR,
                )
                
                def close_error_dialog(e):
                    error_dialog.open = False
                    self.page.update()
                    
                self.page.overlay.append(error_dialog)
                error_dialog.open = True
                self.page.update()
                return
            
            success_dialog = ft.AlertDialog(
                title=ft.Text("Success", color=self.styles.TEXT_PRIMARY),
                content=ft.Text("Password changed successfully!", color=self.styles.TEXT_TERTIARY),
                actions=[ft.TextButton("OK", on_click=lambda e: close_success_dialog(e))],
                bgcolor=self.styles.PRIMARY_COLOR,
            )
            
            def close_success_dialog(e):
                success_dialog.open = False
                self.page.update()
                
            self.page.overlay.append(success_dialog)
            success_dialog.open = True
            self.page.update()
        
        # Create change password page
        change_password_content = ft.Container(
            content=ft.Column([
                # Header
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: self.show_settings(),
                            icon_color=self.styles.TEXT_PRIMARY,
                        ),
                        ft.Text(
                            "Change Password",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=self.styles.TEXT_PRIMARY,
                        ),
                    ]),
                    bgcolor=self.styles.SECONDARY_COLOR,
                    padding=ft.padding.symmetric(vertical=15, horizontal=10),
                ),
                
                # Form content
                ft.Container(
                    content=ft.Column([
                        ft.Container(height=20),
                        
                        # Security notice
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(ft.Icons.SECURITY, color=self.styles.TEXT_SECONDARY),
                                ft.Text(
                                    "Choose a strong password with at least 8 characters",
                                    size=14,
                                    color=self.styles.TEXT_TERTIARY,
                                ),
                            ]),
                            margin=ft.margin.only(bottom=30),
                        ),
                        
                        # Form fields
                        current_password_field,
                        ft.Container(height=20),
                        new_password_field,
                        ft.Container(height=20),
                        confirm_password_field,
                        ft.Container(height=30),
                        
                        # Change password button
                        ft.ElevatedButton(
                            content=ft.Text("Change Password", size=16, weight=ft.FontWeight.BOLD),
                            on_click=change_password,
                            bgcolor=self.styles.ACCENT_COLOR,
                            color=ft.Colors.WHITE,
                            width=200,
                            height=45,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                            ),
                        ),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    expand=True,
                    padding=20,
                ),
                
                # Bottom navigation
                self.create_bottom_navigation(),
            ], spacing=0),
            expand=True,
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.add(change_password_content)
        
    def show_vip_management(self):
        """Show VIP management page"""
        # Clear current content and show VIP management
        self.page.clean()
        
        is_vip = self.user_data.get('vip_status', 'basic') == 'premium'
        
        # Create VIP management page
        vip_management_content = ft.Container(
            content=ft.Column([
                # Header
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: self.show_settings(),
                            icon_color=self.styles.TEXT_PRIMARY,
                        ),
                        ft.Text(
                            "VIP Management",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=self.styles.TEXT_PRIMARY,
                        ),
                    ]),
                    bgcolor=self.styles.SECONDARY_COLOR,
                    padding=ft.padding.symmetric(vertical=15, horizontal=10),
                ),
                
                # VIP status content
                ft.Container(
                    content=ft.Column([
                        # Current status
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Icon(
                                        ft.Icons.STAR if is_vip else ft.Icons.STAR_BORDER,
                                        color=ft.Colors.YELLOW if is_vip else self.styles.TEXT_MUTED,
                                        size=40,
                                    ),
                                    ft.Column([
                                        ft.Text(
                                            "VIP Premium" if is_vip else "Regular Account",
                                            size=20,
                                            weight=ft.FontWeight.BOLD,
                                            color=self.styles.TEXT_PRIMARY,
                                        ),
                                        ft.Text(
                                            "Active" if is_vip else "Upgrade to access all features",
                                            size=14,
                                            color=self.styles.SUCCESS_COLOR if is_vip else self.styles.TEXT_TERTIARY,
                                        ),
                                    ], expand=True),
                                ]),
                                
                                ft.Container(height=20),
                                
                                # VIP benefits
                                ft.Text(
                                    "VIP Benefits:" if is_vip else "Get VIP Benefits:",
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color=self.styles.TEXT_PRIMARY,
                                ),
                                
                                ft.Column([
                                    ft.Row([
                                        ft.Icon(ft.Icons.CHECK_CIRCLE, color=self.styles.SUCCESS_COLOR, size=20),
                                        ft.Text("Access to all trading bots", color=self.styles.TEXT_PRIMARY),
                                    ]),
                                    ft.Row([
                                        ft.Icon(ft.Icons.CHECK_CIRCLE, color=self.styles.SUCCESS_COLOR, size=20),
                                        ft.Text("Advanced trading strategies", color=self.styles.TEXT_PRIMARY),
                                    ]),
                                    ft.Row([
                                        ft.Icon(ft.Icons.CHECK_CIRCLE, color=self.styles.SUCCESS_COLOR, size=20),
                                        ft.Text("Priority customer support", color=self.styles.TEXT_PRIMARY),
                                    ]),
                                    ft.Row([
                                        ft.Icon(ft.Icons.CHECK_CIRCLE, color=self.styles.SUCCESS_COLOR, size=20),
                                        ft.Text("Real-time market analysis", color=self.styles.TEXT_PRIMARY),
                                    ]),
                                    ft.Row([
                                        ft.Icon(ft.Icons.CHECK_CIRCLE, color=self.styles.SUCCESS_COLOR, size=20),
                                        ft.Text("Risk management tools", color=self.styles.TEXT_PRIMARY),
                                    ]),
                                ], spacing=10),
                                
                                ft.Container(height=30),
                                
                                # Action button
                                ft.ElevatedButton(
                                    content=ft.Text(
                                        "Manage Subscription" if is_vip else "Upgrade to VIP",
                                        size=16,
                                        weight=ft.FontWeight.BOLD
                                    ),
                                    on_click=lambda e: self.show_vip_options(e),
                                    bgcolor=ft.Colors.YELLOW if is_vip else self.styles.SUCCESS_COLOR,
                                    color=ft.Colors.BLACK if is_vip else ft.Colors.WHITE,
                                    width=200,
                                    height=45,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                    ),
                                ),
                            ]),
                            bgcolor=self.styles.SECONDARY_COLOR,
                            padding=20,
                            border_radius=10,
                        ),
                    ]),
                    expand=True,
                    padding=20,
                ),
                
                # Bottom navigation
                self.create_bottom_navigation(),
            ], spacing=0),
            expand=True,
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.add(vip_management_content)
        
    def show_bot_config(self):
        """Show bot configuration page"""
        # TODO: Implement bot configuration page
        self.show_settings()
        
    def show_trading_accounts(self):
        """Show trading accounts page"""
        # TODO: Implement trading accounts page
        self.show_settings()
        
    def show_notification_settings(self):
        """Show notification settings page"""
        # TODO: Implement notification settings page
        self.show_settings()
        
    def show_admin_settings(self):
        """Show admin settings page"""
        # TODO: Implement admin settings page
        self.show_settings()
        
    def show_user_management(self):
        """Show user management page with CRUD operations"""
        # Clear current content and show user management
        self.page.clean()
        
        # Sample user data (in real app, this would come from database)
        users_data = [
            {"id": 1, "name": "John Doe", "email": "john@example.com", "vip_status": "basic", "created": "2024-01-10"},
            {"id": 2, "name": "Admin ATV", "email": "admin@atv.com", "vip_status": "premium", "created": "2024-01-01"},
            {"id": 3, "name": "Jane Smith", "email": "jane@example.com", "vip_status": "premium", "created": "2024-01-15"},
        ]
        
        def create_user_card(user):
            return ft.Container(
                content=ft.Row([
                    ft.Column([
                        ft.Text(user["name"], size=16, weight=ft.FontWeight.BOLD, color=self.styles.TEXT_PRIMARY),
                        ft.Text(user["email"], size=12, color=self.styles.TEXT_TERTIARY),
                        ft.Row([
                            ft.Icon(
                                ft.Icons.STAR if user["vip_status"] == "premium" else ft.Icons.STAR_BORDER,
                                color=ft.Colors.YELLOW if user["vip_status"] == "premium" else self.styles.TEXT_MUTED,
                                size=16,
                            ),
                            ft.Text(user["vip_status"].title(), size=12, color=self.styles.TEXT_SECONDARY),
                        ]),
                    ], expand=True),
                    ft.Column([
                        ft.IconButton(
                            icon=ft.Icons.EDIT,
                            icon_color=self.styles.TEXT_SECONDARY,
                            on_click=lambda e, u=user: self.edit_user(u),
                            tooltip="Edit User",
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE,
                            icon_color=self.styles.ERROR_COLOR,
                            on_click=lambda e, u=user: self.delete_user(u),
                            tooltip="Delete User",
                        ),
                    ]),
                ]),
                bgcolor=self.styles.SECONDARY_COLOR,
                padding=15,
                border_radius=10,
                margin=ft.margin.only(bottom=10),
            )
        
        # Create user management page
        user_management_content = ft.Container(
            content=ft.Column([
                # Header
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: self.build(),
                            icon_color=self.styles.TEXT_PRIMARY,
                        ),
                        ft.Text(
                            "User Management",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=self.styles.TEXT_PRIMARY,
                        ),
                        ft.Container(expand=True),
                        ft.IconButton(
                            icon=ft.Icons.ADD,
                            icon_color=self.styles.SUCCESS_COLOR,
                            on_click=lambda e: self.add_user(),
                            tooltip="Add New User",
                        ),
                    ]),
                    bgcolor=self.styles.SECONDARY_COLOR,
                    padding=ft.padding.symmetric(vertical=15, horizontal=10),
                ),
                
                # User list
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            f"Total Users: {len(users_data)}",
                            size=14,
                            color=self.styles.TEXT_TERTIARY,
                        ),
                        ft.Container(height=10),
                        ft.Column([
                            create_user_card(user) for user in users_data
                        ]),
                    ]),
                    expand=True,
                    padding=20,
                ),
                
                # Bottom navigation
                self.create_bottom_navigation(),
            ], spacing=0),
            expand=True,
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.add(user_management_content)
        
    def show_bot_management(self):
        """Show bot management page with CRUD operations"""
        # Clear current content and show bot management
        self.page.clean()
        
        # Sample bot data
        bots_data = [
            {"id": 1, "name": "Binomo Bot", "broker": "Binomo", "status": "active", "profit": 1250.50},
            {"id": 2, "name": "Quotex Bot", "broker": "Quotex", "status": "active", "profit": 850.75},
            {"id": 3, "name": "IQ Option Bot", "broker": "IQ Option", "status": "inactive", "profit": -150.25},
            {"id": 4, "name": "Olymptrade Bot", "broker": "Olymptrade", "status": "active", "profit": 2100.00},
        ]
        
        def create_bot_card(bot):
            return ft.Container(
                content=ft.Row([
                    ft.Column([
                        ft.Text(bot["name"], size=16, weight=ft.FontWeight.BOLD, color=self.styles.TEXT_PRIMARY),
                        ft.Text(f"Broker: {bot['broker']}", size=12, color=self.styles.TEXT_TERTIARY),
                        ft.Row([
                            ft.Icon(
                                ft.Icons.PLAY_CIRCLE if bot["status"] == "active" else ft.Icons.PAUSE_CIRCLE,
                                color=self.styles.SUCCESS_COLOR if bot["status"] == "active" else self.styles.TEXT_MUTED,
                                size=16,
                            ),
                            ft.Text(
                                bot["status"].title(),
                                size=12,
                                color=self.styles.SUCCESS_COLOR if bot["status"] == "active" else self.styles.TEXT_MUTED,
                            ),
                        ]),
                    ], expand=True),
                    ft.Column([
                        ft.Text(
                            f"${bot['profit']:,.2f}",
                            size=14,
                            weight=ft.FontWeight.BOLD,
                            color=self.styles.SUCCESS_COLOR if bot["profit"] > 0 else self.styles.ERROR_COLOR,
                        ),
                        ft.Row([
                            ft.IconButton(
                                icon=ft.Icons.EDIT,
                                icon_color=self.styles.TEXT_SECONDARY,
                                on_click=lambda e, b=bot: self.edit_bot(b),
                                tooltip="Edit Bot",
                            ),
                            ft.IconButton(
                                icon=ft.Icons.DELETE,
                                icon_color=self.styles.ERROR_COLOR,
                                on_click=lambda e, b=bot: self.delete_bot(b),
                                tooltip="Delete Bot",
                            ),
                        ]),
                    ]),
                ]),
                bgcolor=self.styles.SECONDARY_COLOR,
                padding=15,
                border_radius=10,
                margin=ft.margin.only(bottom=10),
            )
        
        # Create bot management page
        bot_management_content = ft.Container(
            content=ft.Column([
                # Header
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: self.build(),
                            icon_color=self.styles.TEXT_PRIMARY,
                        ),
                        ft.Text(
                            "Bot Management",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=self.styles.TEXT_PRIMARY,
                        ),
                        ft.Container(expand=True),
                        ft.IconButton(
                            icon=ft.Icons.ADD,
                            icon_color=self.styles.SUCCESS_COLOR,
                            on_click=lambda e: self.add_bot(),
                            tooltip="Add New Bot",
                        ),
                    ]),
                    bgcolor=self.styles.SECONDARY_COLOR,
                    padding=ft.padding.symmetric(vertical=15, horizontal=10),
                ),
                
                # Bot list
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            f"Total Bots: {len(bots_data)}",
                            size=14,
                            color=self.styles.TEXT_TERTIARY,
                        ),
                        ft.Container(height=10),
                        ft.Column([
                            create_bot_card(bot) for bot in bots_data
                        ]),
                    ]),
                    expand=True,
                    padding=20,
                ),
                
                # Bottom navigation
                self.create_bottom_navigation(),
            ], spacing=0),
            expand=True,
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.add(bot_management_content)
        
    def show_system_stats(self):
        """Show system statistics page"""
        # Clear current content and show system stats
        self.page.clean()
        
        # Sample system stats
        stats_data = {
            "total_users": 1245,
            "active_bots": 8,
            "total_profit": 125470.50,
            "success_rate": 78.5,
            "uptime": "99.8%",
            "active_trades": 23,
        }
        
        def create_stat_card(title, value, icon, color):
            return ft.Container(
                content=ft.Column([
                    ft.Icon(icon, color=color, size=30),
                    ft.Text(str(value), size=20, weight=ft.FontWeight.BOLD, color=self.styles.TEXT_PRIMARY),
                    ft.Text(title, size=12, color=self.styles.TEXT_TERTIARY),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor=self.styles.SECONDARY_COLOR,
                padding=15,
                border_radius=10,
                expand=True,
            )
        
        # Create system stats page
        system_stats_content = ft.Container(
            content=ft.Column([
                # Header
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: self.build(),
                            icon_color=self.styles.TEXT_PRIMARY,
                        ),
                        ft.Text(
                            "System Statistics",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=self.styles.TEXT_PRIMARY,
                        ),
                        ft.Container(expand=True),
                        ft.IconButton(
                            icon=ft.Icons.REFRESH,
                            icon_color=self.styles.TEXT_SECONDARY,
                            on_click=lambda e: self.refresh_stats(),
                            tooltip="Refresh Stats",
                        ),
                    ]),
                    bgcolor=self.styles.SECONDARY_COLOR,
                    padding=ft.padding.symmetric(vertical=15, horizontal=10),
                ),
                
                # Stats grid
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            create_stat_card("Total Users", stats_data["total_users"], ft.Icons.PEOPLE, self.styles.TEXT_SECONDARY),
                            ft.Container(width=10),
                            create_stat_card("Active Bots", stats_data["active_bots"], ft.Icons.SMART_TOY, self.styles.SUCCESS_COLOR),
                        ]),
                        ft.Container(height=10),
                        ft.Row([
                            create_stat_card("Total Profit", f"${stats_data['total_profit']:,.2f}", ft.Icons.TRENDING_UP, self.styles.SUCCESS_COLOR),
                            ft.Container(width=10),
                            create_stat_card("Success Rate", f"{stats_data['success_rate']}%", ft.Icons.ANALYTICS, self.styles.TEXT_SECONDARY),
                        ]),
                        ft.Container(height=10),
                        ft.Row([
                            create_stat_card("System Uptime", stats_data["uptime"], ft.Icons.SCHEDULE, self.styles.SUCCESS_COLOR),
                            ft.Container(width=10),
                            create_stat_card("Active Trades", stats_data["active_trades"], ft.Icons.SHOW_CHART, self.styles.TEXT_SECONDARY),
                        ]),
                    ]),
                    expand=True,
                    padding=20,
                ),
                
                # Bottom navigation
                self.create_bottom_navigation(),
            ], spacing=0),
            expand=True,
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.add(system_stats_content)
        
    def show_audit_logs(self):
        """Show audit logs page"""
        # Clear current content and show audit logs
        self.page.clean()
        
        # Sample audit logs
        logs_data = [
            {"timestamp": "2024-01-15 14:30:25", "user": "admin@atv.com", "action": "User Created", "details": "Created user jane@example.com"},
            {"timestamp": "2024-01-15 14:25:10", "user": "admin@atv.com", "action": "Bot Started", "details": "Started Binomo Bot"},
            {"timestamp": "2024-01-15 14:20:05", "user": "john@example.com", "action": "Login", "details": "Successful login"},
            {"timestamp": "2024-01-15 14:15:30", "user": "admin@atv.com", "action": "VIP Upgraded", "details": "Upgraded user to VIP Premium"},
            {"timestamp": "2024-01-15 14:10:15", "user": "jane@example.com", "action": "Password Changed", "details": "Password updated successfully"},
        ]
        
        def create_log_entry(log):
            return ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text(log["timestamp"], size=12, color=self.styles.TEXT_TERTIARY),
                        ft.Container(expand=True),
                        ft.Text(log["action"], size=12, weight=ft.FontWeight.BOLD, color=self.styles.TEXT_SECONDARY),
                    ]),
                    ft.Text(f"User: {log['user']}", size=12, color=self.styles.TEXT_TERTIARY),
                    ft.Text(log["details"], size=12, color=self.styles.TEXT_PRIMARY),
                ]),
                bgcolor=self.styles.SECONDARY_COLOR,
                padding=15,
                border_radius=10,
                margin=ft.margin.only(bottom=10),
            )
        
        # Create audit logs page
        audit_logs_content = ft.Container(
            content=ft.Column([
                # Header
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: self.build(),
                            icon_color=self.styles.TEXT_PRIMARY,
                        ),
                        ft.Text(
                            "Audit Logs",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=self.styles.TEXT_PRIMARY,
                        ),
                        ft.Container(expand=True),
                        ft.IconButton(
                            icon=ft.Icons.FILTER_LIST,
                            icon_color=self.styles.TEXT_SECONDARY,
                            on_click=lambda e: self.filter_logs(),
                            tooltip="Filter Logs",
                        ),
                    ]),
                    bgcolor=self.styles.SECONDARY_COLOR,
                    padding=ft.padding.symmetric(vertical=15, horizontal=10),
                ),
                
                # Logs list
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            f"Recent Activity ({len(logs_data)} entries)",
                            size=14,
                            color=self.styles.TEXT_TERTIARY,
                        ),
                        ft.Container(height=10),
                        ft.Column([
                            create_log_entry(log) for log in logs_data
                        ]),
                    ]),
                    expand=True,
                    padding=20,
                ),
                
                # Bottom navigation
                self.create_bottom_navigation(),
            ], spacing=0),
            expand=True,
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.add(audit_logs_content)
        
    # CRUD Operation Methods
    def add_user(self):
        """Add new user dialog"""
        def close_dialog(e):
            dialog.open = False
            self.page.update()
        
        def save_user(e):
            # TODO: Implement user creation in database
            print(f"Creating user: {name_field.value}, {email_field.value}")
            close_dialog(e)
            self.show_user_management()  # Refresh the page
        
        name_field = ft.TextField(label="Full Name", width=250)
        email_field = ft.TextField(label="Email", width=250)
        vip_dropdown = ft.Dropdown(
            label="VIP Status",
            width=250,
            options=[
                ft.dropdown.Option("basic", "Basic"),
                ft.dropdown.Option("premium", "Premium"),
            ],
            value="basic",
        )
        
        dialog = ft.AlertDialog(
            title=ft.Text("Add New User", color=self.styles.TEXT_PRIMARY),
            content=ft.Column([
                name_field,
                email_field,
                vip_dropdown,
            ], width=300, height=200),
            actions=[
                ft.TextButton("Cancel", on_click=close_dialog),
                ft.ElevatedButton("Save", on_click=save_user, bgcolor=self.styles.SUCCESS_COLOR),
            ],
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()
        
    def edit_user(self, user):
        """Edit user dialog"""
        def close_dialog(e):
            dialog.open = False
            self.page.update()
        
        def save_changes(e):
            # TODO: Implement user update in database
            print(f"Updating user {user['id']}: {name_field.value}, {vip_dropdown.value}")
            close_dialog(e)
            self.show_user_management()  # Refresh the page
        
        name_field = ft.TextField(label="Full Name", value=user["name"], width=250)
        email_field = ft.TextField(label="Email", value=user["email"], width=250, disabled=True)
        vip_dropdown = ft.Dropdown(
            label="VIP Status",
            width=250,
            options=[
                ft.dropdown.Option("basic", "Basic"),
                ft.dropdown.Option("premium", "Premium"),
            ],
            value=user["vip_status"],
        )
        
        dialog = ft.AlertDialog(
            title=ft.Text("Edit User", color=self.styles.TEXT_PRIMARY),
            content=ft.Column([
                name_field,
                email_field,
                vip_dropdown,
            ], width=300, height=200),
            actions=[
                ft.TextButton("Cancel", on_click=close_dialog),
                ft.ElevatedButton("Save", on_click=save_changes, bgcolor=self.styles.SUCCESS_COLOR),
            ],
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()
        
    def delete_user(self, user):
        """Delete user confirmation dialog"""
        def close_dialog(e):
            dialog.open = False
            self.page.update()
        
        def confirm_delete(e):
            # TODO: Implement user deletion in database
            print(f"Deleting user {user['id']}: {user['name']}")
            close_dialog(e)
            self.show_user_management()  # Refresh the page
        
        dialog = ft.AlertDialog(
            title=ft.Text("Delete User", color=self.styles.ERROR_COLOR),
            content=ft.Text(f"Are you sure you want to delete user '{user['name']}'? This action cannot be undone.", color=self.styles.TEXT_TERTIARY),
            actions=[
                ft.TextButton("Cancel", on_click=close_dialog),
                ft.ElevatedButton("Delete", on_click=confirm_delete, bgcolor=self.styles.ERROR_COLOR),
            ],
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()
        
    def add_bot(self):
        """Add new bot dialog"""
        def close_dialog(e):
            dialog.open = False
            self.page.update()
        
        def save_bot(e):
            # TODO: Implement bot creation in database
            print(f"Creating bot: {name_field.value}, {broker_dropdown.value}")
            close_dialog(e)
            self.show_bot_management()  # Refresh the page
        
        name_field = ft.TextField(label="Bot Name", width=250)
        broker_dropdown = ft.Dropdown(
            label="Broker",
            width=250,
            options=[
                ft.dropdown.Option("Binomo", "Binomo"),
                ft.dropdown.Option("Quotex", "Quotex"),
                ft.dropdown.Option("IQ Option", "IQ Option"),
                ft.dropdown.Option("Olymptrade", "Olymptrade"),
                ft.dropdown.Option("Stockity", "Stockity"),
            ],
        )
        
        dialog = ft.AlertDialog(
            title=ft.Text("Add New Bot", color=self.styles.TEXT_PRIMARY),
            content=ft.Column([
                name_field,
                broker_dropdown,
            ], width=300, height=150),
            actions=[
                ft.TextButton("Cancel", on_click=close_dialog),
                ft.ElevatedButton("Save", on_click=save_bot, bgcolor=self.styles.SUCCESS_COLOR),
            ],
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()
        
    def edit_bot(self, bot):
        """Edit bot dialog"""
        def close_dialog(e):
            dialog.open = False
            self.page.update()
        
        def save_changes(e):
            # TODO: Implement bot update in database
            print(f"Updating bot {bot['id']}: {name_field.value}, {status_dropdown.value}")
            close_dialog(e)
            self.show_bot_management()  # Refresh the page
        
        name_field = ft.TextField(label="Bot Name", value=bot["name"], width=250)
        broker_field = ft.TextField(label="Broker", value=bot["broker"], width=250, disabled=True)
        status_dropdown = ft.Dropdown(
            label="Status",
            width=250,
            options=[
                ft.dropdown.Option("active", "Active"),
                ft.dropdown.Option("inactive", "Inactive"),
            ],
            value=bot["status"],
        )
        
        dialog = ft.AlertDialog(
            title=ft.Text("Edit Bot", color=self.styles.TEXT_PRIMARY),
            content=ft.Column([
                name_field,
                broker_field,
                status_dropdown,
            ], width=300, height=200),
            actions=[
                ft.TextButton("Cancel", on_click=close_dialog),
                ft.ElevatedButton("Save", on_click=save_changes, bgcolor=self.styles.SUCCESS_COLOR),
            ],
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()
        
    def delete_bot(self, bot):
        """Delete bot confirmation dialog"""
        def close_dialog(e):
            dialog.open = False
            self.page.update()
        
        def confirm_delete(e):
            # TODO: Implement bot deletion in database
            print(f"Deleting bot {bot['id']}: {bot['name']}")
            close_dialog(e)
            self.show_bot_management()  # Refresh the page
        
        dialog = ft.AlertDialog(
            title=ft.Text("Delete Bot", color=self.styles.ERROR_COLOR),
            content=ft.Text(f"Are you sure you want to delete bot '{bot['name']}'? This action cannot be undone.", color=self.styles.TEXT_TERTIARY),
            actions=[
                ft.TextButton("Cancel", on_click=close_dialog),
                ft.ElevatedButton("Delete", on_click=confirm_delete, bgcolor=self.styles.ERROR_COLOR),
            ],
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()
        
    def refresh_stats(self):
        """Refresh system statistics"""
        # TODO: Implement stats refresh
        print("Refreshing system statistics...")
        self.show_system_stats()
        
    def filter_logs(self):
        """Filter audit logs"""
        # TODO: Implement log filtering
        print("Filtering audit logs...")
        
    def logout(self):
        """Handle logout"""
        # Clear user data and return to auth
        from pages.auth_handler import AuthHandler
        self.current_page = AuthHandler(self.page, None)
        self.current_page.show_login()
        

        

        

    
    def build(self):
        """Build and display the dashboard"""
        self.page.clean()
        
        # Create main layout
        dashboard_content = ft.Container(
            content=ft.Column([
                # App Header
                self.create_app_header(),
                
                # Horizontal Navigation
                self.create_horizontal_navigation(),
                
                # Main Content (Scrollable) - adjusted for floating navigation
                ft.Container(
                    content=ft.Column([
                        self.create_trading_bot_section(),
                        # Admin Panel (only for admin users) - positioned after Trading Bot section
                        self.create_admin_panel() if self.user_data.get('is_admin', False) else ft.Container(),
                        ft.Container(height=140),  # Extra bottom padding for floating navigation
                    ], scroll=ft.ScrollMode.AUTO),
                    expand=True,
                ),
                
                # Floating Bottom Navigation
                self.create_bottom_navigation(),
                
            ], spacing=0),
            expand=True,
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.add(dashboard_content)
        self.page.update()