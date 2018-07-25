FROM python:3.6

MAINTAINER jihoon6372@hanmail.net

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       vim \
       python3-dev

RUN pip install django \
    uwsgi

WORKDIR /home/docker/django
COPY ./uwsgi.ini .
COPY ./test.py .
COPY ./generator_secret_json.py .

RUN django-admin startproject app .

WORKDIR app
COPY wsgi.py .

WORKDIR /home/docker/django
EXPOSE 8000

RUN python generator_secret_json.py
CMD ["uwsgi", "--ini", "uwsgi.ini"]
