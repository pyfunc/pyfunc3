"""
Functions for checking and creating paths.
"""

import os
import logging


def check_and_create_path(path):
    """
    Check if a path exists and create it if it doesn't.
    
    Args:
        path (str): Path to check and create
        
    Returns:
        bool: True if path exists or was created, False otherwise
    """
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            logging.info(f"Created path: {path}")
        return True
    except Exception as e:
        logging.error(f"Error creating path {path}: {e}")
        return False
