"""
Functions for retrieving configuration values.
"""

import os
import json
import logging
from pathlib import Path


def get_config(folder="/.cfo/", key=None):
    """
    Get configuration values from a JSON config file.
    
    Args:
        folder (str): Path to the folder containing the config file
        key (str): Key to retrieve from the config file
        
    Returns:
        Any: The configuration value for the specified key, or the entire config if no key is specified
    """
    try:
        # Expand user home directory if needed
        if folder.startswith("~"):
            folder = os.path.expanduser(folder)
        
        # Handle absolute paths that start with /
        if folder.startswith("/"):
            config_path = os.path.join(folder, "config.json")
        else:
            # Handle relative paths
            home_dir = str(Path.home())
            config_path = os.path.join(home_dir, folder, "config.json")
        
        # Check if config file exists
        if not os.path.exists(config_path):
            logging.error(f"Config file not found: {config_path}")
            return None
        
        # Read config file
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        # Return specific key or entire config
        if key:
            if key in config:
                return config[key]
            else:
                logging.error(f"Key '{key}' not found in config")
                return None
        return config
    except Exception as e:
        logging.error(f"Error reading config: {e}")
        return None
