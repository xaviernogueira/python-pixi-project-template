# {{cookiecutter.name}}

[![check.yaml](https://github.com/{{cookiecutter.user}}/{{cookiecutter.repository}}/actions/workflows/check.yaml/badge.svg)](https://github.com/{{cookiecutter.user}}/{{cookiecutter.repository}}/actions/workflows/check.yaml)
[![test.yaml](https://github.com/{{cookiecutter.user}}/{{cookiecutter.repository}}/actions/workflows/test.yaml/badge.svg)](https://github.com/{{cookiecutter.user}}/{{cookiecutter.repository}}/actions/workflows/test.yaml)
[![build.yaml](https://github.com/{{cookiecutter.user}}/{{cookiecutter.repository}}/actions/workflows/build.yaml/badge.svg)](https://github.com/{{cookiecutter.user}}/{{cookiecutter.repository}}/actions/workflows/build.yaml)
[![Documentation](https://img.shields.io/badge/documentation-available-brightgreen.svg)](https://{{cookiecutter.user}}.github.io/{{cookiecutter.repository}}/)
[![Release](https://img.shields.io/github/v/release/{{cookiecutter.user}}/{{cookiecutter.repository}})](https://github.com/{{cookiecutter.user}}/{{cookiecutter.repository}}/releases)

# Description

{{cookiecutter.description}}

# Installation

Initialize your project with the provided pixi run command.
```bash
# Install dependencies and pre-commit hooks
pixi run installs
```

Next activate the pixi environment (optionally specifying the dev environment).
```bash
pixi shell -e dev
```

Finally install the module and run the CLI, API, or tests.
```bash
pixi run build # or pixi run build_editable
```

# Usage

## CLI

```bash
python cli.py --help
```

## Running development tasks

Pixi tasks are used to trigger PyInvoke tasks. These tasks are enumerated below grouped by functionality.


### Install and Build

```bash
pixi run installs # install dependencies

pixi run build # build the package
pixi run build_editable # build the package in editable mode
```

### Tests

```bash
pixi run tests # run local tests
pixi run coverage # run local coverage (no internet access)
```

### Other

```bash
pixi run clean # clean out unnecessary files
pixi run format # run formatting
pixi run checks # run pre-commit checks
pixi run docs # generate documentation
pixi run container # build the docker container and run it
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

### Using Ruff with PyCharm

Note: First version of [Ruff plugin](https://github.com/koxudaxi/ruff-pycharm-plugin) would have issues (v0.0.27) apparently due to my PyCharm version (2023.2).

I
