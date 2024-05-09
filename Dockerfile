FROM python:3.12.2 AS build

WORKDIR /app

COPY ./requirements.in ./

RUN python -m venv /.venv \
    && /.venv/bin/pip install -r requirements.in

FROM python:slim AS release
WORKDIR /app

EXPOSE 80
CMD ["/.venv/bin/uvicorn", "backend.app:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8080"]

COPY --from=build /.venv /.venv
COPY . .