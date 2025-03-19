FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Update apt and install awscli
RUN apt-get update -y && apt-get install awscli -y

# Set working directory
WORKDIR /app

# Copy the entire application
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install the local package in editable mode
RUN pip install -e .

# Command to run the application
CMD ["python", "app.py"]
