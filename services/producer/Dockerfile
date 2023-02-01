FROM python:3.11

WORKDIR /usr/src/app

RUN pip install pika

COPY . .

CMD [ "python", "-u", "./app/producer.py" ]
