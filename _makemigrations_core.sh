env=$1

project=django-rest-framework-sample
compose_file=docker-compose-${env}.yml
container=django-${env}


docker-compose -f ${compose_file} run ${container} python manage.py makemigrations
docker-compose -f ${compose_file} down

if type dockle > /dev/null 2>&1; then
    dockle -af settings.py ${project}_${container}
fi