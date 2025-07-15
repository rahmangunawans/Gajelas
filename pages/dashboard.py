import flet as ft
import threading
import time
from styles import AppStyles

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
        """Create bottom navigation bar"""
        nav_items = [
            {"icon": ft.Icons.HOME, "label": "Beranda", "key": "beranda"},
            {"icon": ft.Icons.SMART_TOY, "label": "Active Bots", "key": "bots"},
            {"icon": ft.Icons.HISTORY, "label": "History", "key": "history"},
            {"icon": ft.Icons.PERSON, "label": "Saya", "key": "profile"},
        ]
        
        nav_buttons = []
        for item in nav_items:
            is_active = item["key"] == self.current_tab.lower()
            
            nav_buttons.append(
                ft.Container(
                    content=ft.Column([
                        ft.Icon(
                            item["icon"],
                            color=ft.Colors.PINK if is_active else self.styles.TEXT_MUTED,
                            size=24,
                        ),
                        ft.Text(
                            item["label"],
                            size=10,
                            color=ft.Colors.PINK if is_active else self.styles.TEXT_MUTED,
                            weight=ft.FontWeight.BOLD if is_active else ft.FontWeight.NORMAL,
                        ),
                    ], spacing=2, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=ft.padding.symmetric(vertical=8),
                    on_click=lambda e, key=item["key"]: self.switch_tab(key),
                    expand=True,
                )
            )
        
        return ft.Container(
            content=ft.Row(
                nav_buttons,
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                spacing=0,
            ),
            bgcolor=self.styles.SECONDARY_COLOR,
            padding=ft.padding.symmetric(vertical=5),
            border=ft.border.only(top=ft.BorderSide(1, self.styles.CARD_BORDER)),
        )
    
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
                
                # Main Content (Scrollable)
                ft.Container(
                    content=ft.Column([
                        self.create_trading_bot_section(),
                        ft.Container(height=20),  # Bottom padding
                    ], scroll=ft.ScrollMode.AUTO),
                    expand=True,
                ),
                
                # Bottom Navigation
                self.create_bottom_navigation(),
                
            ], spacing=0),
            expand=True,
            bgcolor=self.styles.PRIMARY_COLOR,
        )
        
        self.page.add(dashboard_content)
        self.page.update()