# DockerFlaskApp

## Summary

This repository contains all the necessary code to launch a Flask app in a Docker.






## `Dockerfile` 

```console
FROM python:3.6-slim
MAINTAINER Dimitri Bettebghor

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev --no-install-recommends

ENV INSTALL_PATH /webapp
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "web_app.app:app"
```

Description :
- [x] `FROM` indicates which Docker image is to be used
- [x] `MAINTAINER` gives the name of the author of the Docker image
- [x] `RUN` launches packages installation 
- [x] `ENV` sets environment variable
- [x] `RUN` mkdir creates a repository
- [x] `WORKDIR` sets the working directory
- [x] `COPY` copies the requirements file where Python modules are listed
- [x] `RUN pip` installs the Python modules listed in `requirements.txt` 

## `docker-compose.yml` 

```console
version: '2'

services:
  web_app:
    build: .
    command: >
      gunicorn -b 0.0.0.0:8000
      --access-logfile -
      --reload
      "web_app.app:app"
    environment:
      PYTHONUNBUFFERED: 'true'
    volumes:
      - '.:/web_app'
    ports:
      - '8000:8000'
```

`docker-compose.yml` file
