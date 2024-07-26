# Copyright 2024 PYBROTOOLS authors.
# See license.md file for details.

# Internal variables
NAME           = pybrotools
INSTALL_STAMP  = .install.stamp
POETRY         = $(shell command -v poetry 2> /dev/null)

# Default construction
.DEFAULT_GOAL := help

# Generate make help
.PHONY: help
help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo ""
	@echo "  install    installs packages and prepare environment"
	@echo "  clean      removes all temp files and dev package"
	@echo "  format     runs ruff linter on source code"
	@echo "  test       runs all the tests using pytest"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."

# Install package
install: $(INSTALL_STAMP)
$(INSTALL_STAMP): pyproject.toml poetry.lock
	@if [ -z $(POETRY) ]; then echo "Poetry could not be found. See https://python-poetry.org/docs/"; exit 2; fi
	$(POETRY) install
	touch $(INSTALL_STAMP)

# Clean up all temporary files
.PHONY: clean
clean:
	find . -type d -name "__pycache__" | xargs rm -rf {};
	rm -rf $(INSTALL_STAMP)
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	pip uninstall -y $(NAME)

# Reformat source code
.PHONY: format
format: $(INSTALL_STAMP)
	$(POETRY) run ruff check --fix ./tests/ src/$(NAME)

# Test python package with pytest
.PHONY: test
test: $(INSTALL_STAMP)
	$(POETRY) run pytest $(TESTOPTS)
