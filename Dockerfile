FROM python:3.10 as base

WORKDIR /usr/src/app

# Execute Tests
FROM base as test
COPY requirements-dev.txt requirements-dev.txt
RUN ["pip", "install", "-r", "requirements-dev.txt"]
COPY . .
RUN ["pip", "install", "-e", "."]
CMD ["pytest"]

FROM base as lint
COPY requirements-dev.txt requirements-dev.txt
RUN ["pip", "install", "-r", "requirements-dev.txt"]
COPY . .
CMD ["python", "-m", "pylint", "src/pemjh", "--exit-zero", "--output-format=parseable"]

FROM base as flake8
COPY requirements-dev.txt requirements-dev.txt
RUN ["pip", "install", "-r", "requirements-dev.txt"]
COPY . .
CMD ["flake8", "--exit-zero"]

# Configure Development Environment
# Requires -v bind to the working directory. Run the following commands in the working folder to start a dev container
# Windows: docker run --rm -v %CD%:/usr/src/app -it {IMAGE} /bin/bash
# Linux: docker run -v ${PWD}:/usr/src/app -it {IMAGE} /bin/bash
FROM base as development
COPY requirements-dev.txt requirements-dev.txt
RUN ["pip", "install", "-r", "requirements-dev.txt"]
COPY . .


