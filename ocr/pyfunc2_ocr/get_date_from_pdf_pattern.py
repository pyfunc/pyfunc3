"""
Patterns for date extraction from PDF documents.
"""

class get_date_from_pdf_pattern:
    """
    Class containing patterns for date extraction from PDF documents.
    """
    
    # Format patterns for output dates
    format_out_list = [
        "%Y-%m-%d",  # 2023-05-14
        "%d.%m.%Y",  # 14.05.2023
        "%d/%m/%Y",  # 14/05/2023
        "%Y.%m.%d",  # 2023.05.14
        "%Y/%m/%d",  # 2023/05/14
        "%d-%m-%Y",  # 14-05-2023
        "%m/%d/%Y",  # 05/14/2023
        "%Y.%m"      # 2023.05 (year.month format)
    ]
    
    # Patterns for cleaning text before date extraction
    pattern_clean_list = [
        "remove_extra_spaces",
        "remove_special_chars"
    ]
    
    # Regular expression patterns for date extraction
    pattern_input_list = [
        # ISO format: YYYY-MM-DD
        r'(\d{4}-\d{1,2}-\d{1,2})',
        
        # European format: DD.MM.YYYY
        r'(\d{1,2}\.\d{1,2}\.\d{4})',
        
        # European format: DD/MM/YYYY
        r'(\d{1,2}/\d{1,2}/\d{4})',
        
        # US format: MM/DD/YYYY
        r'(\d{1,2}/\d{1,2}/\d{4})',
        
        # Date with month name: DD Month YYYY
        r'(\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4})',
        
        # Date with abbreviated month name: DD Mon YYYY
        r'(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{4})',
        
        # German format: DD.MM.YYYY
        r'(\d{1,2}\.\d{1,2}\.\d{4})',
        
        # German month names
        r'(\d{1,2}\s+(?:Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\s+\d{4})',
        
        # Year and month only: YYYY.MM
        r'(\d{4}\.\d{1,2})',
        
        # Year and month only: YYYY/MM
        r'(\d{4}/\d{1,2})'
    ]
