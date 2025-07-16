"""
Quickly create admin user for testing
"""
import os
from database.postgres_manager import PostgresManager

def create_admin():
    """Create admin user with simple password"""
    db = PostgresManager()
    
    # Initialize database first
    db.init_db()
    
    # Create admin user
    admin_data = {
        'email': 'admin@atv.com',
        'password': 'admin123',
        'full_name': 'Admin User',
        'is_admin': True,
        'vip_status': True
    }
    
    try:
        # Check if user already exists
        if db.user_exists('admin@atv.com'):
            print("Admin user already exists!")
            return
            
        # Create the user
        user_id = db.create_user(admin_data)
        if user_id:
            print(f"✓ Admin user created successfully with ID: {user_id}")
            print("Email: admin@atv.com")
            print("Password: admin123")
        else:
            print("❌ Failed to create admin user")
            
    except Exception as e:
        print(f"Error creating admin user: {e}")

if __name__ == "__main__":
    create_admin()