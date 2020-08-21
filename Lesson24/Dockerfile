FROM ubuntu

# Update apt cache
RUN apt update && apt upgrade -y

# Install python
RUN apt install python3.8 -y
RUN apt install python3.8-venv -y
RUN apt install python3-venv -y

# Create project folder
RUN mkdir -p /API_tests/venv
WORKDIR ./API_tests

# Install requirements
RUN python3.8 -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install pytest requests Cerberus jsonschema

# Copy tests
COPY ./REST_service_1/*.py ./REST_service_1/
COPY ./REST_service_2/*.py ./REST_service_2/
COPY ./REST_service_3/*.py ./REST_service_3/

# Run tests
CMD venv/bin/python3 -m pytest ./REST_service_1 -v ; \
    venv/bin/python3 -m pytest ./REST_service_2 -v ; \
    venv/bin/python3 -m pytest ./REST_service_3 -v