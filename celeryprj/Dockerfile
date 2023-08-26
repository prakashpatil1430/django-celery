# Use a more specific base image
FROM python:3.11.4-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /usr/src/app

# Copy and install requirements first to utilize Docker cache
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN  pip install --upgrade pip && \
     pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Copy the entire application code
COPY . /usr/src/app/
