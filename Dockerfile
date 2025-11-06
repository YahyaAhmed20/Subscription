# Start Docker Kernel To Python
FROM python:3.11-slim-bullseye

# Set environment to show logs immediately
ENV PYTHONUNBUFFERED 1

# Update kernel and install MySQL build dependencies
RUN apt-get update && apt-get -y install gcc libpq-dev
   

# Set working directory
WORKDIR /app

# Copy dependency list
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the project
COPY . /app/