FROM python:3.10-slim

WORKDIR /app

COPY . .
RUN pip3 install -r /app/requirements.txt --no-cache-dir && \
    chmod +x gunicorn.sh

EXPOSE 5000

ENTRYPOINT ["sh", "gunicorn.sh"]