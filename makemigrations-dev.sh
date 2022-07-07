docker-compose -f docker-compose-dev.yml run django_dev python manage.py makemigrations
docker-compose -f docker-compose-dev.yml down