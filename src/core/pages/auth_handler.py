import flet as ft
import hashlib
import re
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from core.styles import AppStyles
from services.database.sqlite_manager import SQLiteManager
from core.language import language_manager

class AuthHandler:
    def __init__(self, page: ft.Page, on_success_callback):
        self.page = page
        self.styles = AppStyles()
        self.db_manager = SQLiteManager()
        self.on_success_callback = on_success_callback
        
    def hash_password(self, password):
        """Hash password for storage using bcrypt"""
        import bcrypt
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
        
    def validate_email(self, email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
        
    def create_premium_header(self, title, subtitle=None):
        """Create extremely sophisticated header with luxury visual effects"""
        return ft.Container(
            content=ft.Column([
                # Premium floating logo with multiple sophisticated effects
                ft.Container(
                    content=ft.Stack([
                        # Outer ethereal glow ring with premium animation
                        ft.Container(
                            width=140,
                            height=140,
                            border_radius=70,
                            gradient=ft.RadialGradient(
                                center=ft.alignment.center,
                                radius=1.5,
                                colors=[
                                    ft.Colors.with_opacity(0.4, "#00d4ff"),
                                    ft.Colors.with_opacity(0.2, "#0ea5e9"),
                                    ft.Colors.with_opacity(0.1, "#1e40af"),
                                    ft.Colors.with_opacity(0.05, "#1e3a8a"),
                                    ft.Colors.TRANSPARENT,
                                ],
                                stops=[0.0, 0.3, 0.6, 0.8, 1.0],
                            ),
                            animate=ft.Animation(2000, ft.AnimationCurve.EASE_IN_OUT),
                        ),
                        # Middle luxury glow layer
                        ft.Container(
                            width=115,
                            height=115,
                            border_radius=57.5,
                            gradient=ft.RadialGradient(
                                center=ft.alignment.center,
                                radius=1.0,
                                colors=[
                                    ft.Colors.with_opacity(0.25, "#06b6d4"),
                                    ft.Colors.with_opacity(0.1, "#0891b2"),
                                    ft.Colors.TRANSPARENT,
                                ],
                            ),
                            left=12.5,
                            top=12.5,
                        ),
                        # Premium glassmorphism logo container
                        ft.Container(
                            width=95,
                            height=95,
                            border_radius=47.5,
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.top_left,
                                end=ft.alignment.bottom_right,
                                colors=[
                                    ft.Colors.with_opacity(0.25, "#ffffff"),
                                    ft.Colors.with_opacity(0.1, "#00d4ff"),
                                    ft.Colors.with_opacity(0.15, "#0ea5e9"),
                                    ft.Colors.with_opacity(0.05, "#1e40af"),
                                ],
                            ),
                            border=ft.border.all(1.5, ft.Colors.with_opacity(0.3, "#00d4ff")),
                            shadow=ft.BoxShadow(
                                spread_radius=0,
                                blur_radius=30,
                                color=ft.Colors.with_opacity(0.4, "#00d4ff"),
                                offset=ft.Offset(0, 12),
                            ),
                            content=ft.Column([
                                ft.Text(
                                    "ATV",
                                    size=26,
                                    weight=ft.FontWeight.W_900,
                                    color="#ffffff",
                                    text_align=ft.TextAlign.CENTER,
                                    font_family="SF Pro Display",
                                ),
                                ft.Container(
                                    content=ft.Text(
                                        "AUTOTRADEVIP",
                                        size=5.5,
                                        weight=ft.FontWeight.W_700,
                                        color="#00d4ff",
                                        text_align=ft.TextAlign.CENTER,
                                        font_family="SF Pro Display",
                                    ),
                                    margin=ft.margin.only(top=-2),
                                ),
                            ],
                            spacing=0,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            alignment=ft.alignment.center,
                            left=22.5,
                            top=22.5,
                        ),
                        # Premium highlight overlay effect
                        ft.Container(
                            width=95,
                            height=95,
                            border_radius=47.5,
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.top_center,
                                end=ft.alignment.bottom_center,
                                colors=[
                                    ft.Colors.with_opacity(0.4, "#ffffff"),
                                    ft.Colors.with_opacity(0.1, "#ffffff"),
                                    ft.Colors.TRANSPARENT,
                                ],
                                stops=[0.0, 0.3, 1.0],
                            ),
                            left=22.5,
                            top=22.5,
                        ),
                    ]),
                    width=140,
                    height=140,
                    margin=ft.margin.only(bottom=35),
                ),
                # Luxury title with sophisticated text effects
                ft.Container(
                    content=ft.Stack([
                        # Deep shadow for premium depth
                        ft.Text(
                            title,
                            size=36,
                            weight=ft.FontWeight.W_900,
                            color=ft.Colors.with_opacity(0.4, "#000000"),
                            text_align=ft.TextAlign.CENTER,
                        ),
                        # Secondary shadow for enhanced depth
                        ft.Container(
                            content=ft.Text(
                                title,
                                size=36,
                                weight=ft.FontWeight.W_900,
                                color=ft.Colors.with_opacity(0.2, "#1e40af"),
                                text_align=ft.TextAlign.CENTER,
                            ),
                            left=-1,
                            top=-1,
                        ),
                        # Main premium title with luxury gradient
                        ft.Container(
                            content=ft.Text(
                                title,
                                size=36,
                                weight=ft.FontWeight.W_900,
                                color="#ffffff",
                                text_align=ft.TextAlign.CENTER,
                                font_family="SF Pro Display",
                            ),
                            left=-2,
                            top=-3,
                        ),
                    ]),
                    margin=ft.margin.only(bottom=15),
                ),
                # Sophisticated subtitle with premium typography
                ft.Container(
                    content=ft.Text(
                        subtitle if subtitle else "Platform Trading Eksklusif & Profesional",
                        size=14,
                        color="#94a3b8",
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.W_500,
                        font_family="Inter",
                    ),
                    margin=ft.margin.only(bottom=35),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.padding.only(top=25, bottom=25),
            alignment=ft.alignment.center,
        )
        
    def create_luxury_form_field(self, label, hint_text, password=False, value="", icon=None):
        """Create extremely sophisticated form field with luxury glassmorphism effects"""
        # Enhanced premium icons
        field_icon = icon
        if not field_icon:
            if password:
                field_icon = ft.Icons.SECURITY_ROUNDED
            elif "email" in label.lower():
                field_icon = ft.Icons.MARK_EMAIL_READ_ROUNDED
            elif "name" in label.lower():
                field_icon = ft.Icons.ACCOUNT_CIRCLE_ROUNDED
            elif "phone" in label.lower():
                field_icon = ft.Icons.SMARTPHONE_ROUNDED
                
        # Password visibility toggle function - FIXED
        def toggle_password_visibility(e):
            text_field.password = not text_field.password
            # Update icon based on current state
            if text_field.password:
                e.control.icon = ft.Icons.VISIBILITY
            else:
                e.control.icon = ft.Icons.VISIBILITY_OFF
            self.page.update()
            
        # Suffix icon for password toggle
        suffix_icon = None
        if password:
            suffix_icon = ft.IconButton(
                icon=ft.Icons.VISIBILITY,
                icon_color="#64748b",
                on_click=toggle_password_visibility,
                icon_size=20,
            )
        
        # Premium text field with enhanced styling - FIXED for proper input handling
        text_field = ft.TextField(
            hint_text=hint_text,
            password=password,
            value=value,
            border_color=ft.Colors.TRANSPARENT,
            focused_border_color=ft.Colors.TRANSPARENT,
            cursor_color="#00d4ff",
            text_style=ft.TextStyle(
                size=15,
                color="#ffffff",
                weight=ft.FontWeight.W_500,
                font_family="Inter",
            ),
            hint_style=ft.TextStyle(
                size=15,
                color="#64748b",
                weight=ft.FontWeight.W_400,
                font_family="Inter",
            ),
            bgcolor=ft.Colors.TRANSPARENT,
            content_padding=ft.padding.symmetric(horizontal=60, vertical=18),
            width=300,
            height=55,
            # CRITICAL: Ensure the text field can receive focus and input
            autofocus=False,
            can_reveal_password=False,  # We handle this manually
        )
        
        # Create the visual container with glassmorphism effect
        field_container = ft.Container(
            content=ft.Stack([
                # Premium background with multiple gradient layers
                ft.Container(
                    width=300,
                    height=55,
                    border_radius=16,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_left,
                        end=ft.alignment.bottom_right,
                        colors=[
                            ft.Colors.with_opacity(0.15, "#ffffff"),
                            ft.Colors.with_opacity(0.08, "#00d4ff"),
                            ft.Colors.with_opacity(0.12, "#0ea5e9"),
                            ft.Colors.with_opacity(0.05, "#1e40af"),
                        ],
                    ),
                    border=ft.border.all(1.5, ft.Colors.with_opacity(0.25, "#00d4ff")),
                ),
                # Secondary luxury glow layer
                ft.Container(
                    width=300,
                    height=55,
                    border_radius=16,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[
                            ft.Colors.with_opacity(0.1, "#ffffff"),
                            ft.Colors.TRANSPARENT,
                        ],
                    ),
                ),
                # Luxury icon positioned absolutely
                ft.Container(
                    content=ft.Icon(
                        field_icon,
                        size=22,
                        color="#00d4ff",
                    ),
                    left=20,
                    top=16,
                ),
                # Password visibility toggle positioned absolutely
                ft.Container(
                    content=suffix_icon if password else None,
                    right=15,
                    top=12,
                ) if password else ft.Container(),
                # The actual text field positioned to fill the container
                text_field,
            ]),
            width=300,
            height=55,
            animate=ft.Animation(400, ft.AnimationCurve.EASE_OUT),
        )
        
        return ft.Container(
            content=ft.Column([
                # Luxury floating label
                ft.Container(
                    content=ft.Text(
                        label,
                        size=12,
                        weight=ft.FontWeight.W_700,
                        color="#00d4ff",
                        font_family="Inter",
                    ),
                    padding=ft.padding.only(left=12, bottom=8),
                ),
                # The field container with visual effects
                field_container,
            ],
            spacing=0,
            ),
            margin=ft.margin.only(bottom=25),
            animate=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
            # Store reference to text field for easy access
            data=text_field,  # Store the text field reference here
        )
        
    def create_primary_button(self, text, on_click, width=320):
        """Create ultra-professional button with stunning gradient and animation effects"""
        return ft.Container(
            content=ft.Stack([
                # Gradient background with multiple layers
                ft.Container(
                    width=width,
                    height=58,
                    border_radius=16,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_left,
                        end=ft.alignment.bottom_right,
                        colors=[
                            "#06b6d4",
                            "#0891b2",
                            "#0e7490",
                        ],
                    ),
                ),
                # Glossy overlay effect
                ft.Container(
                    width=width,
                    height=58,
                    border_radius=16,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.center,
                        colors=[
                            ft.Colors.with_opacity(0.3, "#ffffff"),
                            ft.Colors.TRANSPARENT,
                        ],
                    ),
                ),
                # Main button content
                ft.Container(
                    content=ft.TextButton(
                        content=ft.Text(
                            text,
                            size=16,
                            weight=ft.FontWeight.W_700,
                            color="#ffffff",
                            text_align=ft.TextAlign.CENTER,
                            font_family="SF Pro Display",
                        ),
                        on_click=on_click,
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.TRANSPARENT,
                            overlay_color=ft.Colors.with_opacity(0.1, "#ffffff"),
                            padding=ft.padding.symmetric(horizontal=40, vertical=18),
                            shape=ft.RoundedRectangleBorder(radius=16),
                        ),
                    ),
                    width=width,
                    height=58,
                    alignment=ft.alignment.center,
                ),
            ]),
            # Stunning shadow effects
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=25,
                color=ft.Colors.with_opacity(0.4, "#06b6d4"),
                offset=ft.Offset(0, 10),
            ),
            border_radius=16,
            margin=ft.margin.only(bottom=20),
            animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
        )
        
    def create_text_button(self, text, on_click):
        """Create elegant text button with sophisticated hover effects"""
        return ft.Container(
            content=ft.TextButton(
                content=ft.Text(
                    text,
                    size=15,
                    weight=ft.FontWeight.W_600,
                    color="#06b6d4",
                    font_family="Inter",
                ),
                on_click=on_click,
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.TRANSPARENT,
                    overlay_color=ft.Colors.with_opacity(0.08, "#06b6d4"),
                    padding=ft.padding.symmetric(horizontal=24, vertical=12),
                    shape=ft.RoundedRectangleBorder(radius=12),
                ),
            ),
            margin=ft.margin.only(top=8),
            animate=ft.Animation(200, ft.AnimationCurve.EASE_IN_OUT),
        )
        
    def show_login(self):
        """Show login page"""
        self.page.clean()
        
        # Create luxury form fields with language support
        email_field = self.create_luxury_form_field(
            language_manager.get_text("email"), 
            language_manager.get_text("enter_email")
        )
        password_field = self.create_luxury_form_field(
            language_manager.get_text("password"), 
            language_manager.get_text("enter_password"), 
            password=True
        )
        
        # Get text field references using the data attribute (FIXED)
        email_textfield = email_field.data
        password_textfield = password_field.data
        
        # Error message container
        error_container = ft.Container(
            content=ft.Text(
                "",
                size=12,
                color=self.styles.ERROR_COLOR,
                text_align=ft.TextAlign.CENTER,
            ),
            visible=False,
            padding=ft.padding.symmetric(vertical=5),
        )
        
        # Remember me checkbox
        remember_checkbox = ft.Checkbox(
            label="Ingat saya",
            value=False,
            fill_color=self.styles.TEXT_SECONDARY,
            check_color=ft.Colors.WHITE,
            label_style=ft.TextStyle(
                color=self.styles.TEXT_PRIMARY,
                size=14,
            ),
        )
        
        def handle_login(e):
            try:
                email = email_textfield.value.strip() if email_textfield.value else ""
                password = password_textfield.value.strip() if password_textfield.value else ""
                remember_me = remember_checkbox.value
                
                print(f"Login attempt - Email: {email}, Password length: {len(password)}")
                
                # Clear previous errors
                error_container.visible = False
                error_container.content.value = ""
                
                # Validation
                if not email or not password:
                    error_container.content.value = "Email dan password harus diisi"
                    error_container.visible = True
                    self.page.update()
                    return
                    
                if not self.validate_email(email):
                    error_container.content.value = "Format email tidak valid"
                    error_container.visible = True
                    self.page.update()
                    return
                    
                # Check credentials
                print(f"Authenticating user: {email}")
                user = self.db_manager.authenticate_user(email, password)
                print(f"Authentication result: {user}")
                
                if user:
                    print(f"Login successful for user: {user['email']}")
                    if remember_me:
                        print(f"Remember me enabled for user: {user['email']}")
                    self.on_success_callback(user)
                else:
                    print("Authentication failed")
                    error_container.content.value = "Email atau password salah"
                    error_container.visible = True
                    self.page.update()
                    
            except Exception as e:
                print(f"Login error: {e}")
                error_container.content.value = f"Terjadi kesalahan: {str(e)}"
                error_container.visible = True
                self.page.update()
        
        # Mobile-first scrollable login design
        login_content = ft.Column([
            # Compact header
            ft.Container(
                content=self.create_premium_header(
                    language_manager.get_text("login"), 
                    language_manager.get_text("professional_trading_platform")
                ),
                padding=ft.padding.only(top=15, bottom=10),
            ),
            
            # Scrollable form content
            ft.Container(
                content=ft.Column([
                    # Premium form card - compact design
                    ft.Container(
                        content=ft.Column([
                            # Form heading
                            ft.Text(
                                language_manager.get_text("exclusive_access"),
                                size=16,
                                weight=ft.FontWeight.W_900,
                                color="#ffffff",
                                text_align=ft.TextAlign.CENTER,
                                font_family="SF Pro Display",
                            ),
                            
                            ft.Container(height=20),
                            
                            # Form fields
                            email_field,
                            password_field,
                            
                            # Remember me and forgot password
                            ft.Row([
                                ft.Checkbox(
                                    label=language_manager.get_text("remember_me"),
                                    value=False,
                                    fill_color="#00d4ff",
                                    check_color="#ffffff",
                                    label_style=ft.TextStyle(
                                        color="#ffffff",
                                        size=11,
                                        weight=ft.FontWeight.W_600,
                                        font_family="Inter",
                                    ),
                                ),
                                ft.Container(expand=True),
                                ft.TextButton(
                                    content=ft.Text(
                                        language_manager.get_text("forgot_password_link"),
                                        size=11,
                                        weight=ft.FontWeight.W_700,
                                        color="#00d4ff",
                                        font_family="Inter",
                                    ),
                                    on_click=lambda e: self.show_forgot_password(),
                                    style=ft.ButtonStyle(
                                        overlay_color=ft.Colors.with_opacity(0.1, "#00d4ff"),
                                        padding=ft.padding.symmetric(horizontal=8, vertical=4),
                                        shape=ft.RoundedRectangleBorder(radius=6),
                                    ),
                                ),
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                            
                            ft.Container(height=15),
                            
                            # Error message
                            error_container,
                            
                            ft.Container(height=15),
                            
                            # Login button
                            self.create_primary_button(language_manager.get_text("login_now"), handle_login, 300),
                            
                            ft.Container(height=20),
                            
                            # Divider
                            ft.Stack([
                                ft.Container(
                                    height=1,
                                    gradient=ft.LinearGradient(
                                        colors=[
                                            ft.Colors.TRANSPARENT,
                                            ft.Colors.with_opacity(0.4, "#00d4ff"),
                                            ft.Colors.TRANSPARENT,
                                        ]
                                    ),
                                ),
                                ft.Container(
                                    content=ft.Text(
                                        "atau",
                                        size=10,
                                        color="#64748b",
                                        weight=ft.FontWeight.W_600,
                                        font_family="Inter",
                                    ),
                                    bgcolor=ft.Colors.with_opacity(0.95, "#0a0a1a"),
                                    padding=ft.padding.symmetric(horizontal=15),
                                    alignment=ft.alignment.center,
                                ),
                            ]),
                            
                            ft.Container(height=20),
                            
                            # Registration link - lebih prominent
                            ft.Container(
                                content=ft.Column([
                                    ft.Text(
                                        "Belum punya akun?",
                                        size=13,
                                        color="#94a3b8",
                                        weight=ft.FontWeight.W_500,
                                        font_family="Inter",
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    ft.Container(height=8),
                                    ft.Container(
                                        content=ft.TextButton(
                                            content=ft.Text(
                                                "DAFTAR SEKARANG",
                                                size=14,
                                                weight=ft.FontWeight.W_800,
                                                color="#00d4ff",
                                                font_family="SF Pro Display",
                                            ),
                                            on_click=lambda e: self.show_register(),
                                            style=ft.ButtonStyle(
                                                bgcolor=ft.Colors.with_opacity(0.1, "#00d4ff"),
                                                overlay_color=ft.Colors.with_opacity(0.2, "#00d4ff"),
                                                padding=ft.padding.symmetric(horizontal=20, vertical=12),
                                                shape=ft.RoundedRectangleBorder(radius=12),
                                            ),
                                        ),
                                        width=200,
                                        alignment=ft.alignment.center,
                                    ),
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                                margin=ft.margin.only(bottom=20),
                            ),
                            
                        ], spacing=0),
                        padding=ft.padding.all(25),
                        width=340,
                        border_radius=24,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_left,
                            end=ft.alignment.bottom_right,
                            colors=[
                                ft.Colors.with_opacity(0.18, "#ffffff"),
                                ft.Colors.with_opacity(0.08, "#00d4ff"),
                                ft.Colors.with_opacity(0.12, "#0ea5e9"),
                                ft.Colors.with_opacity(0.05, "#1e40af"),
                                ft.Colors.with_opacity(0.03, "#000000"),
                            ],
                        ),
                        border=ft.border.all(1.5, ft.Colors.with_opacity(0.3, "#00d4ff")),
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=30,
                            color=ft.Colors.with_opacity(0.3, "#000000"),
                            offset=ft.Offset(0, 15),
                        ),
                        animate=ft.Animation(600, ft.AnimationCurve.EASE_OUT),
                    ),
                    
                    ft.Container(height=50),  # Extra space for scroll
                    
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                expand=True,
            ),
            
        ], 
        spacing=0,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
        )
        
        # Create main container with background
        main_container = ft.Container(
            content=login_content,
            expand=True,
            bgcolor=ft.Colors.with_opacity(1.0, "#0a0a1a"),
            gradient=ft.RadialGradient(
                center=ft.alignment.top_center,
                radius=1.2,
                colors=[
                    ft.Colors.with_opacity(0.1, "#00d4ff"),
                    ft.Colors.with_opacity(0.05, "#0ea5e9"),
                    ft.Colors.with_opacity(1.0, "#0a0a1a"),
                ],
            ),
            padding=ft.padding.symmetric(horizontal=15, vertical=10),
        )
        
        self.page.add(main_container)
        self.page.update()
        
    def show_register(self):
        """Show registration page with mobile-optimized scrollable design"""
        self.page.clean()
        
        # Create luxury form fields
        username_field = self.create_luxury_form_field("Username", "Masukkan username Anda", icon=ft.Icons.PERSON)
        email_field = self.create_luxury_form_field("Email", "Masukkan email Anda")
        password_field = self.create_luxury_form_field("Password", "Masukkan password Anda", password=True)
        confirm_password_field = self.create_luxury_form_field("Konfirmasi Password", "Masukkan ulang password Anda", password=True)
        
        # Get text field references using the data attribute (FIXED)
        username_textfield = username_field.data
        email_textfield = email_field.data
        password_textfield = password_field.data
        confirm_password_textfield = confirm_password_field.data
        
        # Error message container with premium styling
        error_container = ft.Container(
            content=ft.Text(
                "",
                size=12,
                color="#ef4444",
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.W_600,
                font_family="Inter",
            ),
            visible=False,
            padding=ft.padding.symmetric(vertical=8),
            bgcolor=ft.Colors.with_opacity(0.1, "#ef4444"),
            border_radius=8,
            margin=ft.margin.symmetric(horizontal=5),
        )
        
        # Success message container with premium styling
        success_container = ft.Container(
            content=ft.Text(
                "",
                size=12,
                color="#10b981",
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.W_600,
                font_family="Inter",
            ),
            visible=False,
            padding=ft.padding.symmetric(vertical=8),
            bgcolor=ft.Colors.with_opacity(0.1, "#10b981"),
            border_radius=8,
            margin=ft.margin.symmetric(horizontal=5),
        )
        
        # Terms and conditions checkbox
        terms_checkbox = ft.Checkbox(
            label="",
            value=False,
            fill_color="#00d4ff",
            check_color="#ffffff",
        )
        
        def handle_register(e):
            try:
                username = username_textfield.value.strip() if username_textfield.value else ""
                email = email_textfield.value.strip() if email_textfield.value else ""
                password = password_textfield.value.strip() if password_textfield.value else ""
                confirm_password = confirm_password_textfield.value.strip() if confirm_password_textfield.value else ""
                terms_accepted = terms_checkbox.value
                
                # Clear previous messages
                error_container.visible = False
                success_container.visible = False
                self.page.update()
                
                # Validation
                if not username or not email or not password or not confirm_password:
                    error_container.content.value = "Semua field harus diisi"
                    error_container.visible = True
                    self.page.update()
                    return
                    
                if not self.validate_email(email):
                    error_container.content.value = "Format email tidak valid"
                    error_container.visible = True
                    self.page.update()
                    return
                    
                if len(password) < 6:
                    error_container.content.value = "Password minimal 6 karakter"
                    error_container.visible = True
                    self.page.update()
                    return
                    
                if password != confirm_password:
                    error_container.content.value = "Password tidak cocok"
                    error_container.visible = True
                    self.page.update()
                    return
                    
                if not terms_accepted:
                    error_container.content.value = "Anda harus menyetujui syarat dan ketentuan"
                    error_container.visible = True
                    self.page.update()
                    return
                    
                # Check if user already exists
                if self.db_manager.user_exists(email):
                    error_container.content.value = "Email sudah terdaftar"
                    error_container.visible = True
                    self.page.update()
                    return
                    
                # Create user
                user_data = {
                    'full_name': username,
                    'email': email,
                    'password': password,
                    'phone': '',
                    'is_admin': False
                }
                
                if self.db_manager.create_user(user_data):
                    success_container.content.value = "Registrasi berhasil! Silahkan login."
                    success_container.visible = True
                    self.page.update()
                    
                    # Auto redirect to login after 2 seconds
                    def redirect_to_login():
                        import time
                        time.sleep(2)
                        self.show_login()
                    
                    import threading
                    thread = threading.Thread(target=redirect_to_login)
                    thread.daemon = True
                    thread.start()
                else:
                    error_container.content.value = "Gagal mendaftar. Silahkan coba lagi."
                    error_container.visible = True
                    self.page.update()
            except Exception as e:
                error_container.content.value = f"Terjadi kesalahan: {str(e)}"
                error_container.visible = True
                self.page.update()
        
        register_content = ft.Container(
            content=ft.Stack([
                # Background pattern
                ft.Container(
                    width=400,
                    height=900,
                    gradient=ft.LinearGradient(
                        colors=[
                            ft.Colors.with_opacity(0.08, self.styles.TEXT_SECONDARY),
                            self.styles.PRIMARY_COLOR,
                            ft.Colors.with_opacity(0.03, self.styles.ACCENT_COLOR),
                        ],
                        begin=ft.alignment.top_left,
                        end=ft.alignment.bottom_right,
                    ),
                ),
                # Main content
                ft.Column([
                    ft.Container(height=30),
                    
                    self.create_premium_header("Daftar", "Buat akun ATV - AUTOTRADEVIP"),
                    
                    ft.Container(height=25),
                    
                    # Enhanced form card
                    ft.Container(
                        content=ft.Column([
                            username_field,
                            email_field,
                            password_field,
                            confirm_password_field,
                            
                            # Terms and conditions
                            ft.Container(
                                content=ft.Row([
                                    terms_checkbox,
                                    ft.Column([
                                        ft.Text(
                                            "Saya setuju dengan ",
                                            size=12,
                                            color=self.styles.TEXT_TERTIARY,
                                            spans=[
                                                ft.TextSpan(
                                                    "Syarat dan Ketentuan",
                                                    style=ft.TextStyle(
                                                        color=self.styles.TEXT_SECONDARY,
                                                        decoration=ft.TextDecoration.UNDERLINE,
                                                    ),
                                                ),
                                                ft.TextSpan(" dan "),
                                                ft.TextSpan(
                                                    "Kebijakan Privasi",
                                                    style=ft.TextStyle(
                                                        color=self.styles.TEXT_SECONDARY,
                                                        decoration=ft.TextDecoration.UNDERLINE,
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ], expand=True),
                                ], spacing=8),
                                padding=ft.padding.symmetric(vertical=15),
                            ),
                            
                            error_container,
                            success_container,
                            
                            ft.Container(height=10),
                            
                            self.create_primary_button("DAFTAR", handle_register),
                            
                            ft.Container(height=25),
                            
                            # Divider
                            ft.Container(
                                content=ft.Row([
                                    ft.Container(height=1, bgcolor=self.styles.CARD_BORDER, expand=True),
                                    ft.Text(language_manager.get_text("or"), size=12, color=self.styles.TEXT_MUTED),
                                    ft.Container(height=1, bgcolor=self.styles.CARD_BORDER, expand=True),
                                ], spacing=10),
                                padding=ft.padding.symmetric(vertical=10),
                            ),
                            
                            ft.Row([
                                ft.Text(language_manager.get_text("already_have_account") + " ", size=14, color=self.styles.TEXT_TERTIARY),
                                self.create_text_button(language_manager.get_text("login"), lambda e: self.show_login()),
                            ], alignment=ft.MainAxisAlignment.CENTER),
                            
                        ], spacing=0),
                        bgcolor=self.styles.SECONDARY_COLOR,
                        padding=35,
                        margin=ft.margin.symmetric(horizontal=20),
                        border_radius=20,
                        border=ft.border.all(1, self.styles.CARD_BORDER),
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=25,
                            color=ft.Colors.BLACK26,
                            offset=ft.Offset(0, 10),
                        ),
                    ),
                    
                    ft.Container(height=30),
                    
                ], 
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO,
                ),
            ]),
            expand=True,
            bgcolor=self.styles.PRIMARY_COLOR,
            padding=ft.padding.symmetric(horizontal=10, vertical=20),
            opacity=0,
            animate_opacity=ft.Animation(800, ft.AnimationCurve.EASE_IN_OUT)
        )
        
        self.page.add(register_content)
        register_content.opacity = 1
        self.page.update()
        
    def show_forgot_password(self):
        """Show forgot password page"""
        self.page.clean()
        
        # Create luxury form field
        email_field = self.create_luxury_form_field("Email", "Masukkan email Anda")
        
        # Get text field reference using the data attribute (FIXED)
        email_textfield = email_field.data
        
        # Error message container
        error_container = ft.Container(
            content=ft.Text(
                "",
                size=12,
                color=self.styles.ERROR_COLOR,
                text_align=ft.TextAlign.CENTER,
            ),
            visible=False,
            padding=ft.padding.symmetric(vertical=5),
        )
        
        # Success message container
        success_container = ft.Container(
            content=ft.Text(
                "",
                size=12,
                color=self.styles.SUCCESS_COLOR,
                text_align=ft.TextAlign.CENTER,
            ),
            visible=False,
            padding=ft.padding.symmetric(vertical=5),
        )
        
        def handle_forgot_password(e):
            email = email_textfield.value
            
            # Reset messages
            error_container.visible = False
            success_container.visible = False
            
            # Validation
            if not email:
                error_container.content.value = "Email harus diisi"
                error_container.visible = True
                self.page.update()
                return
                
            if not self.validate_email(email):
                error_container.content.value = "Format email tidak valid"
                error_container.visible = True
                self.page.update()
                return
                
            # Check if user exists
            if not self.db_manager.user_exists(email):
                error_container.content.value = "Email tidak terdaftar"
                error_container.visible = True
                self.page.update()
                return
                
            # Simulate password reset (in real app, would send email)
            success_container.content.value = "Link reset password telah dikirim ke email Anda"
            success_container.visible = True
            self.page.update()
        
        forgot_password_content = ft.Container(
            content=ft.Stack([
                # Background pattern
                ft.Container(
                    width=400,
                    height=900,
                    gradient=ft.LinearGradient(
                        colors=[
                            ft.Colors.with_opacity(0.06, self.styles.TEXT_SECONDARY),
                            self.styles.PRIMARY_COLOR,
                            ft.Colors.with_opacity(0.02, self.styles.ACCENT_COLOR),
                        ],
                        begin=ft.alignment.top_left,
                        end=ft.alignment.bottom_right,
                    ),
                ),
                # Main content
                ft.Column([
                    ft.Container(height=50),
                    
                    self.create_premium_header("Lupa Password", "Masukkan email untuk reset password"),
                    
                    ft.Container(height=30),
                    
                    # Enhanced form card
                    ft.Container(
                        content=ft.Column([
                            email_field,
                            error_container,
                            success_container,
                            
                            ft.Container(height=15),
                            
                            self.create_primary_button("KIRIM LINK RESET", handle_forgot_password),
                            
                            ft.Container(height=25),
                            
                            # Divider
                            ft.Container(
                                content=ft.Row([
                                    ft.Container(height=1, bgcolor=self.styles.CARD_BORDER, expand=True),
                                    ft.Text(language_manager.get_text("or"), size=12, color=self.styles.TEXT_MUTED),
                                    ft.Container(height=1, bgcolor=self.styles.CARD_BORDER, expand=True),
                                ], spacing=10),
                                padding=ft.padding.symmetric(vertical=10),
                            ),
                            
                            ft.Row([
                                self.create_text_button("← Kembali ke Login", lambda e: self.show_login()),
                            ], alignment=ft.MainAxisAlignment.CENTER),
                            
                        ], spacing=0),
                        bgcolor=self.styles.SECONDARY_COLOR,
                        padding=35,
                        margin=ft.margin.symmetric(horizontal=20),
                        border_radius=20,
                        border=ft.border.all(1, self.styles.CARD_BORDER),
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=25,
                            color=ft.Colors.BLACK26,
                            offset=ft.Offset(0, 10),
                        ),
                    ),
                    
                    ft.Container(height=50),
                    
                ], 
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO,
                ),
            ]),
            expand=True,
            bgcolor=self.styles.PRIMARY_COLOR,
            padding=ft.padding.symmetric(horizontal=10, vertical=20),
            opacity=0,
            animate_opacity=ft.Animation(800, ft.AnimationCurve.EASE_IN_OUT)
        )
        
        self.page.add(forgot_password_content)
        forgot_password_content.opacity = 1
        self.page.update()