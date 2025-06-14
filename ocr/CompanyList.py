"""
Module containing the CompanyList class for managing company data.
"""

class CompanyList:
    """
    A class to manage a list of companies and their associated data.
    """
    
    def __init__(self, companies=None):
        """
        Initialize the CompanyList with an optional list of companies.
        
        Args:
            companies (list, optional): List of company names. Defaults to None.
        """
        self.companies = list(companies) if companies is not None else []
        
    def sorted_from_shortest_to_longest_name(self):
        """
        Return a new list of companies sorted by name length (shortest first).
        
        Returns:
            list: Sorted list of company names
        """
        return sorted(self.companies, key=lambda x: (len(str(x)), str(x)))
    
    def add_company(self, company_name):
        """
        Add a company to the list if it doesn't already exist.
        
        Args:
            company_name (str): Name of the company to add.
            
        Returns:
            bool: True if the company was added, False if it already exists.
        """
        if company_name not in self.companies:
            self.companies.append(company_name)
            return True
        return False
    
    def remove_company(self, company_name):
        """
        Remove a company from the list.
        
        Args:
            company_name (str): Name of the company to remove.
            
        Returns:
            bool: True if the company was removed, False if it didn't exist.
        """
        if company_name in self.companies:
            self.companies.remove(company_name)
            return True
        return False
    
    def sort_companies(self):
        """Sort the list of companies alphabetically."""
        self.companies.sort()
    
    def __iter__(self):
        """Make the class iterable over the companies list."""
        return iter(self.companies)
    
    def __len__(self):
        """Return the number of companies in the list."""
        return len(self.companies)
    
    def __contains__(self, company_name):
        """Check if a company is in the list."""
        return company_name in self.companies
