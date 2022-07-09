# syntax=docker/dockerfile:1


###############################################
# set code
###############################################
FROM python:3.10.5-slim-buster as build_base

WORKDIR /tmp

COPY ./src ./src \
    ./Pipfile ./ \
    ./Pipfile.lock ./


###############################################
# install modules for development
###############################################
FROM build_base as build_development

RUN pip install --upgrade --no-cache-dir pip==22.1.2 && \
    pip install --no-cache-dir pipenv==2022.6.7 && \
    pipenv sync --system --dev && \
    pip uninstall -y pipenv


###############################################
# install modules for development
###############################################
FROM build_base as build_production

RUN pip install --upgrade --no-cache-dir pip==22.1.2 && \
    pip install --no-cache-dir pipenv==2022.6.7 && \
    pipenv sync --system && \
    pip uninstall -y pipenv


###############################################
# set environment base
###############################################
FROM python:3.10.5-slim-buster as environment_base

ENV PYTHONUNBUFFERED=1 \
    USER=django \
    WORKDIR=/app

RUN useradd -d /home/${USER} -m -s /bin/bash ${USER}
USER ${USER}

WORKDIR ${WORKDIR}

COPY --from=build_base /tmp/src ./


###############################################
# set environment for development
###############################################
FROM environment_base as development
COPY --from=build_development /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages


###############################################
# set environment for production
###############################################
FROM environment_base as production
COPY --from=build_production /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
