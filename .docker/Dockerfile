FROM python:3.12-slim-bookworm AS builder

# Install build dependencies (needed for some pip packages)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only requirements first for caching
COPY requirements.txt .

# Create virtual environment
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r requirements.txt


FROM python:3.12-slim-bookworm AS final

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Ensure venv is used
ENV PATH="/opt/venv/bin:$PATH"

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Ensure logs are flushed
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy the application code (not .env for security reasons)
COPY . .

# Expose port (adjust to your app)
EXPOSE 8000

# Run your app (example for FastAPI with uvicorn)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
