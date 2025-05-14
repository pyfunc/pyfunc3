"""
Functions for extracting company names from PDF documents.
"""

import os
import re
import logging
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        str: Extracted text
    """
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        logging.error(f"Error extracting text from PDF {pdf_path}: {e}")
        return ""


def get_company_from_pdf(pdf_path, clean_patterns, company_list):
    """
    Extract company names from a PDF document.
    
    Args:
        pdf_path (str): Path to the PDF file
        clean_patterns (list): List of text cleaning patterns
        company_list (list): List of company names to search for
        
    Returns:
        list: List of found company names
    """
    try:
        if not os.path.exists(pdf_path):
            logging.error(f"PDF file not found: {pdf_path}")
            return []
        
        # Extract text from PDF
        text = extract_text_from_pdf(pdf_path)
        if not text:
            logging.warning(f"No text extracted from PDF: {pdf_path}")
            return []
        
        # Clean text
        cleaned_text = text
        for pattern in clean_patterns:
            if pattern == "remove_extra_spaces":
                cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
            elif pattern == "remove_special_chars":
                cleaned_text = re.sub(r'[^\w\s\.\-\/]', ' ', cleaned_text)
        
        # Convert text to lowercase for case-insensitive matching
        cleaned_text_lower = cleaned_text.lower()
        
        # Find companies in text
        found_companies = []
        for company in company_list:
            company_lower = company.lower()
            if company_lower in cleaned_text_lower:
                found_companies.append(company)
        
        return found_companies
    except Exception as e:
        logging.error(f"Error extracting company from PDF {pdf_path}: {e}")
        return []
