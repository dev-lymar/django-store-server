FROM python:3.12.2-slim

WORKDIR /store

ENV DJANGO_SETTINGS_MODULE=store.settings
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /store/

RUN pip install --upgrade pip \
 && pip install -r requirements.txt

RUN adduser --disabled-password celery-user
USER celery-user

COPY . .
