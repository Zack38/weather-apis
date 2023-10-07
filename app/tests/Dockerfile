# Use the official Python image from Docker Hub as a base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY /app/requirements.txt .
COPY /app/seattle-weather.csv .
COPY /pytest.ini .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code into the container
COPY . .

# Expose the port that FastAPI will run on
# EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
# CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
