"""Docs tasks for pyinvoke."""

# %% IMPORTS

from invoke.context import Context
from invoke.tasks import task
from pathlib import Path

from . import cleans, installs

# %% CONFIGS

DOC_FORMAT = "google"
OUTPUT_DIR = "docs/"
PACKAGE_NAME = cleans.get_pyproject_dict()["project"]["name"].replace("-", "_")

# %% TASKS


@task
def serve(ctx: Context, format: str = DOC_FORMAT, port: int = 8088) -> None:
    """Serve the API docs with pdoc."""
    ctx.run(f"pixi run pdoc --docformat={format} --port={port} {Path.cwd()}/src/{PACKAGE_NAME}")


@task
def api(ctx: Context, format: str = DOC_FORMAT, output_dir: str = OUTPUT_DIR) -> None:
    """Generate the API docs with pdoc."""
    ctx.run(
        f"pixi run pdoc --docformat={format} --output-directory={output_dir} {Path.cwd()}/src/{PACKAGE_NAME}"
    )


@task(pre=[installs.pixi_install_docs, cleans.docs, api], default=True)
def all(_: Context) -> None:
    """Run all docs tasks."""
    ...
