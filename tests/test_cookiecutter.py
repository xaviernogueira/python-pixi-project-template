"""Test the project generation."""

# %% IMPORTS

import os
from pytest_cookies.plugin import Cookies
from pytestshellutils.shell import Subprocess

# %% COMMANDS

COMMANDS = [
    "git init",
    "invoke cleans.reset",
    "pixi run installs",
    "pixi run formats",
    "pixi run checks",
    "pixi run docs",
    "pixi run packages",
    #"pixi run containers", # TODO: fix test Dockerfile
]

# %% TESTS


def test_project_generation(cookies: Cookies) -> None:
    """Test the generation of the project."""
    # given
    context = {
        "user": "test",
        "name": "MLOps 123",
        "version": "1.0.0",
        "description": "DONE",
        "python_version": "3.12",
    }
    repository = context["name"].lower().replace(" ", "-")
    package = repository.replace("-", "_")
    # when
    result = cookies.bake(extra_context=context)
    # then
    # - cookies
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()
    assert result.project_path.name == repository

    expected_result = {
        "user": context["user"],
        "email": "",
        "name": context["name"],
        "repository": repository,
        "package": package,
        "license": "NA",
        "version": context["version"],
        "description": context["description"],
        "python_version": context["python_version"],
    }
    assert result.context == expected_result

    env = os.environ.copy()
    env["PIXI_PROJECT_MANIFEST"] = str(result.project_path / "pyproject.toml")

    # - commands
    shell = Subprocess(cwd=result.project_path)
    for command in COMMANDS:
        result = shell.run(*command.split(), env=env)
        assert result.returncode == 0, f"Command failed: {command}"
