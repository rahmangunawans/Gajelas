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
        """Create professional header for auth pages"""
        header_content = [
            # Professional logo section
            ft.Container(
                content=ft.Column([
                    # Modern ATV logo with professional styling
                    ft.Container(
                        content=ft.Stack([
                            # Subtle background circle
                            ft.Container(
                                width=90,
                                height=90,
                                border_radius=45,
                                gradient=ft.LinearGradient(
                                    begin=ft.alignment.top_left,
                                    end=ft.alignment.bottom_right,
                                    colors=[
                                        ft.Colors.with_opacity(0.1, "#06b6d4"),
                                        ft.Colors.with_opacity(0.05, "#3b82f6"),
                                    ],
                                ),
                                border=ft.border.all(1, ft.Colors.with_opacity(0.1, "#06b6d4")),
                            ),
                            # Professional ATV text logo
                            ft.Container(
                                content=ft.Column([
                                    ft.Text(
                                        "ATV",
                                        size=26,
                                        weight=ft.FontWeight.BOLD,
                                        color="#ffffff",
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    ft.Text(
                                        "AUTOTRADEVIP",
                                        size=7,
                                        weight=ft.FontWeight.W_500,
                                        color="#06b6d4",
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ],
                                spacing=2,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                width=90,
                                height=90,
                                alignment=ft.alignment.center,
                            ),
                        ]),
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(bottom=30),
                    ),
                ]),
                alignment=ft.alignment.center,
            ),
            # Professional title
            ft.Container(
                content=ft.Text(
                    title,
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color="#ffffff",
                    text_align=ft.TextAlign.CENTER,
                ),
                padding=ft.padding.only(bottom=8),
            ),
        ]
        
        if subtitle:
            header_content.append(
                ft.Container(
                    content=ft.Text(
                        subtitle,
                        size=16,
                        color="#94a3b8",
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.W_400,
                    ),
                    padding=ft.padding.only(top=5, bottom=20),
                )
            )
            
        return ft.Column(
            header_content,
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
    def create_form_field(self, label, hint_text, password=False, value="", icon=None):
        """Create professional form field with modern styling"""
        # Determine the appropriate icon
        field_icon = icon
        if not field_icon:
            if password:
                field_icon = ft.Icons.LOCK_OUTLINE
            elif "email" in label.lower():
                field_icon = ft.Icons.EMAIL_OUTLINED
            elif "name" in label.lower():
                field_icon = ft.Icons.PERSON_OUTLINE
            elif "phone" in label.lower():
                field_icon = ft.Icons.PHONE_OUTLINED
            else:
                field_icon = ft.Icons.TEXT_FIELDS_OUTLINED
        
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
                weight=ft.FontWeight.W_400,
            ),
            hint_style=ft.TextStyle(
                size=16,
                color="#64748b",
                weight=ft.FontWeight.W_400,
            ),
            bgcolor=ft.Colors.TRANSPARENT,
            content_padding=ft.padding.symmetric(horizontal=16, vertical=18),
            expand=True,
        )
        
        return ft.Container(
            content=ft.Column([
                # Field label
                ft.Container(
                    content=ft.Text(
                        label,
                        size=14,
                        weight=ft.FontWeight.W_600,
                        color="#ffffff",
                    ),
                    padding=ft.padding.only(left=4, bottom=8),
                ),
                # Input field container
                ft.Container(
                    content=ft.Row([
                        ft.Icon(
                            field_icon,
                            size=22,
                            color="#64748b",
                        ),
                        text_field,
                    ], spacing=12),
                    bgcolor="#151528",
                    border_radius=12,
                    border=ft.border.all(1, "#334155"),
                    padding=ft.padding.symmetric(horizontal=16, vertical=2),
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=8,
                        color=ft.Colors.with_opacity(0.1, "#000000"),
                        offset=ft.Offset(0, 2),
                    ),
                ),
            ], spacing=0),
            padding=ft.padding.only(bottom=20),
        )
        
    def create_primary_button(self, text, on_click, width=320):
        """Create modern primary button with professional styling"""
        return ft.Container(
            content=ft.ElevatedButton(
                text,
                on_click=on_click,
                style=ft.ButtonStyle(
                    color=ft.Colors.WHITE,
                    bgcolor="#06b6d4",
                    padding=ft.padding.symmetric(horizontal=40, vertical=18),
                    text_style=ft.TextStyle(
                        size=16,
                        weight=ft.FontWeight.W_600,
                        letter_spacing=0.5,
                    ),
                    shape=ft.RoundedRectangleBorder(radius=12),
                    elevation=0,
                    shadow_color=ft.Colors.TRANSPARENT,
                ),
                width=width,
                height=56,
            ),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=20,
                color=ft.Colors.with_opacity(0.3, "#06b6d4"),
                offset=ft.Offset(0, 8),
            ),
            border_radius=12,
            margin=ft.margin.only(bottom=16),
        )
        
    def create_text_button(self, text, on_click):
        """Create modern text button for navigation"""
        return ft.Container(
            content=ft.TextButton(
                text,
                on_click=on_click,
                style=ft.ButtonStyle(
                    color="#06b6d4",
                    padding=ft.padding.symmetric(horizontal=20, vertical=12),
                    text_style=ft.TextStyle(
                        size=14,
                        weight=ft.FontWeight.W_600,
                    ),
                    shape=ft.RoundedRectangleBorder(radius=8),
                ),
            ),
            alignment=ft.alignment.center,
        )
        
    def show_login(self):
        """Show login page"""
        self.page.clean()
        
        # Create form fields
        email_field = self.create_form_field("Email", "Masukkan email Anda")
        password_field = self.create_form_field("Password", "Masukkan password Anda", password=True)
        
        # Get text field references more safely
        try:
            email_textfield = email_field.content.controls[1].content.controls[-1]
            password_textfield = password_field.content.controls[1].content.controls[-1]
        except (IndexError, AttributeError):
            # Fallback for field access
            email_textfield = email_field.content.controls[1].content.controls[1] if len(email_field.content.controls[1].content.controls) > 1 else email_field.content.controls[1].content.controls[0]
            password_textfield = password_field.content.controls[1].content.controls[1] if len(password_field.content.controls[1].content.controls) > 1 else password_field.content.controls[1].content.controls[0]
        
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
        
        login_content = ft.Container(
            content=ft.Stack([
                # Background pattern
                ft.Container(
                    width=400,
                    height=900,
                    gradient=ft.LinearGradient(
                        colors=[
                            ft.Colors.with_opacity(0.1, self.styles.TEXT_SECONDARY),
                            self.styles.PRIMARY_COLOR,
                            ft.Colors.with_opacity(0.05, self.styles.ACCENT_COLOR),
                        ],
                        begin=ft.alignment.top_left,
                        end=ft.alignment.bottom_right,
                    ),
                ),
                # Main content
                ft.Column([
                    ft.Container(height=40),
                    
                    self.create_header("Masuk", "Selamat datang kembali di ATV"),
                    
                    ft.Container(height=30),
                    
                    # Enhanced form card
                    ft.Container(
                        content=ft.Column([
                            email_field,
                            password_field,
                            
                            # Remember me and Forgot password row
                            ft.Container(
                                content=ft.Row([
                                    remember_checkbox,
                                    ft.Container(expand=True),
                                    self.create_text_button("Lupa Password?", lambda e: self.show_forgot_password()),
                                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                padding=ft.padding.symmetric(vertical=10),
                            ),
                            
                            error_container,
                            
                            ft.Container(height=10),
                            
                            self.create_primary_button("MASUK", handle_login),
                            
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
                                ft.Text("Belum punya akun? ", size=14, color=self.styles.TEXT_TERTIARY),
                                self.create_text_button("Daftar", lambda e: self.show_register()),
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
                    
                    ft.Container(height=40),
                    
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