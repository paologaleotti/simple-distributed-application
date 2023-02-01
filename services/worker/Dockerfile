FROM python:3.11

WORKDIR /app

RUN pip install pika

COPY ./app .

CMD [ "python3 consumer.py" ]