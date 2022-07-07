# syntax=docker/dockerfile:1

FROM python:3.10.5-slim-buster as builder

ARG PIP_OPTION=''

WORKDIR /tmp

COPY ./src ./src \
    ./Pipfile ./ \
    ./Pipfile.lock ./

RUN pip install --upgrade --no-cache-dir pip==22.1.2 && \
    pip install --no-cache-dir pipenv==2022.6.7 && \
    pipenv sync --system ${PIP_OPTION} && \
    pip uninstall -y pipenv


FROM python:3.10.5-slim-buster

ENV PYTHONUNBUFFERED=1 \
    USER=django \
    WORKDIR=/app

RUN useradd -d /home/${USER} -m -s /bin/bash ${USER}
USER ${USER}

WORKDIR ${WORKDIR}

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /tmp/src ./
