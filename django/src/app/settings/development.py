from .base import *  # noqa
from .base import INSTALLED_APPS, MIDDLEWARE

DEBUG = True

ALLOWED_HOSTS = ['*']

MIDDLEWARE.extend([
    'silk.middleware.SilkyMiddleware',
])

INSTALLED_APPS.extend([
    'drf_yasg',
    'silk'
])

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': '`Bearer <token>`とする必要がある',
        }
    },
    'USE_SESSION_AUTH': False,
}
