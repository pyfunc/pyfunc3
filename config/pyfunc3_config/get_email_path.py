"""
Functions for retrieving email paths.
"""

import os
import logging


def get_email_path(email_target, storage_root):
    """
    Get the path for storing email data.
    
    Args:
        email_target (str): Target identifier for the email
        storage_root (str): Root storage directory
        
    Returns:
        str: Path for storing email data
    """
    try:
        # Ensure storage root exists
        if not os.path.exists(storage_root):
            os.makedirs(storage_root)
            logging.info(f"Created storage root directory: {storage_root}")
        
        # Create and return the email path
        email_path = os.path.join(storage_root, email_target)
        return email_path
    except Exception as e:
        logging.error(f"Error creating email path: {e}")
        return None
