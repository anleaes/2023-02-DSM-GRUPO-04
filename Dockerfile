FROM python:3.11.4-slim

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY /docker-resources/files.sh /docker-resources/files.sh

RUN chmod +x /docker-resources/files.sh

RUN sh -c '/docker-resources/files.sh'

RUN apt-get update && apt-get install -y --no-install-recommends curl && \
    curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-dev

COPY . .

ENV PORT 8080

ENV PYTHONUNBUFFERED TRUE
ENV PYTHONDONTWRITEBYTECODE 1

ARG DJANGO_ENV
ENV DJANGO_ENV=$DJANGO_ENV

RUN DJANGO_ENV=$DJANGO_ENV python3 manage.py migrate
RUN DJANGO_ENV=$DJANGO_ENV COLLECT_STATIC=1 python manage.py collectstatic --noinput

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 aigo.wsgi:application