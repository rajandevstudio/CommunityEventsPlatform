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
# Run with Gunicorn (Cloud Run compatible)
# -----------------------------
RUN chmod +x web_server.sh

CMD ["./web_server.sh"]
