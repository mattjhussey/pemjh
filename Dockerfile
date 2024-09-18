FROM python:3.12 as base

WORKDIR /usr/src/app

# Execute Tox
FROM base as tox
RUN ["pip", "install", "tox"]
RUN ["tox"]

# Configure Development Environment
# Requires -v bind to the working directory. Run the following commands in the working folder to start a dev container
# Windows: docker run --rm -v %CD%:/usr/src/app -it {IMAGE} /bin/bash
# Linux: docker run -v ${PWD}:/usr/src/app -it {IMAGE} /bin/bash
FROM base as development
COPY requirements-dev.txt requirements-dev.txt
RUN ["pip", "install", "-r", "requirements-dev.txt"]
COPY . .


