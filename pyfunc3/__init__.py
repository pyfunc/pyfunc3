"""
Main package for month project utilities (pyfunc3).
"""

import os
import sys

# Add the parent directory to the path so we can import the modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import subpackages
from . import file
from . import config
from . import email
from . import ocr

# Version information
__version__ = "0.1.0"
