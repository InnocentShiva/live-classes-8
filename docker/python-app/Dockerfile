#Use official lightweight Python image
FROM python:3.11-slim

#Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

#Set working directory inside container
WORKDIR /app

#Install system dependencies (optional)
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

#Copy dependency file if exists
COPY requirements.txt .

#Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

#Copy application code
COPY . .

#Command to run the application (update as needed)
CMD ["python", "app.py"]
