"""Check tasks for pyinvoke."""

# %% IMPORTS

from invoke.context import Context
from invoke.tasks import task

# %% TASKS


@task
def format(ctx: Context) -> None:
    """Check the formats with ruff."""
    ctx.run()


@task
def static_type(ctx: Context) -> None:
    """Check the types with mypy."""
    ctx.run()


@task
def code(ctx: Context) -> None:
    """Check the codes with ruff."""
    ctx.run()


@task
def test(ctx: Context) -> None:
    """Check the tests with pytest."""
    ctx.run("pixi run pytest --numprocesses='auto' tests/")


@task
def security(ctx: Context) -> None:
    """Check the security with bandit."""
    ctx.run()


@task
def coverage(ctx: Context) -> None:
    """Check the coverage with coverage."""
    ctx.run()


@task(pre=[format, static_type, code, security, coverage], default=True)
def all(_: Context) -> None:
    """Run all check tasks."""
