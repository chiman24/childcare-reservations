# Use the official Python image as base
FROM --platform=linux/amd64 python:3.11.5-alpine

# Install dependencies for building Python packages
RUN apk add --no-cache gcc musl-dev libffi-dev

# Set the working directory inside the container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run database migrations
RUN python manage.py migrate

# Expose port 8000 for Django
EXPOSE 8000

# Start Django application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "childcare.wsgi:application"]
