# Use official Python image as base
FROM python:3.11-slim

# Install system dependencies needed for psycopg2
RUN apt-get update \
  && apt-get install -y --no-install-recommends gcc libpq-dev python3-dev \
  && rm -rf /var/lib/apt/lists/*


# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Remove build tools (keep image small & secure)
RUN apt-get purge -y --auto-remove gcc python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the rest of the application code
COPY . .

# Start the application (replace app.py with your main file)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]