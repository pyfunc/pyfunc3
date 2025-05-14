"""
Functions for downloading emails.
"""

import os
import email
import logging
import datetime
from email.header import decode_header
from .connect import connect


def download_emails(server, username, password, local_path, remote_folder, limit=50, month=0, year=0):
    """
    Download emails from a remote folder to a local path.
    
    Args:
        server (str): IMAP server address
        username (str): Email username
        password (str): Email password
        local_path (str): Local path to save emails
        remote_folder (str): Remote folder to download from
        limit (int): Maximum number of emails to download
        month (int): Month to filter emails (1-12, 0 for all)
        year (int): Year to filter emails (0 for all)
        
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
        
        # Limit the number of emails to download
        if limit > 0 and messages > limit:
            messages = limit
        
        # Download emails
        count = 0
        for i in range(messages, 0, -1):
            # Fetch the email
            status, msg_data = mail.fetch(str(i), '(RFC822)')
            if status != 'OK':
                logging.error(f"Error fetching message {i}: {msg_data}")
                continue
            
            # Parse the email
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)
            
            # Get email date
            date_str = msg.get('Date')
            if date_str:
                try:
                    # Parse the date
                    date_tuple = email.utils.parsedate_tz(date_str)
                    if date_tuple:
                        date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
                        
                        # Filter by month and year if specified
                        if month > 0 and date.month != month:
                            continue
                        if year > 0 and date.year != year:
                            continue
                except Exception as e:
                    logging.error(f"Error parsing date {date_str}: {e}")
            
            # Get email subject
            subject = msg.get('Subject')
            if subject:
                subject = decode_header(subject)[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode()
            else:
                subject = "No Subject"
            
            # Clean subject for filename
            subject = "".join(c if c.isalnum() or c in ' -_' else '_' for c in subject)
            subject = subject[:50]  # Limit subject length
            
            # Generate filename
            filename = f"{i}_{subject}.eml"
            filepath = os.path.join(local_path, filename)
            
            # Save email
            with open(filepath, 'wb') as f:
                f.write(raw_email)
            
            logging.info(f"Downloaded email: {filename}")
            count += 1
        
        logging.info(f"Downloaded {count} emails from {remote_folder}")
        mail.close()
        mail.logout()
        return True
    except Exception as e:
        logging.error(f"Error downloading emails: {e}")
        return False
