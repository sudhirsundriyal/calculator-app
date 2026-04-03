# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy code
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Default command to run app
CMD ["python", "app.py", "10", "20"]
