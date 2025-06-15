.PHONY: help install test lint format build clean dev-install
.DEFAULT_GOAL := help

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install package
	pip install -e .

dev-install: ## Install with development dependencies
	pip install -e ".[dev,test]"

test: ## Run tests
	pytest

test-cov: ## Run tests with coverage
	pytest --cov=quantum_interfaces --cov-report=html

lint: ## Run linter
	ruff check src tests
	mypy src

format: ## Format code
	black src tests
	ruff check --fix src tests

build: ## Build package
	python -m build

clean: ## Clean build artifacts
	rm -rf build/ dist/ *.egg-info/ htmlcov/ .coverage .pytest_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

git-setup: ## Setup git repository
	git init
	git add .
	git commit -m "Initial quantum-interfaces v0.1.0"
	git branch -M main
	git remote add origin https://github.com/quantopus/quantum-interfaces.git
	@echo "Run: git push -u origin main"

release: ## Create release tag
	git tag v$(shell python -c "import sys; sys.path.insert(0, 'src'); from quantum_interfaces import __version__; print(__version__)")
	@echo "Run: git push --tags" 