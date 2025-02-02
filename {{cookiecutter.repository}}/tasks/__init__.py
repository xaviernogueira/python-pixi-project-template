"""Task collections for the project."""

# mypy: ignore-errors

# %% IMPORTS

from invoke import Collection

from . import (
    actions,
    build,
    checks,
    cleans,
    containers,
    docs,
    formats,
    installs,
)

# %% NAMESPACES

ns = Collection()

# %% COLLECTIONS

ns.add_collection(actions)
ns.add_collection(build)
ns.add_collection(checks)
ns.add_collection(cleans)
ns.add_collection(containers)
ns.add_collection(docs)
ns.add_collection(formats)
ns.add_collection(installs)
