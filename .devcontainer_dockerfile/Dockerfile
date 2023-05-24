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

# ユーザーを作成する
ARG USERNAME=user
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# ユーザーを作成する
RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# ユーザーをsudoersに追加する
RUN echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME

# ユーザーを切り替える
USER $USERNAME
