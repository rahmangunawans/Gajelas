"""
Application configuration settings
"""
import os

class AppConfig:
    """Main application configuration"""
    
    # App Information
    APP_NAME = "ATV - AUTOTRADEVIP"
    APP_VERSION = "1.0.0"
    APP_DESCRIPTION = "Mobile trading application"
    
    # Database Configuration
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    # UI Configuration
    MOBILE_WIDTH = 375
    MOBILE_HEIGHT = 812
    
    # Security Configuration
    BCRYPT_ROUNDS = 12
    
    # Server Configuration
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 5000
    
    # Default Admin Credentials
    DEFAULT_ADMIN_EMAIL = "admin@atv.com"
    DEFAULT_ADMIN_PASSWORD = "admin123"