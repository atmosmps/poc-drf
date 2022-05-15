DJANGO_SETTINGS_MODULE = app.settings
APP_COMMAND = python manage.py
PYTEST_CMD = python -m py.test -W ignore::DeprecationWarning --ds=$(DJANGO_SETTINGS_MODULE)
PYTEST_COVERAGE_CMD = $(PYTEST_CMD) --no-cov-on-fail --cov=app --cov-config=app/.coveragerc
MINIMUM_COVERAGE = 90
GIT_FETCH_MAIN_CMD = git fetch origin main:refs/remotes/origin/main

server:
	$(APP_COMMAND) runserver

test:
	$(PYTEST_CMD) -v -x --no-migrations --reuse-db

test-matching:
	$(PYTEST_CMD) -s -v -x -rs $(Q)

coverage:
	$(PYTEST_COVERAGE_CMD)

test-coverage:
	$(PYTEST_COVERAGE_CMD) --cov-report=xml
	$(GIT_FETCH_MAIN_CMD)
	diff-cover ./coverage.xml --compare-branch=main --fail-under $(MINIMUM_COVERAGE)

test-coverage-html:
	$(PYTEST_COVERAGE_CMD) --cov-report=xml --cov-report=html
	$(GIT_FETCH_MAIN_CMD)
	diff-cover ./coverage.xml --compare-branch=main
	echo "Report available on htmlcov/index.html"

test-coverage-diff-html:
	$(PYTEST_COVERAGE_CMD) --cov-report=xml
	$(GIT_FETCH_MAIN_CMD)
	diff-cover ./coverage.xml --compare-branch=main --html-report coverage-diff.html
	echo "Report available on htmlcov/index.html"

lint:
	black --check .
	# flake8 --exclude=*/__init__.py

lint-fix:
	black .

migrations:
	$(APP_COMMAND) makemigrations

migrate:
	$(APP_COMMAND) migrate

check-migrations:
	$(APP_COMMAND) check-migrations

ci-lint:
	black --check .
	# flake8 --exclude=*/__init__.py,./venv

ci-install:
	# pip install -r requirements-dev.txt --cache-dir=$(CACHE_DIR)

ci-coverage:
	$(PYTEST_CMD) --no-cov-on-fail --cov=app --cov-config=src/app/.coveragerc --cov-report=xml --cov-report=term-missing
	$(GIT_FETCH_MAIN_CMD)
	diff-cover coverage.xml --compare-branch=origin/main --fail-under $(MINIMUM_COVERAGE) --html-report coverage-diff.html
