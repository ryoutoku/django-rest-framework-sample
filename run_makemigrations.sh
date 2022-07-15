#!/bin/bash

# create migration files using production

# set current dirname
project=$(basename `pwd`)
compose_file=docker-compose-prod.yml
container=django-prod

# call makemigrations
docker-compose -f ${compose_file} run ${container} python manage.py makemigrations
docker-compose -f ${compose_file} down