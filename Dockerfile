# Use the official Python image with your version of Python
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install wkhtmltopdf and other dependencies
RUN apt-get update \
    && apt-get install -y \
        wkhtmltopdf \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
