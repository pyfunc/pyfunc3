import os
from PyPDF2 import PdfReader
from typing import List

def find_string_in_file_path(directory: str, search_text: str, extensions: List[str] = ['.pdf']) -> List[str]:
    """
    Search for a string in all PDF files (or files with given extensions) in a directory tree.
    Returns a list of file paths where the string was found.
    """
    matches = []
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext.lower()) for ext in extensions):
                file_path = os.path.join(root, file)
                try:
                    reader = PdfReader(file_path)
                    for page in reader.pages:
                        text = page.extract_text()
                        if text and search_text in text:
                            matches.append(file_path)
                            break
                except Exception as e:
                    # Optionally log or print errors for unreadable files
                    pass
    return matches
