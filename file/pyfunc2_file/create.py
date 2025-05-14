"""
Functions for creating directories and files.
"""

import os
import logging


def create_folder(path):
    """
    Create a directory if it doesn't exist.
    
    Args:
        path (str): Path to the directory to create
        
    Returns:
        bool: True if directory was created or already exists, False otherwise
    """
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            logging.info(f"Created directory: {path}")
        return True
    except Exception as e:
        logging.error(f"Error creating directory {path}: {e}")
        return False
