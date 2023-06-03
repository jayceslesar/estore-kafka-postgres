FROM python:3.10-slim-buster

WORKDIR /app

ADD . /app

RUN pip install -e .
RUN apt-get update && \
    apt-get install -y kafkacat && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 80
