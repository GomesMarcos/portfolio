# Dockerfile for Django application with Tailwind CSS and DaisyUI
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    libpq-dev \
    certbot \
    python3-certbot-nginx \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Prepare static files directory
COPY static/ /app/static/

# Install Tailwind CSS CLI and DaisyUI
RUN if [ ! -d /app/static/css ]; then mkdir -p /app/static/css; fi && \
    if [ ! -d /app/static/js ]; then mkdir -p /app/static/js; fi && \
    if [ ! -f /app/static/css/tailwindcss ]; then curl -sLo /app/static/css/tailwindcss https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64; fi && \
    chmod +x /app/static/css/tailwindcss

COPY . .

# Copy entrypoint.sh to container root
COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Running entrypoint
ENTRYPOINT ["scripts/entrypoint.sh"]
