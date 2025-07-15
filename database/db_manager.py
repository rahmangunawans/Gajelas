import sqlite3
import os
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path="atv_database.db"):
        self.db_path = db_path
        
    def init_db(self):
        """Initialize database and create tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create user_sessions table for session management
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                session_token TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                expires_at TIMESTAMP NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Create trading_accounts table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS trading_accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                broker_name TEXT NOT NULL,
                account_balance REAL DEFAULT 0.0,
                is_active BOOLEAN DEFAULT TRUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        conn.commit()
        conn.close()
        
    def create_user(self, user_data):
        """Create a new user"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO users (username, email, password)
                VALUES (?, ?, ?)
            ''', (user_data['username'], user_data['email'], user_data['password']))
            
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError:
            return False
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
            
    def authenticate_user(self, email, password):
        """Authenticate user login"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, username, email, created_at
                FROM users
                WHERE email = ? AND password = ?
            ''', (email, password))
            
            user = cursor.fetchone()
            conn.close()
            
            if user:
                return {
                    'id': user[0],
                    'username': user[1],
                    'email': user[2],
                    'created_at': user[3]
                }
            return None
        except Exception as e:
            print(f"Error authenticating user: {e}")
            return None
            
    def user_exists(self, email):
        """Check if user exists by email"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('SELECT id FROM users WHERE email = ?', (email,))
            user = cursor.fetchone()
            conn.close()
            
            return user is not None
        except Exception as e:
            print(f"Error checking user existence: {e}")
            return False
            
    def get_user_by_id(self, user_id):
        """Get user by ID"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, username, email, created_at
                FROM users
                WHERE id = ?
            ''', (user_id,))
            
            user = cursor.fetchone()
            conn.close()
            
            if user:
                return {
                    'id': user[0],
                    'username': user[1],
                    'email': user[2],
                    'created_at': user[3]
                }
            return None
        except Exception as e:
            print(f"Error getting user by ID: {e}")
            return None
            
    def update_user_password(self, email, new_password):
        """Update user password"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE users
                SET password = ?, updated_at = CURRENT_TIMESTAMP
                WHERE email = ?
            ''', (new_password, email))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error updating password: {e}")
            return False
            
    def create_trading_account(self, user_id, broker_name, account_balance=0.0):
        """Create a new trading account for user"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO trading_accounts (user_id, broker_name, account_balance)
                VALUES (?, ?, ?)
            ''', (user_id, broker_name, account_balance))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error creating trading account: {e}")
            return False
            
    def get_user_trading_accounts(self, user_id):
        """Get all trading accounts for a user"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, broker_name, account_balance, is_active, created_at
                FROM trading_accounts
                WHERE user_id = ? AND is_active = TRUE
            ''', (user_id,))
            
            accounts = cursor.fetchall()
            conn.close()
            
            return [
                {
                    'id': account[0],
                    'broker_name': account[1],
                    'account_balance': account[2],
                    'is_active': account[3],
                    'created_at': account[4]
                }
                for account in accounts
            ]
        except Exception as e:
            print(f"Error getting trading accounts: {e}")
            return []