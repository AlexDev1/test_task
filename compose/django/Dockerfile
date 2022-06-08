# pull official base image
FROM python:3.9-slim-bullseye

ARG APP_HOME=/app

# set work directory
WORKDIR ${APP_HOME}

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN addgroup --system app && adduser --system --ingroup app app

# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy application code to WORKDIR
COPY --chown=app:app ./compose/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint


COPY --chown=app:app ./compose/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY --chown=app:app . ${APP_HOME}


# make django owner of the WORKDIR directory as well.
RUN chown app:app ${APP_HOME}

USER app
RUN mkdir $APP_HOME/staticfiles
ENTRYPOINT ["/entrypoint"]
