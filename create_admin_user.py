#!/usr/bin/env python3
"""
Script to create admin user for ATV mobile app
"""

import os
import sys
from database.postgres_manager import PostgresManager

def create_admin_user():
    """Create admin user with simple credentials"""
    try:
        # Initialize database manager
        db_manager = PostgresManager()
        db_manager.init_db()
        
        # Admin user data
        admin_data = {
            'email': 'admin@atv.com',
            'password': 'admin123',
            'full_name': 'Admin User',
            'phone': '+62123456789',
            'vip_status': True,
            'is_admin': True
        }
        
        # Check if admin already exists
        if db_manager.user_exists(admin_data['email']):
            print(f"Admin user {admin_data['email']} already exists!")
            
            # Update admin status to ensure it's admin
            with db_manager.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE users 
                    SET vip_status = %s, is_admin = %s 
                    WHERE email = %s
                """, (True, True, admin_data['email']))
                conn.commit()
                print("Admin status updated!")
        else:
            # Create new admin user
            try:
                user_id = db_manager.create_user(admin_data)
                if user_id:
                    print(f"✓ Admin user created successfully!")
                    print(f"✓ Email: {admin_data['email']}")
                    print(f"✓ Password: {admin_data['password']}")
                    print(f"✓ VIP Status: {admin_data['vip_status']}")
                    print(f"✓ Admin Status: {admin_data['is_admin']}")
                else:
                    print("✗ Failed to create admin user")
                    return False
            except Exception as e:
                print(f"✗ Error creating admin user: {e}")
                return False
        
        # Verify admin login
        print("\nVerifying admin login...")
        user_data = db_manager.authenticate_user(admin_data['email'], admin_data['password'])
        if user_data:
            print("✓ Admin login verification successful!")
            print(f"✓ User ID: {user_data['id']}")
            print(f"✓ Full Name: {user_data['full_name']}")
            print(f"✓ VIP Status: {user_data['vip_status']}")
            print(f"✓ Admin Status: {user_data['is_admin']}")
            return True
        else:
            print("✗ Admin login verification failed!")
            return False
            
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    print("Creating admin user for ATV mobile app...")
    success = create_admin_user()
    if success:
        print("\n🎉 Admin user setup completed successfully!")
        print("You can now login with: admin@atv.com / admin123")
    else:
        print("\n❌ Admin user setup failed!")
        sys.exit(1)