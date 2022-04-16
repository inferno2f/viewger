FROM python:3.10-slim

WORKDIR /app

RUN apt update && apt install -y gcc libpq-dev
COPY . .
RUN pip3 install -r /app/requirements.txt --no-cache-dir && \
    chmod +x docker-entrypoint.sh
