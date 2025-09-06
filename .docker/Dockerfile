FROM python:3.12-slim-bookworm AS builder

RUN apt -y update && apt -y upgrade

WORKDIR /code

COPY . /code/

CMD uvicorn source.main:app --host 0.0.0.0 --port 8000 --reload
