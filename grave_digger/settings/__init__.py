from os import environ
from split_settings.tools import include
from django.core.exceptions import ImproperlyConfigured

ENV_TYPE = environ.get('DJANGO_ENV', 'local')

base_settings = [
    'components/common.py',
    'components/database.py',
    f'environments/{ENV_TYPE}.py'
]

include(*base_settings)