#!/usr/bin/env python3
"""
Create simple admin account with easy password
"""

import bcrypt
import psycopg2
import os
from datetime import datetime

def create_simple_admin():
    """Create admin account with simple password"""
    
    # Connect to database
    conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
    cur = conn.cursor()
    
    # Admin credentials
    admin_email = "admin@atv.com"
    admin_password = "admin123"
    
    # Hash password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(admin_password.encode('utf-8'), salt).decode('utf-8')
    
    try:
        # Delete existing admin if exists
        cur.execute("DELETE FROM users WHERE email = %s", (admin_email,))
        
        # Create new admin
        cur.execute("""
            INSERT INTO users (email, password_hash, first_name, last_name, is_admin, vip_status, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """, (
            admin_email,
            hashed_password,
            'Admin',
            'ATV',
            True,
            'premium',
            datetime.now(),
            datetime.now()
        ))
        
        admin_id = cur.fetchone()[0]
        
        # Create trading accounts
        brokers = ['Binomo', 'Quotex', 'Olymptrade', 'IQ Option', 'Stockity']
        
        for broker in brokers:
            cur.execute("""
                INSERT INTO trading_accounts (user_id, broker_name, account_balance, is_active, created_at)
                VALUES (%s, %s, %s, %s, %s)
            """, (admin_id, broker, 50000.0, True, datetime.now()))
        
        conn.commit()
        
        # Test login
        cur.execute("SELECT password_hash FROM users WHERE email = %s", (admin_email,))
        stored_hash = cur.fetchone()[0]
        
        if bcrypt.checkpw(admin_password.encode('utf-8'), stored_hash.encode('utf-8')):
            print("✓ Admin account created and tested successfully!")
            print(f"Email: {admin_email}")
            print(f"Password: {admin_password}")
            print(f"Status: VIP Premium Admin")
        else:
            print("✗ Password test failed")
            
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    create_simple_admin()