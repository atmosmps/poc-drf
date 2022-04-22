PYTEST_CMD = python -m py.test -W ignore::DeprecationWarning
PYTEST_COVERAGE_CMD = $(PYTEST_CMD) --no-cov-on-fail --cov=app --cov-config=app/.coveragerc
MINIMUM_COVERAGE = 90
GIT_FETCH_MAIN_CMD = git fetch origin main:refs/remotes/origin/main


# Development
build-run:
	# Run the development server on background
	docker-compose up -d --build
	# Now head to http://0.0.0.0:5000/api/v1/healthcheck

see-log-app:
	docker-compose logs app

build-run-attached:
	# Run the development server attached showing the logs
	docker-compose up --build

stop-docker:
	docker-compose down -v

test: build-run
	docker-compose exec app $(PYTEST_CMD) -v -x -n auto
	make stop-docker

test-matching: build-run
	docker-compose exec app $(PYTEST_CMD) -s -v -x -rs -k $(Q)

coverage: build-run
	docker-compose exec app $(PYTEST_COVERAGE_CMD)
	make stop-docker

test-coverage: build-run
	docker-compose exec app $(PYTEST_COVERAGE_CMD) --cov-report=xml
	$(GIT_FETCH_MAIN_CMD)
	diff-cover ./coverage.xml --compare-branch=main --fail-under $(MINIMUM_COVERAGE)
	make stop-docker

test-coverage-html: build-run
	docker-compose exec app $(PYTEST_COVERAGE_CMD) --cov-report=xml --cov-report=html
	$(GIT_FETCH_MAIN_CMD)
	diff-cover ./coverage.xml --compare-branch=main
	echo "Report available on htmlcov/index.html"
	make stop-docker

test-coverage-diff-html: build-run
	docker-compose exec app $(PYTEST_COVERAGE_CMD) --cov-report=xml
	$(GIT_FETCH_MAIN_CMD)
	diff-cover ./coverage.xml --compare-branch=main --html-report coverage-diff.html
	echo "Report available on htmlcov/index.html"
	make stop-docker

lint: build-run
	docker-compose exec app black --check .
	docker-compose exec app flake8 --exclude=*/__init__.py
	make stop-docker

lint-fix: build-run
	docker-compose exec app black .
	make stop-docker


# CI
ci-lint:
	black --check .
	flake8 --exclude=*/__init__.py,./venv

ci-install:
	pip install -r requirements-dev.txt --cache-dir=$(CACHE_DIR)

ci-coverage:
	$(PYTEST_CMD) --no-cov-on-fail --cov=app --cov-config=src/app/.coveragerc --cov-report=xml --cov-report=term-missing
	$(GIT_FETCH_MAIN_CMD)
	diff-cover coverage.xml --compare-branch=origin/main --fail-under $(MINIMUM_COVERAGE) --html-report coverage-diff.html
