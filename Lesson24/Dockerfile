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
RUN venv/bin/pip install pytest requests

# Copy tests
COPY ./*.py ./

# Run tests
CMD venv/bin/python3 -m pytest -v