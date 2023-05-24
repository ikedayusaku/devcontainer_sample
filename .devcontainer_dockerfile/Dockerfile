FROM python:3.11.3-slim-buster

# コンテナに色々とインストールする

# aptの最新化
RUN apt-get update && \
        apt-get -y upgrade

# Git, cURL
RUN apt-get update && apt-get install -y \
    git curl sudo

# Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false
