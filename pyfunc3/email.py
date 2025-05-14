"""
Email handling utilities for the month project.
"""

# Import from pyfunc3-email package
from pyfunc3_email import connect, download_emails, download_all_attachments_in_inbox

# Re-export
__all__ = ["connect", "download_emails", "download_all_attachments_in_inbox"]
