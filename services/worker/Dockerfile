FROM python:3.11

WORKDIR /usr/src/app

RUN pip install pika

COPY . .

RUN "ls"

CMD [ "python", "-u", "./app/worker.py" ]