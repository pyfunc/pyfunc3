"""
Functions for downloading emails.
"""

import os
import email
import logging
import time
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
    start_time = datetime.datetime.now()
    logging.info(f"{'='*50}")
    logging.info(f"Starting email download process at {start_time}")
    logging.info(f"Server: {server}, Folder: {remote_folder}, User: {username}")
    logging.info(f"Local path: {local_path}, Limit: {limit}, Month: {month}, Year: {year}")
    
    try:
        # Create local path if it doesn't exist
        if not os.path.exists(local_path):
            logging.info(f"Creating directory: {local_path}")
            os.makedirs(local_path, exist_ok=True)
            logging.info(f"Successfully created directory: {local_path}")
        else:
            logging.info(f"Using existing directory: {local_path}")
        
        # Connect to the server
        logging.info(f"Connecting to {server} as {username}...")
        mail = connect(server, username, password)
        if not mail:
            logging.error("Failed to connect to the mail server")
            return False
        logging.info("Successfully connected to the mail server")
        
        try:
            # Select the remote folder
            logging.info(f"Selecting folder: {remote_folder}")
            status, messages = mail.select(remote_folder)
            if status != 'OK':
                logging.error(f"Error selecting folder {remote_folder}: {messages}")
                return False
            
            # Get the number of emails in the folder
            messages = int(messages[0])
            logging.info(f"Found {messages} messages in {remote_folder}")
            
            # Limit the number of emails to download
            if limit > 0 and messages > limit:
                logging.info(f"Limiting download to {limit} most recent messages")
                messages = limit
            
            # Download emails
            count = 0
            skipped = 0
            processed = 0
            last_log_time = time.time()
            log_interval = 30  # Log progress every 30 seconds
            processed_since_last_log = 0
            
            logging.info(f"Starting to process {messages} messages...")
            logging.info("-" * 80)
            logging.info("PROGRESS:  0% |" + " " * 50 + "| 0/{messages} (0 skipped)")
            start_time = time.time()
            
            for i in range(messages, 0, -1):
                current_time = time.time()
                processed += 1
                processed_since_last_log += 1
                
                # Log progress every N messages or every N seconds
                if processed % 100 == 0 or (current_time - last_log_time) >= log_interval:
                    progress = (processed / messages) * 100
                    progress_bar = "=" * int(progress // 2) + ">" + " " * (50 - int(progress // 2) - 1)
                    elapsed = current_time - start_time
                    msgs_per_sec = processed_since_last_log / (current_time - last_log_time) if (current_time - last_log_time) > 0 else 0
                    
                    logging.info(
                        f"PROGRESS: {progress:3.0f}% |{progress_bar}| "
                        f"{processed}/{messages} ({skipped} skipped) | "
                        f"{msgs_per_sec:.1f} msg/s | "
                        f"Elapsed: {elapsed//60:.0f}m {elapsed%60:.0f}s"
                    )
                    last_log_time = current_time
                    processed_since_last_log = 0
                
                msg_info = f"[{processed}/{messages}] Message {i}"
                
                try:
                    # Fetch the email
                    logging.debug(f"{msg_info} - Fetching...")
                    status, msg_data = mail.fetch(str(i), '(RFC822)')
                    if status != 'OK':
                        logging.error(f"{msg_info} - Error fetching: {msg_data}")
                        skipped += 1
                        continue
                    
                    # Parse the email
                    raw_email = msg_data[0][1]
                    msg = email.message_from_bytes(raw_email)
                    
                    # Get email date
                    date_str = msg.get('Date', 'No Date')
                    logging.debug(f"{msg_info} - Date: {date_str}")
                    
                    if date_str != 'No Date':
                        try:
                            # Parse the date
                            date_tuple = email.utils.parsedate_tz(date_str)
                            if date_tuple:
                                date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
                                logging.debug(f"{msg_info} - Parsed date: {date}")
                                
                                # Filter by month and year if specified
                                if month > 0 and date.month != month:
                                    logging.debug(f"{msg_info} - Skipping (wrong month: {date.month} != {month})")
                                    skipped += 1
                                    continue
                                if year > 0 and date.year != year:
                                    logging.debug(f"{msg_info} - Skipping (wrong year: {date.year} != {year})")
                                    skipped += 1
                                    continue
                        except Exception as e:
                            logging.error(f"{msg_info} - Error parsing date {date_str}: {e}", exc_info=True)
                    
                    # Get email subject and from
                    subject = msg.get('Subject', 'No Subject')
                    from_ = msg.get('From', 'Unknown Sender')
                    logging.debug(f"{msg_info} - From: {from_}")
                    
                    if subject:
                        subject = decode_header(subject)[0][0]
                        if isinstance(subject, bytes):
                            try:
                                subject = subject.decode('utf-8', errors='replace')
                            except Exception as e:
                                logging.error(f"{msg_info} - Error decoding subject: {e}")
                                subject = 'Decode_Error'
                    
                    # Clean subject for filename
                    clean_subject = "".join(c if c.isalnum() or c in ' -_' else '_' for c in subject)
                    clean_subject = clean_subject[:50]  # Limit subject length
                    
                    # Generate filename with date and subject
                    if date_str != 'No Date' and 'date' in locals():
                        date_prefix = date.strftime('%Y%m%d_%H%M%S_')
                    else:
                        date_prefix = ''
                        
                    filename = f"{date_prefix}{i:04d}_{clean_subject}.eml"
                    filepath = os.path.join(local_path, filename)
                    
                    # Log message info
                    msg_log = (
                        f"{msg_info} - Subject: {subject[:100]}{'...' if len(subject) > 100 else ''} | "
                        f"From: {from_[:50]}{'...' if len(from_) > 50 else ''} | "
                        f"Date: {date_str}"
                    )
                    logging.info(msg_log)
                    
                    # Save the email
                    try:
                        with open(filepath, 'wb') as f:
                            f.write(raw_email)
                        count += 1
                        logging.debug(f"{msg_info} - Saved to: {filepath}")
                    except Exception as e:
                        logging.error(f"{msg_info} - Error saving email: {e}", exc_info=True)
                        skipped += 1
                        continue
                        
                except Exception as e:
                    logging.error(f"{msg_info} - Error processing message: {e}", exc_info=True)
                    skipped += 1
                    continue
            
            # Log summary
            duration = time.time() - start_time
            hours, rem = divmod(duration, 3600)
            minutes, seconds = divmod(rem, 60)
            
            summary = (
                f"\n{'='*80}\n"
                f"DOWNLOAD SUMMARY\n"
                f"{'='*80}\n"
                f"{'Account:':<20} {username}\n"
                f"{'Folder:':<20} {remote_folder}\n"
                f"{'Time period:':<20} {month or 'All'}/{year or 'All'}\n"
                f"{'Local path:':<20} {os.path.abspath(local_path)}\n"
                f"{'='*80}\n"
                f"{'Total processed:':<20} {processed}\n"
                f"{'Successfully saved:':<20} {count}\n"
                f"{'Skipped:':<20} {skipped}\n"
                f"{'Success rate:':<20} {(count/processed*100 if processed > 0 else 0):.1f}%\n"
                f"{'='*80}\n"
                f"{'Duration:':<20} {int(hours):02d}h {int(minutes):02d}m {int(seconds):02d}s\n"
                f"{'Avg time per msg:':<20} {(duration/processed if processed > 0 else 0):.2f} seconds\n"
                f"{'Messages per hour:':<20} {(processed/duration*3600 if duration > 0 else 0):.1f}\n"
                f"{'='*80}"
            )
            logging.info(summary)
            
            # Save summary to file
            try:
                summary_file = os.path.join(local_path, 'download_summary.txt')
                with open(summary_file, 'w') as f:
                    f.write(summary)
                logging.info(f"Summary saved to: {summary_file}")
            except Exception as e:
                logging.error(f"Failed to save summary file: {e}")
            
            return count > 0
            
        finally:
            # Always close the connection
            try:
                mail.close()
                mail.logout()
                logging.info("Closed connection to mail server")
            except Exception as e:
                logging.error(f"Error closing connection: {e}", exc_info=True)
    
    except Exception as e:
        logging.error(f"Critical error in download_emails: {e}", exc_info=True)
        return False
