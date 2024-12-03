# Xaviers's Pixi Python Project Cookiecutter Template

A python project template to simplify project setup. Adapted originally by @irod973 from https://github.com/fmind/cookiecutter-mlops-package, and now by myself to switch from `poetry` to `pixi`.

This template copy omits the MLFlow functionality. Use the linked mlops-package template if this is desired 

The template provides a robust foundation for building, testing, packaging, and deploying Python packages and Docker Images. Adapt it to your project's needs; the source material is MLOps-focused but is suitable for a wide array of Python projects.

**Source resources**:
- **[MLOps Coding Course (Learning)](https://mlops-coding-course.fmind.dev/)**: Learn how to create, develop, and maintain a state-of-the-art MLOps code base.
- **[MLOps Python Package (Example)](https://github.com/fmind/mlops-python-package)**: Kickstart your MLOps initiative with a flexible, robust, and productive Python package.

## Philosophy

This [Cookiecutter](https://cookiecutter.readthedocs.io/) is designed to be a common ground for diverse python environments. Whether you're working with [Kubernetes](https://www.kubeflow.org/), [Vertex AI](https://cloud.google.com/vertex-ai), [Databricks](https://www.databricks.com/), [Azure ML](https://azure.microsoft.com/en-us/products/machine-learning), or [AWS SageMaker](https://aws.amazon.com/sagemaker/), the core principles of using Python packages and Docker images remain consistent.

This template equips you with the essentials for creating, testing, and packaging your code, providing a solid base for integration into your chosen platform.

You have the freedom to structure your `src/` and `tests/` directories according to your preferences. Alternatively, you can draw inspiration from the structure used in the [MLOps Python Package](https://github.com/fmind/mlops-python-package) project for a ready-made implementation.

We use `pixi` due to it's ability to deterministically manage non-python dependencies (i.e., GDAL or FFMPEG).

## Key Features

(This section was copied into the created project's README so tool info is available to users.)

* **Streamlined Project Structure:** A well-defined directory layout for source code, tests, documentation, tasks, and Docker configurations.
* **Pixi Integration:** Effortless dependency management and packaging with [Pixi](https://pixi.sh/latest/), even with non-python dependencies. Pixi also handles task automation.
* **Automated Testing and Checks:** Pre-configured workflows using [Pytest](https://docs.pytest.org/), [Ruff](https://docs.astral.sh/ruff/), [Mypy](https://mypy.readthedocs.io/), [Bandit](https://bandit.readthedocs.io/), and [Coverage](https://coverage.readthedocs.io/) to ensure code quality, style, security, and type safety.
* **Pre-commit Hooks:** Automatic code formatting and linting with [Ruff](https://docs.astral.sh/ruff/) and other pre-commit hooks to maintain consistency.
* **Dockerized Deployment:** Dockerfile and docker-compose.yml for building and running the package within a containerized environment ([Docker](https://www.docker.com/)).
* **Comprehensive Documentation:** [pdoc](https://pdoc.dev/) generates API documentation, and Markdown files provide clear usage instructions.
* **GitHub Workflow Integration:** Continuous integration and deployment workflows are set up using [GitHub Actions](https://github.com/features/actions), automating testing, checks, and publishing.

## Quick Start

1. **Generate your project:**

```bash
pip install cookiecutter
cookiecutter gh:xaviernogueira/python-pixi-project-template
```

You'll be prompted for the following variables:

- `user`: Your GitHub username.
- `name`: The name of your project.
- `repository`: The name of your GitHub repository.
- `package`: The name of your Python package.
- `license`: The license for your project (Note: use "NA" until we define a standard licence or omit entirely)
- `version`: The initial version of your project.
- `description`: A brief description of your project.
- `python_version`: The Python version to use (e.g., 3.12).

2. **Initialize a git repository:**

```bash
cd {{ cookiecutter.repository }}
git init
# Should also create remote repo, e.g. via Github web console
# Then make first push e.g.
# git commit -m "Initial commit"
# git remote add origin https://github.com/irod973/{{myproject}}.git
# git push -u origin main 
```

3. **Explore the generated project:**

- `src/{{cookiecutter.package}}`: Your Python package source code.
- `tests/`: Unit tests for your package.
- `tasks/`: PyInvoke tasks for automation.
- `Dockerfile`: Configuration for building your Docker image.
- `docker-compose.yml`: Orchestration file for running your project.

4. **Start developing!**

#TODO: update this for pixi!

Use the provided Invoke tasks to manage your development workflow:

- `invoke installs`: Install dependencies and pre-commit hooks.
- `invoke formats`: Format your code.
- `invoke checks`: Run code quality, type, security, and test checks.
- `invoke docs`: Generate API documentation.
- `invoke packages`: Build your Python package.
- `invoke containers`: Build and run your Docker image.

## Example Usage

### Building and Running Your Docker Image

```bash
invoke containers
```

This builds a Docker image based on your [`Dockerfile`](https://github.com/fmind/cookiecutter-mlops-package/blob/main/%7B%7Bcookiecutter.repository%7D%7D/Dockerfile) and runs it.

## License

The source material this is adapted from is licensed under the [MIT License](https://opensource.org/license/mit). See the [`LICENSE.txt`](https://github.com/fmind/cookiecutter-mlops-package/blob/main/LICENSE.txt) file for details.
