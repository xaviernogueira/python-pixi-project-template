# {{cookiecutter.name}}

[![check.yml](https://github.com/{{cookiecutter.user}}/{{cookiecutter.repository}}/actions/workflows/check.yml/badge.svg)](https://github.com/{{cookiecutter.user}}/{{cookiecutter.repository}}/actions/workflows/check.yml)
[![publish.yml](https://github.com/{{cookiecutter.user}}/{{cookiecutter.repository}}/actions/workflows/publish.yml/badge.svg)](https://github.com/{{cookiecutter.user}}/{{cookiecutter.repository}}/actions/workflows/publish.yml)
[![Documentation](https://img.shields.io/badge/documentation-available-brightgreen.svg)](https://{{cookiecutter.user}}.github.io/{{cookiecutter.repository}}/)
[![License](https://img.shields.io/github/license/{{cookiecutter.user}}/{{cookiecutter.repository}})](https://github.com/{{cookiecutter.user}}/{{cookiecutter.repository}}/blob/main/LICENCE.txt)
[![Release](https://img.shields.io/github/v/release/{{cookiecutter.user}}/{{cookiecutter.repository}})](https://github.com/{{cookiecutter.user}}/{{cookiecutter.repository}}/releases)

# Description

{{cookiecutter.description}}.

(This README is generated from a cookiecutter template. Delete this comment and modify your README!)

# Installation

Initialize your project with the provided invoke command.
```bash
invoke installs # Install dependencies and pre-commit hooks
```

# Usage

(The source comes with an example python package and an example FastAPI app. Delete this comment and add details for your application.)

```bash
# Test the example package
poetry run {{cookiecutter.repository}}
```

```bash
# Test the example API
poetry add fastapi uvicorn
poetry run uvicorn main:app --reload
```

## Development Features

* **Streamlined Project Structure:** A well-defined directory layout for source code, tests, documentation, tasks, and Docker configurations.
* **Poetry Integration:** Effortless dependency management and packaging with [Poetry](https://python-poetry.org/).
* **Automated Testing and Checks:** Pre-configured workflows using [Pytest](https://docs.pytest.org/), [Ruff](https://docs.astral.sh/ruff/), [Mypy](https://mypy.readthedocs.io/), [Bandit](https://bandit.readthedocs.io/), and [Coverage](https://coverage.readthedocs.io/) to ensure code quality, style, security, and type safety.
* **Pre-commit Hooks:** Automatic code formatting and linting with [Ruff](https://docs.astral.sh/ruff/) and other pre-commit hooks to maintain consistency.
* **Dockerized Deployment:** Dockerfile and docker-compose.yml for building and running the package within a containerized environment ([Docker](https://www.docker.com/)).
* **Invoke Task Automation:** [PyInvoke](https://www.pyinvoke.org/) tasks to simplify development workflows such as cleaning, installing, formatting, checking, building, documenting, and running MLflow projects.
* **Comprehensive Documentation:** [pdoc](https://pdoc.dev/) generates API documentation, and Markdown files provide clear usage instructions.
* **GitHub Workflow Integration:** Continuous integration and deployment workflows are set up using [GitHub Actions](https://github.com/features/actions), automating testing, checks, and publishing.

Use the provided Invoke tasks to manage your development workflow:

- `invoke installs`: Install dependencies and pre-commit hooks.
- `invoke formats`: Format your code.
- `invoke checks`: Run code quality, type, security, and test checks.
- `invoke docs`: Generate API documentation.
- `invoke packages`: Build your Python package.
- `invoke containers`: Build and run your Docker image.



