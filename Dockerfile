# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
RUN pip install flask

# Run Flask app on port 80
CMD ["python", "app.py", "10", "20"]
