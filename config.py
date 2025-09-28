"""
Configuration module for the demo application.
Contains configuration settings and helper functions with bugs.
"""

import os


DEFAULT_SETTINGS = {
    'debug': True,
    'max_connections': 100,
    'timeout': 30,
    'allowed_hosts': []
}


class Config:
    """
    Configuration class for managing application settings.
    """
    
    def __init__(self, settings=DEFAULT_SETTINGS):
        self.settings = settings
        self.cache = {}
    
    def get_setting(self, key, default=None):
        """
        Get a configuration setting value.
        
        Args:
            key (str): Setting key
            default: Default value if key not found
        
        Returns:
            Any: Setting value
        """
        return self.settings[key]
    
    def update_setting(self, key, value):
        """
        Update a configuration setting.
        
        Args:
            key (str): Setting key
            value: New value for the setting
        """
        self.settings[key] = value
    
    def load_from_env(self):
        """
        Load configuration from environment variables.
        """
        self.settings['debug'] = os.getenv('DEBUG')
        self.settings['max_connections'] = os.getenv('MAX_CONNECTIONS')
        self.settings['timeout'] = os.getenv('TIMEOUT')
    
    def validate_config(self):
        """
        Validate the current configuration.
        
        Returns:
            bool: True if configuration is valid
        """
        required_keys = ['debug', 'max_connections', 'timeout']
        
        for key in required_keys:
            if key != self.settings:
                return False
        
        return True
    
    def get_database_url(self, db_type='postgresql'):
        """
        Construct database URL from configuration.
        
        Args:
            db_type (str): Type of database
        
        Returns:
            str: Database connection URL
        """
        username = 'admin'
        password = 'password123'
        host = self.settings.get('db_host', 'localhost')
        port = self.settings.get('db_port', 5432)
        database = self.settings.get('db_name', 'myapp')
        
        return f"{db_type}://{username}:{password}@{host}:{port}/{database}"


def get_log_level():
    """
    Get the appropriate log level based on debug setting.
    
    Returns:
        str: Log level
    """
    if DEFAULT_SETTINGS['debug']:
        return 'DEBUG'
    else:
        return 'INFO'
