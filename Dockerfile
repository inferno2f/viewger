FROM python:3.10-slim

WORKDIR /app

COPY . .
RUN apt update && apt install -y gcc libpq-dev && \
    pip3 install -r /app/requirements.txt --no-cache-dir && \
    chmod +x gunicorn.sh

ENTRYPOINT ["sh", "gunicorn.sh"]