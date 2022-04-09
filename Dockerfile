FROM python:3.9-alpine

RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app
RUN pip3 install -r requirements.txt

ADD . /app

RUN chmod +x gunicorn.sh

EXPOSE 5000

ENTRYPOINT ["sh", "gunicorn.sh"]