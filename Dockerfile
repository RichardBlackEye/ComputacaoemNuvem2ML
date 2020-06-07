FROM tiangolo/uvicorn-gunicorn:python3.6-alpine3.8

# Make directories suited to your application
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy and install requirements
COPY requirements.txt /usr/src/app

RUN pip3 install --no-cache-dir -r requirements.txt

# Copy contents from your local to your docker container
COPY . /usr/src/app