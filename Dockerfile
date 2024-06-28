FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache mariadb-connector-c-dev gcc musl-dev
RUN apk add --no-cache libffi-dev
RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/


RUN pip install -r requirements.txt
RUN pip install gunicorn==20.1.0
RUN pip install mysqlclient

COPY . /app/