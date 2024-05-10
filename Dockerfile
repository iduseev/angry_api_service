FROM python:3.12.2 AS build

WORKDIR /app

COPY ./pyproject.toml ./

RUN python -m venv /.venv \
    && /.venv/bin/pip install .

FROM python:slim AS release
WORKDIR /app

EXPOSE 8080
ENTRYPOINT ["/.venv/bin/run_server"]
CMD ["--host", "0.0.0.0", "--port", "8080"]

COPY --from=build /.venv /.venv
COPY . .

COPY backend /app/backend
WORKDIR /app

ENV PYTHONPATH=/app