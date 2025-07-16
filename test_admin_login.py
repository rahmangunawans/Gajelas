"""
Test admin login functionality
"""
from database.postgres_manager import PostgresManager

def test_login():
    """Test admin login"""
    db = PostgresManager()
    
    # Test authentication
    result = db.authenticate_user('admin@atv.com', 'admin123')
    
    if result:
        print("✓ Admin login successful!")
        print(f"User ID: {result['id']}")
        print(f"Email: {result['email']}")
        print(f"Full Name: {result['full_name']}")
        print(f"Is Admin: {result['is_admin']}")
        print(f"VIP Status: {result['vip_status']}")
    else:
        print("❌ Admin login failed!")
        
        # Check password hash
        import psycopg2
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM users WHERE email = 'admin@atv.com'")
        result = cursor.fetchone()
        if result:
            print(f"Password hash in database: {result[0]}")
            
            # Test password verification
            is_valid = db.verify_password('admin123', result[0])
            print(f"Password verification result: {is_valid}")
        cursor.close()
        conn.close()

if __name__ == "__main__":
    test_login()