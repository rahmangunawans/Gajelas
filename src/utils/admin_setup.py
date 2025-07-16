"""
Admin user setup utility
"""
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from services.database.postgres_manager import PostgresManager
from config.app_config import AppConfig

def create_admin_user():
    """Create admin user with default credentials"""
    db = PostgresManager()
    
    # Initialize database
    db.init_db()
    
    # Admin user data
    admin_data = {
        'email': AppConfig.DEFAULT_ADMIN_EMAIL,
        'password': AppConfig.DEFAULT_ADMIN_PASSWORD,
        'full_name': 'Admin User',
        'phone': '+1234567890',
        'is_admin': True,
        'vip_status': True
    }
    
    try:
        # Check if admin already exists
        if db.user_exists(admin_data['email']):
            print(f"Admin user {admin_data['email']} already exists!")
            return
            
        # Create admin user
        user_id = db.create_user(admin_data)
        if user_id:
            print(f"✓ Admin user created successfully")
            print(f"Email: {admin_data['email']}")
            print(f"Password: {admin_data['password']}")
            
            # Verify login
            result = db.authenticate_user(admin_data['email'], admin_data['password'])
            if result:
                print("✓ Admin login verification successful")
            else:
                print("❌ Admin login verification failed")
        else:
            print("❌ Failed to create admin user")
            
    except Exception as e:
        print(f"Error creating admin user: {e}")

if __name__ == "__main__":
    create_admin_user()