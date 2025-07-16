import psycopg2
import bcrypt
import os
import sys
from datetime import datetime
from psycopg2.extras import RealDictCursor

# Add utils to path for logger
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
try:
    from utils.logger import logger
except ImportError:
    # Fallback if logger not available
    import logging
    logger = logging.getLogger(__name__)

class PostgresManager:
    def __init__(self, db_url=None):
        self.db_url = db_url or os.environ.get('DATABASE_URL')
        
    def get_connection(self):
        """Get database connection"""
        return psycopg2.connect(self.db_url)
        
    def init_db(self):
        """Initialize database and create tables"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            # Create users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL,
                    first_name VARCHAR(100),
                    last_name VARCHAR(100),
                    full_name VARCHAR(200),
                    phone VARCHAR(20),
                    is_admin BOOLEAN DEFAULT FALSE,
                    vip_status BOOLEAN DEFAULT FALSE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create trading_accounts table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS trading_accounts (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(id),
                    broker_name VARCHAR(100) NOT NULL,
                    account_balance DECIMAL(15,2) DEFAULT 0.0,
                    is_active BOOLEAN DEFAULT TRUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.commit()
            logger.info("Database initialized successfully")
            
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
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        try:
            cursor.execute("""
                SELECT id, email, password_hash, first_name, last_name, full_name, phone, is_admin, vip_status
                FROM users 
                WHERE email = %s
            """, (email,))
            
            user = cursor.fetchone()
            
            if user and self.verify_password(password, user['password_hash']):
                return {
                    'id': user['id'],
                    'email': user['email'],
                    'first_name': user['first_name'],
                    'last_name': user['last_name'],
                    'full_name': user['full_name'],
                    'phone': user['phone'],
                    'is_admin': user['is_admin'],
                    'vip_status': user['vip_status']
                }
            
            return None
            
        except Exception as e:
            logger.error(f"Error authenticating user: {e}")
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
            
            cursor.execute("""
                INSERT INTO users (email, password_hash, first_name, last_name, full_name, phone, is_admin, vip_status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (
                user_data['email'],
                hashed_password,
                user_data.get('first_name', ''),
                user_data.get('last_name', ''),
                user_data.get('full_name', ''),
                user_data.get('phone', ''),
                user_data.get('is_admin', False),
                user_data.get('vip_status', False)
            ))
            
            user_id = cursor.fetchone()[0]
            conn.commit()
            
            # Create default trading accounts for new user
            brokers = ['Binomo', 'Quotex', 'Olymptrade', 'IQ Option', 'Stockity']
            for broker in brokers:
                cursor.execute("""
                    INSERT INTO trading_accounts (user_id, broker_name, account_balance, is_active)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, broker, 1000.0, True))
            
            conn.commit()
            return user_id
            
        except Exception as e:
            print(f"Error creating user: {e}")
            conn.rollback()
            return None
        finally:
            cursor.close()
            conn.close()
    
    def get_user_by_id(self, user_id):
        """Get user by ID"""
        conn = self.get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        try:
            cursor.execute("""
                SELECT id, email, first_name, last_name, is_admin, vip_status
                FROM users 
                WHERE id = %s
            """, (user_id,))
            
            user = cursor.fetchone()
            return dict(user) if user else None
            
        except Exception as e:
            print(f"Error getting user: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
    
    def get_user_trading_accounts(self, user_id):
        """Get all trading accounts for a user"""
        conn = self.get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        try:
            cursor.execute("""
                SELECT id, broker_name, account_balance, is_active
                FROM trading_accounts 
                WHERE user_id = %s
                ORDER BY broker_name
            """, (user_id,))
            
            accounts = cursor.fetchall()
            return [dict(account) for account in accounts]
            
        except Exception as e:
            print(f"Error getting trading accounts: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    
    def update_user_vip_status(self, user_id, vip_status):
        """Update user VIP status"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                UPDATE users 
                SET vip_status = %s, updated_at = %s
                WHERE id = %s
            """, (vip_status, datetime.now(), user_id))
            
            conn.commit()
            return True
            
        except Exception as e:
            print(f"Error updating VIP status: {e}")
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
            cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
            return cursor.fetchone() is not None
            
        except Exception as e:
            print(f"Error checking user existence: {e}")
            return False
        finally:
            cursor.close()
            conn.close()