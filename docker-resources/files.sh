#!/bin/sh

if [ "$DJANGO_ENV" = "production" ]; then
  echo "Running command for prod environment"
  cp .env.production /app
  # cp credentials.json /app
  # Add your production-specific commands here
else
  echo "Running command for prod environment"
  # Add your non-production-specific commands here
fi