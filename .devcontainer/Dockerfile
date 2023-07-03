FROM python:3.10.8

WORKDIR /pydantic-tutorial

RUN apt-get update && \
    apt-get install -y sudo && \
    pip install --upgrade pip

# This line is necessary because you are not starting from an image
ENTRYPOINT [ "/bin/sh", "-c" ]
