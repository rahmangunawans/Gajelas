#!/usr/bin/env python3
"""
Test login functionality
"""

import bcrypt
from database.postgres_manager import PostgresManager

def test_admin_login():
    db = PostgresManager()
    
    # Test credentials
    email = "admin@autotradevip.com"
    password = "AdminVIP123!"
    
    print("Testing admin login...")
    print(f"Email: {email}")
    print(f"Password: {password}")
    
    # Try to authenticate
    result = db.authenticate_user(email, password)
    
    if result:
        print("\n✓ Login successful!")
        print(f"User ID: {result['id']}")
        print(f"Name: {result['first_name']} {result['last_name']}")
        print(f"Admin: {result['is_admin']}")
        print(f"VIP Status: {result['vip_status']}")
        
        # Get trading accounts
        accounts = db.get_user_trading_accounts(result['id'])
        print(f"\nTrading Accounts ({len(accounts)}):")
        for account in accounts:
            print(f"- {account['broker_name']}: ${account['account_balance']}")
        
    else:
        print("\n✗ Login failed!")
        
        # Check if user exists
        if db.user_exists(email):
            print("User exists, password might be wrong")
        else:
            print("User does not exist")

if __name__ == "__main__":
    test_admin_login()