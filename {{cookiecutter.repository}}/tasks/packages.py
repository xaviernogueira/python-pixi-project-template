"""Package tasks for pyinvoke."""

# %% IMPORTS

from invoke.context import Context
from invoke.tasks import task

from . import cleans

# %% CONFIGS

BUILD_FORMAT = "wheel"

# %% TASKS


@task(pre=[cleans.dist])
def build(ctx: Context, format: str = BUILD_FORMAT) -> None:
    """Build the python package."""
    ctx.run(f"hatch build -t {format}")


@task(pre=[build], default=True)
def all(_: Context) -> None:
    """Run all package tasks."""
