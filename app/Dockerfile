FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn

# Copy the entire app directory from the host to the container's /app/app
# This ensures that 'import app.main' works because 'app' is a package in the WORKDIR
COPY . /app/app

# Ensure logs directory exists
RUN mkdir -p /var/log/app

# Start Uvicorn
# Looking for 'app' (the folder) -> 'main' (the file) -> 'app' (the FastAPI instance)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]