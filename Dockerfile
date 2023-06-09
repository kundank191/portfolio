# Use the official Python 3.11 image as the base image
FROM python:3.11-slim

USER root
# copy the dependencies file to the working directory
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory
ENV APP_HOME /app
WORKDIR $APP_HOME

# copy application and any required files
COPY . .

# ENV
ENV PORT 80
# Run the application
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app