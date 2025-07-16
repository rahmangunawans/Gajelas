"""
Logging utility for ATV application
"""
import logging
import os
from datetime import datetime

class ATVLogger:
    """ATV application logger configuration"""
    
    def __init__(self, name="ATV", level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Prevent duplicate handlers
        if not self.logger.handlers:
            self._setup_handlers()
    
    def _setup_handlers(self):
        """Setup logging handlers"""
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # File handler for errors
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        file_handler = logging.FileHandler(
            os.path.join(log_dir, f"atv_{datetime.now().strftime('%Y%m%d')}.log")
        )
        file_handler.setLevel(logging.DEBUG)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)
    
    def debug(self, message):
        """Debug level logging"""
        self.logger.debug(message)
    
    def info(self, message):
        """Info level logging"""
        self.logger.info(message)
    
    def warning(self, message):
        """Warning level logging"""
        self.logger.warning(message)
    
    def error(self, message):
        """Error level logging"""
        self.logger.error(message)
    
    def critical(self, message):
        """Critical level logging"""
        self.logger.critical(message)

# Global logger instance
logger = ATVLogger()