"""
Smart Translation System for ATV Application
Uses automatic translation with fallback to manual translations
"""

class SmartTranslator:
    """Intelligent translation system with auto-translation and manual fallbacks"""
    
    def __init__(self):
        self.current_language = "en"  # Default to English
        
        # Core manual translations for critical UI elements (kept for reliability)
        self.manual_translations = {
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
                "register_now": "REGISTER NOW",
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
                "search_broker_bot": "Search broker or bot...",
                "vip_premium": "VIP Premium",
                "regular": "Regular",
                "notifications": "Notifications",
                "account": "Account",
                "my_profile": "My Profile",
                "welcome": "Welcome",
                "choose_language": "Choose Language",
                "language_changed": "Language changed successfully",
                "current_language": "Current Language",
                "select_language": "Select Language",
                
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
                "dont_have_account": "Don't have an account?",
                "terms_conditions": "Terms and Conditions",
                "privacy_policy": "Privacy Policy",
                "i_agree_with": "I agree with",
                "and": "and",
                "cancel": "Cancel",
                "save": "Save",
                "edit": "Edit",
                "delete": "Delete",
                "confirm": "Confirm",
                "yes": "Yes",
                "no": "No",
                "loading": "Loading...",
                "success": "Success",
                "error": "Error",
                "warning": "Warning",
                "info": "Info",
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
                "register_now": "DAFTAR SEKARANG",
                "send_reset_link": "KIRIM LINK RESET",
                "back_to_login": "← Kembali ke Login",
                "exclusive_access": "Akses Eksklusif",
                "professional_trading_platform": "Platform Trading Profesional",
                "create_atv_account": "Buat Akun ATV - AUTOTRADEVIP",
                "enter_email_for_reset": "Masukkan email untuk reset password",
                
                # Dashboard
                "dashboard": "Dashboard",
                "trading_bots": "Bot Trading",
                "active_bots": "Bot Aktif",
                "history": "Riwayat",
                "profile": "Profil",
                "settings": "Pengaturan",
                "help_support": "Bantuan & Dukungan",
                "logout": "Keluar",
                "language": "Bahasa",
                "search_broker_bot": "Cari broker atau bot...",
                "vip_premium": "VIP Premium",
                "regular": "Reguler",
                "notifications": "Notifikasi",
                "account": "Akun",
                "my_profile": "Profil Saya",
                "welcome": "Selamat Datang",
                "choose_language": "Pilih Bahasa",
                "language_changed": "Bahasa berhasil diubah",
                "current_language": "Bahasa Saat Ini",
                "select_language": "Pilih Bahasa",
                
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
                "dont_have_account": "Belum punya akun?",
                "terms_conditions": "Syarat dan Ketentuan",
                "privacy_policy": "Kebijakan Privasi",
                "i_agree_with": "Saya setuju dengan",
                "and": "dan",
                "cancel": "Batal",
                "save": "Simpan",
                "edit": "Edit",
                "delete": "Hapus",
                "confirm": "Konfirmasi",
                "yes": "Ya",
                "no": "Tidak",
                "loading": "Memuat...",
                "success": "Berhasil",
                "error": "Error",
                "warning": "Peringatan",
                "info": "Info",
            }
        }
        
        # Auto-translation dictionary for common phrases
        self.auto_translations = {
            "zh": {
                "login": "登录", "register": "注册", "email": "邮箱", "password": "密码",
                "cancel": "取消", "save": "保存", "language": "语言", "profile": "个人资料",
                "dashboard": "仪表板", "logout": "退出", "settings": "设置",
                "select_language": "选择语言", "beranda": "首页", "active_bots": "活跃机器人",
                "history": "历史", "search_broker_bot": "搜索经纪商或机器人...",
                "vip_premium": "VIP 高级版", "regular": "普通版", "help_support": "帮助与支持"
            },
            "ja": {
                "login": "ログイン", "register": "登録", "email": "メール", "password": "パスワード",
                "cancel": "キャンセル", "save": "保存", "language": "言語", "profile": "プロフィール",
                "dashboard": "ダッシュボード", "logout": "ログアウト", "settings": "設定",
                "select_language": "言語を選択", "beranda": "ホーム", "active_bots": "アクティブボット",
                "history": "履歴", "search_broker_bot": "ブローカーまたはボットを検索...",
                "vip_premium": "VIPプレミアム", "regular": "レギュラー", "help_support": "ヘルプとサポート"
            },
            "ko": {
                "login": "로그인", "register": "등록", "email": "이메일", "password": "비밀번호",
                "cancel": "취소", "save": "저장", "language": "언어", "profile": "프로필",
                "dashboard": "대시보드", "logout": "로그아웃", "settings": "설정"
            },
            "es": {
                "login": "Iniciar sesión", "register": "Registrarse", "email": "Correo", 
                "password": "Contraseña", "cancel": "Cancelar", "save": "Guardar", 
                "language": "Idioma", "profile": "Perfil", "dashboard": "Panel", 
                "logout": "Cerrar sesión", "settings": "Configuración"
            },
            "fr": {
                "login": "Connexion", "register": "S'inscrire", "email": "Email", 
                "password": "Mot de passe", "cancel": "Annuler", "save": "Sauvegarder", 
                "language": "Langue", "profile": "Profil", "dashboard": "Tableau de bord", 
                "logout": "Déconnexion", "settings": "Paramètres"
            },
            "de": {
                "login": "Anmelden", "register": "Registrieren", "email": "E-Mail", 
                "password": "Passwort", "cancel": "Abbrechen", "save": "Speichern", 
                "language": "Sprache", "profile": "Profil", "dashboard": "Dashboard", 
                "logout": "Abmelden", "settings": "Einstellungen"
            },
            "ar": {
                "login": "تسجيل الدخول", "register": "التسجيل", "email": "البريد الإلكتروني", 
                "password": "كلمة المرور", "cancel": "إلغاء", "save": "حفظ", 
                "language": "اللغة", "profile": "الملف الشخصي", "dashboard": "لوحة التحكم", 
                "logout": "تسجيل الخروج", "settings": "الإعدادات"
            },
            "hi": {
                "login": "लॉगिन", "register": "रजिस्टर", "email": "ईमेल", 
                "password": "पासवर्ड", "cancel": "रद्द करें", "save": "सेव करें", 
                "language": "भाषा", "profile": "प्रोफाइल", "dashboard": "डैशबोर्ड", 
                "logout": "लॉगआउट", "settings": "सेटिंग्स"
            },
            "pt": {
                "login": "Entrar", "register": "Registrar", "email": "E-mail", 
                "password": "Senha", "cancel": "Cancelar", "save": "Salvar", 
                "language": "Idioma", "profile": "Perfil", "dashboard": "Painel", 
                "logout": "Sair", "settings": "Configurações"
            },
            "ru": {
                "login": "Войти", "register": "Регистрация", "email": "Эл. почта", 
                "password": "Пароль", "cancel": "Отмена", "save": "Сохранить", 
                "language": "Язык", "profile": "Профиль", "dashboard": "Панель", 
                "logout": "Выйти", "settings": "Настройки"
            },
            "th": {
                "login": "เข้าสู่ระบบ", "register": "สมัครสมาชิก", "email": "อีเมล", 
                "password": "รหัสผ่าน", "cancel": "ยกเลิก", "save": "บันทึก", 
                "language": "ภาษา", "profile": "โปรไฟล์", "dashboard": "แดชบอร์ด", 
                "logout": "ออกจากระบบ", "settings": "การตั้งค่า"
            },
            "vi": {
                "login": "Đăng nhập", "register": "Đăng ký", "email": "Email", 
                "password": "Mật khẩu", "cancel": "Hủy", "save": "Lưu", 
                "language": "Ngôn ngữ", "profile": "Hồ sơ", "dashboard": "Bảng điều khiển", 
                "logout": "Đăng xuất", "settings": "Cài đặt"
            }
        }
        
    def set_language(self, language_code):
        """Set current language"""
        if language_code in self.get_supported_languages():
            self.current_language = language_code
            return True
        return False
        
    def get_text(self, key):
        """Get translated text with smart fallback system"""
        # 1. Try manual translations first (most reliable)
        if self.current_language in self.manual_translations:
            if key in self.manual_translations[self.current_language]:
                return self.manual_translations[self.current_language][key]
        
        # 2. Try auto-translations
        if self.current_language in self.auto_translations:
            if key in self.auto_translations[self.current_language]:
                return self.auto_translations[self.current_language][key]
        
        # 3. Try English fallback
        if self.current_language != "en" and key in self.manual_translations.get("en", {}):
            return self.manual_translations["en"][key]
            
        # 4. Return key as-is if no translation found
        return key
        
    def get_supported_languages(self):
        """Get list of supported languages"""
        return [
            {"code": "en", "name": "English"},
            {"code": "id", "name": "Bahasa Indonesia"},
            {"code": "zh", "name": "中文 (Chinese)"},
            {"code": "ja", "name": "日本語 (Japanese)"},
            {"code": "ko", "name": "한국어 (Korean)"},
            {"code": "es", "name": "Español (Spanish)"},
            {"code": "fr", "name": "Français (French)"},
            {"code": "de", "name": "Deutsch (German)"},
            {"code": "ar", "name": "العربية (Arabic)"},
            {"code": "hi", "name": "हिन्दी (Hindi)"},
            {"code": "pt", "name": "Português (Portuguese)"},
            {"code": "ru", "name": "Русский (Russian)"},
            {"code": "th", "name": "ไทย (Thai)"},
            {"code": "vi", "name": "Tiếng Việt (Vietnamese)"}
        ]
        
    def add_translation(self, language_code, key, translation):
        """Add or update a translation"""
        if language_code not in self.auto_translations:
            self.auto_translations[language_code] = {}
        self.auto_translations[language_code][key] = translation

# Global translator instance
smart_translator = SmartTranslator()