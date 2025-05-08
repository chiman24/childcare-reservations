
# Use the official Python image as base
# FROM --platform=linux/amd64 python:3.13.3-alpine
FROM --platform=linux/amd64 python:slim-bookworm

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=childcare.settings.prod

# Install dependencies for building Python packages
# RUN apk add --no-cache gcc musl-dev libffi-dev

# Set the working directory inside the container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Set LOAD_MONGO_SECRET to false for initial setup
# This is to prevent the application from trying to load secrets during build
# This is a temporary measure; it should be set to true when running the application
ENV LOAD_MONGO_SECRET=false

# Collect static files
RUN python manage.py collectstatic --noinput --settings=childcare.settings.prod

# Run database migrations
#RUN python manage.py migrate

# Expose port 8000 for Django
EXPOSE 8000

# Set environment LOAD_MONGO_SECRET to true before running the application
ENV LOAD_MONGO_SECRET=true

# Start Django application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "childcare.wsgi:application"]
