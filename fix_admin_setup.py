"""
Fix admin user creation with proper password hash
"""
from database.postgres_manager import PostgresManager

def fix_admin():
    """Create admin user with proper password hash"""
    db = PostgresManager()
    
    # Initialize database
    db.init_db()
    
    # Create admin user data
    admin_data = {
        'email': 'admin@atv.com',
        'password': 'admin123',  # This will be hashed by create_user method
        'full_name': 'Admin User',
        'phone': '+1234567890',
        'is_admin': True,
        'vip_status': True
    }
    
    try:
        # Delete existing admin if exists
        import psycopg2
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE email = 'admin@atv.com'")
        conn.commit()
        cursor.close()
        conn.close()
        
        # Create new admin user
        user_id = db.create_user(admin_data)
        if user_id:
            print(f"✓ Admin user created successfully with ID: {user_id}")
            
            # Test login immediately
            result = db.authenticate_user('admin@atv.com', 'admin123')
            if result:
                print("✓ Login test successful!")
                print(f"Admin email: {result['email']}")
                print(f"Admin name: {result['full_name']}")
                print(f"Is admin: {result['is_admin']}")
                print(f"VIP status: {result['vip_status']}")
            else:
                print("❌ Login test failed!")
        else:
            print("❌ Failed to create admin user")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fix_admin()