import flet as ft
import hashlib
import re
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from core.styles import AppStyles
from services.database.sqlite_manager import SQLiteManager

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
        
    def create_header(self, title, subtitle=None):
        """Create ultra-professional header with stunning visual effects"""
        return ft.Container(
            content=ft.Column([
                # Ultra-modern floating logo with dynamic effects
                ft.Container(
                    content=ft.Stack([
                        # Outer glow ring with pulsing animation
                        ft.Container(
                            width=120,
                            height=120,
                            border_radius=60,
                            gradient=ft.RadialGradient(
                                center=ft.alignment.center,
                                radius=1.2,
                                colors=[
                                    ft.Colors.with_opacity(0.3, "#06b6d4"),
                                    ft.Colors.with_opacity(0.1, "#3b82f6"),
                                    ft.Colors.with_opacity(0.05, "#1e3a8a"),
                                    ft.Colors.TRANSPARENT,
                                ],
                                stops=[0.0, 0.4, 0.7, 1.0],
                            ),
                            animate=ft.Animation(1500, ft.AnimationCurve.EASE_IN_OUT),
                        ),
                        # Main logo container with glassmorphism effect
                        ft.Container(
                            width=100,
                            height=100,
                            border_radius=50,
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.top_left,
                                end=ft.alignment.bottom_right,
                                colors=[
                                    ft.Colors.with_opacity(0.15, "#ffffff"),
                                    ft.Colors.with_opacity(0.05, "#06b6d4"),
                                    ft.Colors.with_opacity(0.1, "#1e3a8a"),
                                ],
                            ),
                            border=ft.border.all(1, ft.Colors.with_opacity(0.2, "#06b6d4")),
                            shadow=ft.BoxShadow(
                                spread_radius=0,
                                blur_radius=25,
                                color=ft.Colors.with_opacity(0.3, "#06b6d4"),
                                offset=ft.Offset(0, 8),
                            ),
                            content=ft.Column([
                                ft.Text(
                                    "ATV",
                                    size=28,
                                    weight=ft.FontWeight.BOLD,
                                    color="#ffffff",
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                ft.Text(
                                    "AUTOTRADEVIP",
                                    size=6,
                                    weight=ft.FontWeight.W_600,
                                    color="#06b6d4",
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ],
                            spacing=0,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            alignment=ft.alignment.center,
                            left=10,
                            top=10,
                        ),
                        # Inner highlight effect
                        ft.Container(
                            width=100,
                            height=100,
                            border_radius=50,
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.top_center,
                                end=ft.alignment.center,
                                colors=[
                                    ft.Colors.with_opacity(0.3, "#ffffff"),
                                    ft.Colors.TRANSPARENT,
                                ],
                            ),
                            left=10,
                            top=10,
                        ),
                    ]),
                    width=120,
                    height=120,
                    margin=ft.margin.only(bottom=30),
                ),
                # Elegant title with gradient text effect
                ft.Container(
                    content=ft.Stack([
                        # Shadow text for depth
                        ft.Text(
                            title,
                            size=34,
                            weight=ft.FontWeight.W_700,
                            color=ft.Colors.with_opacity(0.3, "#000000"),
                            text_align=ft.TextAlign.CENTER,
                        ),
                        # Main gradient title
                        ft.Container(
                            content=ft.Text(
                                title,
                                size=34,
                                weight=ft.FontWeight.W_700,
                                color="#ffffff",
                                text_align=ft.TextAlign.CENTER,
                            ),
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.top_center,
                                end=ft.alignment.bottom_center,
                                colors=["#ffffff", "#06b6d4"],
                            ),
                            left=0,
                            top=-2,
                        ),
                    ]),
                    margin=ft.margin.only(bottom=12),
                ),
                # Sophisticated subtitle with elegant typography
                ft.Container(
                    content=ft.Text(
                        subtitle if subtitle else "Platform Trading Profesional",
                        size=15,
                        color="#94a3b8",
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.W_400,
                    ),
                    margin=ft.margin.only(bottom=25),
                ) if subtitle or True else ft.Container(),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.padding.only(top=20, bottom=20),
            alignment=ft.alignment.center,
        )
        
    def create_form_field(self, label, hint_text, password=False, value="", icon=None):
        """Create ultra-professional form field with glassmorphism and advanced animations"""
        # Determine the appropriate icon with enhanced visual appeal
        field_icon = icon
        if not field_icon:
            if password:
                field_icon = ft.Icons.LOCK_ROUNDED
            elif "email" in label.lower():
                field_icon = ft.Icons.ALTERNATE_EMAIL_ROUNDED
            elif "name" in label.lower():
                field_icon = ft.Icons.PERSON_ROUNDED
            elif "phone" in label.lower():
                field_icon = ft.Icons.PHONE_ROUNDED
            else:
                field_icon = ft.Icons.TEXT_FIELDS_ROUNDED
        
        # Create animated text field with enhanced focus effects
        text_field = ft.TextField(
            hint_text=hint_text,
            password=password,
            value=value,
            border_color=ft.Colors.TRANSPARENT,
            focused_border_color=ft.Colors.TRANSPARENT,
            cursor_color="#06b6d4",
            text_style=ft.TextStyle(
                size=16,
                color="#ffffff",
                weight=ft.FontWeight.W_500,
            ),
            hint_style=ft.TextStyle(
                size=16,
                color="#64748b",
                weight=ft.FontWeight.W_400,
            ),
            bgcolor=ft.Colors.TRANSPARENT,
            content_padding=ft.padding.symmetric(horizontal=20, vertical=18),
            expand=True,
        )
        
        return ft.Container(
            content=ft.Column([
                # Floating label with elegant typography
                ft.Container(
                    content=ft.Text(
                        label,
                        size=13,
                        weight=ft.FontWeight.W_600,
                        color="#06b6d4",
                    ),
                    padding=ft.padding.only(left=8, bottom=8),
                ),
                # Premium glassmorphism input container
                ft.Container(
                    content=ft.Stack([
                        # Background blur effect
                        ft.Container(
                            width=320,
                            height=58,
                            border_radius=16,
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.top_left,
                                end=ft.alignment.bottom_right,
                                colors=[
                                    ft.Colors.with_opacity(0.08, "#ffffff"),
                                    ft.Colors.with_opacity(0.03, "#06b6d4"),
                                    ft.Colors.with_opacity(0.05, "#1e3a8a"),
                                ],
                            ),
                            border=ft.border.all(1, ft.Colors.with_opacity(0.15, "#06b6d4")),
                        ),
                        # Input field row with enhanced spacing
                        ft.Container(
                            content=ft.Row([
                                # Animated icon with glow effect
                                ft.Container(
                                    content=ft.Icon(
                                        field_icon,
                                        size=20,
                                        color="#06b6d4",
                                    ),
                                    padding=ft.padding.only(left=18, right=8),
                                ),
                                # Main text field
                                text_field,
                            ],
                            spacing=0,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            width=320,
                            height=58,
                        ),
                        # Focus glow effect overlay
                        ft.Container(
                            width=320,
                            height=58,
                            border_radius=16,
                            border=ft.border.all(1, ft.Colors.TRANSPARENT),
                            shadow=ft.BoxShadow(
                                spread_radius=0,
                                blur_radius=15,
                                color=ft.Colors.with_opacity(0.2, "#06b6d4"),
                                offset=ft.Offset(0, 4),
                            ),
                        ),
                    ]),
                    # Hover animation for enhanced interactivity
                    animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
                ),
            ],
            spacing=0,
            ),
            margin=ft.margin.only(bottom=20),
            animate=ft.Animation(200, ft.AnimationCurve.EASE_IN_OUT),
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
        
        # Create form fields
        email_field = self.create_form_field("Email", "Masukkan email Anda")
        password_field = self.create_form_field("Password", "Masukkan password Anda", password=True)
        
        # Get text field references from the new structure
        email_textfield = email_field.content.controls[1].content.controls[1].content.controls[1]
        password_textfield = password_field.content.controls[1].content.controls[1].content.controls[1]
        
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
        
        # Ultra-professional login page with stunning visual effects
        login_content = ft.Container(
            content=ft.Stack([
                # Dynamic gradient background with floating particles effect
                ft.Container(
                    width=400,
                    height=900,
                    gradient=ft.RadialGradient(
                        center=ft.alignment.center,
                        radius=1.5,
                        colors=[
                            ft.Colors.with_opacity(0.15, "#06b6d4"),
                            ft.Colors.with_opacity(0.08, "#1e3a8a"),
                            self.styles.PRIMARY_COLOR,
                            ft.Colors.with_opacity(0.05, "#000000"),
                        ],
                        stops=[0.0, 0.3, 0.7, 1.0],
                    ),
                ),
                # Main content with professional layout
                ft.Column([
                    ft.Container(height=50),
                    
                    # Ultra-modern header
                    self.create_header("Masuk", "Selamat datang kembali di platform trading profesional"),
                    
                    ft.Container(height=40),
                    
                    # Premium glassmorphism form card
                    ft.Container(
                        content=ft.Stack([
                            # Card background with sophisticated gradients
                            ft.Container(
                                width=340,
                                height=520,
                                border_radius=24,
                                gradient=ft.LinearGradient(
                                    begin=ft.alignment.top_left,
                                    end=ft.alignment.bottom_right,
                                    colors=[
                                        ft.Colors.with_opacity(0.12, "#ffffff"),
                                        ft.Colors.with_opacity(0.05, "#06b6d4"),
                                        ft.Colors.with_opacity(0.08, "#1e3a8a"),
                                        ft.Colors.with_opacity(0.03, "#000000"),
                                    ],
                                ),
                                border=ft.border.all(1, ft.Colors.with_opacity(0.2, "#06b6d4")),
                                shadow=ft.BoxShadow(
                                    spread_radius=0,
                                    blur_radius=40,
                                    color=ft.Colors.with_opacity(0.3, "#000000"),
                                    offset=ft.Offset(0, 20),
                                ),
                            ),
                            # Form content with elegant spacing
                            ft.Container(
                                content=ft.Column([
                                    # Professional form heading
                                    ft.Container(
                                        content=ft.Text(
                                            "Akses Akun Anda",
                                            size=18,
                                            weight=ft.FontWeight.W_700,
                                            color="#ffffff",
                                            text_align=ft.TextAlign.CENTER,
                                        ),
                                        margin=ft.margin.only(bottom=30),
                                    ),
                                    
                                    # Enhanced form fields
                                    email_field,
                                    password_field,
                                    
                                    # Premium remember me and forgot password section
                                    ft.Container(
                                        content=ft.Row([
                                            ft.Checkbox(
                                                label="Ingat saya",
                                                value=False,
                                                fill_color="#06b6d4",
                                                check_color="#ffffff",
                                                label_style=ft.TextStyle(
                                                    color="#ffffff",
                                                    size=13,
                                                    weight=ft.FontWeight.W_500,
                                                ),
                                            ),
                                            ft.Container(expand=True),
                                            ft.TextButton(
                                                content=ft.Text(
                                                    "Lupa Password?",
                                                    size=13,
                                                    weight=ft.FontWeight.W_600,
                                                    color="#06b6d4",
                                                ),
                                                on_click=lambda e: self.show_forgot_password(),
                                                style=ft.ButtonStyle(
                                                    overlay_color=ft.Colors.with_opacity(0.1, "#06b6d4"),
                                                    padding=ft.padding.symmetric(horizontal=8, vertical=4),
                                                ),
                                            ),
                                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                        margin=ft.margin.symmetric(vertical=15),
                                    ),
                                    
                                    # Error message with elegant styling
                                    error_container,
                                    
                                    ft.Container(height=20),
                                    
                                    # Premium login button
                                    self.create_primary_button("MASUK SEKARANG", handle_login),
                                    
                                    ft.Container(height=30),
                                    
                                    # Elegant divider with glow effect
                                    ft.Container(
                                        content=ft.Stack([
                                            ft.Container(
                                                height=1,
                                                gradient=ft.LinearGradient(
                                                    colors=[
                                                        ft.Colors.TRANSPARENT,
                                                        ft.Colors.with_opacity(0.3, "#06b6d4"),
                                                        ft.Colors.TRANSPARENT,
                                                    ]
                                                ),
                                            ),
                                            ft.Container(
                                                content=ft.Text(
                                                    "atau",
                                                    size=12,
                                                    color="#64748b",
                                                    weight=ft.FontWeight.W_500,
                                                ),
                                                bgcolor=ft.Colors.with_opacity(0.9, "#0a0a1a"),
                                                padding=ft.padding.symmetric(horizontal=15),
                                                alignment=ft.alignment.center,
                                            ),
                                        ]),
                                        margin=ft.margin.symmetric(vertical=20),
                                    ),
                                    
                                    # Registration link with professional styling
                                    ft.Container(
                                        content=ft.Row([
                                            ft.Text(
                                                "Belum punya akun? ",
                                                size=14,
                                                color="#94a3b8",
                                                weight=ft.FontWeight.W_400,
                                            ),
                                            ft.TextButton(
                                                content=ft.Text(
                                                    "Daftar Sekarang",
                                                    size=14,
                                                    weight=ft.FontWeight.W_700,
                                                    color="#06b6d4",
                                                ),
                                                on_click=lambda e: self.show_register(),
                                                style=ft.ButtonStyle(
                                                    overlay_color=ft.Colors.with_opacity(0.1, "#06b6d4"),
                                                    padding=ft.padding.symmetric(horizontal=8, vertical=4),
                                                ),
                                            ),
                                        ], alignment=ft.MainAxisAlignment.CENTER),
                                        margin=ft.margin.only(top=10),
                                    ),
                                ], spacing=0),
                                padding=40,
                                width=340,
                                height=520,
                            ),
                        ]),
                        margin=ft.margin.symmetric(horizontal=20),
                        animate=ft.Animation(600, ft.AnimationCurve.EASE_OUT),
                    ),
                    
                    ft.Container(height=60),
                    
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
            animate_opacity=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
        )
        
        self.page.add(login_content)
        login_content.opacity = 1
        self.page.update()
        
    def show_register(self):
        """Show registration page"""
        self.page.clean()
        
        # Create form fields
        username_field = self.create_form_field("Username", "Masukkan username Anda", icon=ft.Icons.PERSON)
        email_field = self.create_form_field("Email", "Masukkan email Anda")
        password_field = self.create_form_field("Password", "Masukkan password Anda", password=True)
        confirm_password_field = self.create_form_field("Konfirmasi Password", "Masukkan ulang password Anda", password=True)
        
        # Get text field references
        username_textfield = username_field.content.controls[1].content.controls[-1]
        email_textfield = email_field.content.controls[1].content.controls[-1]
        password_textfield = password_field.content.controls[1].content.controls[-1]
        confirm_password_textfield = confirm_password_field.content.controls[1].content.controls[-1]
        
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
        
        # Terms and conditions checkbox
        terms_checkbox = ft.Checkbox(
            label="",
            value=False,
            fill_color=self.styles.TEXT_SECONDARY,
            check_color=ft.Colors.WHITE,
        )
        
        def handle_register(e):
            username = username_textfield.value
            email = email_textfield.value
            password = password_textfield.value
            confirm_password = confirm_password_textfield.value
            agree_terms = terms_checkbox.value
            
            # Reset messages
            error_container.visible = False
            success_container.visible = False
            
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
                
            if not agree_terms:
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
                'username': username,
                'email': email,
                'password': self.hash_password(password)
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
                    
                    self.create_header("Daftar", "Buat akun ATV - AUTOTRADEVIP"),
                    
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
                                    ft.Text("atau", size=12, color=self.styles.TEXT_MUTED),
                                    ft.Container(height=1, bgcolor=self.styles.CARD_BORDER, expand=True),
                                ], spacing=10),
                                padding=ft.padding.symmetric(vertical=10),
                            ),
                            
                            ft.Row([
                                ft.Text("Sudah punya akun? ", size=14, color=self.styles.TEXT_TERTIARY),
                                self.create_text_button("Masuk", lambda e: self.show_login()),
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
        
        # Create form fields
        email_field = self.create_form_field("Email", "Masukkan email Anda")
        
        # Get text field reference
        email_textfield = email_field.content.controls[1].content.controls[-1]
        
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
                    
                    self.create_header("Lupa Password", "Masukkan email untuk reset password"),
                    
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
                                    ft.Text("atau", size=12, color=self.styles.TEXT_MUTED),
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