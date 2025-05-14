# pyfunc2-ocr

OCR utilities for the month project.

## Features

- Extract company names from PDF documents
- Extract dates from PDF documents using various patterns
- Manage company lists for OCR processing

## Installation

```bash
pip install pyfunc2-ocr
```

## Usage

```python
from pyfunc2_ocr import get_company_from_pdf, get_date_from_pdf, get_date_from_pdf_pattern, CompanyList

# Get company list
company_list = CompanyList().sorted_from_shortest_to_longest_name()

# Extract company from PDF
companies = get_company_from_pdf("path/to/file.pdf", [], company_list)

# Extract date from PDF
dates = get_date_from_pdf(
    "path/to/file.pdf",
    get_date_from_pdf_pattern.format_out_list,
    ["remove_extra_spaces"],
    get_date_from_pdf_pattern.pattern_input_list,
    ['en_US', 'de_DE']
)
```

## Classes and Functions

### `CompanyList`

Class for managing and retrieving company names for OCR processing.

**Methods:**
- `__init__(csv_path=None)`: Initialize with an optional CSV file path
- `get_all()`: Get all company names
- `sorted_from_shortest_to_longest_name()`: Get company names sorted from shortest to longest
- `sorted_from_longest_to_shortest_name()`: Get company names sorted from longest to shortest

### `get_company_from_pdf(pdf_path, clean_patterns, company_list)`

Extracts company names from a PDF document.

**Parameters:**
- `pdf_path` (str): Path to the PDF file
- `clean_patterns` (list): List of text cleaning patterns
- `company_list` (list): List of company names to search for

**Returns:**
- `list`: List of found company names

### `get_date_from_pdf(pdf_path, format_out_list, clean_patterns, pattern_input_list, locales=None)`

Extracts dates from a PDF document.

**Parameters:**
- `pdf_path` (str): Path to the PDF file
- `format_out_list` (list): List of output date formats
- `clean_patterns` (list): List of text cleaning patterns
- `pattern_input_list` (list): List of regex patterns for date extraction
- `locales` (list): List of locales for date parsing

**Returns:**
- `list`: List of extracted dates [original_text, date_object, formatted_date]

### `get_date_from_pdf_pattern`

Class containing patterns for date extraction from PDF documents.

**Class Attributes:**
- `format_out_list`: Format patterns for output dates
- `pattern_clean_list`: Patterns for cleaning text before date extraction
- `pattern_input_list`: Regular expression patterns for date extraction
