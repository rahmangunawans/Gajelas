#!/usr/bin/env python3
"""
Fix admin login by updating password hash
"""

import bcrypt
import psycopg2
import os
from datetime import datetime

def fix_admin_password():
    """Update admin password with correct hash"""
    
    # Connect to database
    conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
    cur = conn.cursor()
    
    # New password
    new_password = "AdminVIP123!"
    
    # Hash password correctly
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), salt).decode('utf-8')
    
    try:
        # Update admin password
        cur.execute("""
            UPDATE users 
            SET password_hash = %s, updated_at = %s
            WHERE email = %s
        """, (hashed_password, datetime.now(), 'admin@autotradevip.com'))
        
        conn.commit()
        
        # Test the new password
        cur.execute("SELECT password_hash FROM users WHERE email = %s", ('admin@autotradevip.com',))
        stored_hash = cur.fetchone()[0]
        
        # Verify password works
        if bcrypt.checkpw(new_password.encode('utf-8'), stored_hash.encode('utf-8')):
            print("✓ Password updated and verified successfully!")
            print(f"Email: admin@autotradevip.com")
            print(f"Password: {new_password}")
        else:
            print("✗ Password verification failed")
            
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    fix_admin_password()