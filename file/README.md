# pyfunc2-file

File operations utilities for the month project.

## Features

- Create directories and ensure they exist
- Check and create paths as needed

## Installation

```bash
pip install pyfunc2-file
```

## Usage

```python
from pyfunc2_file import create_folder, check_and_create_path

# Create a directory
create_folder("path/to/directory")

# Check and create a path if it doesn't exist
check_and_create_path("path/to/directory")
```

## Functions

### `create_folder(path)`

Creates a directory if it doesn't exist.

**Parameters:**
- `path` (str): Path to the directory to create

**Returns:**
- `bool`: True if directory was created or already exists, False otherwise

### `check_and_create_path(path)`

Checks if a path exists and creates it if it doesn't.

**Parameters:**
- `path` (str): Path to check and create

**Returns:**
- `bool`: True if path exists or was created, False otherwise
