# pyfunc2

A collection of Python packages for the month project, providing utilities for file operations, configuration management, email handling, and OCR processing.

## Package Structure

The `pyfunc2` package is organized into several subpackages:

- **pyfunc2-file**: File operations utilities
- **pyfunc2-config**: Configuration management utilities
- **pyfunc2-email**: Email handling utilities
- **pyfunc2-ocr**: OCR processing utilities for PDF documents

## Installation

You can install the packages individually or the main package which includes all subpackages:

```bash
# Install main package
pip install pyfunc2

# Or install individual packages
pip install pyfunc2-file
pip install pyfunc2-config
pip install pyfunc2-email
pip install pyfunc2-ocr
```

## Usage

### File Operations

```python
from pyfunc2.file import create_folder, check_and_create_path

# Create a directory
create_folder("path/to/directory")

# Check and create a path if it doesn't exist
check_and_create_path("path/to/directory")
```

### Configuration Management

```python
from pyfunc2.config import get_config, get_email_path

# Get configuration values
config = get_config(folder="/.cfo/", key="emails")

# Get email path
email_path = get_email_path("target", "storage_root")
```

### Email Handling

```python
from pyfunc2.email import connect, download_emails, download_all_attachments_in_inbox

# Connect to an email server
mail = connect("imap.example.com", "username", "password")

# Download emails
download_emails("imap.example.com", "username", "password", "local_path", "INBOX", limit=50, month=5, year=2023)

# Download attachments
download_all_attachments_in_inbox("imap.example.com", "username", "password", "local_path", "INBOX")
```

### OCR Processing

```python
from pyfunc2.ocr import get_company_from_pdf, get_date_from_pdf, get_date_from_pdf_pattern, CompanyList

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

## Development

This project uses Poetry for dependency management. To set up the development environment:

```bash
# Install Poetry
pip install poetry

# Install dependencies
cd pyfunc2
poetry install

# Build the package
poetry build
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
