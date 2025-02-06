# Use an official Python runtime as a base image
FROM python:3.11

# Set the working directory
WORKDIR /app 

# Copy the project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files
RUN python manage.py collecstatic --noinput

# Start the Django app 
CMD ["gunicorn", "--bind", "0.0.0.0:8000", 'lottery.wsgi']
