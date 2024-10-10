VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip
MANAGE = $(PYTHON) manage.py

.PHONY: build run checkmigration

build:
	python3 -m venv $(VENV_DIR) && $(PIP) install -r requirements.txt

run:
	$(MANAGE) runserver

checkmigration:
	$(MANAGE) makemigrations --check --dry-run || (echo "Making migrations..." && $(MANAGE) makemigrations && $(MANAGE) migrate)
