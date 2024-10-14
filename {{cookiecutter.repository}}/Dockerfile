# https://docs.docker.com/engine/reference/builder/
FROM python:{{cookiecutter.python_version}}-slim

# Install dependencies with poetry
RUN pip install --progress-bar off poetry==1.8.2
COPY poetry.lock pyproject.toml ./
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install --progress-bar off -r requirements.txt
RUN rm poetry.lock pyproject.toml

COPY ./src /app
ENV PYTHONPATH="${PYTHONPATH}:/app"
WORKDIR /app

CMD ["uvicorn", "example_app.main:app", "--host", "0.0.0.0"]
