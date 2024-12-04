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

Initialize your project with the provided pixi run command.
```bash
# Install dependencies and pre-commit hooks
pixi run installs
```

# Usage

(The source comes with an example python package and an example FastAPI app. Delete this comment and add details for your application.)

Test the example package
```bash
pixi run {{cookiecutter.repository}}
```

Test the example API with Docker:
```bash
pixi add fastapi uvicorn

# Invoke docker compose
pixi run containers

# Or run with docker compose
docker compose up --build

# Or run with docker
# Note: specify platform if running on Apple M chip
docker build --platform linux/amd64 -t angle-to-geo-image -f Dockerfile .
docker run -it --platform linux/amd64 --name angle-to-geo-test-ctr -p 8000:8000 angle-to-geo-image
```

```bash
pixi add fastapi uvicorn
# Test the API using the local environment
cd src
pixi run uvicorn example_app.main:app --reload
```

## Development Features

* **Streamlined Project Structure:** A well-defined directory layout for source code, tests, documentation, tasks, and Docker configurations.
* **Pixi Integration:** Effortless dependency management and packaging with [Pixi](https://pixi.sh/latest/), even with non-python dependencies.
* **Automated Testing and Checks:** Pre-configured workflows using [Pytest](https://docs.pytest.org/), [Ruff](https://docs.astral.sh/ruff/), [Mypy](https://mypy.readthedocs.io/), [Bandit](https://bandit.readthedocs.io/), and [Coverage](https://coverage.readthedocs.io/) to ensure code quality, style, security, and type safety.
* **Pre-commit Hooks:** Automatic code formatting and linting with [Ruff](https://docs.astral.sh/ruff/) and other pre-commit hooks to maintain consistency.
* **Dockerized Deployment:** Dockerfile and docker-compose.yml for building and running the package within a containerized environment ([Docker](https://www.docker.com/)).
* **Invoke Task Automation:** [PyInvoke](https://www.pypixi run.org/) tasks to simplify development workflows such as cleaning, installing, formatting, checking, building, documenting, and running MLflow projects.
* **Comprehensive Documentation:** [pdoc](https://pdoc.dev/) generates API documentation, and Markdown files provide clear usage instructions.
* **GitHub Workflow Integration:** Continuous integration and deployment workflows are set up using [GitHub Actions](https://github.com/features/actions), automating testing, checks, and publishing.
* **Performance Oriented Packaging:** [hatch](https://hatch.pypa.io/latest/install/) is used for packaging, which provides performance benefits over `setuptools` or `poetry`. See [this](https://hatch.pypa.io/latest/why/#build-backend) for details.

To run the provided Invoke tasks thru pixi:

- `pixi run installs`: Install dependencies and pre-commit hooks.
- `pixi run formats`: Format your code.
- `pixi run checks`: Run code quality, type, security, and test checks.
- `pixi run docs`: Generate API documentation.
- `pixi run packages`: Build your Python package.
- `pixi run containers`: Build and run your Docker image.

### Using Ruff with PyCharm

Note: First version of [Ruff plugin](https://github.com/koxudaxi/ruff-pycharm-plugin) would have issues (v0.0.27) apparently due to my PyCharm version (2023.2).

I upgraded to (2024.2) and Ruff 0.0.39 and now autosave works.
