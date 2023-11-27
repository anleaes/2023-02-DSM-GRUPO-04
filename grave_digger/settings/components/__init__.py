from django.core.exceptions import ImproperlyConfigured
import environ
import os
from grave_digger.settings import ENV_TYPE

config = environ.Env()

if os.path.isfile(f".env.{ENV_TYPE}"):
    config.read_env(f".env.{ENV_TYPE}")
else:
    raise ImproperlyConfigured(f"Env .env.{ENV_TYPE} was not found in the root directory.")