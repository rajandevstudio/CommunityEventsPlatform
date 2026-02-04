# -----------------------------
# Base image (exact Python version)
# -----------------------------
FROM python:3.11.5-slim

# -----------------------------
# Environment variables
# -----------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# -----------------------------
# System dependencies
# -----------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Working directory
# -----------------------------
WORKDIR /app

# -----------------------------
# Install Python dependencies
# -----------------------------
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Copy project code
# -----------------------------
COPY . .

# -----------------------------
# Collect static files
# (Safe even if STATIC_ROOT exists)
# -----------------------------
RUN python manage.py collectstatic --noinput

# -----------------------------
# Run with Gunicorn (Cloud Run compatible)
# -----------------------------
CMD ["gunicorn", "communityeventsplatform.wsgi:application", "--bind", "0.0.0.0:8080", "--workers", "2", "--threads", "4"]