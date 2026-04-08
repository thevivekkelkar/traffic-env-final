# Use Python base image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy all project files into container
COPY . .

# Run your inference script when container starts
CMD ["python", "inference.py"]