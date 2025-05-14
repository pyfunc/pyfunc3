# pyfunc2-email

Email handling utilities for the month project.

## Features

- Connect to IMAP email servers
- Download emails from specific folders
- Download email attachments

## Installation

```bash
pip install pyfunc2-email
```

## Usage

```python
from pyfunc2_email import connect, download_emails, download_all_attachments_in_inbox

# Connect to an email server
mail = connect("imap.example.com", "username", "password")

# Download emails
download_emails("imap.example.com", "username", "password", "local_path", "INBOX", limit=50, month=5, year=2023)

# Download attachments
download_all_attachments_in_inbox("imap.example.com", "username", "password", "local_path", "INBOX")
```

## Functions

### `connect(server, username, password)`

Connects to an IMAP email server.

**Parameters:**
- `server` (str): IMAP server address
- `username` (str): Email username
- `password` (str): Email password

**Returns:**
- `imaplib.IMAP4_SSL`: IMAP connection object or None if connection fails

### `download_emails(server, username, password, local_path, remote_folder, limit=50, month=0, year=0)`

Downloads emails from a remote folder to a local path.

**Parameters:**
- `server` (str): IMAP server address
- `username` (str): Email username
- `password` (str): Email password
- `local_path` (str): Local path to save emails
- `remote_folder` (str): Remote folder to download from
- `limit` (int): Maximum number of emails to download
- `month` (int): Month to filter emails (1-12, 0 for all)
- `year` (int): Year to filter emails (0 for all)

**Returns:**
- `bool`: True if successful, False otherwise

### `download_all_attachments_in_inbox(server, username, password, local_path, remote_folder, limit=50)`

Downloads all attachments from emails in a remote folder to a local path.

**Parameters:**
- `server` (str): IMAP server address
- `username` (str): Email username
- `password` (str): Email password
- `local_path` (str): Local path to save attachments
- `remote_folder` (str): Remote folder to download from
- `limit` (int): Maximum number of emails to process

**Returns:**
- `bool`: True if successful, False otherwise
