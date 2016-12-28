import pika
import random
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(virtual_host='guest'))
channel = connection.channel()


def callback(ch, method, properties, body):
    print('Consuming... {}'.format(body))

    delay = random.randrange(1, 4, 1)
    time.sleep(delay)
    print('Rejected after {} seconds!'.format(delay))

    ch.basic_reject(delivery_tag=method.delivery_tag, requeue=False)


try:
    channel.basic_consume(callback, queue='x.queue', no_ack=False)
    channel.start_consuming()

except:
    connection.close()
