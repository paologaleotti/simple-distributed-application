import random

import pika
from consts import RABBIT_HOST_NAME, RABBIT_QUEUE_NAME

if not RABBIT_HOST_NAME:
    raise Exception


def init_connection(host: str, queue: str):
    connection_params = pika.ConnectionParameters(host=host)
    connection = pika.BlockingConnection(parameters=connection_params)
    channel = connection.channel()
    channel.queue_declare(queue=queue)

    print(f"connected to {host} with queue {queue}")
    return connection, channel


def core():
    connection, channel = init_connection(
        host=RABBIT_HOST_NAME, queue=RABBIT_QUEUE_NAME)

    try:
        while True:
            message = f"value:{random.random()}"
            channel.basic_publish(
                exchange="", routing_key=RABBIT_QUEUE_NAME, body=message)
            print(f"message sent -> {message}")
    except:
        connection.close()
        raise
    finally:
        connection.close()


if __name__ == '__main__':
    core()
