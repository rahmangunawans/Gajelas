import sqlite3
import bcrypt
import os
import sys
from datetime import datetime

# Add utils to path for logger
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
try:
    from utils.logger import logger
except ImportError:
    # Fallback if logger not available
    import logging
    logger = logging.getLogger(__name__)

class SQLiteManager:
    def __init__(self, db_path=None):
        self.db_path = db_path or "database.db"
        
    def get_connection(self):
        """Get database connection"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Enable column access by name
        return conn
        
    def init_db(self):
        """Initialize database and create tables"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            # Create users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    first_name TEXT,
                    last_name TEXT,
                    full_name TEXT,
                    phone TEXT,
                    is_admin BOOLEAN DEFAULT FALSE,
                    vip_status BOOLEAN DEFAULT FALSE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create trading_accounts table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS trading_accounts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER REFERENCES users(id),
                    broker_name TEXT NOT NULL,
                    account_balance REAL DEFAULT 0.0,
                    is_active BOOLEAN DEFAULT TRUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.commit()
            logger.info("SQLite database initialized successfully")
            
        except Exception as e:
            logger.error(f"Error initializing database: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
    
    def hash_password(self, password):
        """Hash password using bcrypt"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
    def verify_password(self, password, hashed_password):
        """Verify password against hash"""
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    
    def authenticate_user(self, email, password):
        """Authenticate user login"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "SELECT id, email, password_hash, full_name, phone, is_admin, vip_status FROM users WHERE email = ?",
                (email,)
            )
            user = cursor.fetchone()
            
            if user and self.verify_password(password, user['password_hash']):
                logger.info(f"User authenticated successfully: {email}")
                return {
                    'id': user['id'],
                    'email': user['email'],
                    'full_name': user['full_name'],
                    'phone': user['phone'],
                    'is_admin': user['is_admin'],
                    'vip_status': user['vip_status']
                }
            else:
                logger.warning(f"Authentication failed for user: {email}")
                return None
                
        except Exception as e:
            logger.error(f"Error during authentication: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
    
    def create_user(self, user_data):
        """Create a new user"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            hashed_password = self.hash_password(user_data['password'])
            
            cursor.execute('''
                INSERT INTO users (email, password_hash, first_name, last_name, full_name, phone, is_admin, vip_status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                user_data['email'],
                hashed_password,
                user_data.get('first_name'),
                user_data.get('last_name'),
                user_data.get('full_name'),
                user_data.get('phone'),
                user_data.get('is_admin', False),
                user_data.get('vip_status', False)
            ))
            
            user_id = cursor.lastrowid
            conn.commit()
            logger.info(f"User created successfully: {user_data['email']}")
            return user_id
            
        except sqlite3.IntegrityError:
            logger.warning(f"User already exists: {user_data['email']}")
            return None
        except Exception as e:
            logger.error(f"Error creating user: {e}")
            conn.rollback()
            return None
        finally:
            cursor.close()
            conn.close()
    
    def get_user_by_id(self, user_id):
        """Get user by ID"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "SELECT id, email, full_name, phone, is_admin, vip_status FROM users WHERE id = ?",
                (user_id,)
            )
            user = cursor.fetchone()
            
            if user:
                return {
                    'id': user['id'],
                    'email': user['email'],
                    'full_name': user['full_name'],
                    'phone': user['phone'],
                    'is_admin': user['is_admin'],
                    'vip_status': user['vip_status']
                }
            return None
            
        except Exception as e:
            logger.error(f"Error getting user by ID: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
    
    def get_user_trading_accounts(self, user_id):
        """Get all trading accounts for a user"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "SELECT * FROM trading_accounts WHERE user_id = ?",
                (user_id,)
            )
            accounts = cursor.fetchall()
            
            return [dict(account) for account in accounts]
            
        except Exception as e:
            logger.error(f"Error getting trading accounts: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    
    def update_user_vip_status(self, user_id, vip_status):
        """Update user VIP status"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "UPDATE users SET vip_status = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
                (vip_status, user_id)
            )
            conn.commit()
            logger.info(f"VIP status updated for user {user_id}: {vip_status}")
            return True
            
        except Exception as e:
            logger.error(f"Error updating VIP status: {e}")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
    
    def user_exists(self, email):
        """Check if user exists by email"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
            return cursor.fetchone() is not None
            
        except Exception as e:
            logger.error(f"Error checking if user exists: {e}")
            return False
        finally:
            cursor.close()
            conn.close()