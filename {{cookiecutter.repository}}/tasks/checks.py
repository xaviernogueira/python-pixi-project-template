"""Check tasks for pyinvoke."""

# %% IMPORTS

from invoke.context import Context
from invoke.tasks import task

from . import installs

# %% TASKS


@task
def format(ctx: Context) -> None:
    """Check the formats with ruff."""
    ctx.run("pixi run -e dev ruff format --check src/ tasks/ tests/")


@task
def static_type(ctx: Context) -> None:
    """Check the types with mypy."""
    ctx.run("pixi run -e dev mypy src/ tasks/")


@task
def code(ctx: Context) -> None:
    """Check the codes with ruff."""
    ctx.run("pixi run -e dev ruff check src/ tasks/ tests/")


@task
def security(ctx: Context) -> None:
    """Check the security with bandit."""
    ctx.run("pixi run -e dev bandit --recursive --configfile=pyproject.toml src/")


@task(pre=[installs.pixi_install_dev, format, static_type, code, security], default=True)
def all(_: Context) -> None:
    """Run all check tasks."""
