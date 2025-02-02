"""Package tasks for pyinvoke."""

# %% IMPORTS

from invoke.context import Context
from invoke.tasks import task

from . import cleans, installs

# %% CONFIGS

BUILD_FORMAT = "wheel"

# %% TASKS


@task(pre=[installs.pixi_install_build, cleans.dist])
def build_package(ctx: Context, format: str = BUILD_FORMAT) -> None:
    """Build the python package."""
    ctx.run(f"pixi run -e build hatch build -t {format}")


@task(pre=[build_package])
def install_editable(ctx: Context) -> None:
    """Build the python package."""
    ctx.run("pixi run -e build pip install -e .")


@task(pre=[build_package])
def install_noneditable(ctx: Context) -> None:
    """Build the python package."""
    ctx.run("pixi run -e build pip install .")


@task(default=True)
def all(ctx: Context, editable: bool = False) -> None:
    """Uses hatch to build the package and then installs it.

    NOTE: Run with invoke packages --editable to install the package in editable mode.
    """
    if editable:
        ctx.run("echo 'Installing the package in editable mode'")
        install_editable(ctx)
    else:
        ctx.run("echo 'Installing the package in non-editable mode'")
