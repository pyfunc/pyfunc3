"""
Functions for connecting to email servers.
"""

import imaplib
import logging


def connect(server, username, password):
    """
    Connect to an IMAP email server.
    
    Args:
        server (str): IMAP server address
        username (str): Email username
        password (str): Email password
        
    Returns:
        imaplib.IMAP4_SSL: IMAP connection object or None if connection fails
    """
    try:
        # Connect to the server
        mail = imaplib.IMAP4_SSL(server)
        
        # Login to the server
        mail.login(username, password)
        
        logging.info(f"Successfully connected to {server} as {username}")
        return mail
    except Exception as e:
        logging.error(f"Error connecting to email server: {e}")
        return None


def downloadAllAttachmentsInInbox(server, username, password, local_path, remote_folder):
    """
    Legacy function for backward compatibility.
    
    Args:
        server (str): IMAP server address
        username (str): Email username
        password (str): Email password
        local_path (str): Local path to save attachments
        remote_folder (str): Remote folder to download from
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        from .download_all_attachments_in_inbox import download_all_attachments_in_inbox
        return download_all_attachments_in_inbox(server, username, password, local_path, remote_folder)
    except Exception as e:
        logging.error(f"Error downloading attachments: {e}")
        return False
