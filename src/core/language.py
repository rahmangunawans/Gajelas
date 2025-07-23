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
                "info": "Information",
                
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
                "register_now": "DAFTAR SEKARANG",
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
                "search_broker_bot": "Cari broker atau bot...",
                "vip_premium": "VIP Premium",
                "regular": "Regular",
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
                "info": "Informasi",
                
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
            },
            "zh": {
                # Auth pages
                "login": "登录",
                "register": "注册",
                "forgot_password": "忘记密码",
                "email": "邮箱",
                "password": "密码",
                "confirm_password": "确认密码",
                "username": "用户名",
                "enter_email": "请输入您的邮箱",
                "enter_password": "请输入您的密码",
                "enter_username": "请输入您的用户名",
                "remember_me": "记住我",
                "forgot_password_link": "忘记密码？",
                "login_now": "立即登录",
                "register_now": "立即注册",
                "send_reset_link": "发送重置链接",
                "back_to_login": "← 返回登录",
                "exclusive_access": "独家访问",
                "professional_trading_platform": "专业交易平台",
                "create_atv_account": "创建 ATV - AUTOTRADEVIP 账户",
                "enter_email_for_reset": "输入邮箱重置密码",
                
                # Dashboard
                "dashboard": "仪表板",
                "trading_bots": "交易机器人",
                "active_bots": "活跃机器人",
                "history": "历史",
                "profile": "个人资料",
                "settings": "设置",
                "help_support": "帮助与支持",
                "logout": "退出",
                "language": "语言",
                "search_broker_bot": "搜索经纪商或机器人...",
                "vip_premium": "VIP 高级版",
                "regular": "普通版",
                "notifications": "通知",
                "account": "账户",
                "my_profile": "我的个人资料",
                "welcome": "欢迎",
                "choose_language": "选择语言",
                "language_changed": "语言更改成功",
                "current_language": "当前语言",
                "select_language": "选择语言",
                
                # Brokers
                "beranda": "首页",
                "binomo": "Binomo",
                "quotex": "Quotex",
                "olymptrade": "Olymptrade",
                "iq_option": "IQ Option",
                "stockity": "Stockity",
                
                # Common
                "or": "或",
                "already_have_account": "已有账户？",
                "dont_have_account": "还没有账户？",
                "terms_conditions": "条款和条件",
                "privacy_policy": "隐私政策",
                "i_agree_with": "我同意",
                "and": "和",
                "cancel": "取消",
                "save": "保存",
                "edit": "编辑",
                "delete": "删除",
                "confirm": "确认",
                "yes": "是",
                "no": "否",
                "loading": "加载中...",
                "success": "成功",
                "error": "错误",
                "warning": "警告",
                "info": "信息",
                
                # Messages (keeping basic for now)
                "all_fields_required": "所有字段都是必需的",
                "invalid_email_format": "无效的邮箱格式",
                "password_min_length": "密码至少需要6个字符",
                "passwords_dont_match": "密码不匹配",
                "must_accept_terms": "您必须接受条款和条件",
                "email_already_registered": "邮箱已注册",
                "registration_successful": "注册成功！请登录。",
                "registration_failed": "注册失败。请重试。",
                "email_and_password_required": "邮箱和密码是必需的",
                "invalid_credentials": "无效的邮箱或密码",
                "reset_link_sent": "密码重置链接已发送到您的邮箱",
                "email_not_registered": "邮箱未注册",
                "email_required": "邮箱是必需的",
            },
            # Adding simplified entries for other languages (basic translations)
            "ja": {
                "login": "ログイン", "register": "登録", "email": "メール", "password": "パスワード",
                "language": "言語", "cancel": "キャンセル", "save": "保存", "profile": "プロフィール",
                "dashboard": "ダッシュボード", "logout": "ログアウト", "settings": "設定"
            },
            "ko": {
                "login": "로그인", "register": "등록", "email": "이메일", "password": "비밀번호",
                "language": "언어", "cancel": "취소", "save": "저장", "profile": "프로필",
                "dashboard": "대시보드", "logout": "로그아웃", "settings": "설정"
            },
            "es": {
                "login": "Iniciar sesión", "register": "Registrarse", "email": "Correo", "password": "Contraseña",
                "language": "Idioma", "cancel": "Cancelar", "save": "Guardar", "profile": "Perfil",
                "dashboard": "Panel", "logout": "Cerrar sesión", "settings": "Configuración"
            },
            "fr": {
                "login": "Connexion", "register": "S'inscrire", "email": "Email", "password": "Mot de passe",
                "language": "Langue", "cancel": "Annuler", "save": "Sauvegarder", "profile": "Profil",
                "dashboard": "Tableau de bord", "logout": "Déconnexion", "settings": "Paramètres"
            },
            "de": {
                "login": "Anmelden", "register": "Registrieren", "email": "E-Mail", "password": "Passwort",
                "language": "Sprache", "cancel": "Abbrechen", "save": "Speichern", "profile": "Profil",
                "dashboard": "Dashboard", "logout": "Abmelden", "settings": "Einstellungen"
            },
            "ar": {
                "login": "تسجيل الدخول", "register": "التسجيل", "email": "البريد الإلكتروني", "password": "كلمة المرور",
                "language": "اللغة", "cancel": "إلغاء", "save": "حفظ", "profile": "الملف الشخصي",
                "dashboard": "لوحة التحكم", "logout": "تسجيل الخروج", "settings": "الإعدادات"
            },
            "hi": {
                "login": "लॉगिन", "register": "रजिस्टर", "email": "ईमेल", "password": "पासवर्ड",
                "language": "भाषा", "cancel": "रद्द करें", "save": "सेव करें", "profile": "प्रोफाइल",
                "dashboard": "डैशबोर्ड", "logout": "लॉगआउट", "settings": "सेटिंग्स"
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
            {"code": "id", "name": "Bahasa Indonesia"},
            {"code": "zh", "name": "中文 (Chinese)"},
            {"code": "ja", "name": "日本語 (Japanese)"},
            {"code": "ko", "name": "한국어 (Korean)"},
            {"code": "es", "name": "Español (Spanish)"},
            {"code": "fr", "name": "Français (French)"},
            {"code": "de", "name": "Deutsch (German)"},
            {"code": "ar", "name": "العربية (Arabic)"},
            {"code": "hi", "name": "हिन्दी (Hindi)"}
        ]

# Global language manager instance
language_manager = LanguageManager()