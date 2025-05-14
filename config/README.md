# pyfunc2-config

Configuration utilities for the month project.

## Features

- Read configuration values from JSON files
- Manage email paths and storage locations

## Installation

```bash
pip install pyfunc2-config
```

## Usage

```python
from pyfunc2_config import get_config, get_email_path

# Get configuration values
config = get_config(folder="/.cfo/", key="emails")

# Get email path
email_path = get_email_path("target", "storage_root")
```

## Functions

### `get_config(folder="/.cfo/", key=None)`

Gets configuration values from a JSON config file.

**Parameters:**
- `folder` (str): Path to the folder containing the config file
- `key` (str): Key to retrieve from the config file

**Returns:**
- The configuration value for the specified key, or the entire config if no key is specified

### `get_email_path(email_target, storage_root)`

Gets the path for storing email data.

**Parameters:**
- `email_target` (str): Target identifier for the email
- `storage_root` (str): Root storage directory

**Returns:**
- `str`: Path for storing email data
