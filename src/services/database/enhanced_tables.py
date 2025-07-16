"""
Enhanced database tables for ATV trading application
"""
import sqlite3
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from utils.logger import logger

class EnhancedTables:
    def __init__(self, db_path="database.db"):
        self.db_path = db_path
    
    def get_connection(self):
        """Get database connection"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def create_enhanced_tables(self):
        """Create additional tables for comprehensive trading application"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            # Trading bots table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS trading_bots (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER REFERENCES users(id),
                    bot_name TEXT NOT NULL,
                    broker_name TEXT NOT NULL,
                    strategy_type TEXT NOT NULL,
                    is_active BOOLEAN DEFAULT FALSE,
                    profit_target REAL DEFAULT 0.0,
                    stop_loss REAL DEFAULT 0.0,
                    investment_amount REAL DEFAULT 0.0,
                    total_trades INTEGER DEFAULT 0,
                    winning_trades INTEGER DEFAULT 0,
                    total_profit REAL DEFAULT 0.0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Trading history table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS trading_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER REFERENCES users(id),
                    bot_id INTEGER REFERENCES trading_bots(id),
                    broker_name TEXT NOT NULL,
                    asset_pair TEXT NOT NULL,
                    trade_type TEXT NOT NULL, -- 'call' or 'put'
                    investment_amount REAL NOT NULL,
                    payout_amount REAL DEFAULT 0.0,
                    result TEXT, -- 'win', 'loss', 'pending'
                    entry_time TIMESTAMP,
                    expiry_time TIMESTAMP,
                    entry_price REAL,
                    exit_price REAL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # VIP subscriptions table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS vip_subscriptions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER REFERENCES users(id),
                    plan_type TEXT NOT NULL, -- 'basic', 'premium', 'ultimate'
                    start_date TIMESTAMP NOT NULL,
                    end_date TIMESTAMP NOT NULL,
                    is_active BOOLEAN DEFAULT TRUE,
                    payment_amount REAL NOT NULL,
                    payment_method TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Notifications table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS notifications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER REFERENCES users(id),
                    title TEXT NOT NULL,
                    message TEXT NOT NULL,
                    type TEXT DEFAULT 'info', -- 'info', 'success', 'warning', 'error'
                    is_read BOOLEAN DEFAULT FALSE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Settings table for user preferences
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_settings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER REFERENCES users(id),
                    setting_key TEXT NOT NULL,
                    setting_value TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(user_id, setting_key)
                )
            ''')
            
            # Audit logs table for admin
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS audit_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER REFERENCES users(id),
                    action TEXT NOT NULL,
                    table_name TEXT,
                    record_id INTEGER,
                    old_values TEXT, -- JSON format
                    new_values TEXT, -- JSON format
                    ip_address TEXT,
                    user_agent TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # System statistics table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS system_stats (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    stat_date DATE NOT NULL,
                    total_users INTEGER DEFAULT 0,
                    active_users INTEGER DEFAULT 0,
                    total_trades INTEGER DEFAULT 0,
                    total_profit REAL DEFAULT 0.0,
                    vip_users INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(stat_date)
                )
            ''')
            
            conn.commit()
            logger.info("Enhanced database tables created successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error creating enhanced tables: {e}")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
    
    def get_all_tables(self):
        """Get list of all tables in database"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
            tables = [row[0] for row in cursor.fetchall()]
            return tables
        except Exception as e:
            logger.error(f"Error getting tables: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    
    def get_table_info(self, table_name):
        """Get information about a specific table"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            
            cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
            row_count = cursor.fetchone()[0]
            
            return {
                'columns': [dict(col) for col in columns],
                'row_count': row_count
            }
        except Exception as e:
            logger.error(f"Error getting table info for {table_name}: {e}")
            return None
        finally:
            cursor.close()
            conn.close()