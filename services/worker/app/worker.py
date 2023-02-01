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


def process_message(channel, method, properties, body):
    print(f"received message: {body}")


def core():
    connection, channel = init_connection(
        host=RABBIT_HOST_NAME, queue=RABBIT_QUEUE_NAME)

    try:
        channel.basic_consume(
            on_message_callback=process_message, queue=RABBIT_QUEUE_NAME)
        channel.start_consuming()
    except:
        connection.close()
        raise
    finally:
        connection.close()


if __name__ == '__main__':
    core()
