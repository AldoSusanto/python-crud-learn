# Use official Python base image
FROM python:3.11-slim

# Install Poetry
RUN pip install --no-cache-dir poetry

# Set working directory inside container
WORKDIR /app

# Copy poetry files and install dependencies
COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copy the rest of your source code
COPY . .

# Cloud Run expects app to listen on PORT 8080
ENV PORT=8080

# Run the app using uvicorn
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8080"]
