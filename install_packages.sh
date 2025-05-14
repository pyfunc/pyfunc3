#!/bin/bash

# Script to install all pyfunc3 packages locally
echo "Installing pyfunc3 packages..."

# Install the file package
echo "Installing pyfunc3-file..."
pip install /home/tom/softreck/cfo/pyfunc3/file/dist/pyfunc3_file-0.1.0-py3-none-any.whl

# Install the config package
echo "Installing pyfunc3-config..."
pip install /home/tom/softreck/cfo/pyfunc3/config/dist/pyfunc3_config-0.1.0-py3-none-any.whl

# Install the email package
echo "Installing pyfunc3-email..."
pip install /home/tom/softreck/cfo/pyfunc3/email/dist/pyfunc3_email-0.1.0-py3-none-any.whl

# Install the ocr package
echo "Installing pyfunc3-ocr..."
pip install /home/tom/softreck/cfo/pyfunc3/ocr/dist/pyfunc3_ocr-0.1.0-py3-none-any.whl

# Install the main package
echo "Installing pyfunc3 main package..."
pip install /home/tom/softreck/cfo/pyfunc3/dist/pyfunc3-0.1.0-py3-none-any.whl

echo "All packages installed successfully!"
