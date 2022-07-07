docker-compose -f docker-compose-prod.yml run -e DJANGO_SETTINGS_MODULE=app.settings.production django_prod python manage.py makemigrations
docker-compose -f docker-compose-prod.yml down