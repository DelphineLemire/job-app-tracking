.PHONY: update
update: ## Uptade the poetry environment
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@poetry shell
	@poetry update --with dev --with docs

.PHONY: check
check: ## Run code quality tools.
	@echo "🚀 Checking Poetry lock file consistency with 'pyproject.toml': Running poetry lock --check"
	@poetry lock --check
	@echo "🚀 Linting code: Running pre-commit"
	@poetry run pre-commit run -a
	@echo "🚀 Static type checking: Running mypy"
	@poetry run mypy .
	@echo "🚀 Checking for obsolete dependencies: Running deptry"
	@poetry run deptry -v .

.PHONY: test
test: ## Test the code with pytest.
	@echo "🚀 Testing code: Running pytest"
	@poetry run pytest --cov --cov-config=pyproject.toml --cov-report=html .

.PHONY: docs-test
docs-test: ## Test if documentation can be built without warnings or errors
	@mkdocs build -s #-v

.PHONY: docs
docs: ## Build and serve the documentation
	@mkdocs serve -a 127.0.0.1:8010

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help