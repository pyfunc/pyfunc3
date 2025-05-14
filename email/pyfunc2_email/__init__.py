"""
Email handling utilities for the month project.
"""

from .connect import connect
from .download_emails import download_emails
from .download_all_attachments_in_inbox import download_all_attachments_in_inbox

__all__ = ["connect", "download_emails", "download_all_attachments_in_inbox"]
