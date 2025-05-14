#!/bin/bash

# Script to install all pyfunc2 packages locally
echo "Installing pyfunc2 packages..."

# Install the file package
echo "Installing pyfunc2-file..."
pip install /home/tom/softreck/cfo/pyfunc2/file/dist/pyfunc2_file-0.1.0-py3-none-any.whl

# Install the config package
echo "Installing pyfunc2-config..."
pip install /home/tom/softreck/cfo/pyfunc2/config/dist/pyfunc2_config-0.1.0-py3-none-any.whl

# Install the email package
echo "Installing pyfunc2-email..."
pip install /home/tom/softreck/cfo/pyfunc2/email/dist/pyfunc2_email-0.1.0-py3-none-any.whl

# Install the ocr package
echo "Installing pyfunc2-ocr..."
pip install /home/tom/softreck/cfo/pyfunc2/ocr/dist/pyfunc2_ocr-0.1.0-py3-none-any.whl

# Install the main package
echo "Installing pyfunc2 main package..."
pip install /home/tom/softreck/cfo/pyfunc2/dist/pyfunc2-0.1.0-py3-none-any.whl

echo "All packages installed successfully!"
