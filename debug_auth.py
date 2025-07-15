#!/usr/bin/env python3
"""
Debug authentication system
"""

import bcrypt
from database.postgres_manager import PostgresManager

def debug_authentication():
    """Debug authentication with exact credentials"""
    
    db = PostgresManager()
    
    # Test credentials from screenshot
    email = "admin@atv.com"
    password = "admin123"
    
    print(f"Testing authentication:")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print()
    
    # Test authentication
    result = db.authenticate_user(email, password)
    
    if result:
        print("✓ Authentication successful!")
        print(f"User data: {result}")
        
        # Get trading accounts
        accounts = db.get_user_trading_accounts(result['id'])
        print(f"Trading accounts: {len(accounts)}")
        for account in accounts:
            print(f"  - {account['broker_name']}: ${account['account_balance']}")
    else:
        print("✗ Authentication failed!")
        
        # Debug: Check if user exists
        if db.user_exists(email):
            print("User exists in database")
            
            # Get stored hash for comparison
            import psycopg2
            import os
            
            conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
            cur = conn.cursor()
            cur.execute("SELECT password_hash FROM users WHERE email = %s", (email,))
            stored_hash = cur.fetchone()[0]
            
            print(f"Stored hash: {stored_hash}")
            
            # Test password verification
            if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
                print("✓ Password verification successful (manual test)")
            else:
                print("✗ Password verification failed (manual test)")
                
            cur.close()
            conn.close()
        else:
            print("User does not exist in database")

if __name__ == "__main__":
    debug_authentication()