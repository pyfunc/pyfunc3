"""
Functions for extracting dates from PDF documents.
"""

import re
import os
import logging
import datetime
import dateutil.parser as dparser
from PyPDF2 import PdfReader
import datefinder


def clean_text(text, clean_patterns):
    """
    Clean text based on specified patterns.
    
    Args:
        text (str): Text to clean
        clean_patterns (list): List of cleaning patterns to apply
        
    Returns:
        str: Cleaned text
    """
    if not text:
        return ""
    
    for pattern in clean_patterns:
        if pattern == "remove_extra_spaces":
            text = re.sub(r'\s+', ' ', text).strip()
        elif pattern == "remove_special_chars":
            text = re.sub(r'[^\w\s\.\-\/]', ' ', text)
    
    return text


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


def get_date_from_pdf(pdf_path, format_out_list, clean_patterns, pattern_input_list, locales=None):
    """
    Extract dates from a PDF document.
    
    Args:
        pdf_path (str): Path to the PDF file
        format_out_list (list): List of output date formats
        clean_patterns (list): List of text cleaning patterns
        pattern_input_list (list): List of regex patterns for date extraction
        locales (list): List of locales for date parsing
        
    Returns:
        list: List of extracted dates [original_text, date_object, formatted_date]
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
        cleaned_text = clean_text(text, clean_patterns)
        
        # Try to find dates using regex patterns
        dates = []
        for pattern in pattern_input_list:
            matches = re.findall(pattern, cleaned_text)
            for match in matches:
                try:
                    # Try to parse the date
                    date_obj = dparser.parse(match, fuzzy=True)
                    
                    # Format the date
                    formatted_date = None
                    for date_format in format_out_list:
                        try:
                            formatted_date = date_obj.strftime(date_format)
                            break
                        except:
                            continue
                    
                    if formatted_date:
                        # Check if we have YYYY.MM format
                        if date_format == "%Y.%m":
                            year_month = formatted_date
                            dates.append([match, date_obj, year_month])
                        else:
                            dates.append([match, date_obj, formatted_date])
                except:
                    continue
        
        # If no dates found with regex, try datefinder
        if not dates:
            try:
                matches = list(datefinder.find_dates(cleaned_text, base_date=datetime.datetime.today()))
                for date_obj in matches:
                    # Format the date
                    formatted_date = None
                    for date_format in format_out_list:
                        try:
                            formatted_date = date_obj.strftime(date_format)
                            break
                        except:
                            continue
                    
                    if formatted_date:
                        # Extract the original text that matched (approximate)
                        date_str = date_obj.strftime("%Y-%m-%d")
                        dates.append([date_str, date_obj, formatted_date])
            except Exception as e:
                logging.error(f"Error using datefinder: {e}")
        
        return dates
    except Exception as e:
        logging.error(f"Error extracting date from PDF {pdf_path}: {e}")
        return []
