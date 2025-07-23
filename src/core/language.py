"""
Language management system for ATV application
"""

class LanguageManager:
    """Manage application languages"""
    
    def __init__(self):
        self.current_language = "en"  # Default to English
        self.languages = {
            "en": {
                # Auth pages
                "login": "Login",
                "register": "Register",
                "forgot_password": "Forgot Password",
                "email": "Email",
                "password": "Password",
                "confirm_password": "Confirm Password",
                "username": "Username",
                "enter_email": "Enter your email",
                "enter_password": "Enter your password",
                "enter_username": "Enter your username",
                "remember_me": "Remember me",
                "forgot_password_link": "Forgot Password?",
                "login_now": "LOGIN NOW",
                "register_now": "REGISTER",
                "send_reset_link": "SEND RESET LINK",
                "back_to_login": "← Back to Login",
                "exclusive_access": "Exclusive Access",
                "professional_trading_platform": "Professional Trading Platform",
                "create_atv_account": "Create ATV - AUTOTRADEVIP Account",
                "enter_email_for_reset": "Enter email to reset password",
                
                # Dashboard
                "dashboard": "Dashboard",
                "trading_bots": "Trading Bots",
                "active_bots": "Active Bots",
                "history": "History",
                "profile": "Profile",
                "settings": "Settings",
                "help_support": "Help & Support",
                "logout": "Logout",
                "language": "Language",
                
                # Brokers
                "beranda": "Home",
                "binomo": "Binomo",
                "quotex": "Quotex",
                "olymptrade": "Olymptrade",
                "iq_option": "IQ Option",
                "stockity": "Stockity",
                
                # Common
                "or": "or",
                "already_have_account": "Already have an account?",
                "terms_conditions": "Terms and Conditions",
                "privacy_policy": "Privacy Policy",
                "i_agree_with": "I agree with",
                "and": "and",
                
                # Messages
                "all_fields_required": "All fields are required",
                "invalid_email_format": "Invalid email format",
                "password_min_length": "Password must be at least 6 characters",
                "passwords_dont_match": "Passwords don't match",
                "must_accept_terms": "You must accept terms and conditions",
                "email_already_registered": "Email already registered",
                "registration_successful": "Registration successful! Please login.",
                "registration_failed": "Registration failed. Please try again.",
                "email_and_password_required": "Email and password are required",
                "invalid_credentials": "Invalid email or password",
                "reset_link_sent": "Password reset link has been sent to your email",
                "email_not_registered": "Email not registered",
                "email_required": "Email is required",
            },
            "id": {
                # Auth pages
                "login": "Masuk",
                "register": "Daftar",
                "forgot_password": "Lupa Password",
                "email": "Email",
                "password": "Password",
                "confirm_password": "Konfirmasi Password",
                "username": "Username",
                "enter_email": "Masukkan email Anda",
                "enter_password": "Masukkan password Anda",
                "enter_username": "Masukkan username Anda",
                "remember_me": "Ingat saya",
                "forgot_password_link": "Lupa Password?",
                "login_now": "MASUK SEKARANG",
                "register_now": "DAFTAR",
                "send_reset_link": "KIRIM LINK RESET",
                "back_to_login": "← Kembali ke Login",
                "exclusive_access": "Akses Eksklusif",
                "professional_trading_platform": "Platform Trading Profesional",
                "create_atv_account": "Buat akun ATV - AUTOTRADEVIP",
                "enter_email_for_reset": "Masukkan email untuk reset password",
                
                # Dashboard
                "dashboard": "Dashboard",
                "trading_bots": "Trading Bot",
                "active_bots": "Bot Aktif",
                "history": "Riwayat",
                "profile": "Profil",
                "settings": "Pengaturan",
                "help_support": "Bantuan & Dukungan",
                "logout": "Keluar",
                "language": "Bahasa",
                
                # Brokers
                "beranda": "Beranda",
                "binomo": "Binomo",
                "quotex": "Quotex",
                "olymptrade": "Olymptrade",
                "iq_option": "IQ Option",
                "stockity": "Stockity",
                
                # Common
                "or": "atau",
                "already_have_account": "Sudah punya akun?",
                "terms_conditions": "Syarat dan Ketentuan",
                "privacy_policy": "Kebijakan Privasi",
                "i_agree_with": "Saya setuju dengan",
                "and": "dan",
                
                # Messages
                "all_fields_required": "Semua field harus diisi",
                "invalid_email_format": "Format email tidak valid",
                "password_min_length": "Password minimal 6 karakter",
                "passwords_dont_match": "Password tidak cocok",
                "must_accept_terms": "Anda harus menyetujui syarat dan ketentuan",
                "email_already_registered": "Email sudah terdaftar",
                "registration_successful": "Registrasi berhasil! Silahkan login.",
                "registration_failed": "Gagal mendaftar. Silahkan coba lagi.",
                "email_and_password_required": "Email dan password harus diisi",
                "invalid_credentials": "Email atau password salah",
                "reset_link_sent": "Link reset password telah dikirim ke email Anda",
                "email_not_registered": "Email tidak terdaftar",
                "email_required": "Email harus diisi",
            }
        }
        
    def set_language(self, language_code):
        """Set current language"""
        if language_code in self.languages:
            self.current_language = language_code
            return True
        return False
        
    def get_text(self, key):
        """Get translated text for current language"""
        return self.languages.get(self.current_language, {}).get(key, key)
        
    def get_available_languages(self):
        """Get list of available languages"""
        return [
            {"code": "en", "name": "English"},
            {"code": "id", "name": "Bahasa Indonesia"}
        ]

# Global language manager instance
language_manager = LanguageManager()