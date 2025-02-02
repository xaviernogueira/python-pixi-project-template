"""Install tasks for pyinvoke."""

# %% IMPORTS

from pathlib import Path

from invoke.context import Context
from invoke.tasks import task

# %% TASKS
MANIFEST: str = str(Path.cwd() / "pyproject.toml")


@task
def pixi_install_dev(ctx: Context) -> None:
    """Install pixi dev packages."""
    ctx.run(f"pixi install -e dev --manifest-path={MANIFEST}")


@task
def pixi_install_docs(ctx: Context) -> None:
    """Install pixi docs packages."""
    ctx.run("pixi install -e docs")


@task
def pixi_install_build(ctx: Context) -> None:
    """Install pixi dev packages."""
    ctx.run(f"pixi install -e build --manifest-path={MANIFEST}")


@task
def pre_commit(ctx: Context) -> None:
    """Install pre-commit hooks on git."""
    ctx.run("pixi run -e dev pre-commit install --hook-type pre-push")
    ctx.run("pixi run -e dev pre-commit install --hook-type commit-msg")


@task(pre=[pixi_install_dev, pre_commit], default=True)
def all(_: Context) -> None:
    """Run all install tasks."""
