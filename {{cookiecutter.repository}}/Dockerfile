FROM ghcr.io/prefix-dev/pixi:0.40.0 AS build

# copy source code, pixi.toml and pixi.lock to the container
RUN mkdir /app
COPY pyproject.toml pixi.lock /app
COPY README.md /app
COPY /src /app/src
COPY /tasks /app/tasks
COPY /tests /app/tests
COPY /.git/ /app/.git
WORKDIR /app

# check that test pass in the deployment environment.
RUN pixi run tests

# install dependencies and build the package in non-editable mode
# NOTE: see tasks/build.py for the build command
RUN pixi run build

# Create the shell-hook bash script to activate the environment
RUN pixi shell-hook -e build > /shell-hook.sh

# extend the shell-hook script to run the command passed to the container
RUN echo 'exec "$@"' >> /shell-hook.sh

FROM ubuntu:24.04 AS runtime

# install CA certificates for CloudRun obstore use
RUN apt-get update && \
    apt-get install -y ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# note that the "prefix" (path) needs to stay the same as in the build container
RUN mkdir /app
COPY --from=build /app /app
COPY --from=build /app/.pixi/envs/build /app/.pixi/envs/default
COPY --from=build /shell-hook.sh /shell-hook.sh
WORKDIR /app
EXPOSE $PORT

# set the entrypoint to the shell-hook script (activate the environment and run the command)
# no more pixi needed in the prod container
ENTRYPOINT ["/bin/bash", "/shell-hook.sh"]

CMD ["python", "src/app.py"]
