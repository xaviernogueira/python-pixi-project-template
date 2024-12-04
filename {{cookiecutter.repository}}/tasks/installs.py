"""Install tasks for pyinvoke."""

# %% IMPORTS

from invoke.context import Context
from invoke.tasks import task
from pathlib import Path

# %% TASKS


@task
def pixi(ctx: Context) -> None:
    """Install poetry packages."""
    manifest: str = str(Path.cwd() / "pyproject.toml")
    ctx.run(f"pixi install --manifest-path={manifest}")


@task
def pre_commit(ctx: Context) -> None:
    """Install pre-commit hooks on git."""
    ctx.run("pixi run pre-commit install --hook-type pre-push")
    ctx.run("pixi run pre-commit install --hook-type commit-msg")


@task(pre=[pixi, pre_commit], default=True)
def all(_: Context) -> None:
    """Run all install tasks."""
    ...
