"""
Functionality for removing empty folders in a directory tree.
"""
import os
from typing import List, Set

def remove_empty_folders(path: str, remove_root: bool = True) -> List[str]:
    """
    Recursively remove empty folders in the specified path.
    
    Args:
        path (str): The root directory path to start searching for empty folders
        remove_root (bool): Whether to remove the root folder if it's empty
        
    Returns:
        List[str]: List of paths that were removed
    """
    removed = []
    
    # Check if path is a directory
    if not os.path.isdir(path):
        return removed
        
    # Recursively process subdirectories
    entries = os.listdir(path)
    for entry in entries:
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            removed.extend(remove_empty_folders(full_path))
    
    # After processing subdirectories, check if current directory is empty
    entries = os.listdir(path)
    if not entries and remove_root:
        try:
            os.rmdir(path)
            removed.append(path)
        except OSError:
            # Directory might have been deleted by another process
            pass
            
    return removed
