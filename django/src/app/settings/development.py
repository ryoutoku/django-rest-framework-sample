from .base import *  # noqa
from .base import INSTALLED_APPS

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS.extend([
    'drf_yasg',
])
