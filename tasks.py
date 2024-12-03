"""Tasks of the project."""

# %% IMPORTS

from invoke import task
from invoke.context import Context

# %% TASKS

@task
def install(ctx: Context) -> None:
    """Install the project."""
    ctx.run("pixi install")


@task
def hooks(ctx: Context) -> None:
    """Setup the project hooks."""
    ctx.run("pixi run pre-commit install")


@task
def test(ctx: Context) -> None:
    """Run the project unit tests."""
    ctx.run("pixi run pytest tests/")
