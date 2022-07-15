#!/bin/bash

# execute test in development
project=$(basename `pwd`)
compose_file=docker-compose-dev.yml
container=django-dev

# call makemigrations
docker-compose -f ${compose_file} run ${container} bash -c 'python -m coverage run manage.py test && python -m coverage html'
docker-compose -f ${compose_file} down