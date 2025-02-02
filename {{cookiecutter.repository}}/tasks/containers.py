"""Container tasks for pyinvoke."""

# %% IMPORTS

from invoke.context import Context
from invoke.tasks import task

from . import build, cleans

# %% CONFIGS

IMAGE_TAG = "latest"
REPOSITORY_NAME = cleans.get_pyproject_dict()["project"]["urls"]["repository"]

# %% TASKS


@task(pre=[build.build_package])
def build_container(ctx: Context, tag: str = IMAGE_TAG) -> None:
    """Build the container image."""
    ctx.run(f"docker build --tag={REPOSITORY_NAME}:{tag} .")


@task
def run_container(ctx: Context, tag: str = IMAGE_TAG) -> None:
    """Run the container image."""
    ctx.run(f"docker run --rm {REPOSITORY_NAME}:{tag}")


@task(pre=[build_container, run_container], default=True)
def all(_: Context) -> None:
    """Run all container tasks."""
