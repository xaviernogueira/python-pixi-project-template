"""Format tasks for pyinvoke."""

# %% IMPORTS

from invoke.context import Context
from invoke.tasks import task

from . import installs
# %% TASKS


@task
def imports(ctx: Context) -> None:
    """Format python imports with ruff."""
    ctx.run("pixi run ruff check --select I --fix")


@task
def sources(ctx: Context) -> None:
    """Format python sources with ruff."""
    ctx.run("pixi run ruff format src/ tasks/ tests/")


@task(pre=[installs.pixi_install_dev, imports, sources], default=True)
def all(_: Context) -> None:
    """Run all format tasks."""
    ...
