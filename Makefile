PYTHON = python
MANAGE = $(PYTHON) manage.py

# Default target
.DEFAULT_GOAL := help

help:
	@echo "Available targets:"
	@echo "  run         : Run the Django development server"
	@echo "  test        : Run Django tests"
	@echo "  migrate     : Run Django migrate"
	@echo "  lint        : Lint the code using Black and pep8"

run:
	$(MANAGE) runserver --settings=todoapp.settings.ci

test:
	$(MANAGE) test --settings=todoapp.settings.ci

migrate:
	$(MANAGE) migrate --settings=todoapp.settings.ci

lint:
	@echo "Linting with flake8..."
	${PYTHON} -m flake8 .

format:
	@echo "Linting with Black..."
	${PYTHON} -m black .
