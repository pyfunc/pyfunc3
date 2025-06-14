# Makefile for pyfunc3 package

.PHONY: all install clean test build

# Default target
all: install

# Install all packages
install:
	@echo "Installing pyfunc3 packages..."
	./install_packages.sh

# Build all packages
build:
	@echo "Building pyfunc3-file package..."
	cd file && poetry build
	@echo "Building pyfunc3-config package..."
	cd config && poetry build
	@echo "Building pyfunc3-email package..."
	cd email && poetry build
	@echo "Building pyfunc3-ocr package..."
	cd ocr && poetry build
	@echo "Building pyfunc3 main package..."
	poetry build

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -rf dist/
	rm -rf file/dist/
	rm -rf config/dist/
	rm -rf email/dist/
	rm -rf ocr/dist/
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	find . -name "*.egg-info" -exec rm -rf {} +

# Run tests
test:
	@echo "Running tests..."
	# Add test commands here when tests are available
	@echo "No tests available yet."

# Create virtual environment
venv:
	@echo "Creating virtual environment..."
	python -m venv .venv
	@echo "Activate with: source .venv/bin/activate"

# Help target
help:
	@echo "Available targets:"
	@echo "  all       - Default target, installs all packages"
	@echo "  install   - Install all packages"
	@echo "  build     - Build all packages"
	@echo "  clean     - Clean build artifacts"
	@echo "  test      - Run tests"
	@echo "  venv      - Create virtual environment"
	@echo "  help      - Show this help message"
