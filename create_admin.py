#!/usr/bin/env python3
"""
Script untuk membuat akun admin dengan status VIP
"""

import bcrypt
import psycopg2
import os
from datetime import datetime

def hash_password(password):
    """Hash password menggunakan bcrypt"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def create_admin_account():
    """Membuat akun admin dengan status VIP"""
    
    # Koneksi ke database
    conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
    cur = conn.cursor()
    
    # Data admin
    admin_email = "admin@autotradevip.com"
    admin_password = "AdminVIP123!"
    admin_first_name = "Admin"
    admin_last_name = "ATV"
    
    # Hash password
    hashed_password = hash_password(admin_password)
    
    try:
        # Cek apakah admin sudah ada
        cur.execute("SELECT id FROM users WHERE email = %s", (admin_email,))
        existing_admin = cur.fetchone()
        
        if existing_admin:
            print(f"Admin dengan email {admin_email} sudah ada.")
            print("Mengupdate status VIP...")
            
            # Update status VIP
            cur.execute("""
                UPDATE users 
                SET vip_status = 'premium', 
                    is_admin = TRUE,
                    updated_at = %s
                WHERE email = %s
            """, (datetime.now(), admin_email))
            
            admin_id = existing_admin[0]
            
        else:
            # Buat akun admin baru
            cur.execute("""
                INSERT INTO users (email, password_hash, first_name, last_name, is_admin, vip_status, created_at, updated_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (
                admin_email,
                hashed_password,
                admin_first_name,
                admin_last_name,
                True,  # is_admin
                'premium',  # vip_status
                datetime.now(),
                datetime.now()
            ))
            
            admin_id = cur.fetchone()[0]
            print(f"Akun admin berhasil dibuat dengan ID: {admin_id}")
        
        # Buat trading accounts untuk semua broker
        brokers = ['Binomo', 'Quotex', 'Olymptrade', 'IQ Option', 'Stockity']
        
        for broker in brokers:
            # Cek apakah trading account sudah ada
            cur.execute("""
                SELECT id FROM trading_accounts 
                WHERE user_id = %s AND broker_name = %s
            """, (admin_id, broker))
            
            existing_account = cur.fetchone()
            
            if not existing_account:
                # Buat trading account baru
                cur.execute("""
                    INSERT INTO trading_accounts (user_id, broker_name, account_balance, is_active, created_at)
                    VALUES (%s, %s, %s, %s, %s)
                """, (admin_id, broker, 10000.0, True, datetime.now()))
                
                print(f"Trading account untuk {broker} berhasil dibuat dengan saldo $10,000")
        
        # Commit perubahan
        conn.commit()
        
        print("\n" + "="*50)
        print("AKUN ADMIN BERHASIL DIBUAT!")
        print("="*50)
        print(f"Email: {admin_email}")
        print(f"Password: {admin_password}")
        print(f"Status: VIP Premium")
        print(f"Admin: Ya")
        print(f"Trading Accounts: {len(brokers)} broker")
        print("="*50)
        
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    create_admin_account()