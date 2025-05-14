"""
Functions for downloading email attachments.
"""

import os
import email
import logging
from email.header import decode_header
from .connect import connect


def download_all_attachments_in_inbox(server, username, password, local_path, remote_folder, limit=50):
    """
    Download all attachments from emails in a remote folder to a local path.
    
    Args:
        server (str): IMAP server address
        username (str): Email username
        password (str): Email password
        local_path (str): Local path to save attachments
        remote_folder (str): Remote folder to download from
        limit (int): Maximum number of emails to process
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Create local path if it doesn't exist
        if not os.path.exists(local_path):
            os.makedirs(local_path)
            logging.info(f"Created directory: {local_path}")
        
        # Connect to the server
        mail = connect(server, username, password)
        if not mail:
            return False
        
        # Select the remote folder
        status, messages = mail.select(remote_folder)
        if status != 'OK':
            logging.error(f"Error selecting folder {remote_folder}: {messages}")
            return False
        
        # Get the number of emails in the folder
        messages = int(messages[0])
        logging.info(f"Found {messages} messages in {remote_folder}")
        
        # Limit the number of emails to process
        if limit > 0 and messages > limit:
            messages = limit
        
        # Download attachments
        attachment_count = 0
        for i in range(messages, 0, -1):
            # Fetch the email
            status, msg_data = mail.fetch(str(i), '(RFC822)')
            if status != 'OK':
                logging.error(f"Error fetching message {i}: {msg_data}")
                continue
            
            # Parse the email
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)
            
            # Get email subject for logging
            subject = msg.get('Subject')
            if subject:
                subject = decode_header(subject)[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode()
            else:
                subject = "No Subject"
            
            # Process email parts
            for part in msg.walk():
                # Skip multipart messages
                if part.get_content_maintype() == 'multipart':
                    continue
                
                # Skip parts without filenames
                filename = part.get_filename()
                if not filename:
                    continue
                
                # Decode filename if needed
                filename_parts = decode_header(filename)
                if filename_parts[0][1] is not None:
                    filename = filename_parts[0][0].decode(filename_parts[0][1])
                elif isinstance(filename_parts[0][0], bytes):
                    filename = filename_parts[0][0].decode()
                else:
                    filename = filename_parts[0][0]
                
                # Clean filename
                filename = "".join(c if c.isalnum() or c in '.-_' else '_' for c in filename)
                
                # Save attachment
                filepath = os.path.join(local_path, filename)
                with open(filepath, 'wb') as f:
                    f.write(part.get_payload(decode=True))
                
                logging.info(f"Downloaded attachment: {filename} from email: {subject}")
                attachment_count += 1
        
        logging.info(f"Downloaded {attachment_count} attachments from {remote_folder}")
        mail.close()
        mail.logout()
        return True
    except Exception as e:
        logging.error(f"Error downloading attachments: {e}")
        return False
