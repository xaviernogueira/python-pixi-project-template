"""Tests tasks for pyinvoke."""

# %% IMPORTS

from invoke.context import Context
from invoke.tasks import task

from . import installs

# %% TASKS


@task(pre=[installs.pixi_install_dev])
def test(
    ctx: Context,
) -> None:
    """Run tests with pytest."""
    ctx.run("pixi run -e dev pytest tests/")


@task(pre=[installs.pixi_install_dev])
def coverage(ctx: Context) -> None:
    """Run tests with pytest and coverage."""
    ctx.run("pixi run -e dev pytest --cov=src/ --cov-fail-under=0 tests/")


@task(default=True)
def all(
    ctx: Context, calculate_coverage: bool = False,
) -> None:
    """Run tests tasks.

    NOTE: if run_integration_tests==True, tests that require internet.
    """
    if calculate_coverage:
        coverage(ctx)
    else:
        test(ctx)
