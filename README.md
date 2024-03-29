# DockerFlaskApp

## Objective

This repository shows how to launch an API with Docker and Flask in Python.:

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

CMD gunicorn -b 0.0.0.0:3333 --access-logfile - "webapp.app:app"
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


For more documentation on these commands and on all available `Dockerfile` commands see [online documentation](https://docs.docker.com/engine/reference/builder/#format)

## `docker-compose.yml` 

```console
version: '3'

services:
  webapp:
    build: .
    command: >
      gunicorn -b 0.0.0.0:3333
      --access-logfile -
      --reload
      "webapp.app:app"
    environment:
      PYTHONUNBUFFERED: 'true'
    volumes:
      - '.:/webapp'
    ports:
      - '3333:3333'
```

`docker-compose.yml` file. Documentation on `docker-compose` file can be found [here](https://docs.docker.com/compose/compose-file/)

## Running the container

Now in a terminal, run

```console
docker-compose up --build
```

You should see all the steps, and if everything works you can now open a browser and type in the URL


```console
localhost:3333/users/Toto
```
and you should see

![Alt text](img/flaskapprunning.PNG)



