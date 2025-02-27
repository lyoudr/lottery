# Use an official Python runtime as a base image
FROM python:3.11


# Set environment variables to prevent Python from writing pyc files and to buffer stdout and stderr
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV ENV=develop
ENV GCP_PROJECT_ID=ann-project-390401

# Set the working directory
WORKDIR /app 

# Copy the project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Change permission for entrypoint.sh to make it executable
RUN chmod +x /app/entrypoint.sh

# Start the Django app 
CMD ["./entrypoint.sh"]
