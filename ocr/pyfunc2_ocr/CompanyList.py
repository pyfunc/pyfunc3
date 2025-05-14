"""
Class for managing company lists for OCR processing.
"""

import os
import csv
import logging


class CompanyList:
    """
    Class for managing and retrieving company names for OCR processing.
    """
    
    def __init__(self, csv_path=None):
        """
        Initialize the CompanyList.
        
        Args:
            csv_path (str, optional): Path to a CSV file containing company names.
                                     If None, will look for company.csv in the current directory.
        """
        self.companies = []
        
        # If no CSV path provided, look for company.csv in the current directory
        if csv_path is None:
            # First check current directory
            if os.path.exists("company.csv"):
                csv_path = "company.csv"
            # Then check month directory
            elif os.path.exists(os.path.join(os.path.dirname(os.path.dirname(__file__)), "month", "company.csv")):
                csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "month", "company.csv")
        
        # Load companies from CSV if available
        if csv_path and os.path.exists(csv_path):
            self._load_from_csv(csv_path)
        else:
            # Default company list if CSV not found
            self.companies = [
                "Amazon",
                "Google",
                "Microsoft",
                "Apple",
                "Facebook",
                "Netflix",
                "Uber",
                "Airbnb",
                "Softreck",
                "PayPal",
                "Wise"
            ]
            logging.warning(f"Company CSV not found at {csv_path}, using default company list")
    
    def _load_from_csv(self, csv_path):
        """
        Load company names from a CSV file.
        
        Args:
            csv_path (str): Path to the CSV file
        """
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row and len(row) > 0 and row[0].strip():
                        self.companies.append(row[0].strip())
            
            logging.info(f"Loaded {len(self.companies)} companies from {csv_path}")
        except Exception as e:
            logging.error(f"Error loading companies from CSV: {e}")
            # Fall back to default list
            self.companies = [
                "Amazon",
                "Google",
                "Microsoft",
                "Apple",
                "Facebook",
                "Netflix",
                "Uber",
                "Airbnb",
                "Softreck",
                "PayPal",
                "Wise"
            ]
    
    def get_all(self):
        """
        Get all company names.
        
        Returns:
            list: List of company names
        """
        return self.companies
    
    def sorted_from_shortest_to_longest_name(self):
        """
        Get company names sorted from shortest to longest.
        
        Returns:
            list: Sorted list of company names
        """
        return sorted(self.companies, key=len)
    
    def sorted_from_longest_to_shortest_name(self):
        """
        Get company names sorted from longest to shortest.
        
        Returns:
            list: Sorted list of company names
        """
        return sorted(self.companies, key=len, reverse=True)
